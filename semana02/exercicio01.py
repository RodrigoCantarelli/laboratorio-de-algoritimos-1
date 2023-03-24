horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario = horasTrabalhadas * 35

if salario < 1000:
    aumento = salario + 300
    print("Seu salario com aumento foi de R$ ",aumento)

else: 
    print("Seu salário foi de: R$ ", salario)
