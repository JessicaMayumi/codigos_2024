class Cachorro extends Canino{
    public Cachorro(String nome , double tamanho, double peso, int idade){
        super(nome, tamanho, peso, idade);
    }

    @Override
    public void fazerBarulho(){
        System.out.println("Au Au") ;
    }

    @Override
    public void comer(){
        System.out.println("Cachorro está comendo OSSO, nhac nhac");
    }

}