#  gênero masculino: 66,47 + (13,75 x peso) 1.203,125 + (5, 003 x altura) 860,516 - (6, 775 x idade) 203,25 = 1926,861
# meus dados: 66.47 + (13.75 x 87.5 = 1.203,125) + (5.003 x 172 = 860,516) - (6,775 x 30 = 203,25) = 1926.861
#  gênero feminino: 655,09 + (9, 563 x peso) + (1,85 x altura) - (4, 676 x idade)

nome_str = input("Digite seu nome ")

print("Olá {}, hoje iremos descobrir a sua Taxa Metabólica Basal "
      "seguindo o cálculo de Harris-Benedict".format(nome_str))

print("Qual o seu sexo?")
while True:
    try:
        sexo = int(input("(1) Masculino, (2) Feminino: "))
        if not 0 < sexo <= 2:
            raise ValueError()
    except ValueError as e:
        print("Valor não permitido, escolha novamente")
    else:
        break

#sexo = int(input("(1) Masculino, (2) Feminino: "))
#if(sexo > 2 or sexo < 1 ):
    #print("Não permitido")

altura = float(input("Digite sua altura em centímetros: "))

peso = float(input("Digite seu peso em kg: "))

idade = int(input("Qual a sua idade? "))

print("Qual o seu nível de atividade física: ")
#nivel_atividade = int(input("(1) sedentário, (2) atividade ligeira, (3) atividade moderada, (4) atividade intensa: "))
while True:
    try:
        nivel_atividade = int(input("(1) sedentário, (2) atividade ligeira, (3) atividade moderada, (4) atividade intensa: "))
        if not 0 < nivel_atividade <= 4:
            raise ValueError()
    except ValueError as e:
        print("Não permitido, escolha novamente")
    else:
        break

if(nivel_atividade == 1):
    nivel_atividade = 1
elif(nivel_atividade == 2):
    nivel_atividade = 1.11
elif(nivel_atividade == 3):
    nivel_atividade = 1.25
elif(nivel_atividade == 4):
    nivel_atividade = 1.48

if(sexo == 1):
    tmb_homem = (66.47 + (13.75 * peso) + (5.003 * altura) - (6.775 * idade))
    print(nome_str + " sua taxa metabólica basal é de aproximadamente {} kcal".format(round(tmb_homem)))
    print(nome_str + " o seu gasto energético diário é de aproximadamente {} "
                     "kcal".format(round(tmb_homem * nivel_atividade)))

if(sexo == 2):
    tmb_mulher = (655.09 + (9.563 * peso) + (1.85 * altura) - (4.676 * idade))
    print(nome_str + " sua taxa metabólica basal é de aproximadamente {} kcal".format(round(tmb_mulher)))
    print(nome_str + " o seu gasto energético diário é de aproximadamente {} "
                     "kcal".format(round(tmb_mulher * nivel_atividade)))
