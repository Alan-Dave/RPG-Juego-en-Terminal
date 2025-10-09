import os
import time
import random






class personaje():            # Atributos principales
    def __init__(self, nombre, vida, poder, stamina):
        self.nombre = nombre
        self.vida = vida
        self.poder = poder
        self.stamina = stamina
        self.dano = 0
# Metodo o accion para atacar al oponente
    moneda = 100
    mochila = []

    def atacar(self):
        
        if self.stamina >= 10:
            
            self.dano = self.poder // 10
            self.stamina -= 10
            if self.nombre == jugador.nombre:
                sonidos_atacar_j()
                oponente.vida -= self.dano
                print(f"\n\033[32m{self.nombre} ataca a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                time.sleep(3)
            else:
                sonidos_atacar_o()
                jugador.vida -= self.dano
                print(f"\n\033[32m{self.nombre} ataca a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                time.sleep(3)
        else:
            from sections.menu import menu
            from sound import sound
            sound.sError()
            if self.nombre == oponente.nombre:
                print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para atacar.\033[0m")
                time.sleep(2.5)
                oponente.elegir_accion()
            if self.nombre == jugador.nombre:
                print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para atacar.\033[0m")
                time.sleep(2.5)
                menu()

# Muestra el estado de un personaje
    def estado(self):
        os.system("cls")
        print(f"\033[38;5;208m[{self.nombre}]               \n"
              f"Vida: {self.vida:.1f}             \n"                
              f"Poder: {self.poder}\n"
              f"Stamina: {self.stamina}\n\033[0m")
    #--------------------------------------------------------------------
    def estado_op(self):
        os.system("cls")
        from sound import sound
        sound.sEstado()
        print("-------------------------------------------------------")
        print(f"\033[38;5;208m  | *          [{oponente.nombre}]      ")
        vida_oponente()
        print(f"  | *         Poder: {oponente.poder}        \n"
              f"  | *         Stamina: {oponente.stamina}    \033[0m \n")
        print("-------------------------------------------------------")
        print(f"Este es el estado de {oponente.nombre}")
        print("")
        print("")
#-----------------------------------------------------------------------------------------------
    def esta_vivo(self):  # esto es para gestionar la vida, pero aun no se usarlo, por ahora solo ignorar
        return self.vida > 0
    
    def esperar(self):
        from sound import sound
        sound.sEsperar()
        print(f"\n\033[32m{self.nombre} decide esperar y recupera +15 de estamina y regenera la vida +15 pts\033[0m")
        self.stamina += 15
        self.vida += 15
        time.sleep(3)




    def esquivar_j(self):
          
        esquivar = ['esquivar', 'no_esquivar']
        esquivo = random.choice(esquivar)
        if oponente.dano > 0:
            if esquivo == 'esquivar':
                jugador.vida += oponente.dano
                print(f"\n\033[32m{jugador.nombre} esquiva con éxito y no recibe daño\033[0m")
                sonidos_esquivar_j()         # Asegúrate de que esta función esté definida o importada.
                time.sleep(3)
            else:  # Si no esquiva, aplica el daño.
                jugador.vida += oponente.dano / 1.5  # Resta el daño a la vida del jugador.
                print(f"\n\033[33m{jugador.nombre} no logra esquivar el ataque y recibe {oponente.dano / 1.5:.1f} de daño\033[0m")
                sonidos_no_esquiva_j()
                time.sleep(3)
        else:
            sonidos_try_esquivar_j()
            print(f"\n\033[96m{jugador.nombre} se prepara para atacar\033[0m")
            time.sleep(2)
            from sections.menu import menu
            return menu




    def esquivar_o(self):
          
        esquivar = ['esquivar', 'no_esquivar']
        esquivo = random.choice(esquivar)
        
        if jugador.dano > 0:
            if esquivo == 'esquivar':
                oponente.vida += jugador.dano
                print(f"\n\033[32m{oponente.nombre} esquiva con éxito y no recibe daño\033[0m")
                sonidos_esquivar_o()         # Asegúrate de que esta función esté definida o importada.
                time.sleep(3)
            else:  # Si no esquiva, aplica el daño.
                oponente.vida += jugador.dano / 1.5  # Resta el daño a la vida del jugador.
                print(f"\n\033[33m{oponente.nombre} no logra esquivar el ataque y recibe {jugador.dano / 1.5:.1f} de daño\033[0m")
                sonidos_no_esquiva_o()
                time.sleep(3)
        else:
            sonidos_try_esquivar_o()
            print(f"\n\033[96m{oponente.nombre} se prepara para atacar\033[0m")
            time.sleep(2)
            from sections.menu import menu
            return menu

    


























    
    def elegir_accion(self):
        #________________________________________________________________________
        if oponente.tipo == tipo.Samurai.tipo:
            acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'corte', 'corte', 'esquivar', 'esquivar']
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'esquivar':
                return self.esquivar_o()
            elif accion == 'corte':
                return tipo.Samurai.CorteDimensional(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            #________________________________________________________________________
        elif oponente.tipo == tipo.Mago.tipo:
            acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'paralizado', 'paralizado', 'Yagai', 'esquivar', 'esquivar'] # Agregar veneno
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'paralizado':
                return tipo.Mago.paralizar(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            elif accion == 'Yagai':
                return tipo.Mago.Yagai(self=oponente)
            elif accion == 'esquivar':
                return self.esquivar_o()
            #________________________________________________________________________
        elif oponente.tipo == tipo.Humano.tipo:
            acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'punch', 'punch', 'esquivar', 'esquivar']
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'punch':
                return tipo.Humano.OnePunch(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            elif accion == 'esquivar':
                return self.esquivar_o()
            #________________________________________________________________________
        elif oponente.tipo == tipo.Ninja.tipo:
            acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'shuriken', 'shuriken', 'esquivar', 'esquivar']
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'shuriken':
                return tipo.Ninja.Shuriken(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            elif accion == 'esquivar':
                return self.esquivar_o()
            
#########################################################################################################################################################






#________________________________________________________________________
        elif oponente.tipo == tipo_2.NarutoS.tipo:
            if oponente.nombre == 'Naruto':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'Rasengan', 'Rasengan', 'RasenShuriken', 'esquivar', 'esquivar']
            elif oponente.nombre == 'Sasuke':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'Chidori', 'Chidori', 'Raikiri', 'esquivar', 'esquivar']
            
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'Rasengan':
                return tipo_2.Naruto.Rasengan(self=oponente)
            elif accion == 'RasenShuriken':
                return tipo_2.Naruto.RasenShuriken(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            elif accion == 'Chidori':
                return tipo_2.Sasuke.Chidori(self=oponente)
            elif accion == 'Raikiri':
                return tipo_2.Sasuke.Raikiri(self=oponente)
            elif accion == 'esquivar':
                return self.esquivar_o()
#________________________________________________________________________
        elif oponente.tipo == tipo_2.Bleach.tipo:
            if oponente.nombre == 'Ichigo':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'Getsuga', 'Getsuga', 'Bankai', 'esquivar', 'esquivar']
            elif oponente.nombre == 'Aizen':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'Kido', 'Kido', 'Kyokasuigetsu', 'esquivar', 'esquivar']
            
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'Rasengan':
                return tipo_2.Ichigo.Getsuga(self=oponente)
            elif accion == 'RasenGetsuga':
                return tipo_2.Ichigo.Bankai(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            elif accion == 'Chidori':
                return tipo_2.Aizen.A_kido(self=oponente)
            elif accion == 'Raikiri':
                return tipo_2.Aizen.Kyokasuigetsu(self=oponente)
            elif accion == 'esquivar':
                return self.esquivar_o()
        #________________________________________________________________________
        elif oponente.tipo == tipo_2.Kof.tipo:
            if oponente.nombre == 'Iori':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'iori_1', 'iori_1', 'iori_2', 'esquivar', 'esquivar']
            elif oponente.nombre == 'Kyo':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'kyo_1', 'kyo_1', 'iori_2', 'esquivar', 'esquivar']
            
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'iori_1':
                return tipo_2.Iori.Iori_1(self=oponente)
            elif accion == 'iori_2':
                return tipo_2.Iori.Iori_2(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            elif accion == 'kyo_1':
                return tipo_2.Kyo.Kyo_1(self=oponente)
            elif accion == 'kyo_2':
                return tipo_2.Kyo.Kyo_2(self=oponente)
            elif accion == 'esquivar':
                return self.esquivar_o()
    #________________________________________________________________________
        elif oponente.tipo == tipo_2.Genshin.tipo:
            if oponente.nombre == 'Kazuha':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'K_elemental', 'K_elemental', 'K_ulti', 'esquivar', 'esquivar']
            elif oponente.nombre == 'Alhacen':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'A_elemental', 'A_elemental', 'A_ulti', 'esquivar', 'esquivar']
            
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'K_elemental':
                return tipo_2.Kazuha.K_elemental(self=oponente)
            elif accion == 'K_ulti':
                return tipo_2.Kazuha.K_ulti(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            elif accion == 'A_elemental':
                return tipo_2.Alhacen.A_elemental(self=oponente)
            elif accion == 'A_ulti':
                return tipo_2.Alhacen.A_ulti(self=oponente)
            elif accion == 'esquivar':
                return self.esquivar_o()
        #________________________________________________________________________
        elif oponente.tipo == tipo_2.DBZ.tipo:
            if oponente.nombre == 'Goku':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'Kamehameha', 'Kamehameha', 'Ssj_g', 'esquivar', 'esquivar']
            elif oponente.nombre == 'Vegeta':
                acciones = ['atacar', 'atacar', 'atacar', 'esperar', 'Garlick_Gun', 'Garlick_Gun', 'Ssj_v', 'esquivar', 'esquivar']
            
            accion = random.choice(acciones)

            if accion == 'atacar':
                return self.atacar()
            elif accion == 'Kamehameha':
                return tipo_2.Goku.Kamehameha(self=oponente)
            elif accion == 'Super_Saiyajin':
                return tipo_2.Goku.Ssj(self=oponente)
            elif accion == 'esperar':
                return self.esperar()
            elif accion == 'Ssj_g':
                return tipo_2.Vegeta.GarlickGun(self=oponente)
            elif accion == 'Ssj_v':
                return tipo_2.Vegeta.Ssj(self=oponente)
            elif accion == 'esquivar':
                return self.esquivar_o()
#________________________________________________________________________





































# _________[Tipos de Personajes]_________________#
#modelos basicos
# _________________________________________________________________________________________________________________
class tipo():
    
    
    class Humano(personaje):
        def __init__(self, nombre):
            super().__init__(nombre, vida=100, poder=120, stamina=60)
        tipo = 'Humano'
        def OnePunch(self):
            if self.stamina >= 30:
                from sound import sound
                sound.sPunch()
                self.dano = self.poder // 3
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} golpea fuertemente a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} golpea fuertemente a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para golpear fuerte.\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina golpear fuerte.\033[0m")
                    time.sleep(2.5)
                    menu()



    class John(Humano):
        def __init__(self, nombre):
            super().__init__(nombre, vida=150, poder=220, stamina=250)

        


    # _________________________________________________________________________________________________________________
                
    class Mago(personaje):
        def __init__(self, nombre):
            super().__init__(nombre, vida=100, poder=160, stamina=150)
        tipo = 'Mago'
        
        def paralizar(self):
            if self.stamina >= 45:
                from sound import sound
                sound.sParalizar()
                self.dano = self.poder // 10
                self.stamina -= 45
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} ha paralizado a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño adicional\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes y pierde un turno.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} ha paralizado a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño adicional\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                    oponente.elegir_accion()
            else:
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para inmovilizar.\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    from sections.menu import menu
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para inmovilizar.\033[0m")
                    time.sleep(2.5)
                    menu()
        
        def Yagai(self):
            if self.stamina >= 80:
                from sound import sound
                sound.sYagai()
                self.dano = self.poder // 3
                self.stamina -= 80
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Yagai letal a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes y pierde un turno.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Yagai letal a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para lanzar Yagai.\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    from sections.menu import menu
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para lanzar Yagai.\033[0m")
                    time.sleep(2.5)
                    menu()
            

        #def envenenamiento():

    # _________________________________________________________________________________________________________________

    class Samurai(personaje):
        def __init__(self, nombre):
            super().__init__(nombre, vida=100, poder=200, stamina=100)
        tipo = 'Samurai'
        def CorteDimensional(self):
            if self.stamina >= 60:
                from sound import sound
                sound.sCorteDimensional()
                self.dano = self.poder // 4
                self.stamina -= 60
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} realiza un corte dimensional a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} realiza un corte dimensional a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\033[31m{self.nombre} no tiene suficiente stamina para cortar la dimensión.\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    from sections.menu import menu
                    print(f"\033[31m{self.nombre} no tiene suficiente stamina para cortar la dimensión.\033[0m")
                    time.sleep(2.5)
                    menu()

    # _________________________________________________________________________________________________________________
                




    class Ninja(personaje):
        def __init__(self, nombre):
            super().__init__(nombre, vida=100, poder=140, stamina=80)
        tipo = 'Ninja'

        def Shuriken(self):
            if self.stamina >= 35:
                from sound import sound
                sound.sShuriken()
                self.dano = self.poder // 4
                self.stamina -= 35
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un shurikens a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un shurikens a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\033[31m{self.nombre} no tiene suficiente stamina para lanzar shurikens.\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    from sections.menu import menu
                    print(f"\033[31m{self.nombre} no tiene suficiente stamina para lanzar shurikens.\033[0m")
                    time.sleep(2.5)
                    menu()







    class Zaji(Ninja):
        def __init__(self, nombre):
            super().__init__(nombre, vida=150, poder=220, stamina=250)

        
























class tipo_2():



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


    """



    CLASES PARA COLOCAR DIFERENCIAS ENTRE PERSONAJES, Y SONIDOS UNICOS




    """

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

    class NarutoS(personaje):

        def __init__(self, nombre, vida, poder, stamina):
            self.nombre = nombre
            self.vida = vida
            self.poder = poder
            self.stamina = stamina
            self.dano = 0  # El atributo 'dano' se inicializa en 0
    # Metodo o accion para atacar al oponente
        moneda = 100
        mochila = []

        tipo = 'Naruto'

        def Rasengan(self):
            if self.stamina >= 60:
                from sound import sound
                sound.sRasengan()
                self.dano = self.poder // 4
                self.stamina -= 60
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Rasengan a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Rasengan a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un Rasengan\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un Rasengan\033[0m")
                    time.sleep(2.5)
                    menu()
                    
        def RasenShuriken(self):
            if self.stamina >= 150:
                from sound import sound
                sound.sRasenShuriken()
                self.dano = self.poder // 2
                self.stamina -= 150
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un RasenShuriken a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un RasenShuriken a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un RasenShuriken\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un RasenShuriken\033[0m")
                    time.sleep(2.5)
                    menu()



        def Chidori(self):
            if self.stamina >= 60:
                from sound import sound
                sound.sChidori()
                self.dano = self.poder // 5
                self.stamina -= 60
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Chidori a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Chidori a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un Chidori\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un Chidori\033[0m")
                    time.sleep(2.5)
                    menu()

        def Raikiri(self):
            if self.stamina >= 150:
                from sound import sound
                sound.sRaikiri()
                self.dano = self.poder // 2
                self.stamina -= 150
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Raikiri a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Raikiri a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un Raikiri\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un Raikiri\033[0m")
                    time.sleep(2.5)
                    menu()

    #Personajes del mundo naruto



    class Naruto(NarutoS):
        def __init__(self, nombre):
            super().__init__(nombre, vida=270, poder=250, stamina=350)  # Naruto tiene alta vida y stamina, con buen poder


    class Sasuke(NarutoS):
        def __init__(self, nombre):
            super().__init__(nombre, vida=230, poder=280, stamina=270)  # Sasuke tiene mayor poder pero menos vida

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################



    class DBZ(personaje):

        def __init__(self, nombre, vida, poder, stamina):
            self.nombre = nombre
            self.vida = vida
            self.poder = poder
            self.stamina = stamina
            self.dano = 0  # El atributo 'dano' se inicializa en 0
    # Metodo o accion para atacar al oponente
        moneda = 100
        mochila = []

        tipo = 'Saiyajin'

        def Kamehameha(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sKamehameha()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Kamehameha a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Kamehameha a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un Kamehameha\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un Kamehameha\033[0m")
                    time.sleep(2.5)
                    menu()



        def GarlickGun(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sGarlickGun()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Garlick Gun a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Garlick Gun a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un Garlick Gun\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un Garlick Gun\033[0m")
                    time.sleep(2.5)
                    menu()


        def Ssj(self):
            if self.stamina >= 150:
                from sound import sound
                sound.sSsj()
                self.stamina -= 150
                self.vida += 100
                self.stamina += 100
                self.poder += 100
                
                if self.nombre == jugador.nombre:
                    
                    print(f"\n\033[32m{self.nombre} se ha transformado en Super Saiyajin\033[0m")
                    print(f"\033[32mvida-stamina-poder +100 \033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    
                    print(f"\n\033[32m{self.nombre} se ha transformado en Super Saiyajin\033[0m")
                    print(f"\033[32mvida-stamina-poder +100\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para usar el Ssj\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina usar el Ssj\033[0m")
                    time.sleep(2.5)
                    menu()




        
    class Goku(DBZ):
        def __init__(self, nombre):
            super().__init__(nombre, vida=250, poder=300, stamina=320)  # Goku tiene estadísticas superiores en todo


    class Vegeta(DBZ):
        def __init__(self, nombre):
            super().__init__(nombre, vida=240, poder=290, stamina=310)  # Vegeta es similar a Goku, pero ligeramente más débil


################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################



    class Kof(personaje):

        def __init__(self, nombre, vida, poder, stamina):
            self.nombre = nombre
            self.vida = vida
            self.poder = poder
            self.stamina = stamina
            self.dano = 0  # El atributo 'dano' se inicializa en 0
    # Metodo o accion para atacar al oponente
        moneda = 100
        mochila = []

        tipo = 'Kof'


        def Iori_1(self):
            if self.stamina >= 30:
                from sound import sound
                sound.sIori_1()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un combo combinado a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un combo combinado a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un combo combinado\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un combo combinado\033[0m")
                    time.sleep(2.5)
                    menu()

        def Kyo_1(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sKyo_1()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un combo combinado a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un combo combinado a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un combo combinado\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un combo combinado\033[0m")
                    time.sleep(2.5)
                    menu()



        def Iori_2(self):
            if self.stamina >= 50:
                from sound import sound
                sound.sIori_2()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un poder a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un poder a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un poder\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un poder\033[0m")
                    time.sleep(2.5)
                    menu()

        def Kyo_2(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sKyo_2()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un poder a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un poder a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un poder\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un poder\033[0m")
                    time.sleep(2.5)
                    menu()






    class Iori(Kof):
        def __init__(self, nombre):
            super().__init__(nombre, vida=160, poder=240, stamina=220)  # Iori tiene un gran poder y stamina moderada


    class Kyo(Kof):
        def __init__(self, nombre):
            super().__init__(nombre, vida=170, poder=230, stamina=210)  # Kyo es un luchador equilibrado

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################



    class Genshin(personaje):

        def __init__(self, nombre, vida, poder, stamina):
            self.nombre = nombre
            self.vida = vida
            self.poder = poder
            self.stamina = stamina
            self.dano = 0  # El atributo 'dano' se inicializa en 0
    # Metodo o accion para atacar al oponente
        moneda = 100
        mochila = []

        tipo = 'Genshin'


        def A_ulti(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sA_ulti()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un ulti a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un ulti a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un ulti\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un ulti\033[0m")
                    time.sleep(2.5)
                    menu()

        def A_elemental(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sA_elemental()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza la elemental a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza la elemental a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para la elemental\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina la elemental\033[0m")
                    time.sleep(2.5)
                    menu()

        def K_ulti(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sK_ulti()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un ulti a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un ulti a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un ulti\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un ulti\033[0m")
                    time.sleep(2.5)
                    menu()

        def K_elemental(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sK_elemental()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza la elemental a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza la elemental a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para la elemental\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina la elemental\033[0m")
                    time.sleep(2.5)
                    menu()








    class Kazuha(Genshin):
        def __init__(self, nombre):
            super().__init__(nombre, vida=150, poder=200, stamina=300)  # Kazuha es ágil y tiene alta stamina


    class Alhacen(Genshin):
        def __init__(self, nombre):
            super().__init__(nombre, vida=170, poder=210, stamina=280)  # Alhacen es balanceado con buena stamina


################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################


    class Bleach(personaje):

        def __init__(self, nombre, vida, poder, stamina):
            self.nombre = nombre
            self.vida = vida
            self.poder = poder
            self.stamina = stamina
            self.dano = 0  # El atributo 'dano' se inicializa en 0
    # Metodo o accion para atacar al oponente
        moneda = 100
        mochila = []

        tipo = 'Segador'


        def Getsuga(self):
            if self.stamina >= 50:
                from sound import sound
                sound.sGetsuga()
                self.dano = self.poder // 5
                self.stamina -= 50
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Getsuga Tensho a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Getsuga Tensho a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un Getsuga Tensho\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un Getsuga Tensho\033[0m")
                    time.sleep(2.5)
                    menu()
                    
        def Bankai(self):
            if self.stamina >= 150:
                from sound import sound
                sound.sBankai()
                self.stamina -= 150
                self.vida += 100
                self.stamina += 100
                self.poder += 100
                
                if self.nombre == jugador.nombre:
                    
                    print(f"\n\033[32m{self.nombre} se ha usado Bankai\033[0m")
                    print(f"\033[32mvida-stamina-poder +100\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    
                    print(f"\n\033[32m{self.nombre} se ha usado Bankai\033[0m")
                    print(f"\033[32mvida-stamina-poder +100\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para usar Bankai\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina usar Bankai\033[0m")
                    time.sleep(2.5)
                    menu()



        def A_kido(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sA_kido()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Kido a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Kido a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un Kido\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un Kido\033[0m")
                    time.sleep(2.5)
                    menu()

        def Kyokasuigetsu(self):
            if self.stamina >= 130:
                from sound import sound
                sound.sKyokasuigetsu()
                self.dano = self.poder // 2
                self.stamina -= 30
                if self.nombre == jugador.nombre:
                    oponente.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Kido a {oponente.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{oponente.nombre} tiene {oponente.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
                elif self.nombre == oponente.nombre:
                    jugador.vida -= self.dano
                    print(f"\n\033[32m{self.nombre} lanza un Kido a {jugador.nombre} y causa \033[31m{self.dano}\033[0m de daño.\033[0m")
                    print(f"\033[32m{jugador.nombre} tiene {jugador.vida:.1f} puntos de vida restantes.\033[0m\n")
                    time.sleep(3)
            else:
                from sections.menu import menu
                from sound import sound
                sound.sError()
                if self.nombre == oponente.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina para un Kido\033[0m")
                    time.sleep(2.5)
                    oponente.elegir_accion()
                if self.nombre == jugador.nombre:
                    print(f"\n\033[31m{self.nombre} no tiene suficiente stamina un Kido\033[0m")
                    time.sleep(2.5)
                    menu()
        


    class Ichigo(Bleach):
        def __init__(self, nombre):
            super().__init__(nombre, vida=180, poder=250, stamina=200)  # Ichigo tiene un gran poder y resistencia


    class Aizen(Bleach):
        def __init__(self, nombre):
            super().__init__(nombre, vida=200, poder=260, stamina=180)  # Aizen es extremadamente poderoso, con alta vida



################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################









































# _________________________________________________________________________________________________________________
            
# Nombres de los personajes


class char():
    # PERSONAJES HUMANO
    Humano = tipo.Humano(nombre="Humano")
    John = tipo.Humano(nombre='John Wick')
    

    #_______________________________
    # PERSONAJES MAGOS
    Mago = tipo.Mago(nombre="Mago")


    #_______________________________
    # PERSONAJES SAMURAI
    Samurai = tipo.Samurai(nombre="Samurai")
    

    
    #_______________________________
    # PERSONAJES NINJA
    Ninja = tipo.Ninja(nombre="Ninja")
    Zaji = tipo.Ninja(nombre='Zaji')


    #_______________________________






    # NARUTO
    Naruto = tipo_2.Naruto(nombre='Naruto')
    Sasuke = tipo_2.Sasuke(nombre='Sasuke')

    # BLEACH
    Ichigo = tipo_2.Ichigo(nombre='Ichigo')
    Aizen = tipo_2.Aizen(nombre='Aizen')

    # GENSHIN
    Kazuha = tipo_2.Kazuha(nombre='Kazuha')
    Alhacen = tipo_2.Alhacen(nombre='Alhacen')

    # DRAGON BALL Z
    Goku = tipo_2.Goku(nombre='Goku')
    Vegeta = tipo_2.Vegeta(nombre='Vegeta')

    # KING OF FIGHTERS
    Kyo = tipo_2.Kyo(nombre='Kyo')
    Iori = tipo_2.Iori(nombre='Iori')


    #__________________________________________________________________________________________________________
    #########################################################################################################################################################




def elegir_personaje():
    global eleccion
    global jugador
    global vida_maxima_j
    jugador = None
    print("\033[33mElige tu personaje:\033[0m\n")

    print("1. Humano                 6. Naruto                   11. Kazuha   \n"
          "2. Mago                   7. Sasuke                   12. Vegeta     \n"
          "3. Samurai                8. Iori                     13. Alhacen  \n"
          "4. Ninja                  9. Kyo                      14. Goku     \n"
          "5. John Wick             10. Ichigo                   15. Aizen     ")
    
    print("\n0. Elegir aleatoriamente")
    
    try:
        eleccion = int(input("\nIntroduce el número de tu elección: "))
        if eleccion == 0:
            jugador = random.choice([
                tipo.Humano("Humano"), tipo.Mago("Mago"), tipo.Samurai("Samurai"), tipo.Ninja("Ninja"),
                tipo.Humano("John Wick"), tipo_2.Naruto("Naruto"), tipo_2.Sasuke("Sasuke"), tipo_2.Ichigo("Ichigo"),
                tipo_2.Kyo("Kyo"), tipo_2.Iori("Iori"), tipo_2.Kazuha("Kazuha"), tipo_2.Alhacen("Alhacen"), tipo_2.Vegeta("Vegeta"), tipo_2.Goku("Goku")
            ])
        elif eleccion == 1:
            jugador = char.Humano
        elif eleccion == 2:
            jugador = char.Mago
        elif eleccion == 3:
            jugador = char.Samurai
        elif eleccion == 4:
            jugador = char.Ninja
        elif eleccion == 5:
            jugador = char.John
        elif eleccion == 6:
            jugador = char.Naruto
        elif eleccion == 7:
            jugador = char.Sasuke
        elif eleccion == 8:
            jugador = char.Iori
        elif eleccion == 9:
            jugador = char.Kyo
        elif eleccion == 10:
            jugador = char.Ichigo
        elif eleccion == 11:
            jugador = char.Kazuha
        elif eleccion == 12:
            jugador = char.Vegeta
        elif eleccion == 13:
            jugador = char.Alhacen
        elif eleccion == 14:
            jugador = char.Goku
        elif eleccion == 15:
            jugador = char.Aizen
    
    

    except ValueError:
        os.system("cls")
        print("\n\033[31mElección no válida.\033[0m\n")
        elegir_personaje()
    
    vida_maxima_j = jugador.vida







def vida_jugador():
    # Asume que entidad tiene un atributo `vida` y `vida_maxima`
    porcentaje_vida = jugador.vida / vida_maxima_o
    # Número total de bloques en la barra de vida
    total_bloques = 10

    # Calcula cuántos bloques llenos deben mostrarse
    bloques_llenos = int(porcentaje_vida * total_bloques)
    
    # Construye la barra de vida
    barra_vida = '█' * bloques_llenos + ' ' * (total_bloques - bloques_llenos)
    
    print(f"  |  vida:   |{barra_vida}| ({int(porcentaje_vida * 100)}%)")







        







oponente = random.choice([
                tipo.Humano("Humano"), tipo.Mago("Mago"), tipo.Samurai("Samurai"), tipo.Ninja("Ninja"),
                tipo.Humano("John Wick"), tipo_2.Naruto("Naruto"), tipo_2.Sasuke("Sasuke"), tipo_2.Ichigo("Ichigo"),
                tipo_2.Kyo("Kyo"), tipo_2.Iori("Iori"), tipo_2.Kazuha("Kazuha"), tipo_2.Alhacen("Alhacen"), tipo_2.Vegeta("Vegeta"), tipo_2.Goku("Goku")
            ])

    




# para que no pelees contra tu propio personaje



def personaje_igual():
    global oponente
    while jugador.nombre == oponente.nombre:
            oponente = None
            oponente = random.choice([
                tipo.Humano("Humano"), tipo.Mago("Mago"), tipo.Samurai("Samurai"), tipo.Ninja("Ninja"),
                tipo.Humano("John Wick"), tipo_2.Naruto("Naruto"), tipo_2.Sasuke("Sasuke"), tipo_2.Ichigo("Ichigo"),
                tipo_2.Kyo("Kyo"), tipo_2.Iori("Iori"), tipo_2.Kazuha("Kazuha"), tipo_2.Alhacen("Alhacen"), tipo_2.Vegeta("Vegeta"), tipo_2.Goku("Goku")
            ])
        

vida_maxima_o = oponente.vida








def vida_oponente():
    # Asume que entidad tiene un atributo `vida` y `vida_maxima`
    porcentaje_vida = oponente.vida / vida_maxima_o
    # Número total de bloques en la barra de vida
    total_bloques = 10

    # Calcula cuántos bloques llenos deben mostrarse
    bloques_llenos = int(porcentaje_vida * total_bloques)
    
    # Construye la barra de vida
    barra_vida = '█' * bloques_llenos + ' ' * (total_bloques - bloques_llenos)
    
    print(f"  | * vida:  |{barra_vida}| ({int(porcentaje_vida * 100)}%)")







personajes_name = [[
                tipo.Humano("Humano"), tipo.Mago("Mago"), tipo.Samurai("Samurai"), tipo.Ninja("Ninja"),
                tipo.Humano("John Wick"), tipo_2.Naruto("Naruto"), tipo_2.Sasuke("Sasuke"), tipo_2.Ichigo("Ichigo"),
                tipo_2.Kyo("Kyo"), tipo_2.Iori("Iori"), tipo_2.Kazuha("Kazuha"), tipo_2.Alhacen("Alhacen"), tipo_2.Vegeta("Vegeta"), tipo_2.Goku("Goku")
            ]]















def sonidos_atacar_j():
    
    from sound import sound

    if jugador.tipo == tipo.Humano.tipo:
        sound.sAtacar()
    elif jugador.tipo == tipo.Mago.tipo:
        sound.sAtacar()
    elif jugador.tipo == tipo.Samurai.tipo:
        sound.sAtacar()
    elif jugador.tipo == tipo.Ninja.tipo:
        sound.sAtacar()



    elif jugador.tipo == tipo_2.NarutoS.tipo:
        if jugador.nombre == 'Naruto':
            sound.sNarutoA() 
        elif jugador.nombre == 'Sasuke':
            sound.sSasukeA()
    elif jugador.tipo == tipo_2.DBZ.tipo:
        if jugador.nombre == 'Goku':
            sound.sGokuA() 
        elif jugador.nombre == 'Vegeta':
            sound.sVegetaA()
    elif jugador.tipo == tipo_2.Genshin.tipo:
        if jugador.nombre == 'Kazuha':
            sound.sKazuhaA() 
        elif jugador.nombre == 'Alhacen':
            sound.sAlhacenA()
    elif jugador.tipo == tipo_2.Kof.tipo:
        if jugador.nombre == 'Iori':
            sound.sIoriA() 
        elif jugador.nombre == 'Kyo':
            sound.sKyoA()
    elif jugador.tipo == tipo_2.Bleach.tipo:
        if jugador.nombre == 'Ichigo':
            sound.sIchigoA() 
        elif jugador.nombre == 'Aizen':
            sound.sAizenA()











def sonidos_atacar_o():
    
    from sound import sound

    if oponente.tipo == tipo.Humano.tipo:
        sound.sAtacar()
    elif oponente.tipo == tipo.Mago.tipo:
        sound.sAtacar()
    elif oponente.tipo == tipo.Samurai.tipo:
        sound.sAtacar()
    elif oponente.tipo == tipo.Ninja.tipo:
        sound.sAtacar()



    elif oponente.tipo == tipo_2.NarutoS.tipo:
        if oponente.nombre == 'Naruto':
            sound.sNarutoA() 
        elif oponente.nombre == 'Sasuke':
            sound.sSasukeA()
    elif oponente.tipo == tipo_2.DBZ.tipo:
        if oponente.nombre == 'Goku':
            sound.sGokuA() 
        elif oponente.nombre == 'Vegeta':
            sound.sVegetaA()
    elif oponente.tipo == tipo_2.Genshin.tipo:
        if oponente.nombre == 'Kazuha':
            sound.sKazuhaA() 
        elif oponente.nombre == 'Alhacen':
            sound.sAlhacenA()
    elif oponente.tipo == tipo_2.Kof.tipo:
        if oponente.nombre == 'Iori':
            sound.sIoriA() 
        elif oponente.nombre == 'Kyo':
            sound.sKyoA()
    elif oponente.tipo == tipo_2.Bleach.tipo:
        if oponente.nombre == 'Ichigo':
            sound.sIchigoA() 
        elif oponente.nombre == 'Aizen':
            sound.sAizenA()

# Funcion de esquivar con probabilidades de fallar
































def sonidos_esquivar_o():
    
    from sound import sound

    if oponente.tipo == tipo.Humano.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Mago.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Samurai.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Ninja.tipo:
        sound.sEsquivar()



    elif oponente.tipo == tipo_2.NarutoS.tipo:
        sound.sNarutoSE()
    elif oponente.tipo == tipo_2.DBZ.tipo:
        if oponente.nombre == 'Goku':
            sound.sGokuE() 
        elif oponente.nombre == 'Vegeta':
            sound.sVegetaE()
    elif oponente.tipo == tipo_2.Genshin.tipo:
        if oponente.nombre == 'Kazuha':
            sound.sKazuhaE() 
        elif oponente.nombre == 'Alhacen':
            sound.sAlhacenE()
    elif oponente.tipo == tipo_2.Kof.tipo:
        if oponente.nombre == 'Iori':
            sound.sIoriE() 
        elif oponente.nombre == 'Kyo':
            sound.sKyoE()
    elif oponente.tipo == tipo_2.Bleach.tipo:
        if oponente.nombre == 'Ichigo':
            sound.sIchigoE() 
        elif oponente.nombre == 'Aizen':
            sound.sAizenE()












def sonidos_esquivar_j():
    
    from sound import sound

    if jugador.tipo == tipo.Humano.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Mago.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Samurai.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Ninja.tipo:
        sound.sEsquivar()



    elif jugador.tipo == tipo_2.NarutoS.tipo:
        sound.sNarutoSE()
    elif jugador.tipo == tipo_2.DBZ.tipo:
        if jugador.nombre == 'Goku':
            sound.sGokuE() 
        elif jugador.nombre == 'Vegeta':
            sound.sVegetaE()
    elif jugador.tipo == tipo_2.Genshin.tipo:
        if jugador.nombre == 'Kazuha':
            sound.sKazuhaE() 
        elif jugador.nombre == 'Alhacen':
            sound.sAlhacenE()
    elif jugador.tipo == tipo_2.Kof.tipo:
        if jugador.nombre == 'Iori':
            sound.sIoriE() 
        elif jugador.nombre == 'Kyo':
            sound.sKyoE()
    elif jugador.tipo == tipo_2.Bleach.tipo:
        if jugador.nombre == 'Ichigo':
            sound.sIchigoE() 
        elif jugador.nombre == 'Aizen':
            sound.sAizenE()































def sonidos_no_esquiva_o():
    
    from sound import sound

    if oponente.tipo == tipo.Humano.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Mago.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Samurai.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Ninja.tipo:
        sound.sEsquivar()



    elif oponente.tipo == tipo_2.NarutoS.tipo:
        if oponente.nombre == 'Naruto':
            sound.sNarutoNE() 
        elif oponente.nombre == 'Sasuke':
            sound.sSasukeNE()
    elif oponente.tipo == tipo_2.DBZ.tipo:
        if oponente.nombre == 'Goku':
            sound.sGokuNE() 
        elif oponente.nombre == 'Vegeta':
            sound.sVegetaNE()
    elif oponente.tipo == tipo_2.Genshin.tipo:
        if oponente.nombre == 'Kazuha':
            sound.sKazuhaNE() 
        elif oponente.nombre == 'Alhacen':
            sound.sAlhacenNE()
    elif oponente.tipo == tipo_2.Kof.tipo:
        if oponente.nombre == 'Iori':
            sound.sIoriNE() 
        elif oponente.nombre == 'Kyo':
            sound.sKyoNE()
    elif oponente.tipo == tipo_2.Bleach.tipo:
        if oponente.nombre == 'Ichigo':
            sound.sIchigoNE() 
        elif oponente.nombre == 'Aizen':
            sound.sAizenNE()












def sonidos_no_esquiva_j():
    
    from sound import sound

    if jugador.tipo == tipo.Humano.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Mago.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Samurai.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Ninja.tipo:
        sound.sEsquivar()



    elif jugador.tipo == tipo_2.NarutoS.tipo:
        if jugador.nombre == 'Naruto':
            sound.sNarutoNE() 
        elif jugador.nombre == 'Sasuke':
            sound.sSasukeNE()
    elif jugador.tipo == tipo_2.DBZ.tipo:
        if jugador.nombre == 'Goku':
            sound.sGokuNE() 
        elif jugador.nombre == 'Vegeta':
            sound.sVegetaNE()
    elif jugador.tipo == tipo_2.Genshin.tipo:
        if jugador.nombre == 'Kazuha':
            sound.sKazuhaNE() 
        elif jugador.nombre == 'Alhacen':
            sound.sAlhacenE()
    elif jugador.tipo == tipo_2.Kof.tipo:
        if jugador.nombre == 'Iori':
            sound.sIoriNE() 
        elif jugador.nombre == 'Kyo':
            sound.sKyoNE()
    elif jugador.tipo == tipo_2.Bleach.tipo:
        if jugador.nombre == 'Ichigo':
            sound.sIchigoNE() 
        elif jugador.nombre == 'Aizen':
            sound.sAizenNE()





























def sonidos_try_esquivar_o():
    
    from sound import sound

    if oponente.tipo == tipo.Humano.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Mago.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Samurai.tipo:
        sound.sEsquivar()
    elif oponente.tipo == tipo.Ninja.tipo:
        sound.sEsquivar()



    elif oponente.tipo == tipo_2.NarutoS.tipo:
        if oponente.nombre == 'Naruto':
            sound.sNarutoTE()
        elif oponente.nombre == 'Sasuke':
            sound.sSasukeTE()
    elif oponente.tipo == tipo_2.DBZ.tipo:
        sound.sDBZTE()
    elif oponente.tipo == tipo_2.Genshin.tipo:
        sound.sGenshinTE()
    elif oponente.tipo == tipo_2.Kof.tipo:
        if oponente.nombre == 'Iori':
            sound.sIoriTE() 
        elif oponente.nombre == 'Kyo':
            sound.sKyoTE()
    elif oponente.tipo == tipo_2.Bleach.tipo:
        sound.sBLeachTE()












def sonidos_try_esquivar_j():
    
    from sound import sound

    if jugador.tipo == tipo.Humano.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Mago.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Samurai.tipo:
        sound.sEsquivar()
    elif jugador.tipo == tipo.Ninja.tipo:
        sound.sEsquivar()



    elif jugador.tipo == tipo_2.NarutoS.tipo:
        if jugador.nombre == 'Naruto':
            sound.sNarutoTE()
        elif jugador.nombre == 'Sasuke':
            sound.sSasukeTE()
    elif jugador.tipo == tipo_2.DBZ.tipo:
        sound.sDBZTE()
    elif jugador.tipo == tipo_2.Genshin.tipo:
        sound.sGenshinTE()
    elif jugador.tipo == tipo_2.Kof.tipo:
        if jugador.nombre == 'Iori':
            sound.sIoriTE() 
        elif jugador.nombre == 'Kyo':
            sound.sKyoTE()
    elif jugador.tipo == tipo_2.Bleach.tipo:
        sound.sBLeachTE()



