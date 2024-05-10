import pygame
import os
from states.stack_base_state import BaseState
from states.stack_game_world import GameWorld

class Title(BaseState):
    def __init__(self, game):
        BaseState.__init__(self, game)
        self.title_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 108)
        self.title = self.title_font.render("BARBARIAN PRINCE", True, pygame.Color("red"))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (self.game.GAME_W / 2, self.game.GAME_H / 4)

        self.background_img = pygame.image.load(os.path.join(self.game.img_folder, 'background.jpg')).convert_alpha()
        self.background_img = pygame.transform.scale(self.background_img, (self.game.GAME_W, self.game.GAME_H + 120))
        self.background_img_rect = self.background_img.get_rect(center=(self.game.GAME_W / 2, self.game.GAME_H / 2))
        
        self.title_img = pygame.image.load(os.path.join(self.game.img_folder, 'bp_cover.png')).convert_alpha()
        self.title_img = pygame.transform.scale2x(self.title_img)
        self.title_img_rect = self.title_img.get_rect()
        self.title_img_rect.center = (self.game.GAME_W / 4, self.game.GAME_H * .6)
        self.title_img2 = pygame.transform.flip(self.title_img, True, False)
        self.title_img_rect2 = self.title_img.get_rect()
        self.title_img_rect2.center = (self.game.GAME_W * .75, self.game.GAME_H * .6)

        self.active_index = 0
        self.options = ["Start Game", "Continue Game", "Options", "Quit Game"]
        self.menu_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 36)

    def update(self, delta_time, actions):
        if actions["up"]:
                self.active_index -= 1 
                if self.active_index < 0:
                    self.active_index = len(self.options) - 1
        if actions["down"]:
                self.active_index += 1 
                if self.active_index > len(self.options) - 1:
                    self.active_index = 0
        if actions["start"]:
            self.handle_menu_selection()
            # new_state = GameWorld(self.game)
            # new_state.enter_state()
        self.game.reset_keys()

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("black")
        return self.menu_font.render(self.options[index], True, color)
    
    def get_text_position(self, text, index):
        center = (self.game.GAME_W / 2, self.game.GAME_H / 2 + (index * self.menu_font.get_linesize()))
        return text.get_rect(center=center)
    
    def handle_menu_selection(self):
        if self.active_index == 0: #PLAY
            new_state = GameWorld(self.game)
            new_state.enter_state()
        elif self.active_index == 1: #CONTINUE
            pass
        elif self.active_index == 2: #OPTIONS
            pass
        elif self.active_index == 3: #QUIT
            self.game.playing = False
            self.game.running = False
        # elif self.active_index == len(self.options) - 1: 
        #     self.game.playing = False
        #     self.game.running = False

    def render(self, display):
        display.blit(self.background_img, (0,0))
        display.blit(self.title_img, self.title_img_rect)
        display.blit(self.title_img2, self.title_img_rect2)
        display.blit(self.title, self.title_rect)
        #display.fill((255,255,255))
        #self.game.draw_text(display, "Game States Demo", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2 )

        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            display.blit(text_render, self.get_text_position(text_render, index))