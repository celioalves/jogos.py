print("***************************************")
print("Olá, bem vindo ao jogo de adivinhação!")
print("***************************************")

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1) :
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input('Digite um número entre 1 e 100: ')
    print("Você digitou:", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        continue

    acertou     = chute == numero_secreto
    chutemaior  = chute > numero_secreto
    chutemenor  = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(chutemaior):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif(chutemenor):
            print("Você errou! Seu chute foi menor que o número secreto.")

print("Fim de jogo")

