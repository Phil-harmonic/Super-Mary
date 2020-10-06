from .. components import info
import pygame

class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = "level"

    def update(self, surface, keys):
        self.draw(surface)

    def draw(self, surface):
        surface.fill((0, 0, 0))