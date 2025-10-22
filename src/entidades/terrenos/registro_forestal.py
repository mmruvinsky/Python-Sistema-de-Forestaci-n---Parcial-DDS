



class RegistroForestal:
    def __init__(self, id_padron: int, tierra: Tierra, 
                 plantacion: Plantacion, propietario: str, avaluo: float):
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo