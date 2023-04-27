###Foi realizada uma pesquisa de algumas características físicas da população de um certa região.###

qtdInd = 0
qtdAzuis = 0
qtdVerdes = 0 
qtdCabelosCastanhos = 0 
qtdLoiros = 0 
qtdOlhosCastanhos = 0 
qtdPretos = 0 
qtdM = 0 
qtdF = 0
maiorIdade = 0

for entrevistados in range (1,16):
    sexo = input("Digite o seu sexo - M (masculino) e F (feminino): ")
    olhos = input("Digite a cor dos olhos - A (azuis), V (verdes) e C (castanhos): ")
    cabelos = input("Digite a cor dos cabelos - L (loiros), C (castanhos) e P (pretos): ")
    idade = int(input("Digite a sua idade: "))
   
    if idade > maiorIdade:
        maiorIdade = idade
    
    if idade > 17 and idade < 36 and sexo == "F" and olhos == "V" and cabelos == "L":
        qtdInd = qtdInd + 1 
    
    elif olhos == "A":
        qtdAzuis += 1
        mediaAzuis = (qtdAzuis*100)/ 15

    elif olhos == "V":
        qtdVerdes += 1
        mediaVerdes = (qtdVerdes*100)/ 15

    elif olhos == "A":
        qtdOlhosCastanhos += 1
        mediaOlhosCastanhos = (qtdOlhosCastanhos*100)/ 15
        
    elif cabelos == "L":
        qtdLoiros += 1
        mediaLoiros = (qtdLoiros*100)/ 15

    elif cabelos == "C":
        qtdCabelosCastanhos += 1
        mediaCabCastanhos = (qtdCabelosCastanhos*100)/ 15

    elif cabelos == "P":
        qtdPretos += 1
        mediapPretos = (qtdPretos*100)/ 15

    elif sexo == "M":
        qtdM += 1
        mediaMasculinos = (qtdM*100)/ 15
        
    elif sexo == "F":
        qtdF += 1
        mediaFemininos = (qtdF*100)/15

print("Maior idade: ", maiorIdade)
print("Quantidade total: ", qtdInd)
print("Porcentagem de olhos Azuis: ", mediaAzuis)
print("Porcentagem de olhos Verdes: ", mediaVerdes)
print("Porcentagem de olhos Castanhos: ", mediaOlhosCastanhos)
print("Porcentagem de cabelos Loiros: ", mediaLoiros)
print("Porcentagem de cabelos Castanhos : ", mediaCabCastanhos)
print("Porcentagem de cabelos Pretos : ", mediapPretos)
print("Porcentagem de Masculinos : ", mediaMasculinos)
print("Porcentagem de Femininos: ", mediaFemininos)
