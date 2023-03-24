### Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.###

valorDesejado = float(input("Escreva o valor que você deseja colocar de gasolina: "))
valorGasolina = float(input("Escreva o valor atual do litro da gasolina: "))

litrosGasolina = valorDesejado / valorGasolina

print("Com o valor de R$",valorDesejado, ", você irá poder colocar ",litrosGasolina, "litros de gasolina!!")
