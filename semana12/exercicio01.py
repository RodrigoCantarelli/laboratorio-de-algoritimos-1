def lerValores(valores):
    for n in range(0, 10):
        valor = int(input("Digite um valor: "))
        valores.append(valor)
        
    print(valores)
    return valores, valor
    
def maior(valores):
    maiores = []
    for n in valores:
        if n > 100:
            maiores.append(n)
            
    print("Valores maiores que 100: ",maiores)


def main():
    valores = []
    
    valores, valor = lerValores(valores)
    maior(valores)
    
main()
