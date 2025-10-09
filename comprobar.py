import os 
import time


def comprobar():
    from player.personaje import jugador, oponente
    if oponente.vida <= 0:
        return resultado()
    if jugador.vida <= 0:
        return resultado()
    





# _______________________________________________________________________
def resultado():
    from player.personaje import jugador, oponente
    os.system("cls")
    print("El ganador de esta reñida pelea es..")
    time.sleep(2)
    if oponente.vida <= 0:
        from sound import sound
        print(f"\n\033[32m[!{jugador.nombre}¡]\033[0m\n")   #<---------------------------- este texto es verde
        sonido_win_j()
        time.sleep(2.5)
        sound.sWin()
    elif jugador.vida <= 0:
        from sound import sound
        print(f"\n\033[38;5;208m[!{oponente.nombre}¡]\033[0m\n")  #<---------------------------- este texto es naranjo
        sonido_win_o()
        time.sleep(2.5)
        sound.sDerrota()
        
        

    print("\033[33mGracias por jugar\033[0m") # estos textos son amarillos
    print("-----------------------------------")
    print("\033[33mJuego terminado\033[0m")
    time.sleep(2.5)
    eleccion_c()











def sonido_win_j():
    from player.personaje import jugador, tipo, tipo_2

    from sound import sound

    if jugador.tipo == tipo.Humano:
        sound.sAtacar()
    elif jugador.tipo == tipo.Mago:
        sound.sAtacar()
    elif jugador.tipo == tipo.Samurai:
        sound.sAtacar()
    elif jugador.tipo == tipo.Ninja:
        sound.sAtacar()



    elif jugador.tipo == tipo_2.NarutoS.tipo:
        if jugador.nombre == 'Naruto':
            sound.Naruto_win() 
        elif jugador.nombre == 'Sasuke':
            sound.Sasuke_win()
    elif jugador.tipo == tipo_2.DBZ.tipo:
        if jugador.nombre == 'Goku':
            sound.Goku_win() 
        elif jugador.nombre == 'Vegeta':
            sound.Vegeta_win()
    elif jugador.tipo == tipo_2.Genshin.tipo:
        if jugador.nombre == 'Kazuha':
            sound.Kazuha_win() 
        elif jugador.nombre == 'Alhacen':
            sound.Alhacen_win()
    elif jugador.tipo == tipo_2.Kof.tipo:
        if jugador.nombre == 'Iori':
            sound.Iori_win() 
        elif jugador.nombre == 'Kyo':
            sound.Kyo_win()
    elif jugador.tipo == tipo_2.Bleach.tipo:
        if jugador.nombre == 'Ichigo':
            sound.Ichigo_win() 
        elif jugador.nombre == 'Aizen':
            sound.Aizen_win()



def sonido_win_o():
    from player.personaje import oponente, tipo, tipo_2

    from sound import sound

    if oponente.tipo == tipo.Humano:
        sound.sAtacar()
    elif oponente.tipo == tipo.Mago:
        sound.sAtacar()
    elif oponente.tipo == tipo.Samurai:
        sound.sAtacar()
    elif oponente.tipo == tipo.Ninja:
        sound.sAtacar()



    elif oponente.tipo == tipo_2.NarutoS.tipo:
        if oponente.nombre == 'Naruto':
            sound.Naruto_win() 
        elif oponente.nombre == 'Sasuke':
            sound.Sasuke_win()
    elif oponente.tipo == tipo_2.DBZ.tipo:
        if oponente.nombre == 'Goku':
            sound.Goku_win() 
        elif oponente.nombre == 'Vegeta':
            sound.Vegeta_win()
    elif oponente.tipo == tipo_2.Genshin.tipo:
        if oponente.nombre == 'Kazuha':
            sound.Kazuha_win() 
        elif oponente.nombre == 'Alhacen':
            sound.Alhacen_win()
    elif oponente.tipo == tipo_2.Kof.tipo:
        if oponente.nombre == 'Iori':
            sound.Iori_win() 
        elif oponente.nombre == 'Kyo':
            sound.Kyo_win()
    elif oponente.tipo == tipo_2.Bleach.tipo:
        if oponente.nombre == 'Ichigo':
            sound.Ichigo_win() 
        elif oponente.nombre == 'Aizen':
            sound.Aizen_win()










# _______________________________________________________________________

def eleccion_c():
    from reset import R
    print("\n¿Deseas volver a jugar?")
    print("1 = SI\n"
        "2 = NON")
    eleccion = int(input("\nEleccion: "))
    try:
        if eleccion == 1:
            R.Reset()
            from main import Juego
            return Juego()
        elif eleccion == 2:
            from sound import sound
            sound.sGameOver()
            print("\n\033[33m**************** Terminando el programa. **************\033[0m\n")
            for i in range(3+1):
                print(i)
                time.sleep(1)
            raise SystemExit()
        else:
            from sound import sound
            sound.sError()
            os.system("cls")
            print("Intente nuevamente")
            eleccion_c()
    except ValueError:
        from sound import sound
        sound.sError()
        os.system("cls")
        print("Intente nuevamente")
        eleccion_c()
# _______________________________________________________________________
#-------------------------------------------------------------------------
    
