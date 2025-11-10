from characters.Models.BaseModel import Personaje

class Kof(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)

class Iori(Kof):
    def __init__(self, nombre):
        super().__init__(nombre, vida=160, poder=240, stamina=220, tipo='Fuego')

    def combo(self):
        if self.stamina < 30:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Iori combo'}

        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Iori combo',
            'dano': dano,
            'tipo': 'Fuego',
        }

    def ulti(self):
        if self.stamina < 30:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Iori ulti'}
        
        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True, 
            'ataque': 'Iori ulti',
            'dano': dano,
            'tipo': 'Fuego',
        }

class Kyo(Kof):
    def __init__(self, nombre):
        super().__init__(nombre, vida=170, poder=230, stamina=210, tipo='Fuego')
    
    def ulti(self):
        if self.stamina < 130:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Kyo ulti'}
        
        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Kyo ulti',
            'dano': dano,
            'tipo': 'Fuego',
        }

    def combo(self):
        if self.stamina < 30:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Kyo combo'}

        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Kyo poder',
            'dano': dano,
            'tipo': 'Fuego',
        }