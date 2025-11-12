from utils.common import time, random

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

    def atacar(self, rival):
        ataque = 'ataque basico'
        tipo = 'basico'

        if self.stamina < 10:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': tipo,
                'msg': 'No tienes suficiente stamina',
            }

        self.dano = 30
        self.stamina -= 10
        rival.vida -= self.dano
        
        return {
            'ok': True,
            'ataque': ataque,
            'dano': self.dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado un {ataque} y hace {self.dano} de daño a {rival.nombre}',
        }
    
    

    def mostrar_estado(jugador, oponente, vida_maxima_j, vida_maxima_o):
        print("---------------------------------------------------------------")
        print(f"{jugador.nombre:^30} VS {oponente.nombre:^30}")
        print("---------------------------------------------------------------")

        # Barra de vida (solo ejemplo, asumí que vida_barra devuelve texto)
        barra_j = f"Vida: {jugador.vida}/{vida_maxima_j}"
        barra_o = f"Vida: {oponente.vida}/{vida_maxima_o}"

        print(f"{barra_j:<30} | {barra_o:<30}")
        print(f"Poder: {jugador.poder:<24} | Poder: {oponente.poder:<24}")
        print(f"Stamina: {jugador.stamina:<22} | Stamina: {oponente.stamina:<22}")
        print("---------------------------------------------------------------")


    def esperar(self):
        self.stamina += 15
        self.vida += 15

        return {
            'ok': True,
            'accion': 'esperar',
            'dano': 0,
            'tipo': 'esperar',
            'msg': f'{self.nombre} ha esperado y se prepara para el combate',
        }

    def esquivar(self, atacante, dano):
        esquivo = random.choice(['esquivar', 'no_esquivar'])

        if dano <= 0:
            return {'msg': f'{self.nombre} se desplaza y se prepara para el combate'}
        if esquivo == 'esquivar':
            # Se esquiva el ataque, no pierde vida
            self.vida += dano
            return {
                'ok': True,
                'accion': 'esquivar',
                'dano': 0,
                'tipo': 'esquivar',
                'msg': f'{self.nombre} esquivó el ataque de {atacante.nombre}!',
            }
        else:
            # Recibe daño reducido
            dano_recibido = dano / 1.5
            self.vida -= dano_recibido
            return {
                'ok': True,
                'accion': 'esquivar',
                'dano': dano_recibido,
                'tipo': 'esquivar',
                'msg': f'{self.nombre} intentó esquivar y recibió {dano_recibido:.1f} de daño de {atacante.nombre}!',
            }




    def elegir_Personaje():
        from utils.commonChar import (Naruto, Sasuke, Ichigo, Aizen, Goku, Vegeta, Alhacen, Kazuha, Iori, Kyo)
        while True:
            eleccion = int(input("\nIntroduce el número de tu elección: "))
            match eleccion:
                case 0:
                    rndm = random.choice([
                        Naruto(), Sasuke(), Ichigo(),
                        Kyo(), Iori(), Kazuha(), Alhacen(), Vegeta(), Goku(), Aizen()
                    ])
                    return rndm
                case 1:
                    return Naruto()
                case 2:
                    return Sasuke()
                case 3:
                    return Iori()
                case 4:
                    return Kyo()
                case 5:
                    return Ichigo()
                case 6:
                    return Kazuha()
                case 7:
                    return Vegeta()
                case 8:
                    return Alhacen()
                case 9:
                    return Goku()
                case 10:
                    return Aizen()
                case _:
                    raise ValueError("Elección inválida. Por favor, elige un número válido.")   

def vida_barra(self, jugador, oponente, vida_maxima_j, vida_maxima_o):
        if self.nombre == jugador.nombre:
            porcentaje_vida = jugador.vida / vida_maxima_j
        if self.nombre == oponente.nombre:
            porcentaje_vida = oponente.vida / vida_maxima_o
        
        total_bloques = 10

        # Calcula cuántos bloques llenos deben mostrarse
        bloques_llenos = int(porcentaje_vida * total_bloques)
        
        # Construye la barra de vida
        barra_vida = '█' * bloques_llenos + ' ' * (total_bloques - bloques_llenos)
        
        print(f"  |  vida:   |{barra_vida}| ({int(porcentaje_vida * 100)}%)")