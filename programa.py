from operacoes import*
import emoji
while True:
    op = int(input("digite 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão: "))
    x= int(input("valor do primeiro número: "))
    y= int(input("valor do segundo número: (não pode ser 0)"))

    if op == 1:
        print(soma(x,y))
        print(emoji.emojize(':thumbs_up:'))
    elif op == 2:
        print(subtracao(x,y))
        print(emoji.emojize(':thumbs_up:'))
    elif op == 3:
        print(multiplicacao(x,y))
    elif op == 4:
        print(divisao(x,y))
        print(emoji.emojize(':thumbs_up:'))

    pergunta = input("você quer continuar? [sim] [não]")
    if pergunta == "não":
        break