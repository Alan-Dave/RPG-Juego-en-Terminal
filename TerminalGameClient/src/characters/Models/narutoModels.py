from characters.Models.BaseModel import Personaje

class NarutoS(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)

class Naruto(NarutoS):
    def __init__(self, nombre):
        super().__init__(nombre, vida=270, poder=250, stamina=350, tipo='Viento')  # Naruto tiene alta vida y stamina, con buen poder

    def Rasengan(self):
        if self.stamina < 60:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Rasengan'}
        
        self.stamina -= 60
        dano = self.poder // 4
        return {
            'ok': True,
            'ataque': 'Rasengan',
            'dano': dano,
            'tipo': 'Rasengan',
        }
       
                
    def RasenShuriken(self):
        if self.stamina < 150:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'RasenShuriken'}
        
        self.stamina -= 150
        dano = self.poder // 2
        return {
            'ok': True,
            'ataque': 'RasenShuriken',
            'dano': dano,
            'tipo': 'RasenShuriken',
        }
    
class Sasuke(NarutoS):
    def __init__(self, nombre):
        super().__init__(nombre, vida=230, poder=280, stamina=270, tipo='Fuego')  # Sasuke tiene mayor poder pero menos vida
    
    def Chidori(self):
        if self.stamina < 60:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Chidori'}
        
        self.stamina -= 60
        dano = self.poder // 5
        return {
            'ok': True,
            'ataque': 'Chidori',
            'dano': dano,
            'tipo': 'Chidori',
        }
    
    def Raikiri(self):
        if self.stamina < 60:
            return {'ok': False, 'error': 'Sin stamina', 'ataque': 'Raikiri'}
        
        self.stamina -= 150
        dano = self.poder // 2
        return {
            'ok': True, 
            'ataque': 'Raikiri',
            'dano': dano,
            'tipo': 'Raikiri',
        }