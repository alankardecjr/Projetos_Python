"""Aplicativo de PDV simples para vendas rápidas usando interface Tkinter."""

import tkinter as tk
from tkinter import messagebox, ttk

class SaborRapidoApp:
    """Classe do aplicativo que controla menu, carrinho e finalização de pedido."""

    def __init__(self, root):
        self.root = root
        self.root.title("Sabor Rápido - PDV")
        self.root.geometry("700x550")
        self.root.configure(padx=15, pady=15)

        # Dados iniciais do menu: nome do produto e preço em reais.
        self.itens_menu = {"Hambúrguer": 10.00, "Batata Frita": 5.00, "Refrigerante": 3.00}
        self.pedido = []

        self.setup_ui()

    def setup_ui(self):
        """Configura os widgets da janela principal, incluindo menu, carrinho e cadastro."""
        
        # --- COLUNA ESQUERDA: Menu e Cadastro ---
        left_frame = tk.Frame(self.root)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        tk.Label(left_frame, text="Menu de Produtos", font=("Arial", 12, "bold")).pack(anchor="w")
        
        # Listbox do Menu
        self.listbox_menu = tk.Listbox(left_frame, font=("Arial", 10), height=10)
        self.listbox_menu.pack(fill="x", pady=5)
        self.atualizar_lista_menu()

        tk.Button(left_frame, text="✚ Adicionar ao Pedido", bg="#d4edda", 
                  command=self.adicionar_ao_pedido).pack(fill="x", pady=5)

        # Área de Cadastro
        tk.Separator(left_frame, orient='horizontal').pack(fill='x', pady=15)
        tk.Label(left_frame, text="Cadastrar Novo Produto", font=("Arial", 10, "bold")).pack(anchor="w")
        
        tk.Label(left_frame, text="Nome:").pack(anchor="w")
        self.entry_item = ttk.Entry(left_frame)
        self.entry_item.pack(fill="x")

        tk.Label(left_frame, text="Preço (R$):").pack(anchor="w")
        self.entry_preco = ttk.Entry(left_frame)
        self.entry_preco.pack(fill="x")

        tk.Button(left_frame, text="Salvar no Menu", command=self.cadastrar_item_menu).pack(fill="x", pady=10)

        # --- COLUNA DIREITA: Carrinho / Resumo ---
        right_frame = tk.LabelFrame(self.root, text=" Carrinho / Pedido Atual ", padx=10, pady=10)
        right_frame.pack(side="right", fill="both", expand=True)

        self.tree_pedido = ttk.Treeview(right_frame, columns=("Item", "Preço"), show="headings", height=12)
        self.tree_pedido.heading("Item", text="Produto")
        self.tree_pedido.heading("Preço", text="Preço (R$)")
        self.tree_pedido.column("Preço", width=80, anchor="center")
        self.tree_pedido.pack(fill="both", expand=True)

        self.lbl_total = tk.Label(right_frame, text="Total: R$ 0.00", font=("Arial", 14, "bold"), fg="#28a745")
        self.lbl_total.pack(pady=10)

        btn_grid = tk.Frame(right_frame)
        btn_grid.pack(fill="x")

        tk.Button(btn_grid, text="✘ Remover Item", bg="#f8d7da", command=self.remover_item_pedido).pack(side="left", fill="x", expand=True, padx=2)
        tk.Button(btn_grid, text="✓ Finalizar", bg="#28a745", fg="white", font=("bold"), command=self.finalizar_pedido).pack(side="right", fill="x", expand=True, padx=2)

    # --- LÓGICA DO SISTEMA ---

    def atualizar_lista_menu(self):
        """Atualiza a lista de produtos disponível no menu."""
        self.listbox_menu.delete(0, tk.END)
        for item, preco in self.itens_menu.items():
            self.listbox_menu.insert(tk.END, f"{item} - R$ {preco:.2f}")

    def adicionar_ao_pedido(self):
        """Adiciona o produto selecionado ao pedido atual no carrinho."""
        selecao = self.listbox_menu.curselection()
        if not selecao:
            return
        
        texto = self.listbox_menu.get(selecao[0])
        nome_item = texto.split(" - R$")[0]
        preco_item = self.itens_menu[nome_item]
        
        self.pedido.append((nome_item, preco_item))
        self.tree_pedido.insert("", tk.END, values=(nome_item, f"{preco_item:.2f}"))
        self.atualizar_total()

    def remover_item_pedido(self):
        """Remove o item selecionado no carrinho e atualiza o total."""
        selecionado = self.tree_pedido.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item no carrinho para remover.")
            return

        for item in selecionado:
            # Pega o índice para manter o carrinho interno em sincronia com a árvore de exibição.
            index = self.tree_pedido.index(item)
            self.pedido.pop(index)
            self.tree_pedido.delete(item)

        self.atualizar_total()

    def atualizar_total(self):
        """Recalcula o valor total atual do carrinho e exibe no rótulo."""
        total = sum(float(item[1]) for item in self.pedido)
        self.lbl_total.config(text=f"Total: R$ {total:.2f}")

    def cadastrar_item_menu(self):
        """Cadastra um novo produto no menu com nome e preço informados."""
        nome = self.entry_item.get().strip()
        preco = self.entry_preco.get().replace(",", ".").strip()

        if not nome or not preco:
            messagebox.showerror("Erro", "Preencha nome e preço.")
            return

        try:
            self.itens_menu[nome] = float(preco)
            self.atualizar_lista_menu()
            self.entry_item.delete(0, tk.END)
            self.entry_preco.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser um número válido.")

    def finalizar_pedido(self):
        """Confirma o pagamento do pedido e limpa a lista de itens após finalizar."""
        if not self.pedido:
            messagebox.showinfo("Carrinho Vazio", "Adicione itens antes de finalizar.")
            return
        
        total = sum(item[1] for item in self.pedido)
        resumo = "\n".join([f"{i[0]}: R$ {i[1]:.2f}" for i in self.pedido])
        
        confirmar = messagebox.askyesno("Confirmar Pagamento", f"Resumo:\n{resumo}\n\nTotal: R$ {total:.2f}\n\nFinalizar venda?")
        
        if confirmar:
            messagebox.showinfo("Sucesso", "Pedido enviado para a cozinha!")
            self.pedido.clear()
            for i in self.tree_pedido.get_children():
                self.tree_pedido.delete(i)
            self.atualizar_total()

if __name__ == "__main__":
    root = tk.Tk()
    app = SaborRapidoApp(root)
    root.mainloop()