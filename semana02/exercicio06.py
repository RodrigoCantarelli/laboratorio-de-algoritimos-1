### Leia um número fornecido pelo usuário. Se esse número for positivo, apresente o dobro do valor digitado. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.###
n1 = int(input("Digite um número: "))

if n1 >= 0:
    dobro = n1 * 2
    print("O dobro do seu número é: ", dobro)
else:
    print("Seu número é inválido!!")
