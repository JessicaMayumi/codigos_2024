abstract class Felino extends Animal {
    public Felino (String nome, double tamanho, double peso, int idade){
        super(nome, tamanho, peso, idade);
    }

    @Override
    public void vaguear(){
        System.out.println("Felino está vagueando");
    }
}