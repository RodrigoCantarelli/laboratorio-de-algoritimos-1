def menu ():
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Mostrar saldo")
    print("4 - Sair")
    opc = int(input("Digite a opção desejada: "))

    return opc
    
def mostrarSaldo(saldo):
    print("Seu saldo é: ", saldo)

def sacar(saldo):
    saque = float(input("Digite o valor do saque: "))
    if saque <= saldo:
        saldoFinal = saldo - saque
        print("Saldo apos o saque: ", saldoFinal)
    else: 
        print("Saldo insuficiente!!")
       
    return saldo
    
def depositar(saldo):
    deposito = float(input("Digite o valor do deposito: "))
    
    saldoFinal = saldo + deposito
       
    return saldo

def main ():
    saldo = 0
    opc = 0 
    
    while opc != 4:
        opc = menu()
        
        if opc == 1:
            saldo = sacar(saldo)
        elif opc == 2:
            saldo = depositar(saldo)
        elif opc == 3:
            mostrarSaldo(saldo)
        elif opc == 4:  
            print("até mais !")
        else:
            print("Opção inválida!! ")
        

main()
