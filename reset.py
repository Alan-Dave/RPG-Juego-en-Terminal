


class R():
    
    def PuntoR():
        from player.personaje import jugador, oponente
        global oponente_s
        global oponente_r
        global jugador_s
        global jugador_r
        oponente_r = 0
        oponente_r = oponente.vida

        oponente_s = 0
        oponente_s = oponente.stamina

        jugador_r = 0
        jugador_r = jugador.vida

        jugador_s = 0
        jugador_s = jugador.stamina

    def Reset():
        from player.personaje import jugador, oponente
        oponente.vida = oponente_r
        oponente.stamina = oponente_s

        jugador.vida = jugador_r
        jugador.stamina = jugador_s

        jugador.moneda += jugador.moneda + 100
        oponente.moneda += oponente.moneda + 100
