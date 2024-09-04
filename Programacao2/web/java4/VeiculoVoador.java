package java4;

public class VeiculoVoador extends Veiculo {
    private double altitude;
        
    public VeiculoVoador (double altitude){
        this.altitude = altitude;
        System.out.println("A altitude é " + altitude);
    }
    
    public void diminuiVelocidade(){
        if (velocidade < 400){
            velocidade += 50;
        }
    }
    
    public void setAltitude(double altitude) {
        this.altitude = altitude;
    }

    public double getAltitude() {
        return altitude;
    }
    
}
