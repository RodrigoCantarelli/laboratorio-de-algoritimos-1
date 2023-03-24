### Ano e se pode votar ###
anoNascimento = int(input("Digite o ano do seu nascimento: "))

idade = 2023 - anoNascimento

if idade >= 18:
    print("Sua idade é: ",idade,", você já pode votar!! ")
else:
    print("Sua idade é:",idade, ", você não pode votar!!")
