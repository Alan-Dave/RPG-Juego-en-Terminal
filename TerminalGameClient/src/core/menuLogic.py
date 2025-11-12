from utils.common import time
from utils.colors import Color
from .eventos import error, valueError

ERRORS = {
    'ERROR': error,
    'VALUEERROR': valueError,
}

def Juego():
    from core.eventos import R, resultado, volver_a_jugar
    from ui.menuUI import bienvenida, volver_a_jugar_UI, eleccion_UI
    from utils.commonChar import Oponente, Personaje
    from core.eventos import resultado
    while True:
        bienvenida()

        eleccion_UI()
        # Elegir personaje
        jugador = Personaje.elegir_Personaje()
        # Crear un oponente distinto al jugador seleccionado
        oponente = Oponente.crear_oponente(jugador.nombre)

        R.PuntoR(jugador=jugador, oponente=oponente)
        vida_maxima_j, vida_maxima_o = R.vida_maxima(jugador=jugador, oponente=oponente)

        # Menú RPG interactivo
        MenuLogic(jugador, oponente, vida_maxima_j, vida_maxima_o)

        # Partida Terminada
        resultado(jugador.nombre, oponente.nombre, jugador.vida, oponente.vida)

        #Opcion de volver a jugar
        volver_a_jugar_UI()
        volver_a_jugar(jugador, oponente)
    #_________________________________________________




def MenuLogic(jugador, oponente, vida_maxima_j, vida_maxima_o):
    from ui.menuUI import menu_UI
    
    while True: 
        menu_UI(jugador, oponente, vida_maxima_j, vida_maxima_o)
        try:
            accion = int(input("\nIntroduce el número de tu elección: "))
            match accion:
                case 1: #JUGADOR ATACA Y OPONENTE ELIGE ACCIÓN
                    c = atacar_(jugador, oponente)     
                case 2: #JUGADOR ESPERA Y OPONENTE ELIGE ACCIÓN
                    c = esperar_(jugador, oponente)
                case 4: #JUGADOR REALIZA UN COMBO Y OPONENTE ELIGE ACCIÓN
                    c = combos_(jugador, oponente)
                case 8: #JUGADOR REALIZA UN ULTIMATE Y OPONENTE ELIGE ACCIÓN
                    c = especiales_(jugador, oponente)
                case 't', 'T': #JUGADOR INGRESA A LA TIENDA
                    c = tienda_(jugador)
                case 'e', 'E': #JUGADOR INGRESA A SU MOCHILA
                    c = mochila_(jugador)
                case 7: #JUGADOR ESQUIVA Y OPONENTE ELIGE ACCIÓN
                    c = esquivar_(jugador, oponente)
                case _:
                    ERRORS['ERROR']()
        except ValueError as e:
            ERRORS['VALUEERROR'](e)
        
        if c:
            break
            







def atacar_(jugador, oponente):
    print("-------------------------------------")
    resultado = jugador.atacar(oponente)
    ok = resultado['ok']
    msg = resultado['msg']
    dano = resultado['dano']

    if ok:
        print(f"\n{Color.CIAN}{msg}{Color.RESET}")
        time.sleep(2)
    else:
        print(f'\n{Color.ROJO}{msg}{Color.RESET}')
        time.sleep(2)
        return


    c = comprobar(jugador, oponente)
    if c:
        return True

    
    resultado_ = oponente.elegir_accion(jugador, dano)
    ok_ = resultado_['ok']
    msg_ = resultado_['msg']
    if ok_:
        print(f'\n{Color.AMARILLO}{msg_}{Color.RESET}')
        time.sleep(2)
    else:
        while True:
            print(f'\n{Color.ROJO}{msg_}{Color.RESET}')
            time.sleep(2)
            oponente.elegir_accion(jugador)
    

    c = comprobar(jugador, oponente)
    if c:
        return True

        
        
    
     


def esperar_(jugador, oponente):
    resultado = jugador.esperar()
    ok = resultado['ok']
    msg = resultado['msg']
    dano = resultado['dano']

    if ok:
        print(f"\n{Color.CIAN}{msg}{Color.RESET}")
        time.sleep(2)
    else:
        print(f'\n{Color.ROJO}{msg}{Color.RESET}')
        time.sleep(2)
        return


    c = comprobar(jugador, oponente)
    if c:
        return True

    
    resultado_ = oponente.elegir_accion(jugador, dano)
    ok_ = resultado_['ok']
    msg_ = resultado_['msg']
    if ok_:
        print(f'\n{Color.AMARILLO}{msg_}{Color.RESET}')
        time.sleep(2)
    else:
        while True:
            print(f'\n{Color.ROJO}{msg_}{Color.RESET}')
            time.sleep(2)
            oponente.elegir_accion(jugador)


    c = comprobar(jugador, oponente)
    if c:
        return True

    



def combos_(jugador, oponente):
    from core.eventos import combos
    resultado = combos(jugador, oponente)
    ok = resultado['ok']
    msg = resultado['msg']
    dano = resultado['dano']
    if ok:
        print(f"\n{Color.CIAN}{msg}{Color.RESET}")
        time.sleep(2)
    else:
        print(f'\n{Color.ROJO}{msg}{Color.RESET}')
        time.sleep(2)
        return


    c = comprobar(jugador, oponente)
    if c:
        return True

    
    resultado_ = oponente.elegir_accion(jugador, dano)
    ok_ = resultado_['ok']
    msg_ = resultado_['msg']
    if ok_:
        print(f'\n{Color.AMARILLO}{msg_}{Color.RESET}')
        time.sleep(2)
    else:
        while True:
            print(f'\n{Color.ROJO}{msg_}{Color.RESET}')
            time.sleep(2)
            oponente.elegir_accion(jugador)


    c = comprobar(jugador, oponente)
    if c:
        return True

    


def tienda_(jugador):
    from TerminalGameClient.src.ui.tiendaUI import Tienda
    Tienda()



def mochila_(jugador):
    from TerminalGameClient.src.ui.mochilaUI import Mochila
    Mochila()



def esquivar_(jugador, oponente):
    print(f'{jugador.nombre} decide esquivar el ataque')

    resultado_ = oponente.elegir_accion(jugador, dano)
    ok_ = resultado_['ok']
    msg_ = resultado_['msg']
    dano_ = resultado_['dano']
    if ok_:
        print(f'\n{Color.AMARILLO}{msg_}{Color.RESET}')
        time.sleep(2)
    else:
        while True:
            print(f'\n{Color.ROJO}{msg_}{Color.RESET}')
            time.sleep(2)
            oponente.elegir_accion(jugador)

    resultado = jugador.esquivar(oponente, dano_)
    ok = resultado['ok']
    msg = resultado['msg']
    dano = resultado['dano']


    c = comprobar(jugador, oponente)
    if c:
        return True

    
    if ok:
        print(f"\n{Color.CIAN}{msg}{Color.RESET}")
        time.sleep(2)
    else:
        print(f'\n{Color.ROJO}{msg}{Color.RESET}')
        time.sleep(2)
        return


    c = comprobar(jugador, oponente)
    if c:
        return True

    
def especiales_(jugador, oponente):
    from core.eventos import especiales
    resultado = especiales(jugador, oponente)
    ok = resultado['ok']
    msg = resultado['msg']
    dano = resultado['dano']

    if ok:
        print(f"\n{Color.CIAN}{msg}{Color.RESET}")
        time.sleep(2)
    else:
        print(f'\n{Color.ROJO}{msg}{Color.RESET}')
        time.sleep(2)
        return


    c = comprobar(jugador, oponente)
    if c:
        return True


    


    resultado_ = oponente.elegir_accion(jugador, dano)
    ok_ = resultado_['ok']
    msg_ = resultado_['msg']
    if ok_:
        print(f'\n{Color.AMARILLO}{msg_}{Color.RESET}')
        time.sleep(2)
    else:
        while True:
            print(f'\n{Color.ROJO}{msg_}{Color.RESET}')
            time.sleep(2)
            oponente.elegir_accion(jugador)


    c = comprobar(jugador, oponente)
    if c:
        return True

    






def comprobar(jugador, oponente):
    if jugador.vida <= 0 or oponente.vida <= 0:
        return True
    else:
        return False


