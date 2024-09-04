public class Main {
    public static void main(String[] args){
        //Gato
        System.out.println("Teste Gato");
        Gato gato = new Gato("Ana Catarina", 1, 2, 3);

        gato.fazerBarulho();
        gato.comer();
        gato.vaguear();
        gato.str();

         //Leão
        System.out.println("\n\nTeste Leão");
        Leao leao = new Leao("Leona", 1, 2, 3);

        leao.fazerBarulho();
        leao.comer();
        leao.str();
        leao.vaguear();
        
        //Cachorro
        System.out.println("\n\nTeste Cachorro");
        Cachorro cachorro = new Cachorro("Pingo", 1, 2, 3);

        cachorro.fazerBarulho();
        cachorro.comer();
        cachorro.str();
        
        //Lobo
        System.out.println("\n\nTeste Lobo");
        Lobo lobo = new Lobo("Rabito", 1, 2, 3);

        lobo.fazerBarulho();
        lobo.comer();
        lobo.str();
        
        //Hipopótamo
        System.out.println("\n\nTeste Hipopótamo");
        Hipopotamo hipopotamo = new Hipopotamo("Blue", 1, 2, 3);

        hipopotamo.fazerBarulho();
        hipopotamo.comer();     
        hipopotamo.str();   
    }
}