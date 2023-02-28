import random  # importando biblioteca random, visto que está não é uma built-in

def jogar():

    nome_str = input("Digite seu nome ")

    print("*********************************************************************************")
    print("Olá " + nome_str + ", Seja bem ao super jogo de adivinhação")
    print("**********************************************************************************")

    total_de_tentativas = 0
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("qual o nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina o nível:"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("O número deve estar entre 1 e 100!!")

        chutemaior = chute > numero_secreto
        chutemenor = chute < numero_secreto
        acertou = chute == numero_secreto

        if(acertou):
            print("Parabéns, você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(chutemaior):
                print("Que pena, seu chute foi maior do que o número secreto.")

            elif(chutemenor):
                print("Que pena, seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim do jogo")
    print("O número secreto era " + numero_secreto.__str__())

if (__name__ == "__main__"):
    jogar()