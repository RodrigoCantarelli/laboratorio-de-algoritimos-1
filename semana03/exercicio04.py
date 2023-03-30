### Faça um algoritmo que leia dois valores. Posteriormente leia uma opção do menu:  ###

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

print("1 - Somar os dois valores")
print("2 - Subtrair os valores")
print("3 - Multiplicar os valores")
print("4 - Dividir os valroes")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    valor = v1 + v2
    print("Seu valor somado é: ",valor)
elif opcao == 2:
    valor = v1 - v2
    print("Seu valor subtraido é: ",valor)
if opcao == 3:
    valor = v1 * v2
    print("Seu valor multiplicado é: ",valor)
if opcao == 4:
    valor = v1 / v2
    print("Seu valor subtraido é: ",valor)
