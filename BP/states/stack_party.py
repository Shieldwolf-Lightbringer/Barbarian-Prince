import pygame
import os
from states.stack_base_state import BaseState

class PartyMenu(BaseState):
    def __init__(self, game, party):
        self.game = game
        self.party = party
        self.inventory_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 16)
        BaseState.__init__(self, game)

    def update(self, delta_time, actions):
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((220, 215, 175))
        #self.game.draw_text(display, "PARTY MENU GOES HERE", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2 )

        x_coord, y_coord = 20, 20
        for character in self.party:
            attribute_y_coord = y_coord
            for attribute in character.__str__():
                char_text = self.inventory_font.render(attribute, True, [80, 80, 80])
                display.blit(char_text, (x_coord, attribute_y_coord))
                attribute_y_coord += self.inventory_font.get_linesize()
            item_y_coord = attribute_y_coord
            item_counts = {}
            for item in character.possessions:
                item_counts[item] = item_counts.get(item, 0) + 1
            for item, count in item_counts.items():
                if count > 1:
                    item_text = self.inventory_font.render(f'{item.title()} x {count}', True, [80, 80, 80])
                else:
                    item_text = self.inventory_font.render(f'{item.title()}', True, [80, 80, 80])
                display.blit(item_text, (x_coord, item_y_coord))
                item_y_coord += self.inventory_font.get_linesize()
            x_coord += 150
            if x_coord >= self.game.GAME_W * 0.85:
                x_coord = 20
                y_coord = 300