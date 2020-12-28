n = int(input('Digite a quantidade de termos da sequência: '))
atual = 1
anterior = 0
proximo = 1
contador = 0
print('\033[035m=============================')
print('---SEQUÊNCIA DE FIBONACCI---')
print('\033[035m=============================')
for contador in range(n-1):
    print('\033[036m{}'.format(atual),end=',')
    proximo = atual + anterior
    anterior = atual
    atual = proximo
print(''.join(str(atual)),end="...")