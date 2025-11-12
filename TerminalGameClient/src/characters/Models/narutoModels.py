from characters.Models.BaseModel import Personaje

class NarutoS(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)

class Naruto(NarutoS):
    def __init__(self):
        super().__init__(nombre='Naruto', vida=270, poder=250, stamina=350, tipo='Viento')  # Naruto tiene alta vida y stamina, con buen poder

    def Rasengan(self, rival):
        ataque = 'Rasengan'
        if self.stamina < 60:
            return {
                'ok': False, 
                'ataque': 'Rasengan', 
                'dano': 0,
                'tipo': 'Rasengan',
                'msg': 'No tienes suficiente stamina', }
        
        self.stamina -= 60
        dano = self.poder // 4
        ataque = 'Rasengan'
        tipo = 'Rasengan'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}'
        }
       
                
    def RasenShuriken(self, rival):
        ataque = 'RasenShuriken'
        if self.stamina < 150:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'RasenShuriken', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 150
        dano = self.poder // 2
        tipo = 'RasenShuriken'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }
    
class Sasuke(NarutoS):
    def __init__(self):
        super().__init__(nombre='Sasuke', vida=230, poder=280, stamina=270, tipo='Fuego')  # Sasuke tiene mayor poder pero menos vida
    
    def Chidori(self, rival):
        ataque = 'Chidori'
        if self.stamina < 60:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Chidori', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 60
        dano = self.poder // 5
        tipo = 'Chidori'
        rival.vida -= dano
        return {
            'ok': True,
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }
    
    def Raikiri(self, rival):
        ataque = 'Raikiri'
        if self.stamina < 60:
            return {'ok': False, 'ataque': ataque, 'dano': 0, 'tipo': 'Raikiri', 'msg': 'No tienes suficiente stamina'}
        
        self.stamina -= 150
        dano = self.poder // 2
        tipo = 'Raikiri'
        rival.vida -= dano
        return {
            'ok': True, 
            'ataque': ataque,
            'dano': dano,
            'tipo': tipo,
            'msg': f'{self.nombre} ha realizado {ataque} y hace {dano} de daño a {rival.nombre}',
        }