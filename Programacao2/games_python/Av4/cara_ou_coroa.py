from Botao import *
import pygame as pg
import random
import sys

pg.init()
# Tela -------------------
tela = pg.display.set_mode((800, 600))
pg.display.set_caption('Cara ou Coroa')

# É aqui que a escolha da IA e do resultado é feita :)
# o movimentos possíveis como lista permite uma manutenção simples caso queira alterar de cara ou coroa para pedra, papel e tesoura por exemplo
def play(escolha):
    movimentos = ['cara', 'coroa']
    movimento_geral = random.choice(movimentos)

    movimentos_possiveis = []
    for m in movimentos:
        if m != escolha:
            movimentos_possiveis.append(m)

    jogada_AI = random.choice(movimentos_possiveis)

    mensagem_resultado = ""
    
    if jogada_AI == movimento_geral:
        mensagem_resultado = 'A Inteligência Artificial ACERTOU, Você errou!\nTENTE NOVAMENTE!'
    elif escolha == movimento_geral:
        mensagem_resultado = 'A Inteligência Artificial, Você ACERTOU!\nPARABÉNS!'
    
    return f"AI escolheu: {jogada_AI}\nVocê escolheu: {escolha}\nCaiu: {movimento_geral}\n{mensagem_resultado}"


botoes = [Botao(150, 30, 300, 100, 'Cara', play), Botao(150, 140, 300, 100, 'Coroa', play)]

resultado_jogo = ""  # Para armazenar o resultado

# Parte principal do game
running = True
while running:
    tela.fill(azul_claro)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit() # ou running = False
            sys.exit()
        if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
            for botao in botoes:
                resultado = botao.clicar()
                if resultado:
                    resultado_jogo = resultado

    for botao in botoes:  # Desenha os botões
        botao.desenhar(tela)

    if resultado_jogo:  # Exibe o resultado
        renderizarTexto(resultado_jogo, 24, vermelho, tela, 150, 300)

    pg.display.flip()
