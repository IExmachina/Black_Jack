from random import *


cardsvalue = ('Ás', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2)
naipes = ("Espada", 'Copas', 'Paus', 'Ouro')

print('Olá, meu nome é Eva.\nSerei sua anfitriã e adversária neste jogo.\nBoa sorte!')

def get_2_cards():
    """
    Não recebe argumentos.
    :return: Gera 2 cartas de baralho pseudo-aleatoria.(Pode repetir)
    """
    card1 = choice(cardsvalue)
    card2 = choice(cardsvalue)
    naipe1 = choice(naipes)
    naipe2 = choice(naipes)
    return print(f'Suas cartas são {card1} de {naipe1} e {card2} de {naipe2}.')


def get_1_card():
    """
    Não recebe argumentos.
    :return: Gera 1 carta de baralho pseudo-aleatoria.(Pode repetir)
    """
    card = choice(cardsvalue)
    naipe = choice(naipes)
    return print(f'Sua carta é {card} de {naipe}.')

def two_cards_to_ia():
    card1 = choice(cardsvalue)
    card2 = choice(cardsvalue)
    naipe1 = choice(naipes)
    naipe2 = choice(naipes)
    retia = card1 + card2 + 2
    return retia, print(f'Tirei duas cartas do baralho. Elas são {card1} de {naipe1} e {card2} de {naipe2}.')



start = input('Você gostaria de receber suas cartas agora? Se sim, aperte enter:')

get_2_cards()

whatnow = input('Você gostaria de mais uma carta? Digite "sim" ou "não":')

if whatnow == 'sim':
    print('Ok, aqui está.')
    get_1_card()
    onemore = input('Você gostaria de mais uma carta? Digite "sim" ou "não":')
    if onemore == 'sim':
        print('Ok, aqui está.')
        get_1_card()
        twomore = input('Você gostaria de mais uma carta? Digite "sim" ou "não":')
        if twomore == 'sim':
            print('Ok, aqui está.')
            get_1_card()
            treemore = input('Você gostaria de mais uma carta? Digite "sim" ou "não":')
            if treemore == 'sim':
                print('Ok, aqui está.')
                get_1_card()
                lastone = input('Você gostaria de mais uma carta? Digite "sim" ou "não":')
                if lastone == 'sim':
                    print("Você estourou. Eu ganhei!")
                elif lastone == 'não':
                    print('Ok, então será minha vez agora.')
                    card1 = choice(cardsvalue)
                    card2 = choice(cardsvalue)
                    naipe1 = choice(naipes)
                    naipe2 = choice(naipes)

                    print(f'Minhas cartas são {card1} de {naipe1} e {card2} de {naipe2}.')

                    if 'K' == card1:
                        card1 = 10
                    elif 'Q' == card1:
                        card1 = 10
                    elif 'J' == card1:
                        card1 = 10

                    if 'K' == card2:
                        card2 = 10
                    elif 'Q' == card2:
                        card2 = 10
                    elif 'J' == card2:
                        card2 = 10

                    sumcards = card1 + card2

                    print(f'A soma das minhas cartas é {sumcards}.')
                    while sumcards < 19:
                        print('Vou pegar mais uma carta')
                        ca = choice(cardsvalue)
                        na = choice(naipes)
                        print(f'Peguei a carta {ca} de {na}')
                        if 'K' == ca:
                            ca = 10
                        elif 'Q' == ca:
                            ca = 10
                        elif 'J' == ca:
                            ca = 10
                        sumcards = sumcards + ca

                    total = sumcards
                    print(f'Parei. O total da soma de minha carta é {total}')

                    if total == 21:
                        print('Tirei 21! Eu ganhei!')
                    elif total > 21:
                        print('Eu perdi. Parabens vc venceu!')
                    elif total in range(16, 20):
                        winner = input('Quem ganhou?')
                        if winner == 'Voce':
                            print('Eu ganhei!!!')
                        elif winner == 'Eu':
                            print('Parabens, vc venceu!')

            elif treemore == 'não':
                print('Ok, então será minha vez agora.')
                card1 = choice(cardsvalue)
                card2 = choice(cardsvalue)
                naipe1 = choice(naipes)
                naipe2 = choice(naipes)

                print(f'Minhas cartas são {card1} de {naipe1} e {card2} de {naipe2}.')

                if 'K' == card1:
                    card1 = 10
                elif 'Q' == card1:
                    card1 = 10
                elif 'J' == card1:
                    card1 = 10

                if 'K' == card2:
                    card2 = 10
                elif 'Q' == card2:
                    card2 = 10
                elif 'J' == card2:
                    card2 = 10

                sumcards = card1 + card2

                print(f'A soma das minhas cartas é {sumcards}.')
                while sumcards < 19:
                    print('Vou pegar mais uma carta')
                    ca = choice(cardsvalue)
                    na = choice(naipes)
                    print(f'Peguei a carta {ca} de {na}')
                    if 'K' == ca:
                        ca = 10
                    elif 'Q' == ca:
                        ca = 10
                    elif 'J' == ca:
                        ca = 10
                    sumcards = sumcards + ca

                total = sumcards
                print(f'Parei. O total da soma de minha carta é {total}')

                if total == 21:
                    print('Tirei 21! Eu ganhei!')
                elif total > 21:
                    print('Eu perdi. Parabens vc venceu!')
                elif total in range(16, 20):
                    winner = input('Quem ganhou?')
                    if winner == 'Voce':
                        print('Eu ganhei!!!')
                    elif winner == 'Eu':
                        print('Parabens, vc venceu!')

        elif twomore == 'não':
            print('Ok, então será minha vez agora.')
            card1 = choice(cardsvalue)
            card2 = choice(cardsvalue)
            naipe1 = choice(naipes)
            naipe2 = choice(naipes)

            print(f'Minhas cartas são {card1} de {naipe1} e {card2} de {naipe2}.')

            if 'K' == card1:
                card1 = 10
            elif 'Q' == card1:
                card1 = 10
            elif 'J' == card1:
                card1 = 10

            if 'K' == card2:
                card2 = 10
            elif 'Q' == card2:
                card2 = 10
            elif 'J' == card2:
                card2 = 10

            sumcards = card1 + card2

            print(f'A soma das minhas cartas é {sumcards}.')
            while sumcards < 19:
                print('Vou pegar mais uma carta')
                ca = choice(cardsvalue)
                na = choice(naipes)
                print(f'Peguei a carta {ca} de {na}')
                if 'K' == ca:
                    ca = 10
                elif 'Q' == ca:
                    ca = 10
                elif 'J' == ca:
                    ca = 10
                sumcards = sumcards + ca

            total = sumcards
            print(f'Parei. O total da soma de minha carta é {total}')

            if total == 21:
                print('Tirei 21! Eu ganhei!')
            elif total > 21:
                print('Eu perdi. Parabens vc venceu!')
            elif total in range(16, 20):
                winner = input('Quem ganhou?')
                if winner == 'Voce':
                    print('Eu ganhei!!!')
                elif winner == 'Eu':
                    print('Parabens, vc venceu!')

    elif onemore == 'não':
        print('Ok, então será minha vez agora.')
        card1 = choice(cardsvalue)
        card2 = choice(cardsvalue)
        naipe1 = choice(naipes)
        naipe2 = choice(naipes)

        print(f'Minhas cartas são {card1} de {naipe1} e {card2} de {naipe2}.')

        if 'K' == card1:
            card1 = 10
        elif 'Q' == card1:
            card1 = 10
        elif 'J' == card1:
            card1 = 10

        if 'K' == card2:
            card2 = 10
        elif 'Q' == card2:
            card2 = 10
        elif 'J' == card2:
            card2 = 10

        sumcards = card1 + card2

        print(f'A soma das minhas cartas é {sumcards}.')
        while sumcards < 19:
            print('Vou pegar mais uma carta')
            ca = choice(cardsvalue)
            na = choice(naipes)
            print(f'Peguei a carta {ca} de {na}')
            if 'K' == ca:
                ca = 10
            elif 'Q' == ca:
                ca = 10
            elif 'J' == ca:
                ca = 10
            sumcards = sumcards + ca

        total = sumcards
        print(f'Parei. O total da soma de minha carta é {total}')

        if total == 21:
            print('Tirei 21! Eu ganhei!')
        elif total > 21:
            print('Eu perdi. Parabens vc venceu!')
        elif total in range(16, 20):
            winner = input('Quem ganhou?')
            if winner == 'Voce':
                print('Eu ganhei!!!')
            elif winner == 'Eu':
                print('Parabens, vc venceu!')

elif whatnow == 'não' or 'nao':
    print('Ok, então será minha vez agora.')
    card1 = choice(cardsvalue)
    card2 = choice(cardsvalue)
    naipe1 = choice(naipes)
    naipe2 = choice(naipes)

    print(f'Minhas cartas são {card1} de {naipe1} e {card2} de {naipe2}.')

    if 'K' == card1:
        card1 = 10
    elif 'Q' == card1:
        card1 = 10
    elif 'J' == card1:
        card1 = 10

    if 'K' == card2:
        card2 = 10
    elif 'Q' == card2:
        card2 = 10
    elif 'J' == card2:
        card2 = 10

    sumcards = card1 + card2

    print(f'A soma das minhas cartas é {sumcards}.')
    while sumcards < 19:
        print('Vou pegar mais uma carta')
        ca = choice(cardsvalue)
        na = choice(naipes)
        print(f'Peguei a carta {ca} de {na}')
        if 'K' == ca:
            ca = 10
        elif 'Q' == ca:
            ca = 10
        elif 'J' == ca:
            ca = 10
        sumcards = sumcards + ca

    total = sumcards
    print(f'Parei. O total da soma de minha carta é {total}')

    if total == 21:
        print('Tirei 21! Eu ganhei!')
    elif total > 21:
        print('Eu perdi. Parabens vc venceu!')
    elif total in range(16, 20):
        winner = input('Quem ganhou?')
        if winner == 'Voce':
            print('Eu ganhei!!!')
        elif winner == 'Eu':
            print('Parabens, vc venceu!')




