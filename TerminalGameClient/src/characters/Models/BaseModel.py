from utils.common import time, os, random



class Personaje:
    def __init__(self, nombre, vida, poder, stamina, tipo):
        self.nombre = nombre
        self.vida = vida
        self.poder = poder
        self.stamina = stamina
        self.dano = 0
        self.moneda = 100
        self.mochila = []
        self.tipo = tipo

    def atacar(self):
        pass

    

    def esperar(self):
        self.stamina += 15
        self.vida += 15
        time.sleep(3)

    def esquivar(self):
        from utils.constants import jugador, oponente
        esquivo = random.choice(['esquivar', 'no_esquivar'])
        if esquivo == 'esquivar':
            jugador.vida += oponente.dano
            
        else:
            daño_recibido = oponente.dano / 1.5
            jugador.vida -= daño_recibido
        time.sleep(3)
