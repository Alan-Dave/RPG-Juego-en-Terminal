from core.sound import sound

SOUNDS_MAP = {
    # ==== Naruto Saga ====
    'Naruto': {
        'atacar': sound.sNarutoA,
        'win': sound.Naruto_win,
        'poder': sound.sRasengan,
        'ulti': sound.sRasenShuriken,
        'esperar': sound.sNarutoE,
        'esquivar': sound.sNarutoSE,
        'no_esquivar': sound.sNarutoNE,
        'try_esquivar': sound.sNarutoTE,
    },
    'Sasuke': {
        'atacar': sound.sSasukeA,
        'win': sound.Sasuke_win,
        'poder': sound.sChidori,
        'ulti': sound.sRaikiri,
        'esperar': sound.sSasukeE,
        'esquivar': sound.sSasukeE,
        'no_esquivar': sound.sSasukeNE,
        'try_esquivar': sound.sSasukeTE,
    },

    # ==== Dragon Ball Z ====
    'Goku': {
        'atacar': sound.sGokuA,
        'win': sound.Goku_win,
        'poder': sound.sKamehameha,
        'ulti': sound.sSsj,
        'esperar': sound.sGokuE,
        'esquivar': sound.sGokuE,
        'no_esquivar': sound.sGokuNE,
        'try_esquivar': sound.sGokuTE,
    },
    'Vegeta': {
        'atacar': sound.sVegetaA,
        'win': sound.Vegeta_win,
        'poder': sound.sGarlickGun,
        'ulti': sound.sSsj,
        'esperar': sound.sVegetaE,
        'esquivar': sound.sVegetaE,
        'no_esquivar': sound.sVegetaNE,
        'try_esquivar': sound.sVegetaTE,
    },

    # ==== Genshin Impact ====
    'Kazuha': {
        'atacar': sound.sKazuhaA,
        'win': sound.Kazuha_win,
        'poder': sound.sK_elemental,
        'ulti': sound.sK_ulti,
        'esperar': sound.sKazuhaE,
        'esquivar': sound.sKazuhaE,
        'no_esquivar': sound.sKazuhaNE,
        'try_esquivar': sound.sKazuhaTE,
    },
    'Alhacen': {
        'atacar': sound.sAlhacenA,
        'win': sound.Alhacen_win,
        'poder': sound.sA_elemental,
        'ulti': sound.sA_ulti,
        'esperar': sound.sAlhacenE,
        'esquivar': sound.sAlhacenE,
        'no_esquivar': sound.sAlhacenNE,
        'try_esquivar': sound.sAlhacenTE,
    },

    # ==== The King of Fighters ====
    'Iori': {
        'atacar': sound.sIoriA,
        'win': sound.Iori_win,
        'poder': sound.sIori_1,
        'ulti': sound.sIori_2,
        'esperar': sound.sIoriE,
        'esquivar': sound.sIoriE,
        'no_esquivar': sound.sIoriNE,
        'try_esquivar': sound.sIoriTE,
    },
    'Kyo': {
        'atacar': sound.sKyoA,
        'win': sound.Kyo_win,
        'poder': sound.sKyo_1,
        'ulti': sound.sKyo_2,
        'esperar': sound.sKyoE,
        'esquivar': sound.sKyoE,
        'no_esquivar': sound.sKyoNE,
        'try_esquivar': sound.sKyoTE,
    },

    # ==== Bleach ====
    'Ichigo': {
        'atacar': sound.sIchigoA,
        'win': sound.Ichigo_win,
        'poder': sound.sGetsuga,
        'ulti': sound.sBankai,
        'esperar': sound.sIchigoE,
        'esquivar': sound.sIchigoE,
        'no_esquivar': sound.sIchigoNE,
        'try_esquivar': sound.sIchigoTE,
    },
    'Aizen': {
        'atacar': sound.sAizenA,
        'win': sound.Aizen_win,
        'poder': sound.sA_kido,
        'ulti': sound.sKyokasuigetsu,
        'esperar': sound.sAizenE,
        'esquivar': sound.sAizenE,
        'no_esquivar': sound.sAizenNE,
        'try_esquivar': sound.sAizenTE,
    },
}


UI_MAP = {
    'intro': sound.sIntro,
    'error': sound.sError,
    'esperar': sound.sEsperar,
    'estado': sound.sEstado,
    'game_over': sound.sGameOver,
    'mochila': sound.sMochila,
    'money': sound.sMoney,
    'pocion': sound.sPocion,
    'salir_tienda': sound.sSalirTienda,
    'tienda': sound.sTienda,
    'win': sound.sWin,
}