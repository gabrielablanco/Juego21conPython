from random import *


def generar_mazo():
    return sample([(x, y) for x in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for y in ['PICAS', 'TREBOLES', 'DIAMANTES', 'CORAZONES']], 52)


def mano_A(mano):
    if mano == []:
        return 0
    return valor_carta(mano[0], True) + mano_A(mano[1:])


def valor_carta(carta, valor):  # Si valor es verdadero, cuenta la cantidad de ases; valor es Falso cuenta las cartas con As valiendo 1
    if (str(carta[0]) in "JQK") and (not valor):
        return 10
    if (carta[0] == 'A' and (not valor)):
        return 1
    else:
        if (carta[0] == 'A') and (valor):
            return 1
        elif (valor):
            return 0
    return int(carta[0])


def valor_mano(mano_A, mano, aux):  # Verifica el valor de la mano y tiene en cuenta los Ases
    if mano == []:
        if (mano_A == 0):
            return aux
        else:
            if (aux + 10 <= 21 - (mano_A - 1)):  # Verifica si se pueden sumar ases con valor 11 dependiendo del puntuja
                return valor_mano(mano_A - 1, mano, aux + 10)  # Como ya se sumaron los ases con valor 1, solo se suma 10 si es necesario
            else:
                return aux
    if (valor_carta(mano[0], False) == 1):
        return valor_mano(mano_A, mano[1:], aux + 1)
    else:
        return valor_mano(mano_A, mano[1:], aux + valor_carta(mano[0], False))


def jugar(mazo, casa, jugador, turno):
    if mazo != []:
        if (casa == [] and jugador == []):  
            return jugar(mazo[4:], casa + mazo[:2], jugador + mazo[2:4], True)
        if (valor_mano(mano_A(casa), casa, 0) <= 21 and valor_mano(mano_A(jugador), jugador, 0) <= 21): 
            imprimir_cartas(casa, jugador, turno, False)
            if (seguir_turno(turno)):  
                if (jugada_casa(casa)):
                    if (valor_mano(mano_A(jugador + [mazo[0]]), jugador + [mazo[0]], 0) < 21):
                        return jugar(mazo[2:], casa + [mazo[1]], jugador + [mazo[0]], turno)
                    else:
                        return jugar(mazo[1:], casa, jugador + [mazo[0]], turno)
                        imprimir_cartas(casa, jugador, turno, True)
                else:
                    return jugar(mazo[1:], casa, jugador + [mazo[0]], turno)
            else:
                if (jugada_casa(casa) and valor_mano(mano_A(jugador), jugador, 0) <= 21):
                    return jugar(mazo[1:], casa + [mazo[0]], jugador, False)
                else:
                    imprimir_cartas(casa, jugador, turno, True)
        else:
            imprimir_cartas(casa, jugador, turno, True)


def jugada_casa(casa):
    if (valor_mano(mano_A(casa), casa, 0) < 18):
        return True
    else:
        return False

def seguir_turno(respuesta):  # Confirma si quiere mas cartas, sino solo juega la casa
    if (respuesta):
        if (input("\nSi desea otra carta, oprima 1 de lo contrario oprima 0: ") == 1):
            return True

def imprimir_cartas(casa, jugador, turno, finalizo):  # Impresiones por pantalla
    if (finalizo):
        print("\nFIN DEL JUEGO\n")
        print ("Los resultados fueron\n: ")
        print("Casa: ", casa)
        print ("Puntaje casa: ", valor_mano(mano_A(casa), casa, False))
        print("Jugador: ", jugador)
        print("Puntaje jugador: ", valor_mano(mano_A(jugador), jugador, False))
        if (valor_mano(mano_A(casa), casa, False) > 21):
            print("EL JUGADOR HA GANADO")
        elif (valor_mano(mano_A(jugador), jugador, False) > 21):
            print("LA CASA HA GANADO")
        elif (valor_mano(mano_A(casa), casa, False) >= valor_mano(mano_A(jugador), jugador, False)):
            print ("LA CASA HA GANADO")
        elif (valor_mano(mano_A(jugador), jugador, False) >= valor_mano(mano_A(casa), casa, False)):
            print ("EL JUGADOR HA GANADO")

    if (finalizo == False):
        print("Casa: [('X', 'XXXXX')],  ", casa[1:])
        print("Jugador: ", jugador)
        print("Puntaje jugador: ", valor_mano(mano_A(jugador), jugador, False))


print(jugar(generar_mazo(), [], [], True))