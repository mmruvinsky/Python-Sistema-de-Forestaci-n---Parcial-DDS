from datetime import date
from src.entidades.personal.trabajador import Trabajador
from src.entidades.personal.herramienta import Herramienta
from src.entidades.personal.tarea import Tarea

class TrabajadorService:
    def trabajar(self, trabajador: Trabajador, fecha: date, 
                 util: Herramienta) -> bool:
        if not trabajador.get_apto_medico() or \
           not trabajador.get_apto_medico().esta_apto():
            return False
        
        # Filtrar tareas de la fecha
        tareas_del_dia = [t for t in trabajador.get_tareas() 
                          if t.get_fecha() == fecha]
        
        # Ordenar por ID descendente (SIN lambda)
        tareas_ordenadas = sorted(tareas_del_dia, 
                                  key=self._obtener_id_tarea, 
                                  reverse=True)
        
        for tarea in tareas_ordenadas:
            print(f"El trabajador {trabajador.get_nombre()} realizó "
                  f"la tarea {tarea.get_id_tarea()} "
                  f"{tarea.get_descripcion()} "
                  f"con herramienta: {util.get_nombre()}")
            tarea.set_completada(True)
        
        return True
    
    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        return tarea.get_id_tarea()