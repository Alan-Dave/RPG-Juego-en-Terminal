import os 
import time

from player.personaje import jugador
from sound import sound

def Mochila():
    

    global cual_usar
    os.system("cls")
    sound.sMochila()
    print("\033[32m********** MOCHILA ***********\033[0m\n")
    print(f"{len(jugador.mochila)}/10       Money: {jugador.moneda}\n")
    print("-----------------------------------------------")
    inventory()
    print("-----------------------------------------------")
    print("1. SI\n"
          "2. NO")
    usar = int(input("\n¿Deseas usar un producto? "))
    print("")
    if usar == 1:
        cual_usar = int(input("Elige el producto que deseas usar: "))
        mochilaComprobator()
        sound.sPocion()
        print(f"Has usado \033[32m{jugador.mochila[cual_usar-1]}\033[0m")
        time.sleep(2)
        jugador.mochila.pop(cual_usar-1)
        Mochila()
    elif usar == 2:
        from sections.menu import menu
        return menu()
    else:
        sound.sError()
        print("\033[31m Opcion Invalida \033[0m")
        time.sleep(2)
        return Mochila()





###
# Un comprobador de pociones, para que detecte que pocion es la que tienes en cada slot

###


def mochilaComprobator():
    
    from player.pocion import pocion

    try:
        if jugador.mochila[cual_usar-1]:
            item = jugador.mochila[cual_usar-1]  # Guardamos el ítem en una variable para evitar múltiples accesos al mismo índice.
            
            if item == 'Pocion_Vida_B':
                jugador.vida += pocion.Pocion_B
                print("\n\033[32m +25 Vida \033[0m")
            elif item == 'Pocion_Stamina_B':
                jugador.stamina += pocion.Pocion_B
                print("\n\033[32m +25 Stamina \033[0m")
            elif item == 'Pocion_Poder_B':
                jugador.poder += pocion.Pocion_B
                print("\n\033[32m +25 Poder \033[0m")
            elif item == 'Pocion_Vida_A':
                jugador.vida += pocion.Pocion_A
                print("\n\033[32m +40 Vida \033[0m")
            elif item == 'Pocion_Stamina_A':
                jugador.stamina += pocion.Pocion_A
                print("\n\033[32m +40 Stamina \033[0m")
            elif item == 'Pocion_Poder_A':
                jugador.poder += pocion.Pocion_A
                print("\n\033[32m +40 Poder \033[0m")
            elif item == 'Pocion_Vida_S':
                jugador.vida += pocion.Pocion_S
                print("\n\033[32m +70 Vida \033[0m")
            elif item == 'Pocion_Stamina_S':
                jugador.stamina += pocion.Pocion_S
                print("\n\033[32m +70 Stamina \033[0m")
            elif item == 'Pocion_Poder_S':
                jugador.poder += pocion.Pocion_S
                print("\n\033[32m +70 Poder \033[0m")
            elif item == 'Pocion_Mix_SS':
                jugador.vida += pocion.Pocion_SS
                jugador.stamina += pocion.Pocion_SS
                jugador.poder += pocion.Pocion_SS
                print("\n\033[32m +45 Vida +45 Stamina +45 Poder\033[0m")
    except IndexError:
        from sound import sound
        sound.sError()
        print("\n\033[31mNo hay ningún objeto en esta casilla, selecciona las casillas que contengan algo.\033[0m")
        time.sleep(2.5)
        return Mochila()












def inventory():
    if jugador.mochila:
        if len(jugador.mochila) == 1:
            print(f"""1. [{jugador.mochila[0]}]          6. []\n"""
                  f"""2. []                              7. []\n"""
                  f"""3. []                              8. []\n"""
                  f"""4. []                              9. []\n"""
                  f"""5. []                             10. []\n"""
            )
        elif len(jugador.mochila) == 2:
            print(f"""1. [{jugador.mochila[0]}]          6. []\n"""
                  f"""2. [{jugador.mochila[1]}]          7. []\n"""
                  f"""3. []                              8. []\n"""
                  f"""4. []                              9. []\n"""
                  f"""5. []                             10. []\n"""
                )
        elif len(jugador.mochila) == 3:
            print(f"""1. [{jugador.mochila[0]}]          6. []\n"""
                  f"""2. [{jugador.mochila[1]}]          7. []\n"""
                  f"""3. [{jugador.mochila[2]}]          8. []\n"""
                  f"""4. []                              9. []\n"""
                  f"""5. []                             10. []\n"""
                )
        elif len(jugador.mochila) == 4:
            print(f"""1. [{jugador.mochila[0]}]          6. []\n"""
                  f"""2. [{jugador.mochila[1]}]          7. []\n"""
                  f"""3. [{jugador.mochila[2]}]          8. []\n"""
                  f"""4. [{jugador.mochila[3]}]          9. []\n"""
                  f"""5. []                             10. []\n"""
                )
        elif len(jugador.mochila) == 5:
            print(f"""1. [{jugador.mochila[0]}]          6. []\n"""
                  f"""2. [{jugador.mochila[1]}]          7. []\n"""
                  f"""3. [{jugador.mochila[2]}]          8. []\n"""
                  f"""4. [{jugador.mochila[3]}]          9. []\n"""
                  f"""5. [{jugador.mochila[4]}]         10. []\n"""
                )
        elif len(jugador.mochila) == 6:
            print(f"""1. [{jugador.mochila[0]}]          6. [{jugador.mochila[5]}]\n"""
                  f"""2. [{jugador.mochila[1]}]          7. []\n"""
                  f"""3. [{jugador.mochila[2]}]          8. []\n"""
                  f"""4. [{jugador.mochila[3]}]          9. []\n"""
                  f"""5. [{jugador.mochila[4]}]         10. []\n"""
                )
        elif len(jugador.mochila) == 7:
            print(f"""1. [{jugador.mochila[0]}]          6. [{jugador.mochila[5]}]\n"""
                  f"""2. [{jugador.mochila[1]}]          7. [{jugador.mochila[6]}]\n"""
                  f"""3. [{jugador.mochila[2]}]          8. []\n"""
                  f"""4. [{jugador.mochila[3]}]          9. []\n"""
                  f"""5. [{jugador.mochila[4]}]         10. []\n"""
                )
        elif len(jugador.mochila) == 8:
            print(f"""1. [{jugador.mochila[0]}]          6. [{jugador.mochila[5]}]\n"""
                  f"""2. [{jugador.mochila[1]}]          7. [{jugador.mochila[6]}]\n"""
                  f"""3. [{jugador.mochila[2]}]          8. [{jugador.mochila[7]}]\n"""
                  f"""4. [{jugador.mochila[3]}]          9. []\n"""
                  f"""5. [{jugador.mochila[4]}]         10. []\n"""
                )
        elif len(jugador.mochila) == 9:
            print(f"""1. [{jugador.mochila[0]}]          6. [{jugador.mochila[5]}]\n"""
                  f"""2. [{jugador.mochila[1]}]          7. [{jugador.mochila[6]}]\n"""
                  f"""3. [{jugador.mochila[2]}]          8. [{jugador.mochila[7]}]\n"""
                  f"""4. [{jugador.mochila[3]}]          9. [{jugador.mochila[8]}]\n"""
                  f"""5. [{jugador.mochila[4]}]         10. []\n"""
                )
        elif len(jugador.mochila) == 10:
            print(f"""1. [{jugador.mochila[0]}]          6. [{jugador.mochila[5]}]\n"""
                  f"""2. [{jugador.mochila[1]}]          7. [{jugador.mochila[6]}]\n"""
                  f"""3. [{jugador.mochila[2]}]          8. [{jugador.mochila[7]}]\n"""
                  f"""4. [{jugador.mochila[3]}]          9. [{jugador.mochila[8]}]\n"""
                  f"""5. [{jugador.mochila[4]}]         10. [{jugador.mochila[9]}]\n"""
                )
    else:
        print(f'1.    []          6.    []\n'
              f'2.    []          7.    []\n'
              f'3.    []          8.    []\n'
              f'4.    []          9.    []\n'
              f'5.    []         10.    []\n'
            )


Mochila()