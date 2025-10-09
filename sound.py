import os
import winsound

# Obtén el directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Carpeta principal donde están los sonidos
sound_dir = os.path.join(script_dir, 'sound')

# Inicializa el diccionario de sonidos
sonidos = {}

# Recorre todas las subcarpetas dentro de la carpeta 'sound'
for root, dirs, files in os.walk(sound_dir):
    for file in files:
        if file.endswith('.wav'):  # Verifica que el archivo sea un archivo de sonido
            # Obtiene la ruta completa del archivo de sonido
            full_path = os.path.join(root, file)
            # Utiliza el nombre del archivo sin la extensión como la clave del diccionario
            sound_name = os.path.splitext(file)[0]
            sonidos[sound_name] = full_path
            print(f"Sonido detectado: {sound_name} -> {full_path}")

# Función para reproducir un sonido dado su nombre
def reproducir_sonido(nombre_sonido):
    ruta = sonidos.get(nombre_sonido)
    if ruta and os.path.exists(ruta):
        winsound.PlaySound(ruta, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        print(f"El archivo de sonido '{nombre_sonido}' no se encontró.")
        if nombre_sonido != 'error':
            sound.sError()



# Funciones para reproducir sonidos específicos
class sound():
    @staticmethod
    def sAtacar():
        reproducir_sonido('Atacar')

    @staticmethod
    def sCorteDimensional():
        reproducir_sonido('CorteDimensional')

    @staticmethod
    def sShuriken():
        reproducir_sonido('Shuriken')

    @staticmethod
    def sPunch():
        reproducir_sonido('Punch')

    @staticmethod
    def sParalizar():
        reproducir_sonido('Paralizar')

    @staticmethod
    def sEsperar():
        reproducir_sonido('Esperar')

    @staticmethod
    def sPocion():
        reproducir_sonido('Pocion')

    @staticmethod
    def sEstado():
        reproducir_sonido('Estado')

    @staticmethod
    def sMoney():
        reproducir_sonido('Money')

    @staticmethod
    def sError():
        reproducir_sonido('Error')

    @staticmethod
    def sMochila():
        reproducir_sonido('Mochila')

    @staticmethod
    def sIntro():
        reproducir_sonido('Intro')

    @staticmethod
    def sWin():
        reproducir_sonido('Win')

    @staticmethod
    def sDerrota():
        reproducir_sonido('Derrota')

    @staticmethod
    def sTienda():
        reproducir_sonido('Tienda')

    @staticmethod
    def sSalirTienda():
        reproducir_sonido('SalirTienda')

    @staticmethod
    def sGameOver():
        reproducir_sonido('GameOver')

    @staticmethod
    def sYagai():
        reproducir_sonido('Yagai')


    @staticmethod
    def sDisparo():
        reproducir_sonido('Disparo')





#____________________________________________________________________________
    # SOnidos de personajes reales
#____________________________________________________________________________
    # NARUTO
    
    @staticmethod
    def sRasengan():
        reproducir_sonido('Rasengan')

    @staticmethod
    def sChidori():
        reproducir_sonido('Chidori')
    
    @staticmethod
    def sRasenShuriken():
        reproducir_sonido('RasenShuriken')

    @staticmethod
    def sRaikiri():
        reproducir_sonido('Raikiri')


    @staticmethod
    def sNarutoA():
        reproducir_sonido('sNarutoA')
        
    @staticmethod
    def sSasukeA():
        reproducir_sonido('sSasukeA')
#____________________________________________________________________________
    # GENSHIN
    
    @staticmethod
    def sA_ulti():
        reproducir_sonido('A_ulti')
    
    @staticmethod
    def sA_elemental():
        reproducir_sonido('A_elemental')
    
    @staticmethod
    def sK_ulti():
        reproducir_sonido('K_ulti')
    
    @staticmethod
    def sK_elemental():
        reproducir_sonido('K_elemental')

    
    @staticmethod
    def sKazuhaA():
        reproducir_sonido('sKazuhaA')
        
    @staticmethod
    def sAlhacenA():
        reproducir_sonido('sAlhacenA')
#____________________________________________________________________________
    # BLEACH    
    
    @staticmethod
    def sGetsuga():
        reproducir_sonido('Getsuga')
    
    @staticmethod
    def sA_kido():
        reproducir_sonido('A_kido')

    @staticmethod
    def sBankai():
        reproducir_sonido('Bankai')

    @staticmethod
    def sKyokasuigetsu():
        reproducir_sonido('Kyokasuigetsu')


    @staticmethod
    def sIchigoA():
        reproducir_sonido('sIchigoA')
        
    @staticmethod
    def sAizenA():
        reproducir_sonido('sAizenA')
#____________________________________________________________________________
    # KING OF FIGHTERS

    @staticmethod
    def sIori_1():
        reproducir_sonido('Iori_1')
    
    @staticmethod
    def sIori_2():
        reproducir_sonido('Iori_2')

    @staticmethod
    def sKyo_1():
        reproducir_sonido('Kyo_1')
    
    @staticmethod
    def sKyo_2():
        reproducir_sonido('Kyo_2')

    

    @staticmethod
    def sIoriA():
        reproducir_sonido('sIoriA')
        
    @staticmethod
    def sKyoA():
        reproducir_sonido('sKyoA')
#____________________________________________________________________________
    # DRAGON BALL Z

    @staticmethod
    def sKamehameha():
        reproducir_sonido('Kamehameha')
    
    @staticmethod
    def sGarlickGun():
        reproducir_sonido('GarlickGun')

    @staticmethod
    def sSsj():
        reproducir_sonido('Ssj')



    @staticmethod
    def sGokuA():
        reproducir_sonido('sGokuA')

    @staticmethod
    def sVegetaA():
        reproducir_sonido('sVegetaA')
        



    # WIN


    @staticmethod
    def Ichigo_win():
        reproducir_sonido('Ichigo_win')
    
    @staticmethod
    def Aizen_win():
        reproducir_sonido('Aizen_win')
    
    @staticmethod
    def Goku_win():
        reproducir_sonido('Goku_win')
    
    @staticmethod
    def Vegeta_win():
        reproducir_sonido('Vegeta_win')
    
    @staticmethod
    def Kazuha_win():
        reproducir_sonido('Kazuha_win')
    
    @staticmethod
    def Alhacen_win():
        reproducir_sonido('Alhacen_win')
    
    @staticmethod
    def Naruto_win():
        reproducir_sonido('Naruto_win')
    
    @staticmethod
    def Sasuke_win():
        reproducir_sonido('Sasuke_win')

    @staticmethod
    def Iori_win():
        reproducir_sonido('Iori_win')
    
    @staticmethod
    def Kyo_win():
        reproducir_sonido('Kyo_win')








    # ESQUIVAR
    @staticmethod
    def sEsquivar():
        reproducir_sonido('sEsquivar')
    

    @staticmethod
    def sKyoE():
        reproducir_sonido('sKyoE')
    
    @staticmethod
    def sIoriE():
        reproducir_sonido('sIoriE')
    
    @staticmethod
    def sGokuE():
        reproducir_sonido('sGokuE')
    
    @staticmethod
    def sVegetaE():
        reproducir_sonido('sVegetaE')
    
    @staticmethod
    def sKazuhaE():
        reproducir_sonido('sKazuhaE')
    
    @staticmethod
    def sAlhacenE():
        reproducir_sonido('sAlhacenE')
    
    @staticmethod
    def sNarutoSE():
        reproducir_sonido('sNarutoSE')
    
    @staticmethod
    def sIchigoE():
        reproducir_sonido('sIchigoE')
    
    @staticmethod
    def sAizenE():
        reproducir_sonido('sAizenE')


    # NO LOGRAN ESQUIVAR
    
    @staticmethod
    def sKyoNE():
        reproducir_sonido('sKyoNE')
    
    @staticmethod
    def sIoriNE():
        reproducir_sonido('sIoriNE')
    
    @staticmethod
    def sGokuNE():
        reproducir_sonido('sGokuNE')
    
    @staticmethod
    def sVegetaNE():
        reproducir_sonido('sVegetaNE')
    
    @staticmethod
    def sKazuhaNE():
        reproducir_sonido('sKazuhaNE')
    
    @staticmethod
    def sAlhacenNE():
        reproducir_sonido('sAlhacenNE')
    
    @staticmethod
    def sNarutoNE():
        reproducir_sonido('sNarutoNE')
    
    @staticmethod
    def sSasukeNE():
        reproducir_sonido('sSasukeNE')

    @staticmethod
    def sIchigoNE():
        reproducir_sonido('sIchigoNE')
    
    @staticmethod
    def sAizenNE():
        reproducir_sonido('sAizenNE')

    

    # INTENTA ESQUIVAR


    @staticmethod
    def sKyoTE():
        reproducir_sonido('sKyoTE')
    
    @staticmethod
    def sIoriTE():
        reproducir_sonido('sIoriTE')
    




    @staticmethod
    def sDBZTE():
        reproducir_sonido('sDBZTE')
    

    @staticmethod
    def sGenshinTE():
        reproducir_sonido('sGenshinTE')
    
    
    @staticmethod
    def sNarutoTE():
        reproducir_sonido('sNarutoTE')

    def sSasukeTE():
        reproducir_sonido('sSasukeTE')
    

    @staticmethod
    def sBLeachTE():
        reproducir_sonido('sBleachTE')