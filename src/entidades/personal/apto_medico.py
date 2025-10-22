from datetime import date

class AptoMedico:
    def __init__(self, apto: bool, fecha_emision: date, 
                 observaciones: str = ""):
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones