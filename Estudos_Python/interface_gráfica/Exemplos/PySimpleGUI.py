import PySimpleGUI as sg

# Configura tema de interface
sg.theme('DarkAmber')

# Define o layout do formulário em uma lista de linhas
layout = [
    [sg.Text('Texto na linha 1')],
    [sg.Text('Entre com um texto na linha 2'), sg.InputText(key='-INPUT-')],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

# Cria a janela com título e layout
window = sg.Window('Bem-Vindo ao PySimpleGUI', layout)

# Loop principal de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    # Exibe valor do campo de entrada
    print('Você entrou com:', values['-INPUT-'])

window.close()