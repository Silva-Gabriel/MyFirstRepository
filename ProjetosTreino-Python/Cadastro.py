from PySimpleGUI import PySimpleGUI as sg
from time import sleep
sg.theme('LightBlue2')
ordem = [
    [sg.Text('Nome'),sg.Input(key='Nome',size=(20,1),background_color='#7FFFD4')],
    [sg.Text('Sobrenome'),sg.Input(key='Sobrenome',size=(20,1,5),background_color='#7FFFD4')],
    [sg.Text('CPF'), sg.Input(key='CPF',size=(20,1),background_color='#7FFFD4')],
    [sg.Text('Estado'), sg.Input(key='Estado',size=(20,1),background_color='#7FFFD4')],
    [sg.Text('Cidade'), sg.Input(key='Cidade',size=(20,1),background_color='#7FFFD4')],
    [sg.Button('Cadastrar',size=(15,1))]
    ]
janela = sg.Window('Login Screen',ordem)
while True:
    actions,values = janela.read()
    if actions == sg.WINDOW_CLOSED:
        break
    if actions == 'Cadastrar':
        if (values['Nome'] != '' and values['Sobrenome'] != '' and values['CPF'] != '' and values['Estado'] != '' and values['Cidade'] != ''):
            print('\033[034mNome:',values['Nome'])
            print('\033[034mSobrenome:',values['Sobrenome'])
            if len(values['CPF']) == 11:
                teste = values['CPF'].zfill(11)
            cpf = '{}.{}.{}-{}'.format(values['CPF'][:3], values['CPF'][3:6], values['CPF'][6:9], values['CPF'][9:])
            print(f'\033[034mCPF: {cpf[:14]}')
            print('\033[034mEstado: ',values['Estado'])
            print('\033[034mCidade: ',values['Cidade'])
            print('\033[033mCadastro efetuado com sucesso!')
        else:
            print('\033[031mOs campos não foram preenchidos corretamente,tente novamente mais tarde!\n O programa será encerrado em...')
            sleep(2)
            print('\033[036m3...')
            sleep(1.5)
            print('\033[033m2...')
            sleep(1.5)
            print('\033[031m1...')
            print('\033[034mEND')
            exit()





