import os, sys
os.chdir(sys.path[0])
import pygame
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()

    def run(self, state): 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            # #填充颜色
            # self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            # image = get_image(GRAPHICS["mario_bros"], 145, 32, 16, 16, (0, 0, 0), 5)
            # self.screen.blit(image, (300, 300))
            state.update(self.screen, self.keys)
            pygame.display.update()
            self.clock.tick(60)

def load_graphics(path, accept = (".jpg", ".png", ".bmp", ".gif")):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)#splitext分拆文件名+后缀
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics

def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (x, y, width, height))#(0, 0)代表画到哪个位置， (x, y, w, h)代表sheet里哪个区域要取出来
    image.set_colorkey(colorkey)#根据底色抠图
    image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))#放大图片
    return image

