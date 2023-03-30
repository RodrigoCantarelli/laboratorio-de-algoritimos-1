### Um professor quer fazer um algoritmo para testar se uma questão de múltipla escolha está certa ###

alternativa = input("Digite a alternativa: ")

if alternativa == "A":
    print("Resposta errada!!")
elif alternativa == "B":
    print("Resposta certa, parabéns !!")
elif alternativa == "C":
    print("Resposta errada!!")
elif alternativa == "D":
    print("Resposta errada!!")
else:
    print("Está alternativa não existe, escolha entre: A, B, C e D")
