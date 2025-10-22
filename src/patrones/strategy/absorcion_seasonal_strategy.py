from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        mes = fecha.month
        if 3 <= mes <= 8:  # Verano
            return 5
        else:  # Invierno
            return 2