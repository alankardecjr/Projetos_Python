import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import database

class JanelaCadastroPedidos(tk.Toplevel):
    def __init__(self, master, dados_venda):
        super().__init__(master)
               
         # --- PALETA DE CORES ---
        self.bg_fundo = "#f4f5f9"
        self.bg_card = "#ffffff"
        self.cor_borda = "#d1d5db"
        self.cor_texto = "#1f2937"
        self.cor_lbl = "#4b5563"
        self.cor_btn_1 = "#4b5563"   
        self.cor_btn_2 = "#374151"   
        self.cor_btn_sair = "#1f2937" 
        self.cor_hover_field = "#3b82f6"   
        self.cor_hover_btn = "#6b7280"

        self.title("Alê Sapatilhas - Painel de Pedidos")
        self.geometry("450x750")
        self.configure(bg=self.bg_fundo)
        
        
        # Dados da venda: (id, nome_cliente, valor_total, status_pgto, status_log, data)
        self.venda_id = dados_venda[0]
        self.criar_widgets(dados_venda)
        
        # Bloqueia interação com a janela principal até fechar esta
        self.grab_set()

    def criar_treeview(self, parent, colunas, cabecalhos, altura):
        """Cria Treeviews personalizadas com Scrollbar integrada"""
        frame_tree = tk.Frame(parent, bg=self.bg_card, highlightbackground=self.cor_borda, highlightthickness=1)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                        background=self.bg_card, 
                        foreground=self.cor_texto, 
                        fieldbackground=self.bg_card, 
                        rowheight=25, 
                        font=("Segoe UI", 9))
        
        style.configure("Treeview.Heading", 
                        background=self.bg_fundo, 
                        foreground=self.cor_lbl, 
                        font=("Segoe UI", 9, "bold"), 
                        relief="flat")
        
        # Cor de seleção (Hover Field)
        style.map("Treeview", background=[('selected', self.cor_hover_field)])

        tree = ttk.Treeview(frame_tree, columns=colunas, show="headings", height=altura)
        for col, head in zip(colunas, cabecalhos):
            tree.heading(col, text=head)
            tree.column(col, anchor="center", width=100)

        vsb = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        
        tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
        return frame_tree, tree

    def criar_widgets(self, d):
        main_frame = tk.Frame(self, bg=self.bg_fundo, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # Cabeçalho do Pedido
        tk.Label(main_frame, text=f"PEDIDO: #{self.venda_id}", bg=self.bg_fundo, 
                 fg=self.cor_texto, font=("Segoe UI", 14, "bold")).pack(anchor="w")

        # --- SEÇÃO: DADOS DO CLIENTE ---
        tk.Label(main_frame, text="DADOS DO CLIENTE", bg=self.bg_fundo, 
                 fg=self.cor_lbl, font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(15, 5))
        
        f_cli, self.tree_cli = self.criar_treeview(main_frame, ("id", "nome", "tel"), 
                                                   ("ID", "Nome do Cliente", "Telefone"), 4)
        f_cli.pack(fill="x")
        # Preenchimento inicial (Mock)
        self.tree_cli.insert("", "end", values=(1, d[1], "(00) 00000-0000"))

        # --- SEÇÃO: DETALHES DA VENDA (PRODUTOS) ---
        tk.Label(main_frame, text="PRODUTOS DO PEDIDO", bg=self.bg_fundo, 
                 fg=self.cor_lbl, font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(15, 5))
        
        f_prod, self.tree_prod = self.criar_treeview(main_frame, ("prod", "qtd", "subtotal"), 
                                                     ("Produto", "Qtd", "Subtotal"), 6)
        f_prod.pack(fill="both", expand=True)
        # Preenchimento inicial (Mock)
        self.tree_prod.insert("", "end", values=("Sapatilha Modelo X", "2", f"R$ {d[2]:.2f}"))

        # --- SEÇÃO: STATUS (DROPDOWNS) ---
        status_frame = tk.Frame(main_frame, bg=self.bg_fundo)
        status_frame.pack(fill="x", pady=20)

        self.var_venda = tk.StringVar(value=d[3])
        self.var_entrega = tk.StringVar(value=d[4])

        for label, var, opts in [("PAGAMENTO", self.var_venda, ["Pendente", "Confirmada", "Cancelada"]),
                                 ("LOGÍSTICA", self.var_entrega, ["À Entregar", "Em Trânsito", "Entregue"])]:
            container = tk.Frame(status_frame, bg=self.bg_fundo)
            container.pack(side="left", fill="x", expand=True, padx=5)
            tk.Label(container, text=label, bg=self.bg_fundo, fg=self.cor_lbl, font=("Segoe UI", 7, "bold")).pack(anchor="w")
            opt = tk.OptionMenu(container, var, *opts)
            opt.config(bg=self.bg_card, relief="flat", highlightthickness=1, highlightbackground=self.cor_borda)
            opt.pack(fill="x", pady=2)

        # --- CONTAINER DE BOTÕES ---
        btn_container = tk.Frame(main_frame, bg=self.bg_fundo)
        btn_container.pack(fill="x", side="bottom", pady=5)

        # Linha 1: Botões de Navegação
        linha1 = tk.Frame(btn_container, bg=self.bg_fundo)
        linha1.pack(fill="x", pady=2)
        
        self.btn_cli = self.criar_botao(linha1, "VER CLIENTE", self.cor_btn_1, self.abrir_clientes)
        self.btn_cli.pack(side="left", fill="x", expand=True, padx=(0, 2))
        
        self.btn_ven = self.criar_botao(linha1, "VER VENDAS", self.cor_btn_1, self.abrir_vendas)
        self.btn_ven.pack(side="left", fill="x", expand=True, padx=(2, 0))

        # Linha 2: Ações Finais
        self.btn_atua = self.criar_botao(btn_container, "ATUALIZAR", self.cor_btn_2, self.atualizar)
        self.btn_atua.pack(fill="x", pady=2, ipady=5)

        self.btn_sair = self.criar_botao(btn_container, "FECHAR", self.cor_btn_sair, self.destroy)
        self.btn_sair.pack(fill="x", pady=2)

    def criar_botao(self, parent, texto, cor, comando):
        """Cria botões padronizados com efeito hover"""
        btn = tk.Button(parent, text=texto, bg=cor, fg="white", font=("Segoe UI", 9, "bold"),
                        relief="flat", cursor="hand2", command=comando)
        btn.bind("<Enter>", lambda e: btn.config(bg=self.cor_hover_btn))
        btn.bind("<Leave>", lambda e: btn.config(bg=cor))
        return btn

    def abrir_clientes(self):
        """Chama a tela de Cadastro de Clientes"""
        try:
            import cadastro_clientes
            cadastro_clientes.JanelaCadastroClientes(self)
        except (ImportError, AttributeError):
            messagebox.showinfo("Navegação", "Chamando JanelaCadastroClientes...")

    def abrir_vendas(self):
        """Chama a tela de Cadastro de Vendas"""
        try:
            import cadastro_vendas
            cadastro_vendas.JanelaCadastroVendas(self)
        except (ImportError, AttributeError):
            messagebox.showinfo("Navegação", "Chamando JanelaCadastroVendas...")

    def atualizar(self):
        """Salva as alterações no Banco de Dados"""
        try:
            database.atualizar_status_venda_financeiro(self.venda_id, self.var_venda.get())
            database.atualizar_status_entrega(self.venda_id, self.var_entrega.get())
            messagebox.showinfo("Sucesso", "Status do pedido atualizados!")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar banco: {e}")

if __name__ == "__main__":
    # Apenas para teste independente
    root = tk.Tk()
    root.withdraw()
    dados_mock = (1, "Cliente Exemplo", 150.00, "Pendente", "À Entregar")
    JanelaCadastroPedidos(root, dados_mock)
    root.mainloop()