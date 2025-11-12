from characters.Models.BaseModel import Personaje

class Kof(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)

class Iori(Kof):
    def __init__(self):
        super().__init__(nombre='Iori', vida=160, poder=240, stamina=220, tipo='Fuego')

    def combo(self, rival):
        ataque = 'Iori combo'
        if self.stamina < 30:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Fuego', 'msg': 'No tienes suficiente stamina'}

        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Fuego'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }

    def ulti(self, rival):
        ataque = 'Iori ulti'
        if self.stamina < 30:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Fuego', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Fuego'
        rival.vida -= dano
        return {
            'ok': True, 
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }

class Kyo(Kof):
    def __init__(self):
        super().__init__(nombre='Kyo', vida=170, poder=230, stamina=210, tipo='Fuego')
    
    def ulti(self, rival):
        ataque = 'Kyo ulti'
        if self.stamina < 130:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Fuego', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Fuego'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }

    def combo(self, rival):
        ataque = 'Kyo combo'
        if self.stamina < 30:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Fuego', 'msg': 'No tienes suficiente stamina'}

        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Fuego'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }