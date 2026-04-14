import tkinter as tk

# Exemplo simples de janela Tkinter com um rótulo.
# tkinter._test() é útil para validar instalação, mas aqui criamos uma janela controlada.

def main():
    root = tk.Tk()
    root.title('Exemplo Tkinter')

    label = tk.Label(root, text='Olá, Mundo!')
    label.pack(padx=20, pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()