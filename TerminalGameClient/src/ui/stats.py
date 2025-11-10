from utils.common import os
from utils.constants import vida_maxima_o, vida_maxima_j

def vida(self):
    from utils.constants import oponente, jugador
    if self.nombre == jugador.nombre:
        porcentaje_vida = jugador.vida / vida_maxima_j
    if self.nombre == oponente.nombre:
        porcentaje_vida = oponente.vida / vida_maxima_o
    
    total_bloques = 10

    # Calcula cuántos bloques llenos deben mostrarse
    bloques_llenos = int(porcentaje_vida * total_bloques)
    
    # Construye la barra de vida
    barra_vida = '█' * bloques_llenos + ' ' * (total_bloques - bloques_llenos)
    
    print(f"  |  vida:   |{barra_vida}| ({int(porcentaje_vida * 100)}%)")

def estado():
        from utils.constants import oponente, jugador
        os.system("cls")
        print("-------------------------------------------------------")
        print(f"\033[38;5;208m  | *          [{oponente.nombre}]      ")
        vida()
        print(f"  | *         Poder: {oponente.poder}        \n"
              f"  | *         Stamina: {oponente.stamina}    \033[0m \n")
        print("-------------------------------------------------------")
        print(f"Este es el estado de {oponente.nombre}")
        print("")
        print("")