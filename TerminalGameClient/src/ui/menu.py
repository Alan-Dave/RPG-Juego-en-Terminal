from utils.common import os, time
from utils.colors import Color



def menu():
    from utils.constants import jugador, oponente

    # Diccionario con los movimientos, costos y formato
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

    while True:
        os.system("cls")

        if not jugador:
            print("\033[31mNo se ha elegido ningún personaje.\033[0m")
            jugador = elegir_Personaje()
            continue

        jugador.estado()
        time.sleep(1)
        print(f"------------ Oponente [{oponente.nombre}] ---------------------|")

        print("\n---------------------------------------------------------------------------")
        print("  1. Atacar                  2. Ver estado               3. Esperar         \n "
              "[-10 stamina]                                   [+15 stamina y +15 vida]\n")

        # Mostrar las habilidades desde el diccionario
        if jugador.nombre in MOVIMIENTOS:
            for key, (nombre, costo) in MOVIMIENTOS[jugador.nombre].items():
                print(f"{key}. {nombre:<20} [-{costo} stamina]")
        else:
            print("4. Habilidad no definida")

        print("\n\033[33m5. TIENDA\033[0m                    \033[33m6. MOCHILA\033[0m")

        opciones()

        jugador.stamina += 5
        oponente.stamina += 5
        oponente.dano = 0
        jugador.dano = 0




def eleccion():
    print(f"{Color.AMARILLO}Elige tu Personaje:{Color.RESET}\n")

    print(f"""{Color.CIAN}
1. Naruto                 6. Kazuha   
2. Sasuke                 7. Vegeta     
3. Iori                   8. Alhacen  
4. Kyo                    9. Goku     
5. Ichigo                10. Aizen
{Color.RESET}""")
    
    print(f"\n{Color.VERDE}0. Elegir aleatoriamente{Color.RESET}")
