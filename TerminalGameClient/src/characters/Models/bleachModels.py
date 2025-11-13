from .BaseModel import Personaje
from core import SOUNDS_MAP

class Bleach(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)

class Ichigo(Bleach):
    def __init__(self):
        super().__init__(nombre='Ichigo', vida=180, poder=250, stamina=200, tipo='Segador')

    def getsuga(self, rival):
        SOUNDS_MAP[self.nombre]['poder']()
        ataque = 'Getsuga Tensho'
        if self.stamina < 50:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': 'espiritual',
                'msg': 'No tienes suficiente stamina',
            }

        self.stamina -= 50
        dano = self.poder // 5
        tipo = 'espiritual'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }

    def bankai(self, rival):
        SOUNDS_MAP[self.nombre]['ulti']()
        ataque = 'Bankai'
        if self.stamina < 150:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': 'Transformacion',
                'msg': 'No tienes suficiente stamina',
            }

        self.stamina -= 150
        self.vida += 100
        self.stamina += 100
        self.poder += 100
        tipo = 'Transformación'
        return {
            'ok': True,
            'ataque': ataque,
            'dano': 0,
            'tipo': tipo,
            'msg': f'{self.nombre} se ha transformado en {ataque} y aumenta sus estadisticas',
        }

class Aizen(Bleach):
    def __init__(self):
        super().__init__(nombre='Aizen', vida=200, poder=260, stamina=180, tipo='Segador')

    def kyokasuigetsu(self, rival):
        SOUNDS_MAP[self.nombre]['poder']()
        ataque = 'Kyokasuigetsu'
        if self.stamina < 130:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': 'ilusion',
                'msg': 'No tienes suficiente stamina',
            }

        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'ilusion'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }

    def kido(self, rival):
        SOUNDS_MAP[self.nombre]['ulti']()
        ataque = 'Kido Avanzado'
        if self.stamina < 130:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': 'magia',
                'msg': 'No tienes suficiente stamina',
            }

        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'magia'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }
