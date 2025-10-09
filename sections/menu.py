
import os
import time









def menu():
    from player.personaje import tipo, tipo_2, jugador, oponente
    while True:
        os.system("cls")
        if jugador:
            jugador.estado()  # Muestra el estado del personaje elegido
            time.sleep(1)
            print(f"------------ Oponente [{oponente.nombre}] ---------------------|")
            # Muestra el estado del oponente
        else:
            from player.personaje import elegir_personaje
            print("\033[31mNo se ha elegido ningún personaje.\033[0m")
            elegir_personaje()
            continue




        
        print("\n---------------------------------------------------------------------------")
        print("  1. Atacar                  2. Ver estado               3. Esperar         \n "
                "[-10 stamina]                                   [+15 stamina y +15 vida]\n")
        if jugador.tipo == tipo.Mago.tipo:
            print("4. Paralizar                  7. Esquivar          8.     Yagai                         \n"
                    "[-45 stamina]               [-15 stamina]           [-80 stamina]             \n")
        elif jugador.tipo == tipo.Ninja.tipo:
            print("4. Shuriken                   7. Esquivar             \n"
                    "[-35 stamina]               [-15 stamina]    ")                        
        elif jugador.tipo == tipo.Humano.tipo:
            print("4. One Punch                  7. Esquivar\n"
                    "[-30 stamina]               [-15 stamina]  ")             
        elif jugador.tipo == tipo.Samurai.tipo:
            print("4. Corte Dimensional          7. Esquivar\n"
                    "   [-60 stamina]            [-15 stamina]      ")
            
################################################################################################################################

        elif jugador.tipo == tipo_2.NarutoS.tipo:
            if jugador.nombre == 'Naruto':
                print("4. Rasengan               7. Esquivar            8. RasenShuriken         \n"
                        "[-60 stamina]           [-15 stamina]            [-150 stamina]    ")
            elif jugador.nombre == 'Sasuke':
                print("4. Chidori                7. Esquivar               8. Raikiri         \n"
                      "[-60 stamina]             [-15 stamina]           [-150 stamina]    ")

        elif jugador.tipo == tipo_2.Bleach.tipo:
            if jugador.nombre == 'Ichigo':
                print("4. Getsuga  Tensho         7. Esquivar             8. Bankai         \n"
                        "   [-50 stamina]        [-15 stamina]          [-160 stamina]    ")
            elif jugador.nombre == 'Aizen':
                print("4. Kido                    7. Esquivar            8. Kyokasuigetsu         \n"
                        "[-50 stamina]           [-15 stamina]            [-130 stamina]    ")
        
        elif jugador.tipo == tipo_2.Genshin.tipo:
            if jugador.nombre == 'Kazuha':
                print("4. Elemental               7. Esquivar              8. Ulti         \n"
                        "[-50 stamina]           [-15 stamina]          [-130 stamina]    ")
            elif jugador.nombre == 'Alhacen':
                print("4. Elemental               7. Esquivar              8. Ulti        \n"
                        "[-50 stamina]            [-15 stamina]          [-130 stamina]            ")

        elif jugador.tipo == tipo_2.Kof.tipo:
            if jugador.nombre == 'Iori':
                print("4. Combo                   7. Esquivar             8. Especial         \n"
                        "[-50 stamina]           [-15 stamina]           [-130 stamina]    ")
            elif jugador.nombre == 'Kyo':
                print("4. Combo                  7. Esquivar             8. Especial         \n"
                        "[-50 stamina]          [-15 stamina]           [-130 stamina]    ")
        
        elif jugador.tipo == tipo_2.DBZ.tipo:
            if jugador.nombre == 'Goku':
                print("4. Kamehameha           7. Esquivar              8. Super Saiyajin         \n"
                        "[-50 stamina]         [-15 stamina]               [-130 stamina]    ")
            elif jugador.nombre == 'Vegeta':
                print("4. Garlick Gun          7. Esquivar              8. Super Saiyajin         \n"
                        "[-50 stamina]          [-15 stamina]           [-130 stamina]    ")




        print("\n\033[33m5. TIENDA\033[0m                    \033[33m6. MOCHILA\033[0m")



        opciones()

        jugador.stamina += 5
        oponente.stamina += 5
        oponente.dano = 0
        jugador.dano = 0








################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################










################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

















def opciones():
    global accion
    try:
        from player.personaje import jugador, oponente
        from comprobar import comprobar
        accion = int(input("\nIntroduce el número de tu elección: "))
        if accion == 1:
            print("-------------------------------------")
            jugador.atacar()
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif accion == 2:
            print("-------------------------------------")
            oponente.estado_op()
            time.sleep(3)
            print("")
            menu()
        elif accion == 3:
            print("-------------------------------------")
            jugador.esperar()
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif accion == 4:

            combos()

        elif accion == 5:   
            from sound import sound
            sound.sTienda()
            from sections.tienda import Tienda
            sound.sTienda()
            Tienda()
        elif accion == 6:
            from sections.mochila import Mochila
            Mochila()
        elif accion == 7:
            from player.personaje import sonidos_try_esquivar_j
            print("-------------------------------------")
            sonidos_try_esquivar_j()
            print(f"\n\033[96m{jugador.nombre} ha decidido esquivar\033[0m")
            time.sleep(2)
            oponente.elegir_accion()
            jugador.esquivar_j()
            comprobar()

        elif accion == 8:
            
            especiales()

        else:
            print("-------------------------------------")
            print("\033[31mAcción no valida, por favor intente nuevamente\033[0m") # este texto es rojo
            time.sleep(1)
    except ValueError:
        from sound import sound
        sound.sError()
        print("\n\033[32mValueError\033[0m")
        print("\033[31mValor invalido, ingresa nuevamente\033[0m")
        time.sleep(2)
        menu()
    #-------------------------------------------------------------------------
    # _______________________________________________________________________












################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################










def combos():
    from player.personaje import tipo, tipo_2, jugador, oponente
    from comprobar import comprobar

    if jugador.tipo == tipo.Mago.tipo:
        print("-------------------------------------")

        tipo.Mago.paralizar(self=jugador)
        print("")
        comprobar()

    elif jugador.tipo == tipo.Ninja.tipo:
        print("-------------------------------------")

        tipo.Ninja.Shuriken(self=jugador)
        print("")
        comprobar()
        oponente.elegir_accion()
        comprobar()

    elif jugador.tipo == tipo.Humano.tipo:
        print("-------------------------------------")

        tipo.Humano.OnePunch(self=jugador)
        print("")
        comprobar()
        oponente.elegir_accion()
        comprobar()

    elif jugador.tipo == tipo.Samurai.tipo:
        print("-------------------------------------")

        tipo.Samurai.CorteDimensional(self=jugador)
        print("")
        comprobar()
        oponente.elegir_accion()
        comprobar()





    #########################################################
    elif jugador.tipo == tipo_2.NarutoS.tipo:
        print("-------------------------------------")

        if jugador.nombre == 'Naruto':
            tipo_2.Naruto.Rasengan(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Sasuke':
            tipo_2.Sasuke.Chidori(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
    
    elif jugador.tipo == tipo_2.Bleach.tipo:
        print("-------------------------------------")
        if jugador.nombre == 'Ichigo':
            tipo_2.Ichigo.Getsuga(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Aizen': 
            tipo_2.Aizen.A_kido(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()   
    
    elif jugador.tipo == tipo_2.DBZ.tipo:
        print("-------------------------------------")
        if jugador.nombre == 'Goku':
            tipo_2.Goku.Kamehameha(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Vegeta':
            tipo_2.Vegeta.GarlickGun(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()

    elif jugador.tipo == tipo_2.Genshin.tipo:
        print("-------------------------------------")
        if jugador.nombre == 'Kazuha':
            tipo_2.Kazuha.K_elemental(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Alhacen':
            tipo_2.Alhacen.A_elemental(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
    
    elif jugador.tipo == tipo_2.Kof.tipo:
        print("-------------------------------------")
        if jugador.nombre == 'Iori':
            tipo_2.Iori.Iori_1(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Kyo':
            tipo_2.Kyo.Kyo_1(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()























################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################















def especiales():
    from player.personaje import tipo, tipo_2, jugador, oponente
    from comprobar import comprobar

    if jugador.tipo == tipo.Mago.tipo:
        print("-------------------------------------")

        tipo.Mago.Yagai(self=jugador)
        print("")
        comprobar()
        oponente.elegir_accion()
        comprobar()

    elif jugador.tipo == tipo.Ninja.tipo:
                    # Ataque Especial ninja
        print("-------------------------------------")

        tipo.Ninja.Shuriken(self=jugador)
        print("")
        comprobar()
        oponente.elegir_accion()
        comprobar()

    elif jugador.tipo == tipo.Humano.tipo:   
                # Ataque Especial shuriken
        print("-------------------------------------")

        tipo.Humano.OnePunch(self=jugador)
        print("")
        comprobar()
        oponente.elegir_accion()
        comprobar()

    elif jugador.tipo == tipo.Samurai.tipo:    
                # Ataque Especial samurai
        print("-------------------------------------")
        
        tipo.Samurai.CorteDimensional(self=jugador)
        print("")
        comprobar()
        oponente.elegir_accion()
        comprobar()

    




    #########################################################
    elif jugador.tipo == tipo_2.NarutoS.tipo:
        print("-------------------------------------")

        if jugador.nombre == 'Naruto':
            tipo_2.Naruto.RasenShuriken(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Sasuke':
            tipo_2.Sasuke.Raikiri(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
    
    elif jugador.tipo == tipo_2.Bleach.tipo:
        print("-------------------------------------")
        if jugador.nombre == 'Ichigo':
            tipo_2.Ichigo.Bankai(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Aizen': 
            tipo_2.Aizen.Kyokasuigetsu(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()   
    
    elif jugador.tipo == tipo_2.DBZ.tipo:
        print("-------------------------------------")
        if jugador.nombre == 'Goku':
            tipo_2.Goku.Ssj(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Vegeta':
            tipo_2.Vegeta.Ssj(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()

    elif jugador.tipo == tipo_2.Genshin.tipo:
        print("-------------------------------------")
        if jugador.nombre == 'Kazuha':
            tipo_2.Kazuha.K_ulti(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Alhacen':
            tipo_2.Alhacen.A_ulti(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
    
    elif jugador.tipo == tipo_2.Kof.tipo:
        print("-------------------------------------")
        if jugador.nombre == 'Iori':
            tipo_2.Iori.Iori_2(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()
        elif jugador.nombre == 'Kyo':
            tipo_2.Kyo.Kyo_2(self=jugador)
            print("")
            comprobar()
            oponente.elegir_accion()
            comprobar()

