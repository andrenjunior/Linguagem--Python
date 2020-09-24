print('---------------------------------')
print('        JOGO DO ACERTO           ')
print('---------------------------------')
numero_secreto = 42
total_tentativas = 0
rodada = 1
print('PENSANDO EM UM NÚMERO AGORA!! QUAL SERÁ?')
print('QUER TENTAR ACERTAR?')
print('---------------------------------')
print('(1) FACIL (2) MÉDIO (3) DIFÍCIL')
nivel = int(input('Digite o nível: '))
print('---------------------------------')
if (nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1,total_tentativas + 1 ):
    print('Tentaiva {} de {}'.format(rodada,total_tentativas))

    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Você Acertou!!')
        break
    elif (menor):
        print('Você errou !! Seu chute foi menor que o número secreto!!')
    elif (maior):
        print('Você errou!! Seu chute foi maior que o número secreto!!')
          
    
print('---------------------------------')
print('        FIM DO JOGO              ') 
print('---------------------------------')   
    


