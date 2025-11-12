from characters.Models.BaseModel import Personaje

class Genshin(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)

class Kazuha(Genshin):
    def __init__(self):
        super().__init__(nombre='Kazuha', vida=150, poder=200, stamina=300, tipo='Anemo')  # Kazuha es ágil y tiene alta stamina

    def K_ulti(self, rival):
        ataque = 'Kazuha ulti'
        if self.stamina < 130:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Anemo', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Anemo'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }


    def K_elemental(self, rival):
        ataque = 'Kazuha elemental'
        if self.stamina < 130:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Anemo', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Anemo'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }

class Alhacen(Genshin):
    def __init__(self):
        super().__init__(nombre='Alhacen', vida=170, poder=210, stamina=280, tipo='Dendro')  # Alhacen es balanceado con buena stamina
    
    def A_ulti(self, rival):
        ataque = 'Alhacen ulti'
        if self.stamina < 130:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Dendro', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Dendro'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }
        
    def A_elemental(self, rival):
        ataque = 'Alhacen elemental'
        if self.stamina < 130:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Dendro', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Dendro'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }