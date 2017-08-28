from random import sample


def generar_mazo():
    return sample([(x, y) for x in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for y in
                   ['PICAS', 'TREBOLES', 'DIAMANTES', 'CORAZONES']], 52)


def valor_carta(carta):
    if carta[0] == 'J' or carta[0] == 'K' or carta[0] == 'Q':
        return 10
    if carta[0] == 'A':
        return 1
    return int(carta[0])


def valor_mano(mano):
    if len(mano) <= 0:
        return 0
    return valor_carta(mano[0]) + valor_mano(mano[1:])



def jugar(mazo, casa, jugador, turno):
    if mazo != []:

        print("Casa: [('X', 'XXXXX')],  ", casa[1:])
        print("Jugador:", jugador)
        if(valor_mano(casa) < 21 and valor_mano(jugador) < 21):
             if len(casa) == 0 and len(jugador) == 0:
                 return jugar(mazo[4:], casa + [mazo[0]] + [mazo[1]], jugador + [mazo[2]] + [mazo[3]], turno)
             if valor_mano(jugador) < 21 and turno == True:
                 if (input("Si desea otra carta, oprima 1 de lo contrario oprima 0: ") != 0):
                    return jugar(mazo[1:], casa, jugador + [mazo[1]], turno)
                 return jugar(mazo, casa, jugador, False)
             if(valor_mano(casa) < valor_mano(jugador)):
                return jugar(mazo[1:], casa + [mazo[1]], jugador, turno)
        if valor_mano(casa) > 21:
            print("\n\nEL JUGADOR HA GANADO, las cartas de cada uno fueron:")

            print("Casa:   ", casa, " Suma: ", valor_mano(casa))
            print("Jugador:", jugador, " Suma: ", valor_mano(jugador))
        else:
            print("\n\nLA CASA HA GANADO, las cartas de cada uno fueron:")

            print("Casa:   ", casa, " Suma: ", valor_mano(casa))
            print("Jugador:", jugador, " Suma: ", valor_mano(jugador))


jugar(generar_mazo(),[], [], True)