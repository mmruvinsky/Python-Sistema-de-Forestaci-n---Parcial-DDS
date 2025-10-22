from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    def __init__(self, cantidad: int):
        self._cantidad = cantidad
    
    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        return self._cantidad
    
