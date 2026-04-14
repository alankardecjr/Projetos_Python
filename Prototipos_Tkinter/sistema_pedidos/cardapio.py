"""Interface de sistema de pedidos local com cadastro de produtos e resumo de vendas."""

import tkinter as tk
from tkinter import messagebox, ttk

class SistemaPedidos:
    """Classe principal do sistema de pedidos que organiza o fluxo e a interface."""

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Pedidos Local - JAD")
        self.root.geometry("800x600")

        # Dados iniciais do menu. Cada produto mapeia um nome para o preço de venda.
        self.menu_produtos = {
            "Hambúrguer": 25.00,
            "Batata Frita": 15.00,
            "Refrigerante": 7.00,
            "Suco Natural": 9.00
        }

        # Estado do pedido atual e valor total acumulado.
        self.pedido_atual = []
        self.total_valor = 0.0

        self.setup_ui()

    def setup_ui(self):
        """Constrói a interface gráfica com menu, carrinho e cadastro de produtos."""
        # --- Título ---
        tk.Label(self.root, text="Registro de Pedidos", font=("Arial", 18, "bold")).pack(pady=10)

        # --- Frame Principal ---
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20)

        # --- Coluna Esquerda: Menu de Seleção ---
        self.menu_frame = tk.LabelFrame(main_frame, text="Menu (Clique para Adicionar)", padx=10, pady=10)
        self.menu_frame.pack(side="left", fill="both", expand=True)
        self.atualizar_botoes_menu()

        # --- Coluna Direita: Resumo do Pedido ---
        resumo_frame = tk.LabelFrame(main_frame, text="Resumo do Pedido", padx=10, pady=10)
        resumo_frame.pack(side="right", fill="both", expand=True)

        self.lista_pedido = tk.Listbox(resumo_frame, font=("Arial", 11))
        self.lista_pedido.pack(fill="both", expand=True)

        self.label_total = tk.Label(resumo_frame, text="Total: R$ 0.00", font=("Arial", 14, "bold"), fg="green")
        self.label_total.pack(pady=10)

        # --- Botões de Ação (Conflito resolvido: Exclusão rápida) ---
        btn_remover = tk.Button(resumo_frame, text="Remover Último Item", command=self.remover_ultimo, bg="#ffcccb")
        btn_remover.pack(fill="x", pady=2)

        btn_finalizar = tk.Button(resumo_frame, text="Finalizar e Cobrar", command=self.finalizar_pedido, bg="#90ee90", font=("bold"))
        btn_finalizar.pack(fill="x", pady=5)

        # --- Rodapé: Cadastro de Novos Produtos ---
        cadastro_frame = tk.LabelFrame(self.root, text="Cadastrar Novo Produto (Flexibilidade)", padx=10, pady=5)
        cadastro_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(cadastro_frame, text="Nome:").grid(row=0, column=0)
        self.ent_nome = tk.Entry(cadastro_frame)
        self.ent_nome.grid(row=0, column=1, padx=5)

        tk.Label(cadastro_frame, text="Preço:").grid(row=0, column=2)
        self.ent_preco = tk.Entry(cadastro_frame)
        self.ent_preco.grid(row=0, column=3, padx=5)

        tk.Button(cadastro_frame, text="Adicionar ao Menu", command=self.cadastrar_produto).grid(row=0, column=4, padx=10)

    def atualizar_botoes_menu(self):
        """Atualiza o painel de produtos criando botões para cada item do menu."""
        # Limpa botões existentes para atualizar a lista
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

        for produto, preco in self.menu_produtos.items():
            btn = tk.Button(self.menu_frame, text=f"{produto}\nR$ {preco:.2f}", 
                            width=15, height=3, command=lambda p=produto, v=preco: self.adicionar_item(p, v))
            btn.pack(pady=5, fill="x")

    def adicionar_item(self, nome, preco):
        """Adiciona o item selecionado ao pedido atual e atualiza a visualização."""
        self.pedido_atual.append((nome, preco))
        self.lista_pedido.insert(tk.END, f"{nome} - R$ {preco:.2f}")
        self.atualizar_total()

    def remover_ultimo(self):
        """Remove o último item adicionado ao pedido atual."""
        if self.pedido_atual:
            self.pedido_atual.pop()
            self.lista_pedido.delete(tk.END)
            self.atualizar_total()

    def atualizar_total(self):
        """Recalcula o valor total do pedido e atualiza o rótulo de total."""
        self.total_valor = sum(item[1] for item in self.pedido_atual)
        self.label_total.config(text=f"Total: R$ {self.total_valor:.2f}")

    def cadastrar_produto(self):
        """Lê novo produto do formulário e adiciona ao menu disponível."""
        nome = self.ent_nome.get()
        try:
            preco = float(self.ent_preco.get())
            if nome:
                self.menu_produtos[nome] = preco
                self.atualizar_botoes_menu()
                self.ent_nome.delete(0, tk.END)
                self.ent_preco.delete(0, tk.END)
            else:
                messagebox.showwarning("Erro", "Digite o nome do produto.")
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido. Use ponto para centavos.")

    def finalizar_pedido(self):
        """Exibe o resumo da compra e limpa o pedido para o próximo cliente."""
        if not self.pedido_atual:
            messagebox.showwarning("Aviso", "O pedido está vazio!")
            return
        
        resumo = "\n".join([f"{i[0]}: R$ {i[1]:.2f}" for i in self.pedido_atual])
        mensagem = f"--- RESUMO DO PEDIDO ---\n{resumo}\n\nTOTAL A PAGAR: R$ {self.total_valor:.2f}"
        
        messagebox.showinfo("Pedido Finalizado", mensagem)
        
        # Limpa para o próximo cliente
        self.pedido_atual = []
        self.lista_pedido.delete(0, tk.END)
        self.atualizar_total()

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaPedidos(root)
    root.mainloop()