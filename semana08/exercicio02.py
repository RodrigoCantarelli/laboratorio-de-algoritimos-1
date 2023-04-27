###Crie um programa que calcule e exiba na tela a média aritmética de um conjunto de 10 números lidos do usuário utilizando o laço de repetição for.###

media = 0 

for numero in range (1, 11):
    numero = int(input("Digite um número: "))
    media = media + numero
    
media = media / 10
print("Media dos números: ", media)
