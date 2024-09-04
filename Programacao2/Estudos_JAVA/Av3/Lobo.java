class Lobo extends Canino{
    public Lobo(String nome, double tamanho, double peso, int idade){
        super(nome, tamanho, peso, idade);
    }

    @Override
    public void fazerBarulho(){
        System.out.println("Auuuuu");
    }

    @Override
    public void comer(){
        System.out.println("Lobo está comendo CARNE, nhac nhac");
    }

}