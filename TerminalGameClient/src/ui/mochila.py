from utils.common import os, time
from core.sound import sound

def Mochila():
    from utils.constants import jugador
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
        return menu()
    else:
        sound.sError()
        print("\033[31m Opcion Invalida \033[0m")
        time.sleep(2)
        return Mochila()





###
# Un comprobador de pociones, para que detecte que pocion es la que tienes en cada slot

###


def mochilaComprobator(cual_usar):
    from utils.constants import jugador, pocion

    if not jugador.mochila:
        print("\033[31mTu mochila está vacía.\033[0m")
        return

    try:
        item = jugador.mochila[cual_usar - 1]
    except IndexError:
        print("\033[31mÍtem inválido.\033[0m")
        return

    # Mapeo de pociones a sus efectos
    efectos = {
        'Pocion_Vida_B': ('vida', pocion.Pocion_B, "+25 Vida"),
        'Pocion_Stamina_B': ('stamina', pocion.Pocion_B, "+25 Stamina"),
        'Pocion_Poder_B': ('poder', pocion.Pocion_B, "+25 Poder"),
        'Pocion_Vida_A': ('vida', pocion.Pocion_A, "+40 Vida"),
        'Pocion_Stamina_A': ('stamina', pocion.Pocion_A, "+40 Stamina"),
        'Pocion_Poder_A': ('poder', pocion.Pocion_A, "+40 Poder"),
        'Pocion_Vida_S': ('vida', pocion.Pocion_S, "+70 Vida"),
        'Pocion_Stamina_S': ('stamina', pocion.Pocion_S, "+70 Stamina"),
        'Pocion_Poder_S': ('poder', pocion.Pocion_S, "+70 Poder"),
        'Pocion_Mix_SS': ('mix', pocion.Pocion_SS, "+45 Vida +45 Stamina +45 Poder"),
    }

    if item in efectos:
        stat, cantidad, mensaje = efectos[item]

        if stat == 'mix':
            jugador.vida += cantidad
            jugador.stamina += cantidad
            jugador.poder += cantidad
        else:
            setattr(jugador, stat, getattr(jugador, stat) + cantidad)

        print(f"\n\033[32m {mensaje} \033[0m")

        # Opcional: eliminar la poción usada
        jugador.mochila.pop(cual_usar - 1)

    else:
        print("\033[33mNo puedes usar este ítem.\033[0m")




def inventory():
    from utils.constants import jugador

    slots = 10
    mochila = jugador.mochila if jugador.mochila else []

    # Rellenamos con espacios vacíos si tiene menos de 10
    items = [f"[{item}]" for item in mochila] + ["[]"] * (slots - len(mochila))

    # Formato de dos columnas
    for i in range(5):
        print(f"{i+1}. {items[i]:<20} {i+6}. {items[i+5]}")



Mochila()