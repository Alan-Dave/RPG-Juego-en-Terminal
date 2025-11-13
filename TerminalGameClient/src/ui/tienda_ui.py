from utils.common import os

def Tienda(jugador):
    os.system("cls")
    print("\033[32m********** TIENDA ***********\033[0m\n")

    print("\033[32m!Bienvenido¡, ¿que desea llevar?\033[0m\n")
    print(f"                                               Money: \033[33m{jugador.moneda}\033[0m")
    print("")
    print(f'1. Pocion_Vida_B       $20          6. Pocion_Poder_A    $40\n'
        f'2. Pocion_Stamin_B     $20          7. Pocion_Vida_S     $80\n'
        f'3. Pocion_Poder_B      $20          8. Pocion_Stamin_S   $80\n'
        f'4. Pocion_Vida_A       $40          9. Pocion_Poder_S    $80\n'
        f'5. Pocion_Stamin_A     $40          10. Pocion_Mix_SS    $100\n'
        )
    print("\nB = Basico: 25.pts\n"
        "A = Intermedio: 40.pts\n"
        "S = Avanzado: 70.pts\n"
        "SS = Legendario: 35.pts All stats                          R = Salir\n")
    
    
    


    # INSTALAR INTELLICODE EN EXTENSIONES DE VS

