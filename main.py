"""
游戏主要入口
"""
import pygame
from source import tools, setup
from source.states import main_menu, load_screen, level

def main():
    state_dict = {
        "main_menu": main_menu.MainMenu(),
        "load_sreen": load_screen.LoadScreen(),
        "level": level.Level()
    }
    game = tools.Game(state_dict, "main_menu")
    game.run(state)

if __name__ == "__main__":
    main()
