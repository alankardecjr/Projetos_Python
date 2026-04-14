from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        # Retorna um botão simples como conteúdo principal da aplicação
        return Button(text='Olá, Mundo!')


if __name__ == '__main__':
    # Inicia o loop principal do Kivy
    ExemploApp().run()