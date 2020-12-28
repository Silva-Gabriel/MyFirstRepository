from PySimpleGUI import PySimpleGUI as sg
sg.theme('LightBrown13')
org = [
    [sg.Text('Username'),sg.Input(key='Username',size=(20,2))],
    [sg.Text('Password'),sg.Input(key='Password', password_char='*',size=(20,2))],
    [sg.Text('ID number'), sg.Input(key='ID number', password_char='*', size=(20, 2))],
    [sg.Checkbox('Save login?')],
    [sg.Button('Login',size=(30,1))]
]
janela = sg.Window('Login Screen',org)
while True:
    actions,values = janela.read()
    if actions == sg.WINDOW_CLOSED:
        break
    if actions == 'Login':
        if values['Username'] == 'gabriel' and values['Password'] == 'soldierspy14' and values['ID number'] == 'M3UN0M3G@BR13L':
            print('\033[036mWelcome,this is my first graphical interface!')
        else:
            print('\033[031mInvalid Username or Password,try again.')






