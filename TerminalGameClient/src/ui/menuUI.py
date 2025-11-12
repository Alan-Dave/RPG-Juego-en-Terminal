from utils.common import time, os
from utils.colors import Color
from core.sound_dispatcher import UI_MAP

def bienvenida():
    try:
        os.system("cls")
        UI_MAP['intro']()
        print("\033[33m *** Bienvenido al juego RPG *** \033[0m\n")
        enter = input("   Presiona enter para empezar\n")
    except ValueError:
        pass

def volver_a_jugar_UI():
    print("\033[33mGracias por jugar\033[0m") # estos textos son amarillos
    print("-----------------------------------")
    print("\033[33mJuego terminado\033[0m")
    time.sleep(2.5)
    print("\n¿Deseas volver a jugar?")
    print("1 = SI\n"
        "2 = NON")

    
def eleccion_UI():
    os.system("cls")
    print(f"{Color.AMARILLO}Elige tu Personaje:{Color.RESET}\n")

    print(f"""{Color.CIAN}
1. Naruto                 6. Kazuha   
2. Sasuke                 7. Vegeta     
3. Iori                   8. Alhacen  
4. Kyo                    9. Goku     
5. Ichigo                10. Aizen
{Color.RESET}""")
    
    print(f"\n{Color.VERDE}0. Elegir aleatoriamente{Color.RESET}")


def menu_UI(jugador, oponente, vida_maxima_j, vida_maxima_o):
    from utils.commonChar import Personaje
    MOVIMIENTOS = {
        "Naruto": {
            4: ("Rasengan", 60),
            7: ("Esquivar", 15),
            8: ("RasenShuriken", 150),
        },
        "Sasuke": {
            4: ("Chidori", 60),
            7: ("Esquivar", 15),
            8: ("Raikiri", 150),
        },
        "Ichigo": {
            4: ("Getsuga Tensho", 50),
            7: ("Esquivar", 15),
            8: ("Bankai", 160),
        },
        "Aizen": {
            4: ("Kido", 50),
            7: ("Esquivar", 15),
            8: ("Kyokasuigetsu", 130),
        },
        "Kazuha": {
            4: ("Elemental", 50),
            7: ("Esquivar", 15),
            8: ("Ulti", 130),
        },
        "Alhacen": {
            4: ("Elemental", 50),
            7: ("Esquivar", 15),
            8: ("Ulti", 130),
        },
        "Iori": {
            4: ("Combo", 50),
            7: ("Esquivar", 15),
            8: ("Especial", 130),
        },
        "Kyo": {
            4: ("Combo", 50),
            7: ("Esquivar", 15),
            8: ("Especial", 130),
        },
        "Goku": {
            4: ("Kamehameha", 50),
            7: ("Esquivar", 15),
            8: ("Super Saiyajin", 130),
        },
        "Vegeta": {
            4: ("Garlick Gun", 50),
            7: ("Esquivar", 15),
            8: ("Super Saiyajin", 130),
        },
    }

    os.system("cls")

    if not jugador:
        print("\033[31m⚠ No se ha elegido ningún personaje.\033[0m")
        jugador = Personaje.elegir_Personaje()

    Personaje.mostrar_estado(jugador, oponente, vida_maxima_j, vida_maxima_o)
    time.sleep(1)

    ancho_total = 70
    print("─" * ancho_total)
    print(f"🆚  Enfrentamiento contra: \033[36m{oponente.nombre}\033[0m".center(ancho_total))
    print("─" * ancho_total)

    print(f"""
\033[32m┌───────────────────────────── OPCIONES ─────────────────────────────┐\033[0m
│  1. Atacar              [-10 stamina]                                │
│  2. Esperar             [+15 stamina y +15 vida]                     │
│                                                                 │
│  T. \033[33mTienda\033[0m                E. \033[33mMochila\033[0m                        │
\033[32m└──────────────────────────────────────────────────────────────────┘\033[0m
""")

    # Mostrar habilidades especiales
    if jugador.nombre in MOVIMIENTOS:
        print("\033[34m╔═════════════ HABILIDADES ESPECIALES ═════════════╗\033[0m")
        for key, (nombre, costo) in MOVIMIENTOS[jugador.nombre].items():
            print(f"  {key}. {nombre:<25} [-{costo} stamina]")
        print("\033[34m╚══════════════════════════════════════════════════╝\033[0m")
    else:
        print("\033[31m⚠ Este personaje no tiene habilidades definidas.\033[0m")

        