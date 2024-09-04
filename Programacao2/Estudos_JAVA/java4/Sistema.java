package java4;

public class Sistema {
    	public static void main(String[] args) {

		VeiculoTerrestre v1 = new VeiculoTerrestre(2); 
		VeiculoAquatico v2 = new VeiculoAquatico(2.1); 
        VeiculoVoador v3 = new VeiculoVoador(2.2); 

		System.out.println(v1);
        System.out.println(v2);
        System.out.println(v3);

	}
}
