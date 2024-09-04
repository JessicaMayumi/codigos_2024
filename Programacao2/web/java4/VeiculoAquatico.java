package java4;

public class VeiculoAquatico extends Veiculo{
    private double profundidade;
        
    public VeiculoAquatico (double profundidade){
        this.profundidade = profundidade;
        System.out.println("A profundidade é " + profundidade);
    }
    
    public void diminuiVelocidade(){
        if (velocidade < 400){
            velocidade += 50;
        }
    }

    public void setProfundidade(double profundidade) {
        this.profundidade = profundidade;
    }

    public double getProfundidade() {
        return profundidade;
    }
}
