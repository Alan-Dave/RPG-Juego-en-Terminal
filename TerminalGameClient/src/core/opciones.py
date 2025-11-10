from utils.common import random, time

def elegir_Personaje():
    from utils.commonChar import (Naruto, Sasuke, Ichigo, Aizen, Goku, Vegeta, Alhacen, Kazuha, Iori, Kyo)
    while True:
        eleccion = int(input("\nIntroduce el número de tu elección: "))
        match eleccion:
            case 0:
                rndm = random.choice([
                    Naruto("Naruto"), Sasuke("Sasuke"), Ichigo("Ichigo"),
                    Kyo("Kyo"), Iori("Iori"), Kazuha("Kazuha"), Alhacen("Alhacen"), Vegeta("Vegeta"), Goku("Goku"), Aizen("Aizen")
                ])
                return rndm
            case 1:
                return Naruto('Naruto')
            case 2:
                return Sasuke('Sasuke')
            case 3:
                return Iori('Iori')
            case 4:
                return Kyo('Kyo')
            case 5:
                return Ichigo('Ichigo')
            case 6:
                return Kazuha('Kazuha')
            case 7:
                return Vegeta('Vegeta')
            case 8:
                return Alhacen('Alhacen')
            case 9:
                return Goku('Goku')
            case 10:
                return Aizen('Aizen')
            case _:
                raise ValueError("Elección inválida. Por favor, elige un número válido.")   



def opciones():
    from utils.constants import jugador, oponente
    from eventos import combos, especiales
    from sound import sound
    from utils.colors import Color
    
    try:
        accion = int(input("\nIntroduce el número de tu elección: "))
        match accion:
            case 1:
                print("-------------------------------------")
                jugador.atacar()
                print("")
                oponente.elegir_accion()       
            case 2:
                print("-------------------------------------")
                print(f"\n{Color.CIAN}{jugador.nombre} ha decidido atacar{Color.RESET}")
                time.sleep(2)
                oponente.elegir_accion()
                jugador.atacar()
            case 3:
                print("-------------------------------------")
                jugador.esperar()
                print("")
                oponente.elegir_accion()
            case 4:
                combos()
            case 5:   
                from ui.tienda import Tienda
                Tienda()
            case 6:
                from ui.mochila import Mochila
                Mochila()
            case 7:
                print("-------------------------------------")
                print(f"\n{Color.CIAN}{jugador.nombre} ha decidido esquivar{Color.RESET}")
                time.sleep(2)
                oponente.elegir_accion()
                jugador.esquivar()  
            case 8:
                especiales()
            case _:
                print("-------------------------------------")
                print(f"{Color.ROJO}Acción no válida, por favor intente nuevamente{Color.RESET}")
                time.sleep(1)
    except ValueError:
        sound.sError()
        print(f"\n{Color.VERDE}ValueError{Color.RESET}")
        print(f"{Color.ROJO}Valor inválido, ingresa nuevamente{Color.RESET}")
        time.sleep(2)
