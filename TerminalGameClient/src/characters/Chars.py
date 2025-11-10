from utils.commonChar import *
from utils.commonClass import Humano, Mago, Samurai, Ninja

#----------------GENERICOS----------------------
# PersonajeS HUMANO
humano = Humano(nombre="Humano")
john = John(nombre='John Wick')

#_______________________________
# PersonajeS MAGOS
mago = Mago(nombre="Mago")

#_______________________________
# PersonajeS SAMURAI
samurai = Samurai(nombre="Samurai")

#_______________________________
# PersonajeS NINJA
ninja = Ninja(nombre='Ninja')
zaji = Zaji(nombre='Zaji')


#------------ANIME-----------------
# NARUTO
naruto = Naruto(nombre='Naruto')
sasuke = Sasuke(nombre='Sasuke')

# BLEACH
ichigo = Ichigo(nombre='Ichigo')
aizen = Aizen(nombre='Aizen')

# GENSHIN
kazuha = Kazuha(nombre='Kazuha')
alhacen = Alhacen(nombre='Alhacen')

# DRAGON BALL Z
goku = Goku(nombre='Goku')
vegeta = Vegeta(nombre='Vegeta')

# KING OF FIGHTERS
kyo = Kyo(nombre='Kyo')
iori = Iori(nombre='Iori')


Personajes_name = [
                naruto.nombre,
                sasuke.nombre,
                ichigo.nombre,
                aizen.nombre,
                kazuha.nombre,
                alhacen.nombre,
                goku.nombre,
                vegeta.nombre,
                samurai.nombre,
                ninja.nombre,
                mago.nombre,
                humano.nombre,
                kyo.nombre,
                iori.nombre,
                john.nombre,
                zaji.nombre,
                ]


