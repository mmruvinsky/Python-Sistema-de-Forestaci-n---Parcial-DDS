import time
from datetime import date

# --- ENTIDADES ---
from src.entidades.terrenos.tierra import Tierra
from src.entidades.terrenos.registro_forestal import RegistroForestal
from src.entidades.personal.trabajador import Trabajador
from src.entidades.personal.tarea import Tarea
from src.entidades.personal.herramienta import Herramienta
from src.entidades.cultivos.lechuga import Lechuga

# --- SERVICIOS ---
from src.servicios.terrenos.tierra_service import TierraService
from src.servicios.terrenos.plantacion_service import PlantacionService
from src.servicios.personal.trabajador_service import TrabajadorService
from src.servicios.negocio.fincas_service import FincasService
from src.servicios.registro_forestal_service import RegistroForestalService   # ✅ corregido

# --- RIEGO Y CONTROL ---
from src.servicios.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from src.servicios.riego.sensores.humedad_reader_task import HumedadReaderTask
from src.servicios.riego.control.control_riego_task import ControlRiegoTask




def main():
    print("=== SISTEMA DE GESTIÓN FORESTAL ===\n")

    # 1. Crear terreno y plantación
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )

    plantacion = terreno.get_finca()

    # 2. Crear registro forestal
    registro_service = RegistroForestalService()
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )

    # 3. Plantar cultivos
    plantacion_service = PlantacionService()
    plantacion_service.plantar(plantacion, "Pino", 5)
    plantacion_service.plantar(plantacion, "Olivo", 5)
    plantacion_service.plantar(plantacion, "Lechuga", 5)
    plantacion_service.plantar(plantacion, "Zanahoria", 5)

    # 4. Iniciar sistema de riego (Observer)
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    tarea_control = ControlRiegoTask(
        sensor_temperatura=tarea_temp,
        sensor_humedad=tarea_hum,
        plantacion=plantacion,
        plantacion_service=plantacion_service
    )

    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()

    # 5. Crear trabajador con tareas
    tareas = [
        Tarea(1, date.today(), "Desmalezar"),
        Tarea(2, date.today(), "Abonar"),
        Tarea(3, date.today(), "Marcar surcos")
    ]

    trabajador = Trabajador(43888734, "Juan Perez", tareas)
    trabajador_service = TrabajadorService()
    trabajador_service.asignar_apto_medico(
        trabajador, True, date.today(), "Estado de salud: excelente"
    )

    herramienta = Herramienta(1, "Pala", True)
    trabajador_service.trabajar(trabajador, date.today(), herramienta)

    # 6. Operaciones de negocio
    fincas_service = FincasService()
    fincas_service.add_finca(registro)
    fincas_service.fumigar(1, "Insecticida Orgánico")

    caja_lechugas = fincas_service.cosechar_y_empaquetar(Lechuga)
    caja_lechugas.mostrar_contenido_caja()

    # 7. Persistencia
    registro_service.persistir(registro)
    registro_leido = RegistroForestalService.leer_registro("Juan Perez")
    registro_service.mostrar_datos(registro_leido)

    # 8. Detener threads (limpieza)
    time.sleep(10)
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()

    tarea_temp.join(timeout=2.0)
    tarea_hum.join(timeout=2.0)
    tarea_control.join(timeout=2.0)

    print("\n=== SISTEMA FINALIZADO ===")


if __name__ == "__main__":
    main()
