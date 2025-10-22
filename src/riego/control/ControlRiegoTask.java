package riego.control;

import entidades.terrenos.Plantacion;
import excepciones.AguaAgotadaException;
import riego.sensores.HumedadReaderTask;
import riego.sensores.TemperaturaReaderTask;
import servicios.terrenos.PlantacionService;

/**
 * Tarea de control de riego automatizado.
 * Monitorea sensores de temperatura y humedad para decidir cuándo regar.
 *
 * REFACTORIZADO: Usa inyección de dependencias.
 */
public class ControlRiegoTask implements Runnable {
    private final TemperaturaReaderTask tempTask;
    private final HumedadReaderTask humTask;
    private Plantacion finca;
    private final PlantacionService plantacionService;

    private volatile boolean ejecutando = true;

    /**
     * Constructor con inyección de dependencias.
     *
     * @param tempTask Tarea de lectura de temperatura
     * @param humTask Tarea de lectura de humedad
     * @param finca Plantación a regar
     * @param plantacionService Servicio de plantación (inyectado)
     */
    public ControlRiegoTask(TemperaturaReaderTask tempTask, HumedadReaderTask humTask,
                           Plantacion finca, PlantacionService plantacionService) {
        this.tempTask = tempTask;
        this.humTask = humTask;
        this.finca = finca;
        this.plantacionService = plantacionService;
    }

    @Override
    public void run() {
        while (ejecutando) {
            try {
                double temp = tempTask.getUltimaTemperatura();
                double hum = humTask.getUltimaHumedad();

                if (!Double.isNaN(temp) && !Double.isNaN(hum)) {
                    if (temp >= 8 && temp <= 15 && hum < 50) {
                        plantacionService.regar(this.finca);
                    }
                }

                Thread.sleep(2500); // frecuencia de control
            } catch (AguaAgotadaException e) {
                // Agua agotada: detener riego y notificar
                System.err.println(e.getFullMessage());
                System.err.println("Sistema de riego detenido automáticamente por falta de agua.");
                ejecutando = false;
                break;
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }

    public void detener() {
        ejecutando = false;
    }
}
