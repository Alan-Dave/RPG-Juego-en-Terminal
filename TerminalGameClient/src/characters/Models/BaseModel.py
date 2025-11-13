from utils.common import random
from core import SOUNDS_MAP
from core.eventos import ERRORS



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
        SOUNDS_MAP[self.nombre]['atacar']()
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
        SOUNDS_MAP[self.nombre]['esperar']()
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
        SOUNDS_MAP[self.nombre]['try_esquivar']()
        esquivo = random.choice(['esquivar', 'no_esquivar'])

        if dano <= 0:
            return {
                'ok': None,
                'accion': 'esquivar',
                'dano': 0,
                'tipo': 'esquivar',
                'msg': f'{self.nombre} se desplaza y se prepara para el combate'
                }
        
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
            SOUNDS_MAP[self.nombre]['no_esquivar']()
            # Recibe daño reducido
            dano_recibido = dano / 1.5
            self.vida -= dano_recibido
            return {
                'ok': False,
                'accion': 'esquivar',
                'dano': dano_recibido,
                'tipo': 'esquivar',
                'msg': f'{self.nombre} intentó esquivar y recibió {dano_recibido:.1f} de daño de {atacante.nombre}!',
            }


    def elegir_Personaje():
        from utils.data import characters_list, characters_dict

        try:
            eleccion = int(input("\nIntroduce el número de tu elección: "))
            match eleccion:
                case 0:
                    rndm = random.choice(characters_list)
                    return rndm
                case 1:
                    return characters_dict['Naruto']
                case 2:
                    return characters_dict['Sasuke']
                case 3:
                    return characters_dict['Iori']
                case 4:
                    return characters_dict['Kyo']
                case 5:
                    return characters_dict['Ichigo']
                case 6:
                    return characters_dict['Kazuha']
                case 7:
                    return characters_dict['Vegeta']
                case 8:
                    return characters_dict['Alhacen']
                case 9:
                    return characters_dict['Goku']
                case 10:
                    return characters_dict['Aizen']
                case _:
                    ERRORS['ERROR']()
        except ValueError as e:
            ERRORS['VALUEERROR'](e)



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