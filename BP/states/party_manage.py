import pygame
from .base import BaseState


class PartyManagement(BaseState):
    def __init__(self):
        super(PartyManagement, self).__init__()
        self.active_index = 0
        self.options = ["Give Item", "Use Item", "Dismiss", "Return"]
        self.next_state = "GAMEPLAY"
        self.menu_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 36)
        self.establish_data_path()

    def initialize(self):
        self.active_index = 0

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("black")
        return self.menu_font.render(self.options[index], True, color)
    
    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * self.menu_font.get_linesize()))
        return text.get_rect(center=center)
    
    def handle_action(self):
        if self.active_index == 0:
            pass
        elif self.active_index == 1:
            pass
        elif self.active_index == 2:
            pass
        elif self.active_index == 3:
            self.next_state = "GAMEPLAY"
            self.done = True
        

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
            elif event.key == pygame.K_UP:
                self.active_index -= 1 
                if self.active_index < 0:
                    self.active_index = len(self.options) - 1
            elif event.key == pygame.K_DOWN:
                self.active_index += 1 
                if self.active_index > len(self.options) - 1:
                    self.active_index = 0
            elif event.key == pygame.K_RETURN:
                self.handle_action()


    def draw(self, surface):
        surface.fill(pygame.Color(220, 215, 175))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
