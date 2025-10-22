from src.entidades.cultivos.cultivo import Cultivo

class Olivo(Cultivo):
    def __init__(self, superficie: float, agua: int):
        super().__init__(superficie, agua)