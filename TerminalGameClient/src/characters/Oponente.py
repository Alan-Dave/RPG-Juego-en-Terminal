from utils.common import random


def elegir_accion():
        from utils.constants import oponente
        from utils.commonChar import Naruto, Sasuke, Ichigo, Aizen, Kyo, Iori, Kazuha, Alhacen, Goku, Vegeta

        POWER_MAP = {
            'Naruto': {
                'rasengan': Naruto.Rasengan,
                'rasenshuriken': Naruto.RasenShuriken
            }, 
            'Sasuke': {
                'chidori': Sasuke.Chidori,
                'raikiri': Sasuke.Raikiri
            },
            'Ichigo': {
                'getsuga': Ichigo.getsuga,
                'bankai': Ichigo.bankai
            },
            'Aizen': {
                'kido': Aizen.kido,
                'kyokasuigetsu': Aizen.kyokasuigetsu
            },
            'Kyo': {
                'kyo_1': Kyo.combo,
                'kyo_2': Kyo.ulti
            },
            'Iori': {   
                'iori_1': Iori.combo,
                'iori_2': Iori.ulti
            },
            'Kazuha': {
                'k_elemental': Kazuha.K_elemental,
                'k_ulti': Kazuha.K_ulti
            },
            'Alhacen': {
                'a_elemental': Alhacen.A_elemental,
                'a_ulti': Alhacen.A_ulti
            },
            'Goku': {
                'kamehameha': Goku.Kamehameha,
                'ssj_g': Goku.Ssj
            },
            'Vegeta': {
                'garlick_gun': Vegeta.GarlickGun,
                'ssj_v': Vegeta.Ssj
            },
        }

        especiales = list(POWER_MAP.get(oponente.nombre, {}).values())
        
        acciones = ['atacar', 'esperar', 'esquivar']
        if especiales:
            acciones.append('especial')

        accion = random.choice(acciones)
        
        if accion == 'atacar':
            return oponente.atacar()
        elif accion == 'esperar':
            return oponente.esperar()
        elif accion == 'esquivar':
            return oponente.esquivar()
        elif accion == 'especial' and especiales:
            especial = random.choice(especiales)
            return especial(self=oponente)
        else:
            print(f"[!] {oponente.nombre} no tiene acciones disponibles.")
        
def Personaje_distinto(nombre_jugador):
    from utils.commonChar import Naruto, Sasuke, Ichigo, Aizen, Kyo, Iori, Kazuha, Alhacen, Goku, Vegeta
    while nombre_jugador == oponente.nombre:
            oponente = None
            oponente = random.choice([
                Naruto("Naruto"), Sasuke("Sasuke"), Ichigo("Ichigo"), Kyo("Kyo"), Iori("Iori"), Kazuha("Kazuha"), Alhacen("Alhacen"), Vegeta("Vegeta"), Goku("Goku"), Aizen("Aizen")
            ])








