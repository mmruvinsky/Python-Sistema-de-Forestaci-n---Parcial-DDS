from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from src.patrones.observer.observer import Observer
T = TypeVar('T')

class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []
    
    def agregar_observador(self, observador: Observer[T]):
        if observador not in self._observadores:
            self._observadores.append(observador)
    
    def notificar_observadores(self, evento: T):
        for observador in self._observadores:
            observador.actualizar(evento)