import forca
import adivinha_numero

def escolhe_jogo():
    print("*********************************")
    print("******Bem vindo aos jogos!*******")
    print("*******Escolha o seu jogo********")
    print("*********************************")

    print("Digite 1 para Jogo de adivinhação.")
    print("Digite 2 para Jogo da Forca.")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando adivinhação")
        adivinha_numero.jogar()
    elif (jogo == 2):
        print("Jogando forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()