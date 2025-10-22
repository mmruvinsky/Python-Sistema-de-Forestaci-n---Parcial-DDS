from abc import ABC
from datetime import date
from src.entidades.cultivos.cultivo import Cultivo
from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from src.patrones.strategy.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from src.patrones.strategy.absorcion_constante_strategy import AbsorcionConstanteStrategy

class CultivoService(ABC):
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia
    
    def absorver_agua(self, cultivo: Cultivo) -> int:
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            date.today(), 0, 0, cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida



