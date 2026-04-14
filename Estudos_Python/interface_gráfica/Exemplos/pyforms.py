import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

class ExemploSimples(BaseWidget):

    def __init__(self):
        super(ExemploSimples, self).__init__('ExemploSimples')
        # Definition of the form fields
        self._nome = ControlText('Nome', 'Default value')
        self._sobrename = ControlText('Sobrenome')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Pressione o Botão')

        # O botão foi criado, mas o exemplo minimalista não implementa callback.
        # Em um aplicativo real, use self._button.value = self.on_button_pressed ou
        # self._button = ControlButton('Pressione o Botão', default=self.on_button_pressed)


# Execute the application
if __name__ == '__main__':
    from pyforms import start_app
    start_app(ExemploSimples)