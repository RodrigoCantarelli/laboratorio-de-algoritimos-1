def aprovado(media):
    print("Parabéns, você foi aprovado com média: ", media)

def recuperacao(media):
    print("Você está em exame, com média: ", media)

def reprovado(media):
    print("Você foi reprovado, com média: ", media)    

def main():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))
    n5 = float(input("Digite a quinta nota: "))
    media = (n1 + n2 + n3 + n4 + n5) / 5
    
    if media >= 7:
        aprovado(media)
    elif media >= 4 and media < 7:
        recuperacao(media)
    else:
        reprovado(media)
    
main()
