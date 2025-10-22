from src.patrones.observer.observer import Observer
import threading, time
from src.servicios.agua.agua_agotada_exception import AguaAgotadaException  

class ControlRiegoTask(threading.Thread, Observer[float]):
    def __init__(self, sensor_temperatura, sensor_humedad, 
                 plantacion, plantacion_service):
        threading.Thread.__init__(self, daemon=True)
        Observer.__init__(self)
        
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        
        self._ultima_temperatura = 0.0
        self._ultima_humedad = 0.0
        self._detenido = threading.Event()
        
        # Observar sensores
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)
    
    def actualizar(self, evento: float):
        # Actualiza temperatura o humedad
        pass
    
    def run(self):
        while not self._detenido.is_set():
            if self._debe_regar():
                try:
                    self._plantacion_service.regar(self._plantacion)
                except AguaAgotadaException:
                    print("No hay agua suficiente")
            time.sleep(2.5)
    
    def _debe_regar(self) -> bool:
        return (8 <= self._ultima_temperatura <= 15 
                and self._ultima_humedad < 50)