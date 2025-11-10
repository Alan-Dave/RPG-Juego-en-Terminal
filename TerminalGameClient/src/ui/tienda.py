from utils.common import os, time


def Tienda():
    global producto
    
    os.system("cls")
    print("\033[32m********** TIENDA ***********\033[0m\n")

    print("\033[32m!Bienvenido¡, ¿que desea llevar?\033[0m\n")
    print(f"                                               Money: \033[33m{jugador.moneda}\033[0m")
    print("")
    print(f'1. Pocion_Vida_B       $20          6. Pocion_Poder_A    $40\n'
        f'2. Pocion_Stamin_B     $20          7. Pocion_Vida_S     $80\n'
        f'3. Pocion_Poder_B      $20          8. Pocion_Stamin_S   $80\n'
        f'4. Pocion_Vida_A       $40          9. Pocion_Poder_S    $80\n'
        f'5. Pocion_Stamin_A     $40          10. Pocion_Mix_SS    $100\n'
        )
    print("\nB = Basico: 25.pts\n"
        "A = Intermedio: 40.pts\n"
        "S = Avanzado: 70.pts\n"
        "SS = Legendario: 35.pts All stats")
    
    print("\n1. Si\n"
        "2. No\n")
    opcion_1 = int(input("¿Deseas Comprar? "))
    
    
    if opcion_1 == 1:
        producto = int(input("\nElige el producto: "))
        match producto:
            case 1:
                moneyComprobator()
                jugador.mochila.append('Pocion_Vida_B')
                jugador.moneda -= pocion.Pocion_B_Precio
                return Tienda()
            case 2:
                moneyComprobator()
                jugador.mochila.append('Pocion_Stamin_B')
                jugador.moneda -= pocion.Pocion_B_Precio
                return Tienda()
            case 3:
                moneyComprobator()
                jugador.mochila.append('Pocion_Poder_B')
                jugador.moneda -= pocion.Pocion_B_Precio
                return Tienda()
            case 4:
                moneyComprobator()
                jugador.mochila.append('Pocion_Vida_A')
                jugador.moneda -= pocion.Pocion_A_Precio
                return Tienda()
            case 5:
                moneyComprobator()
                jugador.mochila.append('Pocion_Stamin_A')
                jugador.moneda -= pocion.Pocion_A_Precio
                return Tienda()
            case 6:
                moneyComprobator()
                jugador.mochila.append('Pocion_Poder_A')
                jugador.moneda -= pocion.Pocion_A_Precio
                return Tienda()
            case 7:
                moneyComprobator()
                jugador.mochila.append('Pocion_Vida_S')
                jugador.moneda -= pocion.Pocion_S_Precio
                return Tienda()
            case 8:
                moneyComprobator()
                jugador.mochila.append('Pocion_Stamin_S')
                jugador.moneda -= pocion.Pocion_S_Precio
                return Tienda()
            case 9:
                moneyComprobator()
                jugador.mochila.append('Pocion_Poder_S')
                jugador.moneda -= pocion.Pocion_S_Precio
                return Tienda()
            case 10:
                moneyComprobator()
                jugador.mochila.append('Pocion_Mix_SS')
                jugador.moneda -= pocion.Pocion_SS_Precio
                return Tienda()
    elif opcion_1 == 2:
        from TerminalGameClient.src.core.sound import sound
        sound.sSalirTienda()
        from sections.menu import menu
        return menu()
    else:
        from TerminalGameClient.src.core.sound import sound
        sound.sError()
        print("\033[31mOpcion Invalida, Ingrese nuevamente\033[0m")
        time.sleep(2)
        return Tienda()


    # INSTALAR INTELLICODE EN EXTENSIONES DE VS

def moneyComprobator():
    from TerminalGameClient.src.core.sound import sound
    global producto
    if producto in range(1, 4):
        if jugador.moneda > pocion.Pocion_B_Precio:
            sound.sMoney()
        elif jugador.moneda < pocion.Pocion_B_Precio:
            sound.sError()
            print("\n\033[31mNo tienes monedas suficientes para ese producto\033[0m")
            time.sleep(2)
            return Tienda()

    elif producto in range(4, 7):
        if jugador.moneda > pocion.Pocion_A_Precio:
            sound.sMoney()
        elif jugador.moneda < pocion.Pocion_A_Precio:
            sound.sError()
            print("\n\033[31mNo tienes monedas suficientes para ese producto\033[0m")
            time.sleep(2)
            return Tienda()

    elif producto in range(7, 10):
        if jugador.moneda > pocion.Pocion_S_Precio:
            sound.sMoney()
        elif jugador.moneda < pocion.Pocion_S_Precio:
            sound.sError()
            print("\n\033[31mNo tienes monedas suficientes para ese producto\033[0m")
            time.sleep(2)
            return Tienda()

    elif producto == 10:
        if jugador.moneda > pocion.Pocion_SS_Precio:
            sound.sMoney()
        elif jugador.moneda < pocion.Pocion_SS_Precio:
            print("\n\033[31mNo tienes monedas suficientes para ese producto\033[0m")
            time.sleep(2)
            return Tienda()
    else:
        sound.sError()
        print("\033[31mNo tenemos mas productos\033[0m")
        time.sleep(2)
        return Tienda()

"""
EN ESTA PARTE SE AGREGARAN MOCHILAS DE INVENTARIO Y MONEDAS
"""


