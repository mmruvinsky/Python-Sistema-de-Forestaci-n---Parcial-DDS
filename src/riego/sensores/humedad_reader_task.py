import threading, random, time
from src.patrones.observer.observable import Observable

class HumedadReaderTask(threading.Thread, Observable[float]):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self):
        while not self._detenido.is_set():
            humedad = random.uniform(0, 100)       # genera humedad aleatoria
            self.notificar_observadores(humedad)   # avisa a los observadores
            time.sleep(3.0)                        # espera 3 segundos

    def detener(self):
        self._detenido.set()
