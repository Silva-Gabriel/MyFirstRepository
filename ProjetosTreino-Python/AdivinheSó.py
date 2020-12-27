#Um jogo simples de adivinhação de números.
#Jogue contra a máquina e veja se sua sorte está a favor ou contra você!
import random
import time
contadorDeTentativas = 0
IA= random.randint(1,20)
print("\033[035mEstou pensando em um número de 1 à 20***")
time.sleep(1)
print("Tente adivinhar qual é...")
PLAYER = 1
while(PLAYER != IA):
    if(PLAYER <= 20 and PLAYER >= 1):
        PLAYER = int(input("\033[036mSua tentativa: "))
        if(PLAYER > IA):
            print("\033[031mUm pouco menos...")
        elif(PLAYER < IA):
            print("\033[032mUm pouco mais...")
        contadorDeTentativas += 1
    else:
        PLAYER = int(input("ERRO...Digite novamente sua tentativa: "))
print(f"\033[033mVocê acertou!")
time.sleep(2)
if(contadorDeTentativas <= 5):
    print("*************************************************************")
    print(f"Parabéns,você é um bruxo?Precisou somente de {contadorDeTentativas} tentativas.")
    print("*************************************************************")
elif(contadorDeTentativas > 5 and contadorDeTentativas <= 10):
    print("************************************************************************************************************")
    print(f"Parabéns,você precisou de {contadorDeTentativas} tentativas,tente novamente e melhore sua sorte com números :)")
    print("*************************************************************************************************************")
else:
    print("*****************************************************************************************")
    print(f"Parabéns,você demorou um pouco,mas conseguiu acertar,seu número de tentativas foi:{contadorDeTentativas}")
    print("*****************************************************************************************")



