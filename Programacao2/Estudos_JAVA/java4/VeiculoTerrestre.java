package java4;

public class VeiculoTerrestre extends Veiculo{
    private int qtdRodas;
    
    public VeiculoTerrestre (int qtdRodas){
		this.qtdRodas = qtdRodas;
		System.out.println("Quantidade de Rodas é " + qtdRodas);
	}

    public void diminuiVelocidade(){
        if (velocidade < 400){
            velocidade += 50;
        }
    }

    public void setQtdRodas(int qtdRodas) {
        this.qtdRodas = qtdRodas;
    }

    public int getQtdRodas() {
        return qtdRodas;
    }

}
