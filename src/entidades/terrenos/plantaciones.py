


class Plantacion:
    def __init__(self, nombre: str, superficie: float, agua: int = 500):
        self._nombre = nombre
        self._superficie = superficie
        self._cultivos = []
        self._trabajadores = []
        self.set_agua_disponible(agua)
    
    def set_agua_disponible(self, agua: int):
        """Establece la cantidad de agua disponible para la plantación.
        Args:
            agua (int): Cantidad de agua en litros.
        Raises:
            ValueError: Si el agua es negativa."""
        if agua < 0:
            raise ValueError("agua no puede ser negativa")
        self._agua_disponible = agua
    
    def get_superficie_ocupada(self) -> float:
        """Obtiene la superficie ocupada por los cultivos en la plantación.
        Returns:
            float: Superficie ocupada en metros cuadrados.
        """
        return sum(c.get_superficie() for c in self._cultivos)
    
    