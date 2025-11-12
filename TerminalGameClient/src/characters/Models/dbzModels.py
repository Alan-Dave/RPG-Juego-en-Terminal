from characters.Models.BaseModel import Personaje

class DBZ(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)
                         
class Goku(DBZ):
    def __init__(self):
        super().__init__(nombre='Goku', vida=250, poder=300, stamina=320, tipo='Saiyajin')  # Goku tiene estadísticas superiores en todo

    def Kamehameha(self, rival):
        ataque = 'Kamehameha'
        if self.stamina < 130:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': 'Saiyajin',
                'msg': 'No tienes suficiente stamina',
            }

        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Saiyajin'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }

    def Ssj(self, rival):
        ataque = 'Super Saiyajin'
        if self.stamina < 150:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': 'Transformación',
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

class Vegeta(DBZ):
    def __init__(self):
        super().__init__(nombre='Vegeta', vida=240, poder=290, stamina=310, tipo='Saiyajin')  # Vegeta es similar a Goku, pero ligeramente más débil
    
    def Ssj(self, rival):
        ataque = 'Super Saiyajin'
        if self.stamina < 150:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': 'Transformación',
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
                

    def GarlickGun(self, rival):
        ataque = 'Garlick Gun'
        if self.stamina < 130:
            return {
                'ok': False,
                'ataque': ataque,
                'dano': 0,
                'tipo': 'Combo',
                'msg': 'No tienes suficiente stamina',
            }

        self.stamina -= 30
        dano = self.poder // 2
        tipo = 'Combo'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }



    