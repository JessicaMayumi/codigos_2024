package java4;

public abstract class Veiculo {
    protected int velocidade = 0;
    
    public void aumentaVelocidade(){
        if (velocidade <150){
            velocidade++;
        }
    }
    public abstract void diminuiVelocidade();
}

