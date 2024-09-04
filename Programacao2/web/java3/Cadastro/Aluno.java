package Cadastro;

public class Aluno extends Pessoa{
	private int cdCurso;
	private boolean idAtivo;	

	public Aluno(){
		super.getDsNome();
		System.out.println("Criando aluno..." + this.getDsNome());
	}

	public int getCdCurso() {
		return cdCurso;
	}
	public boolean getIdAtivo() {
		return idAtivo;
	}

	public void setCdCurso(int cdCurso) {
		this.cdCurso = cdCurso;
	}
	
	public void setIdAtivo(boolean idAtivo) {
		this.idAtivo = idAtivo;
	}
}
