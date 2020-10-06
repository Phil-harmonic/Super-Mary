"""
存放游戏启动时的代码
"""
import pygame
from . import constants as C
from . import tools

pygame.init()
SCREEN = pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))

#加载图片
GRAPHICS = tools.load_graphics("resources/graphics")