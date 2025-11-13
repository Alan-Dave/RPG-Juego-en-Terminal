from utils.common import os
from core.mochila_log import inventory, Mochila_log



def Mochila(jugador):
    os.system("cls")
    print("\033[32m********** MOCHILA ***********\033[0m\n")
    print(f"{len(jugador.mochila)}/10       Money: {jugador.moneda}\n")
    print("-----------------------------------------------")
    inventory(jugador)
    print("-----------------------------------------------")

    print('\n R = Salir\n')
    
    Mochila_log(jugador)






###
# Un comprobador de pociones, para que detecte que pocion es la que tienes en cada slot

###






