import threading, random, time
from src.patrones.observer.observable import Observable

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self):
        while not self._detenido.is_set():
            temp = random.uniform(-25, 50)      # genera temperatura aleatoria
            self.notificar_observadores(temp)   # avisa a los observadores
            time.sleep(2.0)                     # espera 2 segundos

    def detener(self):
        self._detenido.set()
