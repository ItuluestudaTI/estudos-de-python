import pygame #importando a biblioteca
import random


pygame.init() #executando adisplay biblioteca

x = 1280 #definindo o cumprimento
y = 728 #definindo a altura

screen = pygame.display.set_mode((x, y)) #criando a tela
pygame.display.set_caption('Pitomba') #criano o nome do jogo a ser exibido

bg = pygame.image.load('images/bg.jpg').convert_alpha() #definindo o background e eocnvertendo em alpha pra poder editar
bg = pygame.transform.scale(bg, (x, y)) #escolhendo o tamanho do fundo

alien = pygame.image.load('images/alien.png').convert_alpha() #carregando a imagem da nave
alien = pygame.transform.scale(alien, (50, 50))#define o tamanho da nave do alien


playerImg = pygame.image.load('images/spaceship.png').convert_alpha() #carregando a imagem do player
playerImg = pygame.transform.scale(playerImg, (80, 80)) #conversão do tamanho da nave
playerImg = pygame.transform.rotate(playerImg, -90) #mudar a rotação da nave

missil = pygame.image.load('images/missil.png').convert_alpha()
missil = pygame.transform.scale(missil, (25, 25))
missil = pygame.transform.rotate(missil, -90)

pos_alien_x = 500 #posição do alien pra frente
pos_alien_y = 360 #posição do alien de cima pra baixo

pos_player_x = 200 #posição do personagem
pos_player_y = 300

vel_x_missil = 0
pos_x_missil = 215
pos_y_missil = 314

triggered = False

pontos = 10

rodando = True #rodando é verdadeiro

font = pygame.font.SysFont('font/PixelGameFont.ttf', 50) #deinindo a fonte

#transformando as imagens em objetos que podem interagir
player_rect = playerImg.get_rect() 
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()

#funções
def respawn():
    x = 1350
    y = random.randint(1, 640) #definindo a posição y como sendo um número aleatório entre 1 e 640
    return [x, y]

def respawn_missil():
    triggered = False #quando o tiro for falso ele vai anular a função de correr do tiro
    respawn_missil_x = pos_player_x #ele vai respawnar na posição do player
    respawn_missil_y = pos_player_y
    vel_x_missil = 0 #vai zerar a velocidade
    return [respawn_missil_x, respawn_missil_y, triggered, vel_x_missil]

#houver uma colisão entre o jogador e o alien
def colisions(): # vai somar pontos
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos += 1
        return True
    else:
        return False


while rodando: #criando o loop de tela
    for event in pygame.event.get(): #detectando as teclas
        if event.type == pygame.QUIT: #se a tecla pressionada for o X
            rodando = False #Definindo 'rodando' como False
            #o loop se quebra e o jogo fecha apenas se apertar o X
    screen.blit(bg, (0, 0)) #criando um fundo na posição 0, 0
    
    rel_x = x % bg.get_rect().width #vai definir o rel_x como o resto do tamanho do fundo
    screen.blit(bg, (rel_x - bg.get_rect().width, 0)) #vai criar o background
    if rel_x < 1280: #nessa posição vai ficar mudando o valor
        screen.blit(bg, (rel_x, 0)) #quando  imagem chegar no fim ele vai carregar outra igual
        
    #teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1: #limite para subir
        pos_player_y -= 1 #subir tecla cima
        if not triggered:
            pos_y_missil -= 1
        
    if tecla[pygame.K_DOWN] and pos_player_y < 665: #limite para descer
        pos_player_y += 1 #descer tecla baixo
        
        if not triggered:
            pos_y_missil += 1
        
    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_missil = 3
        
    # respawn
    
    if pos_alien_x == 50: # se a posição x do alien for igual a 50
        pos_alien_x = respawn()[ 0 ] # vai definir a posição x do alien como 0
        pos_alien_y = respawn()[ 1 ] #e vai definir a posição y do alien como 1
        
    if pos_x_missil == 1280:
        pos_x_missil, pos_y_missil, triggered, vel_x_missil = respawn_missil()
    
    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[ 0 ]
        pos_alien_y = respawn()[ 1 ]
        
    #A posição do rect
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x
    
    missil_rect.y = pos_y_missil
    missil_rect.x = pos_x_missil
    
    alien_rect.y = pos_alien_y
    alien_rect.x = pos_alien_x

        
        
    #movimento atualizando
    x -= 1 #velocidade do bg passando
    pos_alien_x -= 2 #o alien se move até o fim da tela sozinho
    
    pos_x_missil += vel_x_missil
    
    pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), missil_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), alien_rect, 4)
    
    #desenhando os pontos
    score = font.render(f' PONTOS: {int(pontos)}', True, (0, 0, 0))
    score.blit(score, (50, 50))
    
    
    #criando imagens
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_x_missil, pos_y_missil))
    screen.blit(playerImg, (pos_player_x, pos_player_y))
    
    print(pontos)
    
    pygame.display.update() #fica atualizando a tela
