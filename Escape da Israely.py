import pygame
from pygame import mixer
from sys import exit
import time

pygame.init()
tela = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("SuperShy")

#funcoes
def digitar(mensagem, cor, eixoX, eixoY, tamanho): #funcao de mostrar escritas
        fonte = pygame.font.SysFont("Arial", tamanho, bold=False, italic=False) #variavel definidora de qual fonte usar
        texto = fonte.render(mensagem, True, cor) #define amensagem a ser mostrada
        tela.blit(texto,[(int(eixoX)),(int(eixoY))])
        textorectI = texto.get_rect(topleft=(eixoX, eixoY))

def dialogos(mensagem, cor, tamanho): #funcao de mostrar escritas com 'caixa' de dialogo
    digitar(mensagem, cor, 100, 500, tamanho)    

def andar(): #funcao pra movimento do personagem
    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    #linhas pra andar
    if keys[pygame.K_w]:
         player_pos.y -= 200 * dt
    if keys[pygame.K_s]:
         player_pos.y += 200 * dt
    if keys[pygame.K_a]:
         player_pos.x -= 200 * dt
    if keys[pygame.K_d]:
         player_pos.x += 200 * dt
    #linhas pra correr
    if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
         player_pos.y -= 300 * dt
    if keys[pygame.K_s] and keys[pygame.K_LSHIFT]:
         player_pos.y += 300 * dt
    if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
         player_pos.x -= 300 * dt
    if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
         player_pos.x += 300 * dt
    #limite de onde pode chegar
    if player_pos.x <= 70:
        player_pos.x = 70
    elif player_pos.x >= 675:
        player_pos.x = 675
    elif player_pos.y <= 0:
        player_pos.y = 0
    elif player_pos.y >= 530:
        player_pos.y = 530
    else:
        pass

def acao(texto, cor): #Mostra pro jogador quando pode usar a tecla de acao "E"
    digitar("E", "white", 15, 10, 30)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        dialogos(texto, cor, 30)




        
#variaveis imagens
#Tela inicial
playn = pygame.image.load('imagens/playn.png')#play normal  
playnrect = playn.get_rect(midtop=(400,300))
playc = pygame.image.load('imagens/playc.png')#play clicado
playcrect = playc.get_rect(midtop=(400,300))
detail = pygame.image.load('imagens/detail.png')#detalhes da tela de menu
titulo = pygame.image.load('imagens/titulo.png')
titulorect = titulo.get_rect(center=(400,150))

israodio = pygame.image.load('imagens/israodio.gif')
#personagens
perso1 = pygame.image.load('imagens/pers1.png')
perso1rect = perso1.get_rect(center=(600, 100))
perso2 = pygame.image.load('imagens/pers2.png')
perso2rect = perso2.get_rect(center=(600, 100))
israely = pygame.image.load('imagens/israely.png')
israelyrect = israely.get_rect(center=(400, 100))
#primeiro mapa
mapainicial = pygame.image.load('imagens/mapa inicial.png')
computador = pygame.image.load('imagens/computador.png')
comprect = computador.get_rect(bottomleft=(509, 50))
computador = pygame.transform.scale(computador, (40, 40))
#portas
porta = pygame.image.load('imagens/portaf.png')
porta = pygame.transform.scale(porta, (85,85))
portarect = porta.get_rect(center=(400, 300))
portaa = pygame.image.load('imagens/portaa.png')
portaa = pygame.transform.scale(portaa, (85,85))
portaarect = portaa.get_rect(center=(400, 300))
portaalr = pygame.image.load('imagens/portaalr.png')
portaalr = pygame.transform.scale(portaalr, (85,85))
portaalrect = portaalr.get_rect(center=(60,300))
portafl = pygame.image.load('imagens/portafl.png')
portafl = pygame.transform.scale(portafl, (85,85))
portaflrect = portafl.get_rect(center=(60, 300))
armario = pygame.image.load('imagens/armario.png')#armario
armario = pygame.transform.scale(armario, (228, 82))
armariorect = armario.get_rect(topright=(440, 8))
parmario = pygame.image.load('imagens/portaarmario.png')
print(armariorect.midbottom)
parmariorect = parmario.get_rect(center=(326,49))
# parmariorect = parmario.get_rect(center=)


#audios
tenso = mixer.Sound('audios/tenso.mp3')
tenso.set_volume(0.1)
zap = mixer.Sound('audios/whatsapp.mp3')
zap.set_volume(0.1)

#posicionamento
dt = 0
eixox = 570
eixoy = 70
player_pos = pygame.Vector2(eixox, eixoy)
#qual personagem jogar
personagem = input("Escolha entre Homem ou Mulher: \n")
if personagem.lower() == "homem" or personagem.lower() == "m" or personagem.lower() == "man":
    personagem = perso1
    personagem_rect = perso1rect
elif personagem.lower() == "mulher" or personagem.lower() == "w" or personagem.lower() == "women":
    personagem = perso2
    personagem_rect = perso2rect
else:
    pass
#variaveis verdadeiras pras cenas
run = True #variavel geral pro codigo funcionar
inmenu = True #variavel pro menu inicial
jumpscare = True #variavel pro jumpscare da israely
quarto1 = True #variavel do quarto 1
#variaveis pra abrir as portas

inventario = []

while run: # evento geral pro jogo rodar
    #evento pra fechar a aba
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    while inmenu: #loop pra continuar no menu inicial
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
                    tenso.stop()
                    inmenu = False
        pygame.display.update()
    while jumpscare: #loop pra aparecer o jumpscare da israely

        tela.blit(israodio,(0,0))
        digitar("VOCE NAO FEZ O TRABALHO", "dark red", 100, 520, 50)
        pygame.display.update()
        zap.play()
        time.sleep(1)
        # zap.play()
        # time.sleep(2)
        jumpscare = False

    while quarto1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
       
        
        tela.blit(mapainicial,(0,0))
        tela.blit(computador, comprect)
        
        if "chave do quarto" not in inventario:
            tela.blit(portafl, portaflrect)
        else:
            tela.blit(portaalr, portaalrect)
        tela.blit(armario, armariorect)
        tela.blit(parmario, (parmariorect.x, parmariorect.y+20))
        
        tela.blit(personagem, player_pos)
        andar()
        if player_pos.distance_to(comprect.center) < 30:
            acao('''O computador no qual vc deveria ter feito o trabalho.
                         Bom, agora ja era''', "white")
            
        if "chave do quarto" in inventario:
            if player_pos.distance_to(portaflrect.center) < 50:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_f]:
                    quarto1 = False
                acao('''Voce abriu a porta, pode fugir
                     Clique F para entrar''', "white")
        else:
            if player_pos.distance_to(portaflrect.center) < 50:
                acao('''A porta esta trancada.
Procure algo para abrir a porta.''', "white")
        
        if player_pos.distance_to(parmariorect.center) < 50:
            acao('''Voce encontrou a CHAVE DO SEU QUARTO
                 Este item foi adicionado ao seu inventário''', "white")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                inventario.append("chave do quarto")
        
            pygame.display.update()
                
                
        pygame.display.update()
        

    clock.tick(60)
    
    
