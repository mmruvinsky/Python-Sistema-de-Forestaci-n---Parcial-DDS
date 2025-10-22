from src.servicios.cultivos.cultivo_service import CultivoService
from src.patrones.strategy.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy


class OlivoService(ArbolService):
    """
    Servicio para el cultivo Olivo.
    También utiliza la estrategia de absorción estacional.
    """

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
