class Leao extends Felino{
    public Leao(String nome, double tamanho, double peso, int idade){
        super(nome, tamanho, peso, idade);
    }

    @Override
    public void fazerBarulho(){
        System.out.println("Raaawr");
    }

    @Override
    public void comer(){
        System.out.println("Leao está comendo CARNE, nhac nhac");
    }
}