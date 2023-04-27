###ma empresa de pesquisa deseja saber qual jornal é mais lido em Santa Maria (A, B ou C). Faça um algoritmo que leia a opinião de 20 pessoas, ao final mostre a porcentagem de cada uma das revistas, em ordem crescente###

qtdA = 0
qtdB = 0
qtdC = 0
 
for entrevistado in range (1,21):
    resposta = input("Digite qual o jornal você prefere (A,B ou C): ")
    if resposta == "A":
        qtdA += 1
        porcentagemA = (qtdA * 100)/20

    elif resposta == "B":
        qtdB += 1
        porcentagemB = (qtdB * 100)/20
        
    elif resposta == "C":
        qtdC += 1
        porcentagemC = (qtdC * 100)/20
        
print("Porcentagem que preferem A: ", porcentagemA)
print("Porcentagem que preferem B: ", porcentagemB)
print("Porcentagem que preferem C: ", porcentagemC)
