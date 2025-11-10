from characters.Models.BaseModel import Personaje

class Genshin(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)

class Kazuha(Genshin):
    def __init__(self, nombre):
        super().__init__(nombre, vida=150, poder=200, stamina=300, tipo='Anemo')  # Kazuha es ágil y tiene alta stamina

    def K_ulti(self):
        if self.stamina < 130:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Kazuha ulti'}
        
        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Kazuha ulti',
            'dano': dano,
            'tipo': 'Anemo',
        }


    def K_elemental(self):
        if self.stamina < 130:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Kazuha elemental'}
        
        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Kazuha elemental',
            'dano': dano,
            'tipo': 'Anemo',
        }

class Alhacen(Genshin):
    def __init__(self, nombre):
        super().__init__(nombre, vida=170, poder=210, stamina=280, tipo='Dendro')  # Alhacen es balanceado con buena stamina
    
    def A_ulti(self):
        if self.stamina < 130:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Alhacen ulti'}
        
        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Alhacen ulti',
            'dano': dano,
            'tipo': 'Dendro',
        }
        
    def A_elemental(self):
        if self.stamina < 130:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Alhacen elemental'}
        
        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Alhacen elemental',
            'dano': dano,
            'tipo': 'Dendro',
        }