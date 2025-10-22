from abc import ABC, abstractmethod

class Cultivo(ABC):
    _contador_id = 0
    
    def __init__(self, superficie: float, agua: int):
        Cultivo._contador_id += 1
        self._id = Cultivo._contador_id
        self._superficie = superficie
        self._agua = agua
    
    @abstractmethod
    def mostrar_datos(self):
        pass