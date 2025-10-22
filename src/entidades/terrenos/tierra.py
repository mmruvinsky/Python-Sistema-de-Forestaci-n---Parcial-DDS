



class Tierra:
    def __init__(self, id_padron: int, superficie: float, domicilio: str):
        self._id_padron = id_padron
        self._domicilio = domicilio
        self._finca = None
        self.set_superficie(superficie)  # Valida
    
    def set_superficie(self, superficie: float):
        """Establece la superficie del terreno.
        Args:
            superficie (float): Superficie en metros cuadrados.
        Raises:
            ValueError: Si la superficie es menor o igual a cero.
        """
        if superficie <= 0:
            raise ValueError("superficie debe ser mayor a cero")
        self._superficie = superficie
    
    def get_superficie(self) -> float:
        """Obtiene la superficie del terreno.
        Returns:
            float: Superficie en metros cuadrados.
        """
        return self._superficie
