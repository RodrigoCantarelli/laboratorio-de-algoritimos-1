### Faça um algoritmo que leia dois valores e apresente: ###

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

if v1 > v2:
    print(v2,"<", v1)
elif v2 > v1:
    print(v1, "<", v2)
elif v1 == v2:
    print(v1, "=", v2)
