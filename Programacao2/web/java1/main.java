import java.util.Scanner;
class Input {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Insira seu nome: ");
        String inp = input.nextLine();
        System.out.print("Insira sua idade: ");
        int idade = input.nextInt();
        System.out.println("Olá, " + inp);
        System.out.println("Você tem " + idade + " anos.");
    }
}
