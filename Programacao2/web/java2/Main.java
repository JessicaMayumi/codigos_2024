package java2;
public class Main { //add args no terminal
    public static void main(String[] args){
        System.out.println("Testes");
        System.out.println(args[0]);
        System.out.println(args[1]);
    }
}



public class Main { //pegar o numero de args na lista
    public static void main(String[] args){
        System.out.println(args.length);

    }
}



public class Main { //loop atẽ acabar a lista
    public static void main(String[] args){
        System.out.println("Apenas Testes");

        for (String lista : args){
            System.out.println(lista);
        }

    }
}

public class Main { //loop pelo index
    public static void main(String[] args){
        System.out.println("Apenas Testes");

        for (int i=0; i<args.length; i++){
            System.out.println(args[i]);
        }

    }
}


