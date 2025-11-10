from utils.common import os
from core.sound import sound


def bienvenida():
    from core.opciones import elegir_Personaje
    try:
        print("\033[33m *** Bienvenido al juego RPG *** \033[0m\n")
        sound.sIntro()
        
        enter = input("   Presiona enter para empezar\n")
    except ValueError:
        os.system("cls")
        elegir_Personaje()

#_____________________________________________________
# JUEGO
def Juego():
    from core.eventos import R
    from ui.menu import menu
    from core.opciones import elegir_Personaje
    from characters.Oponente import Personaje_distinto
    os.system("cls")

    bienvenida()

    # Elegir personaje
    
    jugador = elegir_Personaje()
    Personaje_distinto(jugador.nombre)

    R.PuntoR()
    # Menú RPG interactivo
    
    menu()

    # Partida Terminada
    from core.eventos import resultado
    resultado()
    #_________________________________________________

# ALL
if __name__ == "__main__":
    Juego()
