def dobro(valor):
    dobroValor = valor * 2
    print("Dobro do valor: ", dobroValor)

def triplo(valor):
    triploValor = valor * 3
    print("Triplo do valor: ", triploValor)

def main():
    valor = float(input("Digite um valor: "))
    
    dobro(valor)
    triplo(valor)
    
main()
