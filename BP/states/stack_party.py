import pygame
import os
from states.stack_base_state import BaseState

class PartyMenu(BaseState):
    def __init__(self, game):
        self.game = game
        BaseState.__init__(self, game)

    def update(self, delta_time, actions):
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(display, "PARTY MENU GOES HERE", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2 )
