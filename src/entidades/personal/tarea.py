from datetime import date

class Tarea:
    def __init__(self, id_tarea: int, fecha: date, descripcion: str):
        self._id_tarea = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion
        self._completada = False