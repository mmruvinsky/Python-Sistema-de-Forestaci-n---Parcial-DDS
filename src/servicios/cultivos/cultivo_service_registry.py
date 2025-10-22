from threading import Lock
from src.entidades.cultivos.cultivo import Cultivo
from src.entidades.cultivos.pino import Pino
from src.entidades.cultivos.olivo import Olivo
from src.entidades.cultivos.lechuga import Lechuga
from src.entidades.cultivos.zanahoria import Zanahoria

from src.servicios.cultivos.pino_service import PinoService
from src.servicios.cultivos.olivo_service import OlivoService
from src.servicios.cultivos.lechuga_service import LechugaService
from src.servicios.cultivos.zanahoria_service import ZanahoriaService


class CultivoServiceRegistry:
    """Singleton + Registry Pattern
    
    Centraliza los servicios de todos los cultivos y despacha automáticamente
    las operaciones sin usar isinstance() ni condicionales.
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    # ------------------------------------------------------------------
    # Inicialización de servicios y handlers
    # ------------------------------------------------------------------
    def _inicializar_servicios(self):
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        # Diccionario que mapea el tipo de cultivo con el método correspondiente
        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

    # ------------------------------------------------------------------
    # Métodos de despacho por tipo
    # ------------------------------------------------------------------
    def _absorber_agua_pino(self, cultivo: Cultivo) -> int:
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo: Cultivo) -> int:
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo: Cultivo) -> int:
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo: Cultivo) -> int:
        return self._zanahoria_service.absorver_agua(cultivo)

    # ------------------------------------------------------------------
    # Método público
    # ------------------------------------------------------------------
    def absorber_agua(self, cultivo: Cultivo) -> int:
        """Despacha automáticamente al servicio correcto según el tipo de cultivo."""
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)
