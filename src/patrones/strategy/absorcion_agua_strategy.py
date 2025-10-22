from abc import ABC, abstractmethod

class AbsorcionAguaStrategy(ABC):
    @abstractmethod
    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo) -> int:
        pass