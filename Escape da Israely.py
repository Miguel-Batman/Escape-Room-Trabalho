import pygame
from pygame import mixer
from sys import exit
import time

pygame.init()
tela = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("SuperShy")

#funcoes
def digitar(mensagem, cor, eixoX, eixoY, tamanho):#funcao de mostrar escritas
        fonte = pygame.font.SysFont("Arial", tamanho, bold=False, italic=False)
        texto = fonte.render(mensagem, True, cor)
        tela.blit(texto,[(int(eixoX)),(int(eixoY))])
        
#imagens
playn = pygame.image.load('imagens/playn.png')#play normal  
playnrect = playn.get_rect(midtop=(400,300))
playc = pygame.image.load('imagens/playc.png')#play clicado
playcrect = playc.get_rect(midtop=(400,300))

detail = pygame.image.load('imagens/detail.png')#detalhes da tela de menu
titulo = pygame.image.load('imagens/titulo.png')
titulorect = titulo.get_rect(center=(400,150))

israodio = pygame.image.load('imagens/israodio.gif')
perso1 = pygame.image.load('imagens/pers1.png')
#audios
tenso = mixer.Sound('audios/tenso.mp3')
zap = mixer.Sound('audios/whatsapp.mp3')
zap.set_volume(1)

#posicionamento



run = True
click = True
s = True
while run:
    #evento pra fechar a aba
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    while click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        tenso.play()
        tela.blit(detail,(0,0))
    
        mouse_pos = pygame.mouse.get_pos()
        if playnrect.collidepoint(mouse_pos):
            tela.blit(playc, playcrect)
        else:
            tela.blit(playn, playnrect)

        tela.blit(titulo, titulorect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playcrect.collidepoint(mouse_pos) or playnrect.collidepoint(mouse_pos):
                    click = False
                    tenso.stop()
        pygame.display.update()
    while s:

        tela.blit(israodio,(0,0))
        digitar("VOCE NAO FEZ O TRABALHO", "dark red", 100, 520, 50)
        pygame.display.update()
        zap.play()
        time.sleep(2)
        zap.play()
        time.sleep(2)
        s = False
    


    clock.tick(60)
    
