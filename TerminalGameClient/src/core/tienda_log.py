from utils.common import time
from utils.constants import pocion
from core.eventos import ERRORS
from core import UI_MAP


def Tienda_log(jugador):
    try:
        producto = input("\nElige el producto: ")

        if producto.isdigit():
            producto = int(producto)
            
        pociones = {
            1: 'Pocion_Vida_B',
            2: 'Pocion_Stamin_B',
            3: 'Pocion_Poder_B',
            4: 'Pocion_Vida_A',
            5: 'Pocion_Stamin_A',
            6: 'Pocion_Poder_A',
            7: 'Pocion_Vida_S',
            8: 'Pocion_Stamin_S',
            9: 'Pocion_Poder_S',
            10: 'Pocion_Mix_SS',
        }
        match producto:
            case 1:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_B_Precio
            case 2:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_B_Precio
            case 3:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_B_Precio
            case 4:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_A_Precio
            case 5:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_A_Precio
            case 6:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_A_Precio
            case 7:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_S_Precio
            case 8:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_S_Precio
            case 9:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_S_Precio
            case 10:
                moneyComprobator(jugador, producto)
                jugador.mochila.append(pociones[producto])
                jugador.moneda -= pocion.Pocion_SS_Precio
            case 'r' | 'R':
                UI_MAP['salir_tienda']()
                return True
            case _:
                ERRORS['ERROR']()
    except ValueError as e:
        ERRORS['VALUEERROR'](e)
        

def moneyComprobator(jugador, producto):
    if producto in range(1, 4):
        if jugador.moneda > pocion.Pocion_B_Precio:
            UI_MAP['money']()
        elif jugador.moneda < pocion.Pocion_B_Precio:
            UI_MAP['error']()
            print("\n\033[31mNo tienes monedas suficientes para ese producto\033[0m")
            time.sleep(2)

    elif producto in range(4, 7):
        if jugador.moneda > pocion.Pocion_A_Precio:
            UI_MAP['money']()
        elif jugador.moneda < pocion.Pocion_A_Precio:
            UI_MAP['error']()
            print("\n\033[31mNo tienes monedas suficientes para ese producto\033[0m")
            time.sleep(2)

    elif producto in range(7, 10):
        if jugador.moneda > pocion.Pocion_S_Precio:
            UI_MAP['money']()
        elif jugador.moneda < pocion.Pocion_S_Precio:
            UI_MAP['error']()
            print("\n\033[31mNo tienes monedas suficientes para ese producto\033[0m")
            time.sleep(2)

    elif producto == 10:
        if jugador.moneda > pocion.Pocion_SS_Precio:
            UI_MAP['money']()
        elif jugador.moneda < pocion.Pocion_SS_Precio:
            print("\n\033[31mNo tienes monedas suficientes para ese producto\033[0m")
            time.sleep(2)
    else:
        UI_MAP['error']()
        print("\033[31mNo tenemos mas productos\033[0m")
        time.sleep(2)

"""
EN ESTA PARTE SE AGREGARAN MOCHILAS DE INVENTARIO Y MONEDAS
"""


