abstract class Canino extends Animal {
    public Canino (String nome , double tamanho, double peso, int idade){
        super(nome, tamanho, peso, idade);
    }

    @Override
    public void vaguear(){
        System.out.println("Canino está vagueando");
    }
}