class Gato extends Felino{
    public Gato(String nome, double tamanho, double peso, int idade){
        super(nome, tamanho, peso, idade);
    }

    @Override
    public void fazerBarulho(){
        System.out.println("Miau");
    }

    @Override
    public void comer(){
        System.out.println("Gato está comendo PEIXE, nhac nhac");
    }

    @Override
    public void vaguear(){
        System.out.println("Gato está vagueando");
    }
}