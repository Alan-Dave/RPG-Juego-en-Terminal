from utils.common import os, time
from utils.colors import Color
from core.sound import sound
from core import SOUNDS_MAP, UI_MAP
   
# _______________________________________________________________________
def combos(self, rival):
    # Mapeo de (tipo, nombre) → acción especial
    acciones_combo = {
    'Naruto': {
        'rasengan': lambda rival: self.Rasengan(rival),
    },
    'Sasuke': {
        'chidori': lambda rival: self.Chidori(rival),
    },
    'Ichigo': {
        'getsuga': lambda rival: self.getsuga(rival),
    },
    'Aizen': {
        'kido': lambda rival: self.kido(rival),
    },
    'Kyo': {
        'kyo_1': lambda rival: self.combo(rival),
    },
    'Iori': {
        'iori_1': lambda rival: self.combo(rival),
    },
    'Kazuha': {
        'k_elemental': lambda rival: self.K_elemental(rival),
    },
    'Alhacen': {
        'a_elemental': lambda rival: self.A_elemental(rival),
    },
    'Goku': {
        'kamehameha': lambda rival: self.Kamehameha(rival),
    },
    'Vegeta': {
        'garlick_gun': lambda rival: self.GarlickGun(rival),
    },
}
    accion = list(acciones_combo.get(self.nombre, {}).values())

    if accion:
        return accion[0](rival)
    else:
        print(f"⚠️ No hay un combo definido para {self.nombre}.")


    
    

def especiales(self, rival):
    # Mapeo de (tipo, nombre) → acción especial
    acciones_combo = {
    'Naruto': {
        'rasengan': lambda rival: self.RasenShuriken(rival),
    },
    'Sasuke': {
        'chidori': lambda rival: self.Raikiri(rival),
    },
    'Ichigo': {
        'getsuga': lambda rival: self.bankai(rival),
    },
    'Aizen': {
        'kido': lambda rival: self.kyokasuigetsu(rival),
    },
    'Kyo': {
        'kyo_1': lambda rival: self.ulti(rival),
    },
    'Iori': {
        'iori_1': lambda rival: self.ulti(rival),
    },
    'Kazuha': {
        'k_elemental': lambda rival: self.K_ulti(rival),
    },
    'Alhacen': {
        'a_elemental': lambda rival: self.A_ulti(rival),
    },
    'Goku': {
        'kamehameha': lambda rival: self.Ssj(rival),
    },
    'Vegeta': {
        'garlick_gun': lambda rival: self.Ssj(rival),
    },
}
    accion = list(acciones_combo.get(self.nombre, {}).values())

    if accion:
        return accion[0](rival)
    else:
        print(f"⚠️ No hay un combo definido para {self.nombre}.")





def resultado(jugador_nombre, oponente_nombre, jugador_vida, oponente_vida):
    os.system("cls")
    print("El ganador de esta reñida pelea es..")
    time.sleep(2)
    jugador_gana = oponente_vida <= 0 and jugador_vida > 0
    oponente_gana = oponente_vida > 0 and jugador_vida <= 0

    if jugador_gana or oponente_gana:
        print(f"\n\033[32m[!{jugador_nombre if jugador_gana else oponente_nombre}¡]\033[0m\n")   #<---------------------------- este texto es verde
        sonido_win(jugador_nombre if jugador_gana else oponente_nombre)
        time.sleep(2.5)
        return True if jugador_gana else False

        
        
    

class R:
    
    oponente_r = 0
    oponente_s = 0
    jugador_r = 0
    jugador_s = 0

    @classmethod
    def PuntoR(cls, jugador, oponente):
        
        cls.oponente_r = oponente.vida
        cls.oponente_s = oponente.stamina
        cls.jugador_r = jugador.vida
        cls.jugador_s = jugador.stamina

        
    def vida_maxima(jugador, oponente):

        vida_maxima_j = jugador.vida
        vida_maxima_o = oponente.vida

        return vida_maxima_j, vida_maxima_o

    @classmethod
    def Reset(cls, jugador, oponente):
        
        oponente.vida = cls.oponente_r
        oponente.stamina = cls.oponente_s
        jugador.vida = cls.jugador_r
        jugador.stamina = cls.jugador_s
        jugador.moneda += 100
        oponente.moneda += 100



def sonido_win(nombre):

    tipos = {
        'Naruto': SOUNDS_MAP['Naruto']['win'],
        'Sasuke': SOUNDS_MAP['Sasuke']['win'],
        'Ichigo': SOUNDS_MAP['Ichigo']['win'],
        'Aizen': SOUNDS_MAP['Aizen']['win'],
        'Goku': SOUNDS_MAP['Goku']['win'],
        'Vegeta': SOUNDS_MAP['Vegeta']['win'],
        'Kazuha': SOUNDS_MAP['Kazuha']['win'],
        'Alhacen': SOUNDS_MAP['Alhacen']['win'],
        'Iori': SOUNDS_MAP['Iori']['win'],
        'Kyo': SOUNDS_MAP['Kyo']['win'],
    }

    if nombre in tipos:
        tipos[nombre]()
    else:
        tipos[nombre]()
# _______________________________________________________________________
# _______________________________________________________________________

def volver_a_jugar(jugador, oponente, resultado):
    if resultado:
        UI_MAP['win']()
    else:
        UI_MAP['derrota']()

    while True:
        try:
            eleccion = int(input("\nEleccion: "))
            if eleccion == 1:
                R.Reset(jugador, oponente)
                break
            elif eleccion == 2:
                sound.sGameOver()
                print("\n\033[33m**************** Terminando el programa. **************\033[0m\n")
                for i in range(3+1):
                    print(i)
                    time.sleep(1)
                raise SystemExit()
            else:
                error()
        except ValueError as e:
            valueError(e)
        
# _______________________________________________________________________
#-------------------------------------------------------------------------
    
def error():
    UI_MAP['error']()
    print("-------------------------------------")
    print(f"{Color.ROJO}Acción no válida, por favor intente nuevamente{Color.RESET}")
    time.sleep(1)

def valueError(e):
    UI_MAP['error']()
    print(f"\n{Color.VERDE}ValueError: {e}{Color.RESET}")
    print(f"{Color.ROJO}Valor inválido, ingresa nuevamente{Color.RESET}")
    time.sleep(2)


ERRORS = {
    'ERROR': error,
    'VALUEERROR': valueError,
}