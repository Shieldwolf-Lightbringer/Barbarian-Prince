import pygame
from .base import BaseState


class Battle(BaseState):
    def __init__(self):
        super(Battle, self).__init__()
        self.title = self.font.render("BATTLE!", True, pygame.Color("white"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.instructions = self.font.render("Press space to finish the battle.", True, pygame.Color("white"))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] + 50)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
            elif event.key == pygame.K_RETURN:
                pass
            elif event.key == pygame.K_SPACE:
                self.next_state = "GAMEPLAY"
                self.done = True


    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions, self.instructions_rect)