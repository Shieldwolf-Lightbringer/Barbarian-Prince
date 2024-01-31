import sys
import pygame
import random
from states.menu import Menu
from states.gameplay import Gameplay
from states.game_over import GameOver
from states.splash import Splash
from game import Game

pygame.init()
info = pygame.display.Info() # this gets the width and height of the monitor
monitor_width = info.current_w
monitor_height = info.current_h

screen = pygame.display.set_mode((monitor_width, monitor_height)) #((1440, 900))  #main monitor resolution for development
states = {
     "MENU": Menu(),
     "SPLASH": Splash(),
     "GAMEPLAY": Gameplay(),
     "GAME_OVER": GameOver(),
}

if __name__ == '__main__':
    game = Game(screen, states, "SPLASH")
    game.run()
    pygame.quit()
    sys.exit()
