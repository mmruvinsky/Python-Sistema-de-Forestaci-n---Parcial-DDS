import pickle
from pathlib import Path
from src.entidades.terrenos.registro_forestal import RegistroForestal
from src.excepciones import *

class RegistroForestalService:
    def persistir(self, registro: RegistroForestal):
        propietario = registro.get_propietario()
        nombre_archivo = f"{propietario}.dat"
        ruta = Path("data") / nombre_archivo
        
        # Crear directorio si no existe
        ruta.parent.mkdir(exist_ok=True)
        
        try:
            with open(ruta, 'wb') as archivo:
                pickle.dump(registro, archivo)
            print(f"Registro de {propietario} persistido exitosamente en {ruta}")
        except Exception as e:
            raise PersistenciaException(
                f"Error al persistir registro: {e}",
                str(ruta),
                TipoOperacion.ESCRITURA
            )
    
    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacío")
        
        nombre_archivo = f"{propietario}.dat"
        ruta = Path("data") / nombre_archivo
        
        if not ruta.exists():
            raise PersistenciaException(
                f"Archivo no encontrado: {ruta}",
                str(ruta),
                TipoOperacion.LECTURA
            )
        
        try:
            with open(ruta, 'rb') as archivo:
                registro = pickle.load(archivo)
            print(f"Registro de {propietario} recuperado exitosamente desde {ruta}")
            return registro
        except Exception as e:
            raise PersistenciaException(
                f"Error al leer registro: {e}",
                str(ruta),
                TipoOperacion.LECTURA
            )