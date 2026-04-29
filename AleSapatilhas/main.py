import tkinter as tk
from tkinter import messagebox, ttk
import database 
from cadastro_clientes import JanelaCadastroClientes
from cadastro_produtos import JanelaCadastroProdutos    
from cadastro_pedidos import JanelaCadastroPedidos
from cadastro_vendas import JanelaCadastroVendas
 

class SistemaAlêSapatilhas:
    def __init__(self, root):
        self.root = root
        self.root.title("Alê Sapatilhas - Gestão Integrada")
        self.root.geometry("1200x750")
        
        # --- PALETA DE CORES ---
        self.bg_fundo = "#f4f5f9"
        self.bg_card = "#ffffff"
        self.cor_borda = "#d1d5db"
        self.cor_texto = "#1f2937"
        self.cor_lbl = "#4b5563"
        self.cor_btn_menu = "#4b5563" 
        self.cor_btn_sair = "#1f2937" 
        self.cor_hover_btn = "#6b7280"
        self.cor_destaque = "#3b82f6"

        self.root.configure(bg=self.bg_fundo)
        self.modo_atual = "clientes"
        self.setup_ui()
        self.exibir_clientes()

    def setup_ui(self):
        # --- MENU LATERAL ---
        self.sidebar = tk.Frame(self.root, bg=self.cor_btn_sair, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="ALÊ\nSAPATILHAS", font=("Segoe UI", 16, "bold"), 
                 bg=self.cor_btn_sair, fg="white", pady=20).pack()

        # Configuração padrão dos botões do menu
        btn_estilo = {
            "font": ("Segoe UI", 10, "bold"), "bg": self.cor_btn_menu, "fg": "white",
            "relief": "flat", "activebackground": self.cor_hover_btn, 
            "activeforeground": "white", "cursor": "hand2", "anchor": "w", "padx": 20
        }

        botoes = [
            ("➕ GERAR VENDA", self.abrir_venda),
            ("📑 LISTAR PEDIDOS", self.exibir_pedidos),
            ("👤 CAD. CLIENTES", self.abrir_cadastro_cliente),
            ("👥 LISTAR CLIENTES", self.exibir_clientes),
            ("📦 CAD. PRODUTOS", self.abrir_cadastro_produto),
            ("👠 LISTAR PRODUTOS", self.exibir_produtos),
            ("📊 RELATÓRIOS", self.exibir_relatorios),
            ("", None), # Botão em branco
            ("🚪 SAIR DO SISTEMA", self.confirmar_saida)
        ]

        for texto, comando in botoes:
            if texto == "":
                tk.Label(self.sidebar, bg=self.cor_btn_sair, pady=10).pack()
                continue
            
            cor_bg = self.cor_btn_sair if "SAIR" in texto else self.cor_btn_menu
            btn = tk.Button(self.sidebar, text=texto, command=comando, **btn_estilo)
            if "SAIR" in texto: btn.config(bg=self.cor_btn_sair)
            btn.pack(fill="x", pady=2)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.cor_hover_btn))
            btn.bind("<Leave>", lambda e, b=btn, c=cor_bg: b.config(bg=c))

        # --- ÁREA PRINCIPAL ---
        self.container = tk.Frame(self.root, bg=self.bg_fundo, padx=20, pady=20)
        self.container.pack(side="right", fill="both", expand=True)

        # Header da Área
        self.lbl_titulo = tk.Label(self.container, text="Lista de Clientes", font=("Segoe UI", 18, "bold"),
                                   bg=self.bg_fundo, fg=self.cor_texto)
        self.lbl_titulo.pack(anchor="w", pady=(0, 20))

        # --- TREEVIEW (Tabela) ---
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background=self.bg_card, foreground=self.cor_texto, 
                             fieldbackground=self.bg_card, rowheight=30, font=("Segoe UI", 10))
        self.style.map("Treeview", background=[('selected', self.cor_destaque)])
        
        self.tree_frame = tk.Frame(self.container, bg=self.bg_card, highlightthickness=1, highlightbackground=self.cor_borda)
        self.tree_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.tree_frame, show="headings", selectmode="browse")
        self.tree.pack(side="left", fill="both", expand=True)

        # Barra de Rolagem
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Grades e Duplo Clique
        self.tree.bind("<Double-1>", lambda e: self.editar_selecionado())

    # --- FUNÇÕES DE EXIBIÇÃO ---

    def preparar_colunas(self, colunas):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = colunas
        for col in colunas:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, anchor="center", width=120)

    def exibir_clientes(self):
        self.modo_atual = "clientes"
        self.lbl_titulo.config(text="👥 Listagem de Clientes")
        self.preparar_colunas(("id", "nome", "telefone", "aniversário", "cidade", "status"))
        
        for c in database.listar_clientes():
            # Selecionando apenas dados principais para a grid (c[0]=id, c[1]=nome, c[2]=tel, c[3]=aniv, c[8]=cidade, c[11]=status)
            self.tree.insert("", "end", values=(c[0], c[1], c[2], c[3], c[8], c[11]))

    def exibir_produtos(self):
        self.modo_atual = "produtos"
        self.lbl_titulo.config(text="👠 Listagem de Produtos")
        self.preparar_colunas(("id", "produto", "cor", "tam", "preço", "estoque", "status"))
        
        for i in database.listar_itens():
            # i[0]=id, i[1]=nome, i[2]=cor, i[3]=tam, i[5]=venda, i[6]=qtd, i[9]=status
            self.tree.insert("", "end", values=(i[0], i[1], i[2], i[3], f"R$ {i[5]:.2f}", i[6], i[9]))

    def exibir_pedidos(self):
        self.modo_atual = "vendas"
        self.lbl_titulo.config(text="📑 Histórico de Pedidos")
        self.preparar_colunas(("id", "cliente", "valor", "pagamento", "entrega", "data"))
        
        for v in database.listar_vendas_controle():
            self.tree.insert("", "end", values=(v[0], v[1], f"R$ {v[2]:.2f}", v[3], v[4], v[5]))

    def exibir_relatorios(self):
        lucro = database.relatorio_lucro_detalhado()
        messagebox.showinfo("Relatório Financeiro", f"Lucro Total Estimado:\nR$ {lucro:.2f}")

    # --- FUNÇÕES DE AÇÃO ---

    def editar_selecionado(self):
        item = self.tree.selection()
        if not item: return
        valores = self.tree.item(item, "values")
        id_item = valores[0]

        if self.modo_atual == "clientes":
            # Aqui você chamaria sua JanelaCadastroClientes(dados=database.buscar_cliente(id_item))
            messagebox.showinfo("Editar", f"Abrindo Cliente ID: {id_item}")
        elif self.modo_atual == "produtos":
            # Aqui você chamaria sua JanelaCadastroProdutos(dados=database.buscar_produto(id_item))
            messagebox.showinfo("Editar", f"Abrindo Produto ID: {id_item}")

    def abrir_venda(self):
        messagebox.showinfo("Vendas", "Abrindo módulo de PDV...")

    def abrir_cadastro_cliente(self):
        messagebox.showinfo("Cadastro", "Abrindo formulário de cliente...")

    def abrir_cadastro_produto(self):
        # Aqui você importa sua JanelaCadastroProdutos
        from cadastro_produtos import JanelaCadastroProdutos
        JanelaCadastroProdutos(self.root)

    def confirmar_saida(self):
        if messagebox.askyesno("Sair", "Deseja encerrar o sistema?"):
            self.root.destroy()

if __name__ == "__main__":
    database.criar_tabelas()
    root = tk.Tk()
    app = SistemaAlêSapatilhas(root)
    root.mainloop()