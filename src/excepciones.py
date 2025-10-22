# persistencia_exception.py
from enum import Enum

class TipoOperacion(Enum):
    ESCRITURA = "escritura"
    LECTURA = "lectura"

class PersistenciaException(Exception):
    def __init__(self, mensaje: str, nombre_archivo: str, 
                 tipo_operacion: TipoOperacion):
        super().__init__(mensaje)
        self._mensaje = mensaje
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion
    
    def get_user_message(self) -> str:
        return self._mensaje

# agua_agotada_exception.py
class AguaAgotadaException(Exception):
    pass

# superficie_insuficiente_exception.py
class SuperficieInsuficienteException(Exception):
    pass