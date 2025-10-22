package riego.sensores;

public class HumedadReaderTask implements Runnable {
    private volatile double ultimaHumedad = Double.NaN;
    private volatile boolean ejecutando = true;

    @Override
    public void run() {
        while (ejecutando) {
            try {
                ultimaHumedad = leerSensor();
                System.out.printf("[Humedad] %.2f %% %n", ultimaHumedad);
                Thread.sleep(3000); // simula muestreo
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }

    private double leerSensor() {
        return Math.random() * 100; // entre 0% y 100%
    }

    public double getUltimaHumedad() {
        return ultimaHumedad;
    }

    public void detener() {
        ejecutando = false;
    }
}
