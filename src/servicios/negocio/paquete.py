from typing import TypeVar, Generic, List

T = TypeVar('T')

class Paquete(Generic[T]):
    _contador_id = 0
    
    def __init__(self, tipo_contenido: type):
        Paquete._contador_id += 1
        self._id_paquete = Paquete._contador_id
        self._tipo_contenido = tipo_contenido
        self._contenido: List[T] = []
    
    def agregar(self, item: T):
        self._contenido.append(item)
    
    def mostrar_contenido_caja(self):
        print(f"\nContenido de la caja:")
        print(f"  Tipo: {self._tipo_contenido.__name__}")
        print(f"  Cantidad: {len(self._contenido)}")
        print(f"  ID Paquete: {self._id_paquete}")