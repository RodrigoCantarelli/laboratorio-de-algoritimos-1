### Escreva um programa que imprima na tela a sequência de Fibonacci até o décimo termo utilizando o laço de repetição for.###

anterior = 0
proximo = 1
ultimo = 1

for numero in range (0,11):
    print(anterior)
    soma = proximo + anterior
    anterior = proximo
    proximo = soma
