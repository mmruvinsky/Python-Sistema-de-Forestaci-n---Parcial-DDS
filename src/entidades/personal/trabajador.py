from typing import List
from src.entidades.personal.tarea import Tarea

class Trabajador:
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy()  # Defensive copy
        self._apto_medico = None