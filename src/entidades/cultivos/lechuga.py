from src.entidades.cultivos.cultivo import Cultivo

class Lechuga(Cultivo):
    def __init__(self, superficie: float):
        super().__init__(superficie)