from characters.Models.BaseModel import Personaje

class Bleach(Personaje):
    def __init__(self, nombre, vida, poder, stamina, tipo):
        super().__init__(nombre, vida, poder, stamina, tipo)

class Ichigo(Bleach):
    def __init__(self, nombre):
        super().__init__(nombre, vida=180, poder=250, stamina=200, tipo='Segador')

    def getsuga(self):
        if self.stamina < 50:
            return {"ok": False, "error": "Sin stamina", "ataque": "Getsuga Tensho"}

        self.stamina -= 50
        dano = self.poder // 5
        return {
            "ok": True,
            "ataque": "Getsuga Tensho",
            "dano": dano,
            "tipo": "espiritual",
        }

    def bankai(self):
        if self.stamina < 150:
            return {"ok": False, "error": "Sin stamina", "ataque": "Bankai"}

        self.stamina -= 150
        self.vida += 100
        self.stamina += 100
        self.poder += 100
        return {
            "ok": True,
            "ataque": "Bankai",
            "efecto": "+100 vida, stamina y poder",
            "tipo": "transformacion",
        }

class Aizen(Bleach):
    def __init__(self, nombre):
        super().__init__(nombre, vida=200, poder=260, stamina=180, tipo='Segador')

    def kyokasuigetsu(self):
        if self.stamina < 130:
            return {"ok": False, "error": "Sin stamina", "ataque": "Kyokasuigetsu"}

        self.stamina -= 30
        dano = self.poder // 2
        return {
            "ok": True,
            "ataque": "Kyokasuigetsu",
            "dano": dano,
            "tipo": "ilusion",
        }

    def kido(self):
        if self.stamina < 130:
            return {"ok": False, "error": "Sin stamina", "ataque": "Kido Avanzado"}

        self.stamina -= 30
        dano = self.poder // 2
        return {
            "ok": True,
            "ataque": "Kido Avanzado",
            "dano": dano,
            "tipo": "magia",
        }
