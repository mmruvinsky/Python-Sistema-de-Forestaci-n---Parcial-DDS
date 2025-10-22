package riego.sensores;

public class TemperaturaReaderTask implements Runnable{
    private volatile double ultimaTemperatura = Double.NaN;
    private volatile boolean ejecutando = true;

    @Override
    public void run() {
        while (ejecutando) {
            try {
                ultimaTemperatura = leerSensor();
                System.out.printf("[Temperatura] %.2f °C%n", ultimaTemperatura);
                Thread.sleep(2000); // simula muestreo
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }

    private double leerSensor() {
        return -25 + Math.random() * 75; // entre -25 y 50 °C
    }

    public double getUltimaTemperatura() {
        return ultimaTemperatura;
    }

    public void detener() {
        ejecutando = false;
    }

}
