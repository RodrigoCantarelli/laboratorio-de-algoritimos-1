def totalLaranjas(laranjas):
    if laranjas <= 12:
        valorLaranja = laranjas * 0.4
        
    else:
        valorLaranja = laranjas * 0.25
    
    print("Quantidade de laranjas: ", laranjas, ", Preço total: R$", valorLaranja)

def main():
    laranjas = int(input("Digite o total de laranjas: "))
    
    totalLaranjas(laranjas)
    
main()
