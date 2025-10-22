from src.servicios.cultivos.cultivo_service import CultivoService
from src.patrones.strategy.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy



class PinoService(ArbolService):
    """
    Servicio para el cultivo Pino.
    Usa una estrategia de absorción estacional: más agua en verano, menos en invierno.
    """

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
