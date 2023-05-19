###Faça um algoritmo que leia tenha um vetor e apresente o seguinte menu###

def inserirValor(valores):
    
    valor = int(input("Digite o valor: "))
    valores.append(valor)

    print("Valor inserido com sucesso!")
    return valores

def excluirValor(valores):
    valor = int(input("Qual valor excluir: "))
    valores.remove(valor)
    
    print("Valor removido com sucesso!")
    return valores

def listarValor(valores):
    print("Os valores listados no menu são: ",valores)

def main():
    valores = []

    opc = 0    
    while opc != 4:
        opc = int(input("Opção 1 - Inserir\nOpção 2 - Retirar\nOpção 3 - Listar\nOpção 4 - Sair "))
        if opc == 1:
            valores = inserirValor(valores)
        if opc == 2:
            valores = excluirValor(valores)
        if opc == 3:
            listarValor(valores)
        if opc == 4:
            print("Até logo !")
    
main()
