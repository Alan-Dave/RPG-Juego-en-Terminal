from utils.common import time
from core import UI_MAP
from core.eventos import ERRORS

def Mochila_log(jugador):
    try:
        usar = input("\n¿Que producto deseas usar? ").strip()

        if usar.lower() == 'r':
            return True

        if usar.isdigit():
            usar = int(usar)
        else:
            print("\033[31mDebes ingresar un número válido.\033[0m")
            return

        mochilaComprobator(usar, jugador)
        UI_MAP['pocion']()
        print(f"Has usado \033[32m{jugador.mochila[usar-1]}\033[0m")  # <- Aquí dará error si ya hiciste pop
        time.sleep(2)

    except ValueError as e:
        ERRORS['VALUEERROR'](e)




def mochilaComprobator(cual_usar, jugador):
    from utils.constants import pocion

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

        nombre_item = jugador.mochila[cual_usar-1] if cual_usar-1 < len(jugador.mochila) else "Ítem usado"
        print(f"Has usado \033[32m{nombre_item}\033[0m")


    else:
        print("\033[33mNo puedes usar este ítem.\033[0m")




def inventory(jugador):
    slots = 10
    mochila = jugador.mochila if jugador.mochila else []

    # Rellenamos con espacios vacíos si tiene menos de 10
    items = [f"[{item}]" for item in mochila] + ["[]"] * (slots - len(mochila))

    # Formato de dos columnas
    for i in range(5):
        print(f"{i+1}. {items[i]:<20} {i+6}. {items[i+5]}")