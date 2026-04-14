from flexx import flx

class Exemplo(flx.Widget):

    def init(self):
        # Dois botões simples na mesma tela
        flx.Button(text='Olá')
        flx.Button(text='Mundo')


if __name__ == '__main__':
    # Cria e inicializa o aplicativo Flexx
    a = flx.App(Exemplo, title='Flexx demonstração')
    m = a.launch()
    flx.run()