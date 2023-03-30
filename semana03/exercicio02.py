### Um sistema de uma loja de roupas permite que as peças de roupas sejam vendidas de três formas diferentes: ###

valorRoupa = float(input("Digite o valor da roupa: "))
print("1 - Pagamento à vista")
print("2 - Pagamento em 2x")
print("3 - Pagamento em 3x ")
opcao = int(input("Digite a opção de pagamento: "))

if opcao  == 1:
    print("O valor da roupa à vista é R$ ",valorRoupa)
elif opcao == 2:
    valorRoupa = valorRoupa / 2 
    print("O valor da roupa em 2x é de: R$",valorRoupa)
elif opcao == 3:
    valorRoupa = valorRoupa / 3
    print("O valor da roupa em 3x é de: R$",valorRoupa)
