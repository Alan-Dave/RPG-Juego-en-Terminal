import os

from sound import sound












def bienvenida():
    try:
        from player.personaje import elegir_personaje
        print("\033[33m *** Bienvenido al juego RPG *** \033[0m\n")
        sound.sIntro()
        
        enter = input("   Presiona enter para empezar\n")
    except ValueError:
        os.system("cls")
        elegir_personaje()




























#_____________________________________________________
# JUEGO
def Juego():
    from reset import R
    os.system("cls")

    bienvenida()

    # Elegir personaje
    from player.personaje import elegir_personaje, personaje_igual
    elegir_personaje()
    personaje_igual()

    R.PuntoR()
    # Menú RPG interactivo
    from sections.menu import menu
    menu()

    # Partida Terminada
    from comprobar import resultado
    resultado()
    #_________________________________________________


    

















# ALL

Juego()
