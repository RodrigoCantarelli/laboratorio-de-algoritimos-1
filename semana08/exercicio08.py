###Utilizando a estrutura de repetição for, faça um programa em python que receba 10 números e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.###

qtdEntre = 0
qtdFora = 0

for entrevistados in range (0,10):
    numero = int(input("Digite o número: "))
    if numero > 10 and numero < 20:
        qtdEntre += 1
    else:
        qtdFora += 1

print("Quantidade de números entre 10 e 20: ", qtdEntre)
print("Quantidade de números fora do intervalo", qtdFora)
