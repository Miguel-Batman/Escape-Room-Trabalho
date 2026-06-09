#Importar a biblioteca
import pygame
from pygame import mixer#importar o mixer pra tocar musicas
from sys import exit #importar o exit pra fechar o jogo sem dar erro
#termo necessario para exeutar o pygame
pygame.init()

#variavel pra tela e relogio de fps
tela = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#variaveis pro movimento do personagem
dt = 0
ex = tela.get_width() / 2
ey = tela.get_height() / 2
player_pos = pygame.Vector2(ex,ey)
#função pra digitar
def digitar(mensagem, cor, eixoX, eixoY):
        fonte = pygame.font.SysFont("Arial", 40, bold=False, italic=False)
        texto = fonte.render(mensagem, True, cor)
        tela.blit(texto,[(int(eixoX)),(int(eixoY))])
#funcao pra mostrar dialogos em um espaco especifico
def dialogos(mensagem, cor, tamanho):
    digitar(mensagem, cor, 100, 500, tamanho)
    #funcao de movimento do personagem
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

#variaveis pra imagem e som
zap = mixer.Sound("audios/whatsapp.mp3")#o local do arquivo deve conter as pastas e o nome exato do arquivo
zap.set_volume(0.1)#definir o volume da musica, o valor deve ser entre 0.0 e 1.0
zap.play()#tocar a musica, o comando play() deve ser chamado depois do set_volume() pra funcionar
titulo = pygame.image.load("imagens/titulo.png")#o local do arquivo deve conter as pastas e o nome exato do arquivo
titulorect = titulo.get_rect(center=(400, 400))#variavel pra pegar o retangulo da imagem. O centro do retangulo é definido como o centro da tela, ou seja, (400, 300)
#variavel verdadeira pra o codigo executar enquanto for True
run = True
#Loop que continua executando enquanto run = True
while run:
    #evento pra declarar run = False ao clicar o "x" da aba
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Preenchimento completo da tela
    tela.fill("white")
    #estrutura do CIRCLE(Tela exposta, cor, ((Eixo X, Eixo Y)), Tamanho)
    pygame.draw.circle(tela, "red", ((800/2, 600/2)), 50)
    #Estrutura do RECT(tela exposta, cor, [eixo X, eixo Y, largura, altura])
    pygame.draw.rect(tela, "orange", [30, 30, 50, 50])
    #linhas pra digitar textos no codigo com a funcao
    digitar("Sofiazinha legalzinha", "blue", 180, 60)
    #como colocar imagens usando rect
    tela.blit(titulo, titulorect)#o titulorect é a variavel que tem o retangulo da imagem, o blit é a função que coloca a imagem na tela usando o retangulo pra definir a posição
    #bloco pra funcao de movimento do personagem
    pygame.draw.circle(tela, "pink", player_pos, 20)
    andar()

    #função que mostra as informações na tela
    pygame.display.flip()
    #Definidor de FPS
    clock.tick(60)
pygame.quit()
