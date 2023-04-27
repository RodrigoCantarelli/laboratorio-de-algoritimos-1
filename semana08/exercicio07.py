###Faça um algoritmo que peça dois números para o usuário (o primeiro sempre será menor que o segundo), posteriormente apresente somente os números pares no intervalo entre os dois número###

primeiro = int(input("Digite o primeiro valor: "))
ultimo = int(input("Digite o ultimo valor: "))

if primeiro > ultimo:
    aux = primeiro
    primeiro = ultimo
    ultimo = aux

for numero in range (primeiro + 1, ultimo):
    if numero % 2 == 0:
        print("Numero par entre o intervalo: ", numero)
