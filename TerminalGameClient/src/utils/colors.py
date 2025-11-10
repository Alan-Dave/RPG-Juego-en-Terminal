class Color:
    # 🎨 Colores ANSI
    RESET = "\033[0m"

    # Colores básicos
    NEGRO   = "\033[30m"
    ROJO    = "\033[31m"
    VERDE   = "\033[32m"
    AMARILLO = "\033[33m"
    AZUL    = "\033[34m"
    MAGENTA = "\033[35m"
    CIAN    = "\033[36m"
    BLANCO  = "\033[37m"

    # Colores brillantes
    ROJO_CLARO     = "\033[91m"
    VERDE_CLARO    = "\033[92m"
    AMARILLO_CLARO = "\033[93m"
    AZUL_CLARO     = "\033[94m"
    MAGENTA_CLARO  = "\033[95m"
    CIAN_CLARO     = "\033[96m"
    BLANCO_CLARO   = "\033[97m"

    # Estilos
    NEGRITA    = "\033[1m"
    CURSIVA    = "\033[3m"
    SUBRAYADO  = "\033[4m"
    PARPADEO   = "\033[5m"

    # Fondos (opcional)
    BG_ROJO    = "\033[41m"
    BG_VERDE   = "\033[42m"
    BG_AZUL    = "\033[44m"
    BG_NEGRO   = "\033[40m"
    BG_BLANCO  = "\033[47m"
    BG_AMARILLO = "\033[43m"
    BG_MAGENTA = "\033[45m"
    BG_CIAN    = "\033[46m"