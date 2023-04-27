###Escreva um programa que coloque na tela meia árvore de natal com asteriscos. O número de ramos deverá ser introduzido pelo usuário. Exemplos com 4 ramos:###

ramos = int(input("Digite a quantidade de ramos: "))

contador = ""

for algoritmo in range (0,ramos):
    contador += "*"
    print(contador)
