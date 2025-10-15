
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0
player = pygame.image.load("WeedMan.png")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 200
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkgreen")

    
    screen.blit(player,player_pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt


    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()