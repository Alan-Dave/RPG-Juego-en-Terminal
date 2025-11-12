from .BaseModel import Personaje
from utils.common import random



class Oponente(Personaje):
    def __init__(self, personaje):
        # Llamamos directamente al constructor de la clase base Personaje
        # en lugar de usar super() para evitar llamar al __init__ de la
        # clase de personaje (p. ej. Kyo) cuando usamos herencia dinámica.
        Personaje.__init__(
            self,
            nombre=personaje.nombre,
            vida=personaje.vida,
            poder=personaje.poder,
            stamina=personaje.stamina,
            tipo=personaje.tipo
        )

    @staticmethod
    def crear_oponente(nombre_jugador):
        from utils.commonChar import Naruto, Sasuke, Ichigo, Aizen, Kyo, Iori, Kazuha, Alhacen, Goku, Vegeta
        """Crea un oponente aleatorio distinto del jugador."""
        # Personaje base distinto al jugador
        candidatos = [
            Naruto(), Sasuke(), Ichigo(), Kyo(),
            Iori(), Kazuha(), Alhacen(), Vegeta(),
            Goku(), Aizen()
        ]
        candidatos = [c for c in candidatos if c.nombre != nombre_jugador]
        personaje = random.choice(candidatos)

        # Crea una clase combinada entre Oponente y la clase del personaje
        clase_dinamica = type("OponenteDinamico", (Oponente, personaje.__class__), {})
        return clase_dinamica(personaje)

    def elegir_accion(self, rival, dano):

        POWER_MAP = {
    'Naruto': {
        'rasengan': lambda rival: self.Rasengan(rival),
        'rasenshuriken': lambda rival: self.RasenShuriken(rival)
    },
    'Sasuke': {
        'chidori': lambda rival: self.Chidori(rival),
        'raikiri': lambda rival: self.Raikiri(rival)
    },
    'Ichigo': {
        'getsuga': lambda rival: self.getsuga(rival),
        'bankai': lambda rival: self.bankai(rival)
    },
    'Aizen': {
        'kido': lambda rival: self.kido(rival),
        'kyokasuigetsu': lambda rival: self.kyokasuigetsu(rival)
    },
    'Kyo': {
        'kyo_1': lambda rival: self.combo(rival),
        'kyo_2': lambda rival: self.ulti(rival)
    },
    'Iori': {
        'iori_1': lambda rival: self.combo(rival),
        'iori_2': lambda rival: self.ulti(rival)
    },
    'Kazuha': {
        'k_elemental': lambda rival: self.K_elemental(rival),
        'k_ulti': lambda rival: self.K_ulti(rival)
    },
    'Alhacen': {
        'a_elemental': lambda rival: self.A_elemental(rival),
        'a_ulti': lambda rival: self.A_ulti(rival)
    },
    'Goku': {
        'kamehameha': lambda rival: self.Kamehameha(rival),
        'ssj_g': lambda rival: self.Ssj(rival)
    },
    'Vegeta': {
        'garlick_gun': lambda rival: self.GarlickGun(rival),
        'ssj_v': lambda rival: self.Ssj(rival)
    },
}



        especiales = list(POWER_MAP.get(self.nombre, {}).values())
        acciones = ['atacar', 'esperar', 'esquivar']
        if especiales:
            acciones.append('especial')

        accion = random.choice(acciones)
        if accion == 'atacar':
            return self.atacar(rival)
        elif accion == 'esperar':
            return self.esperar()
        elif accion == 'esquivar':
            return self.esquivar(rival, dano)
        elif accion == 'especial' and especiales:
            especial = random.choice(especiales)
            return especial(rival)
        else:
            print(f"[!] {self.nombre} no tiene acciones disponibles.")
