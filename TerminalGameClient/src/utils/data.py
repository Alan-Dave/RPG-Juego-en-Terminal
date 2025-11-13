# characters/Models/__init__.py
from characters.Models.bleachModels import (Ichigo, Aizen)
from characters.Models.narutoModels import (Naruto, Sasuke)
from characters.Models.dbzModels import (Goku, Vegeta)
from characters.Models.genshinModels import (Kazuha, Alhacen)
from characters.Models.kofModels import (Kyo, Iori)




characters_list = [Naruto(), Sasuke(), Ichigo(), Kyo(), Iori(), Kazuha(), Alhacen(), Vegeta(), Goku(), Aizen()]
characters_dict = {
    'Naruto': Naruto(),
    'Sasuke': Sasuke(),
    'Ichigo': Ichigo(),
    'Aizen': Aizen(),
    'Kyo': Kyo(),
    'Iori': Iori(),
    'Kazuha': Kazuha(),
    'Alhacen': Alhacen(),
    'Goku': Goku(),
    'Vegeta': Vegeta(),
    }