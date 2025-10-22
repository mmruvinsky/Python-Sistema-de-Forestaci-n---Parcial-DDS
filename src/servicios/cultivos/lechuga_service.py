from src.servicios.cultivos.cultivo_service import CultivoService
from src.patrones.strategy.absorcion_constante_strategy import AbsorcionConstanteStrategy

class LechugaService(CultivoService):
    """
    Servicio para el cultivo Lechuga.
    Usa una estrategia de absorción constante (1L por riego).
    """

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(1))
  