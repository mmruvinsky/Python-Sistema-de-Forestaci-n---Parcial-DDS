from src.servicios.cultivos.cultivo_service import CultivoService
from src.patrones.strategy.absorcion_constante_strategy import AbsorcionConstanteStrategy

class ZanahoriaService(CultivoService):
    """
    Servicio para el cultivo Zanahoria.
    Usa una estrategia de absorción constante (2L por riego).
    """

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))