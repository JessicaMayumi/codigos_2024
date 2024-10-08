package modelo;

import utils.GeradorMapaComAnotacao.Ignorar;
import utils.GeradorMapaComAnotacao.NomePropriedade;

public class Telefone {

	private String numero;
	public String codigoPais;
	private String operadora;
	
	public String getNumero() { return numero; }
	public void setNumero(String n) { numero = n; }
	
	// anotação para permitir acesso ao campo de outra forma
	// similar a um "alias" em tempo de execução apenas
	@NomePropriedade("codigoInternacional")
	public String getCodigoPais() {	return codigoPais; }
	
	public void setCodigoPais(String codp) { codigoPais = codp; }
	
	// anotação para ignorar este método 
	@Ignorar
	public String getOperadora() { return operadora; }
	
	public void setOperadora(String op) { operadora = op; }
	
	@Override
	public String toString() {
		return "Telefone [numero=" + numero + ", codigoPais=" 
	    + codigoPais + ", operadora=" + operadora + "]";
	}
	
	
}