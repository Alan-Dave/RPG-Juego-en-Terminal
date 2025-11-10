from characters.Models.BaseModel import Personaje

class DBZ(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)
                         
class Goku(DBZ):
    def __init__(self, nombre):
        super().__init__(nombre, vida=250, poder=300, stamina=320, tipo='Saiyajin')  # Goku tiene estadísticas superiores en todo

    def Kamehameha(self):
        if self.stamina < 130:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Kamehameha'}

        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Kamehameha',
            'dano': dano,
            'tipo': 'Saiyajin',
        }

    def Ssj(self):
        if self.stamin < 150:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Ssj'}

        self.stamina -= 150
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Ssj',
            'dano': dano,
            'tipo': 'Saiyajin',
        }

class Vegeta(DBZ):
    def __init__(self, nombre):
        super().__init__(nombre, vida=240, poder=290, stamina=310, tipo='Saiyajin')  # Vegeta es similar a Goku, pero ligeramente más débil
    
    def Ssj(self):

        if self.stamin < 150:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Ssj'}

        self.stamina -= 150
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Ssj',
            'dano': dano,
            'tipo': 'Saiyajin',
        }
                

    def GarlickGun(self):

        if self.stamina < 130:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Kamehameha'}

        self.stamina -= 30
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'Garlick Gun',
            'dano': dano,
            'tipo': 'Saiyajin',
        }



    