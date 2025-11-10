from utils.common import os, time
   
# _______________________________________________________________________
def combos():
    from utils.constants import jugador, oponente
    from utils.commonChar import Naruto, Sasuke, Ichigo, Aizen, Kyo, Iori, Kazuha, Alhacen, Goku, Vegeta, John

    # Mapeo de (tipo, nombre) → acción especial
    acciones_combo = {
        ("NarutoS", "Naruto"): lambda j: Naruto.Rasengan(self=j),
        ("NarutoS", "Sasuke"): lambda j: Sasuke.Chidori(self=j),

        ("Bleach", "Ichigo"): lambda j: Ichigo.Getsuga(self=j),
        ("Bleach", "Aizen"): lambda j: Aizen.A_kido(self=j),

        ("DBZ", "Goku"): lambda j: Goku.Kamehameha(self=j),
        ("DBZ", "Vegeta"): lambda j: Vegeta.GarlickGun(self=j),

        ("Genshin", "Kazuha"): lambda j: Kazuha.K_elemental(self=j),
        ("Genshin", "Alhacen"): lambda j: Alhacen.A_elemental(self=j),

        ("Kof", "Iori"): lambda j: Iori.Iori_1(self=j),
        ("Kof", "Kyo"): lambda j: Kyo.Kyo_1(self=j),
    }

    # Buscar acción por tipo y nombre
    accion = acciones_combo.get((jugador.tipo, jugador.nombre)) or \
             acciones_combo.get((jugador.tipo, None))

    if accion:
        ejecutar_accion(accion)
    else:
        print("⚠️ No hay combo definido para este personaje.")

def ejecutar_accion(accion):
    """Ejecuta una acción estándar con su secuencia de comprobaciones."""
    from core.eventos import comprobar
    print("-------------------------------------")
    accion(jugador)
    print("")
    comprobar()
    if hasattr(oponente, "elegir_accion"):
        oponente.elegir_accion()
        comprobar()
    

def especiales():
    from core.eventos import comprobar

    # Mapeo de (tipo, nombre) → ataque especial
    acciones_especiales = {
        ("NarutoS", "Naruto"): lambda j: Naruto.RasenShuriken(self=j),
        ("NarutoS", "Sasuke"): lambda j: Sasuke.Raikiri(self=j),

        ("Bleach", "Ichigo"): lambda j: Ichigo.Bankai(self=j),
        ("Bleach", "Aizen"): lambda j: Aizen.Kyokasuigetsu(self=j),

        ("DBZ", "Goku"): lambda j: Goku.Ssj(self=j),
        ("DBZ", "Vegeta"): lambda j: Vegeta.Ssj(self=j),

        ("Genshin", "Kazuha"): lambda j: Kazuha.K_ulti(self=j),
        ("Genshin", "Alhacen"): lambda j: Alhacen.A_ulti(self=j),

        ("Kof", "Iori"): lambda j: Iori.Iori_2(self=j),
        ("Kof", "Kyo"): lambda j: Kyo.Kyo_2(self=j),
    }

    # Buscar acción por tipo y nombre
    accion = acciones_especiales.get((jugador.tipo, jugador.nombre)) or \
             acciones_especiales.get((jugador.tipo, None))

    if accion:
        ejecutar_accion(accion)
    else:
        print("⚠️ No hay ataque especial definido para este personaje.")

def resultado(nombre):
    from utils.constants import jugador, oponente
    from core.sound import sound
    os.system("cls")
    print("El ganador de esta reñida pelea es..")
    time.sleep(2)
    if (oponente.vida <= 0 and jugador.vida > 0) or (oponente.vida > 0 and jugador.vida <= 0):
        print(f"\n\033[32m[!{jugador.nombre if jugador.vida > 0 else oponente.nombre}¡]\033[0m\n")   #<---------------------------- este texto es verde
        sonido_win(nombre)
        time.sleep(2.5)
        sound.sWin()
    elif jugador.vida <= 0:
        print(f"\n\033[38;5;208m[!{oponente.nombre}¡]\033[0m\n")  #<---------------------------- este texto es naranjo
        sonido_win(nombre)
        time.sleep(2.5)
        sound.sDerrota()
        
        
    print("\033[33mGracias por jugar\033[0m") # estos textos son amarillos
    print("-----------------------------------")
    print("\033[33mJuego terminado\033[0m")
    time.sleep(2.5)
    eleccion_c()

class R():
    def PuntoR():
        from utils.constants import jugador, oponente
        oponente_r = 0
        oponente_r = oponente.vida

        oponente_s = 0
        oponente_s = oponente.stamina

        jugador_r = 0
        jugador_r = jugador.vida

        jugador_s = 0
        jugador_s = jugador.stamina

    def Reset():
        from utils.constants import jugador, oponente
        oponente.vida = oponente_r
        oponente.stamina = oponente_s

        jugador.vida = jugador_r
        jugador.stamina = jugador_s

        jugador.moneda += jugador.moneda + 100
        oponente.moneda += oponente.moneda + 100



def sonido_win(nombre):
    from sound_dispatcher import SOUNDS_MAP

    tipos = {
        'Naruto': SOUNDS_MAP['Naruto']['win'],
        'Sasuke': SOUNDS_MAP['Naruto']['win'],
        'Ichigo': SOUNDS_MAP['Bleach']['win'],
        'Aizen': SOUNDS_MAP['Bleach']['win'],
        'Goku': SOUNDS_MAP['DBZ']['win'],
        'Vegeta': SOUNDS_MAP['DBZ']['win'],
        'Kazuha': SOUNDS_MAP['Genshin']['win'],
        'Alhacen': SOUNDS_MAP['Genshin']['win'],
        'Iori': SOUNDS_MAP['Kof']['win'],
        'Kyo': SOUNDS_MAP['Kof']['win'],
    }

    if nombre in tipos:
        tipos[nombre]()
    else:
        tipos[nombre]()
# _______________________________________________________________________
# _______________________________________________________________________

def eleccion_c():
    from core.sound import sound
    print("\n¿Deseas volver a jugar?")
    print("1 = SI\n"
        "2 = NON")
    eleccion = int(input("\nEleccion: "))
    while True:
        try:
            if eleccion == 1:
                R.Reset()
                return True
            elif eleccion == 2:
                sound.sGameOver()
                print("\n\033[33m**************** Terminando el programa. **************\033[0m\n")
                for i in range(3+1):
                    print(i)
                    time.sleep(1)
                raise SystemExit()
            else:
                sound.sError()
                os.system("cls")
                print("Intente nuevamente")
        except ValueError:
            sound.sError()
            os.system("cls")
            print("Intente nuevamente")
# _______________________________________________________________________
#-------------------------------------------------------------------------
    
