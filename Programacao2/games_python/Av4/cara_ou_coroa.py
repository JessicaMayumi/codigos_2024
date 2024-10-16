import pygame as pg
import random
import sys

pg.init()
# Tela -------------------
tela = pg.display.set_mode((800, 600))
pg.display.set_caption('Cara ou Coroa')
# Cores -----------------
azul_claro = (204, 255, 255)
azul_escuro = (0, 102, 204)
vermelho = (255, 102, 102)

def desenhar_texto(texto, tamanho, cor, superficie, x, y):
    fonte = pg.font.SysFont(None, tamanho)
    #Sim! Eu precisei fazer um trem inteiro para quebrar a linha pq esse demônio não queria funcinar
    linhas = texto.split("\n")  # Divide o texto por quebras de linha
    deslocamento_y = y
    for linha in linhas:
        texto_superficie = fonte.render(linha, True, cor)
        superficie.blit(texto_superficie, (x, deslocamento_y))
        deslocamento_y += 30  # Distância entre as linhas de texto

# Função do jogo
def jogar(escolha):
    movimentos = ['cara', 'coroa']
    movimento_geral = random.choice(movimentos)

    movimentos_possiveis = []
    for m in movimentos:
        if m != escolha:
            movimentos_possiveis.append(m)

    jogada_AI = random.choice(movimentos_possiveis)

    mensagem_resultado = ""
    
    if jogada_AI == movimento_geral:
        mensagem_resultado = 'AI ACERTOU, Você errou!\nTENTE NOVAMENTE!'
    elif escolha == movimento_geral:
        mensagem_resultado = 'AI errou, Você ACERTOU!'
    
    return f"AI escolheu: {jogada_AI}\nVocê escolheu: {escolha}\nCaiu: {movimento_geral}\n{mensagem_resultado}"

# Classe do botão
class Botao:
    def __init__(self, x, y, altura, largura,  texto, acao):
        self.rect = pg.Rect(x, y, altura, largura)
        self.texto = texto
        self.acao = acao
        self.clicado = False

    def desenhar(self, superficie):
        # Desenha um retângulo azul escuro
        pg.draw.rect(superficie, azul_escuro, self.rect)
        # Desenha o texto sobre o botão
        desenhar_texto(self.texto, 30, azul_claro, superficie, self.rect.x + 115, self.rect.y + 35)

    def clicar(self):
        mouse = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            return self.acao(self.texto.lower())
        return None

botoes = [Botao(30, 30, 300, 100, 'Cara', jogar), Botao(30, 140, 300, 100, 'Coroa', jogar)]

resultado_jogo = ""  # Para armazenar o resultado

# Loop principal do jogo
rodando = True
while rodando:  # Faz o jogo funcionar
    tela.fill(azul_claro)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
            for botao in botoes:
                resultado = botao.clicar()
                if resultado:
                    resultado_jogo = resultado

    for botao in botoes:  # Desenha os botões
        botao.desenhar(tela)

    if resultado_jogo:  # Exibe o resultado
        desenhar_texto(resultado_jogo, 24, vermelho, tela, 30, 300)

    pg.display.flip()
