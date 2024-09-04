
abstract class Animal{
    private String nome;
    private double tamanho;
    private double peso;
    private int idade;
    
    public Animal(String nome , double tamanho, double peso, int idade){
        this.nome = nome;
        this.tamanho = tamanho;
        this.peso = peso;
        this.idade = idade;
    }

    public void fazerBarulho(){
        System.out.println("Animal está fazendo barulho");
    }

    public void comer(){
        System.out.println("Animal está comendo");
    }

    public void vaguear(){
        System.out.println("Animal está vagueando");
    }

    public void str(){
        System.out.println("Nome:" + this.getNome() + "\nTamanho:" + this.getTamanho() + "\nPeso:" + this.getPeso() + "\nIdade:" + this.getIdade());
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

   	public double getTamanho() {
		return tamanho;
	} 

	public void setTamanho(double tamanho) {
		this.tamanho = tamanho;
	}  

    public double getPeso() {
		return peso;
	} 

	public void setPeso(double peso) {
		this.peso = peso;
	} 

    public int getIdade() {
		return idade;
	} 

	public void setIdade(int idade) {
		this.idade = idade;
	}   
}