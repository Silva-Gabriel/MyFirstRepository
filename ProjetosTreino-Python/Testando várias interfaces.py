from PySimpleGUI import PySimpleGUI as sg
def janela_login():
    layout = [
        [sg.Text('Name')],
        [sg.Input()],
        [sg.Button('Próximo')]

    ]
    return sg.Window('Login',layout,finalize=True)


def janela_pedido():
    sg.theme('reddit')
    layout = [
        [sg.Text('Fazer pedido')],
        {sg.Checkbox('Pizza Mussa', key='pizza1'), sg.Checkbox('pizza frango c/ Catupiry', key='pizza2')},
        [sg.Button('Voltar'), sg.Button('Fazer pedido')]
    ]
    return sg.Window('Montar pedido',layout, finalize=True)


janela1, janela2 = janela_login(), None
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Próximo':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Pizza 1 e 2')
        elif values['pizza1'] == True:
            sg.popup('Pizza 1')
        elif values['pizza2'] == True:
            sg.popup('Pizza 2')
