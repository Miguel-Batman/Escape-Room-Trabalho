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

def dialogos(mensagem, cor, tamanho):#funcao de mostrar escritas com caixa de dialogo
    digitar(mensagem, cor, 100, 500, tamanho)
    


def andar():
    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
         player_pos.y -= 200 * dt
    if keys[pygame.K_s]:
         player_pos.y += 200 * dt
    if keys[pygame.K_a]:
         player_pos.x -= 200 * dt
    if keys[pygame.K_d]:
         player_pos.x += 200 * dt
    
        
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
perso1rect = perso1.get_rect(center=(600, 100))

mapainicial = pygame.image.load('imagens/mapa inicial.png')
computador = pygame.image.load('imagens/computador.png')
comprect = computador.get_rect(bottomleft=(509, 50))
computador = pygame.transform.scale(computador, (40, 40))
#audios
tenso = mixer.Sound('audios/tenso.mp3')
zap = mixer.Sound('audios/whatsapp.mp3')
zap.set_volume(0.1)

#posicionamento
dt = 0
player_pos = pygame.Vector2(570, 70)


run = True
click = True
s = True
quarto1 = True
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
        time.sleep(1)
        # zap.play()
        # time.sleep(2)
        s = False


    while quarto1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
       
        
        tela.blit(mapainicial,(0,0))
        tela.blit(computador, comprect)
        tela.blit(perso1, player_pos)
        andar()
        if player_pos.distance_to(comprect.center) < 30:
            digitar("E", "black", 500, 20, 30)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                dialogos('''O computador no qual vc deveria ter feito o trabalho
                         Bom agora ja era''', "black", 30)
            
                pygame.display.update()
                
                
        pygame.display.update()
        

    clock.tick(60)
    
    
