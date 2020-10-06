import os, sys
os.chdir(sys.path[0])

import pygame
pygame.init()

w, h = 500, 500
pygame.display.set_mode((w, h))
screen = pygame.display.get_surface()

bgpic = pygame.image.load("background.png")
bgpic = pygame.transform.scale(bgpic, (w, h))

mario_image = pygame.image.load("man.png")

#创建精灵
mario = pygame.sprite.Sprite()
mario.image = mario_image
mario.rect = mario.image.get_rect()
mario.rect.x, mario.rect.y = w / 2, h /2

#玩家组
player_group = pygame.sprite.Group()
player_group.add(mario)

#开始游戏
while True:
    #更新部分
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                mario.rect.y += 10
            if keys[pygame.K_UP]:
                mario.rect.y -= 10
            if keys[pygame.K_RIGHT]:
                mario.rect.x += 10
            if keys[pygame.K_LEFT]:
                mario.rect.x -= 10
            
    #画图部分
    screen.blit(bgpic, (0, 0))
    player_group.draw(screen)
    pygame.display.update()
