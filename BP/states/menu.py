import pygame
from .base import BaseState


class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        self.active_index = 0
        self.options = ["Title Screen", "Start Game", "Continue Game", "Options", "Quit Game"]
        self.next_state = "GAMEPLAY"
        self.font = pygame.font.Font(None, 36)

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("black")
        return self.font.render(self.options[index], True, color)
    
    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)
    
    def handle_action(self):
        if self.active_index == 0:
            self.next_state = "SPLASH"
            self.done = True
        elif self.active_index == 1:
            self.next_state = "GAMEPLAY"
            self.done = True
        elif self.active_index == 2:
            pass
        elif self.active_index == 3:
            pass
        elif self.active_index == len(self.options) - 1: 
            self.quit = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_UP:
            #     self.active_index = 1 if self.active_index <= 0 else 0
            # elif event.key == pygame.K_DOWN:
            #     self.active_index = 0 if self.active_index >= 1 else 1
            if event.key == pygame.K_UP:
                self.active_index -= 1 
                if self.active_index < 0:
                    self.active_index = len(self.options) - 1
            elif event.key == pygame.K_DOWN:
                self.active_index += 1 
                if self.active_index > len(self.options) - 1:
                    self.active_index = 0
            elif event.key == pygame.K_RETURN:
                self.handle_action()
            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        #surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
