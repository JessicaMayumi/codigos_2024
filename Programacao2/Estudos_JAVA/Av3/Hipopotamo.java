class Hipopotamo extends Animal{
    public Hipopotamo(String nome, double tamanho, double peso, int idade){
        super(nome, tamanho, peso, idade);
    }

    @Override
    public void fazerBarulho(){
        System.out.println("roonn roonn");
    }

    @Override
    public void comer(){
        System.out.println("Hipopótamo está comendo MELANCIA, nhac nhac");
    }

}