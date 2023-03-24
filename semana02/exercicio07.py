### Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde ´ h corresponde a altura): ###

altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo: ")

if sexo == "masculino":
    pesoIdealHomens = (72.7 * altura) - 58
    print("Seu peso ideal é: ", pesoIdealHomens)
else:
    pesoIdealMulheres = (62.1 * altura) - 44.7
    print("Seu peso ideal é: ", pesoIdealMulheres)
