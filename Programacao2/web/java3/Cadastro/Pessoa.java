package Cadastro;

public class Pessoa {
	private int cdCadastro;
	private char idFisicaJuridica;
	private String dsCpfCnpj;
	private boolean idAtivo;
	private String dsNome;
	private char idEstadoCivil;
	private String dsEmail;

	public Pessoa (String dsNome){
		this.dsNome = dsNome;
		this.idAtivo = true;
		System.out.println("Criando pessoa...");
	}

	public int getCdCadastro() {
		return cdCadastro;
	}

	public String getDsCpfCnpj() {
		return dsCpfCnpj;
	}

	public String getDsEmail() {
		return dsEmail;
	}

	public String getDsNome() {
		return dsNome;
	}

	public boolean getIdAtivo() {
		return idAtivo;
	}
	
	public char getIdEstadoCivil() {
		return idEstadoCivil;
	}

	public char getIdFisicaJuridica() {
		return idFisicaJuridica;
	}

	public void setCdCadastro(int cdCadastro) {
		this.cdCadastro = cdCadastro;
	}

	public void setDsCpfCnpj(String dsCpfCnpj) {
		this.dsCpfCnpj = dsCpfCnpj;
	}

	public void setDsEmail(String dsEmail) {
		this.dsEmail = dsEmail;
	}

	public void setDsNome(String dsNome) {
		this.dsNome = dsNome;
	}		

	public void setIdAtivo(boolean idAtivo) {
		this.idAtivo = idAtivo;
	}	

	public void setIdEstadoCivil(char idEstadoCivil) {
		this.idEstadoCivil = idEstadoCivil;
	}

	public void setIdFisicaJuridica(char idFisicaJuridica) {
		this.idFisicaJuridica = idFisicaJuridica;
	}
	
}