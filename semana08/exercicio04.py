### Faça um algoritmo que leia 10 números inteiros e ao final apresente: ###

somaPar = 0
somaZero = 0 
somaImpar = 0

for numero in range (1, 11):
    numero = int(input("Digite um número: "))
    if numero == 0:
        somaZero = somaZero + 1

    elif numero % 2 == 0:
        somaPar = somaPar + 1

    else:
        somaImpar = somaImpar + 1

print("Total Par: ",somaPar)
print("Total Zero: ",somaZero)
print("Total Impar: ",somaImpar)
