import pygame
import os


class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        # self.dimensions = pygame.display.get_window_size()
        self.x = self.screen_rect[2]
        self.y = self.screen_rect[3]
        self.persist = {}
        self.font = pygame.font.Font(None, 24)

    def load_data(self):
        game_folder = os.getcwd() 
        self.img_folder = os.path.join(game_folder, 'img')
        self.sound_folder = os.path.join(game_folder, 'sound')
        self.music_folder = os.path.join(game_folder, 'music')
        self.maps_folder = os.path.join(game_folder, 'maps')

    def startup(self, persistent):
        self.persist = persistent
    
    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass

    