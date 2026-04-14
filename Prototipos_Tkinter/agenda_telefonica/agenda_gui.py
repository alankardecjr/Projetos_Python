import os
import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*args, **kwargs):
        return False

load_dotenv()
DB_URL = os.getenv("DATABASE_URL", "dbname=postgres user=admin password=1234 host=localhost port=5432")

def query(sql, params=None, fetch=False):
    try:
        with psycopg2.connect(DB_URL) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchall() if fetch else None
    except Exception as e:
        messagebox.showerror("Erro no Banco", str(e))
        return None

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda PostgreSQL")
        self.root.geometry("500x450")
        self.root.columnconfigure(0, weight=1)
        
        query("CREATE TABLE IF NOT EXISTS agenda (id SERIAL PRIMARY KEY, nome TEXT, telefone TEXT)")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(fill="x")
        frame.columnconfigure(1, weight=1)

        tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w")
        self.ent_nome = tk.Entry(frame)
        self.ent_nome.grid(row=0, column=1, sticky="ew")

        tk.Label(frame, text="Tel:").grid(row=1, column=0)
        self.ent_tel = tk.Entry(frame)
        self.ent_tel.grid(row=1, column=1, sticky="ew")

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Adicionar", command=self.add, bg="green", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Excluir", command=self.delete, bg="red", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Atualizar Lista", command=self.load).pack(side="left", padx=5)

        self.tree = ttk.Treeview(root, columns=("ID", "Nome", "Tel"), show="headings")
        for col in ("ID", "Nome", "Tel"): self.tree.heading(col, text=col)
        self.tree.column("ID", width=50)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.load()

    def load(self):
        self.tree.delete(*self.tree.get_children())
        rows = query("SELECT * FROM agenda ORDER BY id", fetch=True) or []
        for r in rows:
            self.tree.insert("", "end", values=r)

    def add(self):
        n, t = self.ent_nome.get(), self.ent_tel.get()
        if n and t:
            query("INSERT INTO agenda (nome, telefone) VALUES (%s, %s)", (n, t))
            self.load()
            self.ent_nome.delete(0, "end"); self.ent_tel.delete(0, "end")
        else:
            messagebox.showwarning("Atenção", "Preencha nome e telefone")

    def delete(self):
        selected = self.tree.selection()
        if not selected: return
        idx = self.tree.item(selected[0])['values'][0]
        if messagebox.askyesno("Confirmar", f"Excluir ID {idx}?"):
            query("DELETE FROM agenda WHERE id = %s", (idx,))
            self.load()

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            v = self.tree.item(selected[0])['values']
            self.ent_nome.delete(0, "end"); self.ent_nome.insert(0, v[1])
            self.ent_tel.delete(0, "end"); self.ent_tel.insert(0, v[2])

if __name__ == "__main__":
    app_root = tk.Tk()
    AgendaApp(app_root)
    app_root.mainloop()
    