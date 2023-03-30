### Faça um algoritmo que apresente qual veículo o usuário pode dirigir ###

carteira = input("Digite a sua carteira atual: ")

if carteira == "A":
    print("Você pode dirigir motos e triciclos !!")
elif carteira == "B":
    print("Você pode dirigir carros de passeio!!")
elif carteira == "C":
    print("Você pode dirigir veículos de carga acima de 3,5 toneladas!!")
elif carteira == "D":
    print("Você pode dirigir veículos com mais de 8 passageiros !!")
elif carteira == "E":
    print("Você pode dirigir veículos com unidade acoplada acima de 6 toneldas!!")
