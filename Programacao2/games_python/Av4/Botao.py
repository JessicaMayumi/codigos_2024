import pygame as pg

# Cores -----------------
azul_claro = (204, 255, 255)
azul_escuro = (0, 102, 204)
vermelho = (255, 102, 102)

def renderizarTexto(texto, tamanho, cor, superficie, x, y):
    fonte = pg.font.SysFont(None, tamanho)
    #Sim! Eu precisei fazer um trem inteiro para quebrar a linha pq esse demônio não queria funcinar
    linhas = texto.split("\n")  # Divide o texto por quebras de linha
    deslocamento_y = y
    for linha in linhas:
        texto_superficie = fonte.render(linha, True, cor)
        superficie.blit(texto_superficie, (x, deslocamento_y))
        deslocamento_y += 30  # Distância entre as linhas de texto

class Botao:
    def __init__(self, x, y, altura, largura,  texto, acao):
        self.rect = pg.Rect(x, y, altura, largura)
        self.texto = texto
        self.acao = acao
        self.clicado = False

    def desenhar(self, superficie):
        pg.draw.rect(superficie, azul_escuro, self.rect)
        renderizarTexto(self.texto, 30, azul_claro, superficie, self.rect.x + 115, self.rect.y + 35)

    def clicar(self):
        mouse = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            return self.acao(self.texto.lower())
        return None
