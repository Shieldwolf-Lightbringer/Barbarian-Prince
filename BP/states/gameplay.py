import pygame
import game_actions
import characters
import events
from game_console import Console
from .base import BaseState
from os import path
from math import cos, sin, pi, sqrt, radians
from random import choice, randint

ROWS = 23
COLUMNS = 20
HEX_RADIUS = 60  # if below 60, subsurface outside surface area
HEX_SIDE_LENGTH = int(HEX_RADIUS * sqrt(3))
MAP_WIDTH = (HEX_RADIUS * 3/2) * COLUMNS + (HEX_RADIUS * .55)
MAP_HEIGHT = (HEX_RADIUS * 2) * (ROWS - 3) + (HEX_RADIUS * .70)
hexagon_dict = {}
outline_color = (255, 255, 0)
parchment_color = (220, 215, 175)

plains = [(1,1),(1,2),(1,4),(1,8),(1,9),(1,10),(1,12),(1,13),(1,19),(1,20),(1,21),(1,22),(2,8),(2,9),(2,10),
          (2,11),(2,12),(2,19),(2,23),(3,5),(3,8),(3,11),(3,16),(3,18),(3,20),(3,21),(4,10),(4,12),(4,13),
          (4,15),(4,16),(4,17),(5,2),(5,7),(5,10),(5,12),(5,15),(5,17),(5,20),(5,21),(5,23),(6,1),(6,2),
          (6,4),(6,7),(6,8),(6,12),(6,13),(6,14),(6,15),(6,17),(6,20),(6,21),(6,22),(6,23),(7,1),(7,2),
          (7,4),(7,6),(7,7),(7,8),(7,14),(7,17),(7,18),(7,20),(7,22),(8,10),(8,17),(8,18),(8,19),(8,20),
          (8,21),(8,22),(8,23),(9,2),(9,5),(9,6),(9,7),(9,9),(9,10),(9,17),(9,19),(9,20),(9,21),(10,4),(10,5),
          (10,8),(10,12),(10,13),(10,14),(10,17),(11,4),(11,10),(11,15),(11,16),(11,18),(12,5),(12,13),(12,16),
          (12,17),(12,21),(13,1),(13,3),(13,5),(13,14),(13,15),(13,17),(13,18),(13,19),(13,20),(13,21),(13,22),
          (13,23),(14,2),(14,3),(14,16),(14,18),(14,20),(15,13),(15,14),(15,16),(16,2),(16,13),(16,14),(16,15),
          (16,16),(16,19),(16,20),(17,4),(17,14),(17,18),(17,20),(17,23),(18,3),(18,14),(18,19),(18,23),(19,5),
          (19,6),(19,11),(19,14),(19,15),(19,18),(19,19),(20,4),(20,14),(20,18),(20,19)] #complete
plains_green = (217, 217, 90)

farmlands = [(2,16),(2,17),(2,22),(3,17),(3,19),(3,22),(3,23),(4,18),(4,19),(4,20),(4,22),(4,23),
             (5,19),(6,18),(6,19),(7,19),(8,16),(9,16),(10,9),(13,16),(14,14),(14,15),(15,1),(15,15),
             (16,1), (18,22),(19,21),(19,22),(19,23),(20,21),(20,22),(20,23)] #complete
farmlands_brown = (190, 171, 167)

forests = [(1,11),(1,16),(1,17),(1,18),(1,23),(2,2),(2,3),(2,15),(2,18),(2,20),(2,21),(3,2),(3,3),(3,9),(3,10),
           (3,14),(3,15),(4,1),(4,2),(4,8),(4,9),(4,14),(4,21),(5,1),(5,5),(5,8),(5,9),(5,13),(5,14),(5,16),(5,18),
           (5,22),(6,6),(6,10),(6,16),(7,5),(7,9),(7,11),(7,12),(7,15),(7,16),(7,21),(7,23),(8,2),(8,3),(8,5),(8,7),
           (8,8),(8,9),(8,11),(8,12),(8,13),(8,14),(8,15),(9,3),(9,8),(9,11),(9,13),(9,15),(9,18),(10,2),(10,7),
           (10,18),(11,17),(11,20),(12,1),(12,2),(12,18),(12,19),(12,20),(12,22),(13,4),(13,12),(14,4),(14,13),
           (14,17),(14,19),(15,3),(15,4),(15,17),(15,18),(15,19),(15,20),(15,21),(16,4),(16,18),(16,21),(17,16),
           (17,17),(17,22),(18,15),(18,17),(18,20),(18,21),(19,16),(19,17),(19,20),(20,15),(20,17),(20,20)] #complete
forests_green = (56, 109, 93)

hills = [(1,5),(1,7),(2,4),(2,5),(2,7),(3,7),(4,6),(5,6),(6,5),(8,1),(8,6),(9,4),(9,12),(9,22),(9,23),
         (10,1),(10,3),(10,10),(10,11),(10,19),(10,23),(11,1),(11,2),(11,7),(11,8),(11,9),(11,12),(11,13),
         (12,3),(12,8),(12,9),(12,10),(12,15),(13,6),(13,9),(13,10),(14,5),(14,6),(14,7),(14,10),(14,11),
         (14,12),(15,11),(15,12),(16,10),(16,12),(17,1),(17,2),(17,9),(17,11),(17,13),(17,15),(17,19),
         (18,8),(18,11),(18,12),(18,13),(18,18),(19,4),(19,12),(19,13),(20,3),(20,5),(20,7),(20,9),(20,10),
         (20,13)] #complete
hills_red = (175, 79, 90)

mountains = [(1,3),(2,1),(3,1),(3,4),(4,3),(4,4),(4,5),(5,3),(5,4),(6,3),(7,3),(8,4),(9,1),(10,6),
             (10,20),(10,21),(10,22),(11,5),(11,6),(11,11),(11,14),(11,21),(11,22),(11,23),(12,4),
             (12,6),(12,7),(12,11),(12,12),(12,14),(12,23),(13,7),(13,11),(13,13),(15,5),(15,6),
             (16,3),(16,5),(16,11),(17,3),(17,5),(17,6),(17,12),(18,1),(18,2),(18,4),(18,5),(18,6),
             (18,7),(18,9),(18,10),(19,1),(19,2),(19,3),(19,7),(19,8),(19,9),(19,10),(20,1),(20,2),
             (20,6),(20,8),(20,11),(20,12)] #complete
mountains_gray = (208, 200, 224)

deserts = [(1,6),(2,6),(3,6),(4,7),(13,8),(14,8),(14,9),(15,7),(15,8),(15,9),(15,10),
           (16,6),(16,7),(16,8),(16,9),(17,7),(17,8),(17,10)] #complete
deserts_yellow = (236, 236, 198)

swamps = [(1,14),(1,15),(2,13),(2,14),(3,12),(3,13),(4,11),(5,11),(6,9),(6,11),(7,10),(7,13),(9,14),
          (10,15),(10,16),(11,3),(11,19),(13,2),(14,1),(14,21),(14,22),(14,23),(15,2),(15,22),(15,23),
          (16,17),(16,22),(16,23),(17,21),(18,16),(20,16)] #complete
swamps_blue = (213, 236, 244)

towns = {(1,1):['Ogon', (pygame.Rect(0, 240, 80, 80))],
         (1,9):['Angleae', (pygame.Rect(0, 240, 80, 80))],
         (2,16):['Galden', (pygame.Rect(0, 320, 80, 80))],
         (4,19):['Halowich', (pygame.Rect(0, 240, 80, 80))],
         (4,22):['Lower Drogat', (pygame.Rect(0, 320, 80, 80))],
         (7,19):['Brigud', (pygame.Rect(0, 320, 80, 80))],
         (9,16):['Erwyn', (pygame.Rect(0, 320, 80, 80))],
         (10,4):['Cumry', (pygame.Rect(0, 240, 80, 80))],
         (10,9):['Cawther', (pygame.Rect(0, 320, 80, 80))],
         (15,1):['Weshor', (pygame.Rect(0, 320, 80, 80))],
         (14,15):['Tulith', (pygame.Rect(0, 240, 80, 80))],
         (17,20):['Lullwyn', (pygame.Rect(0, 240, 80, 80))]}
castles = {(3,23):['Drogat Castle', (pygame.Rect(0, 400, 80, 80))],
           (12,12):['Huldra Castle', (pygame.Rect(0, 400, 80, 80))],
           (19,23):['Aeravir Castle', (pygame.Rect(0, 400, 80, 80))]}
temples = {(7,11):["Branwyn's Temple", (pygame.Rect(80, 320, 80, 80))],
           (10,21):['Sulwyth Temple', (pygame.Rect(80, 80, 80, 80))],
           (13,9):["Donat's Temple", (pygame.Rect(80, 240, 80, 80))],
           (18,5):['Temple of Zhor', (pygame.Rect(80, 0, 80, 80))],
           (20,18):['Temple of Duffyd', (pygame.Rect(80, 160, 80, 80))]}
oasis = [(2,6),(14,9),(16,7),(16,9)]
ruins = {(2,6):['The Dead Plains', (pygame.Rect(0, 80, 80, 80))],
         (9,1):["Jakor's Keep", (pygame.Rect(0, 0, 80, 80))],
         (20,9):['Ruins of Pelgar', (pygame.Rect(0, 160, 80, 80))]}
roads = {(1,9):[1,4],(2,7):[0,3],(2,8):[0,4],
        (2,16):[2],(3,17):[3,5],(3,18):[0,3],(3,19):[0,2],(4,19):[2,3,5],
        (4,20):[0,3],(4,21):[0,4],(3,22):[1,3],(3,23):[0,1,3],(4,22):[4],
        (5,20):[1,5],(6,19):[1,4],(7,19):[1,2,4],
        (8,18):[0,4],(8,17):[0,3],(8,16):[1,3],(9,16):[4],
        (8,19):[3,5],(8,20):[0,2],(9,21):[2,5],(10,21):[5],
        (12,8):[2,4],(11,9):[1,4],(10,9):[1,3],(10,10):[0,3],(10,11):[0,2],(11,12):[3,5],(11,13):[0,2],
        (12,13):[2,5],(13,14):[2,5],(14,14):[3,5],(14,15):[0,1,4],
        (13,16):[1,3],(13,17):[0,3],(13,18):[0,3],(13,19):[0,3],(13,20):[0,2],(14,20):[1,5],(15,20):[1,4],
        (16,19):[2,4],(17,20):[1,2,5],
        (18,19):[1,4],(19,19):[1,4],(20,18):[1,4],
        (18,20):[2,5],(19,21):[2,5],(20,21):[3,5],(20,22):[0,4],(19,23):[1,4],(18,23):[1,4],
        (15,15):[1,4],(16,14):[1,4],(17,14):[1,4],(18,13):[4],
        (19,12):[0],(19,11):[1,3],(20,10):[0,4],(20,9):[3],
        (18,3):[2],(19,4):[3,5],(19,5):[0,3],(19,6):[0,5],(18,5):[2],}
rivers = {(1,1):[3],(1,2):[0,1],(2,1):[3,4],(2,2):[0,1],(3,2):[2,3,4],(3,3):[0],
          (4,1):[3],(4,2):[0,1,5],(5,2):[2,3,4],(5,3):[0],(6,1):[2,3],(6,2):[0,5],
          (7,1):[3],(7,2):[0,1,5],(8,1):[2,3,4],(8,2):[0],(9,1):[3],(9,2):[0,1,5],
          (10,1):[2,3,4],(10,2):[0],(11,1):[3],(11,2):[0,1,5],(12,1):[2,3,4],(12,2):[0,2,3],
          (13,1):[2,3],(13,2):[0,2,3,5],(14,1):[0,1,2,3,5],(14,2):[0,5],(15,1):[3,4],(15,2):[0,1,5],
          (16,1):[2,3,4],(16,2):[0],(17,1):[3],(17,2):[0,1,5],(18,1):[2,3,4],(18,2):[0],
          (19,1):[3],(19,2):[0,1,5],(20,1):[3,4],(20,2):[0,1],
          (13,3):[0,5],(12,3):[0,5],(11,3):[2,3],(11,4):[0,4,5],(10,3):[2],(10,4):[1,2],
          (11,5):[4,5],(10,5):[1,2,3],(11,6):[5],(10,6):[0,5],(9,6):[2,3],(9,7):[0,5],
          (8,6):[2,3],(8,7):[0,5],(7,7):[2,3],(7,8):[0,4,5],(6,7):[2],(6,8):[1,2],
          (7,9):[3,4,5],(6,9):[1,2,3],(6,10):[0,5],(7,10):[0,1,2,5],(8,9):[4],(8,10):[4,5],
          (5,10):[2,3],(5,11):[0,5],(4,10):[2,3],(4,11):[0,4,5],(3,11):[2],(3,12):[1,2,3],
          (4,12):[5],(3,13):[0,5],(2,12):[2,3],(2,13):[0,4,5],(1,13):[2],(1,14):[1,2,3],
          (2,14):[5],(1,15):[0],
          (7,11):[1,2],(8,11):[3,4,5],(7,12):[1],(8,12):[0,1],(9,12):[3,4],(9,13):[0,1,2],
          (10,12):[4],(10,13):[4,5],(9,14):[1,2],(10,14):[4,5],(9,15):[1,2],(10,15):[4,5],
          (9,16):[1,2],(10,16):[3,4,5],(9,17):[1],(10,17):[0,1,2],(11,17):[4],(11,18):[3,4,5],
          (10,18):[1],(11,19):[0,1,2],(12,18):[2,3,4],(12,19):[0,3,4,5],(13,18):[2,3],(13,19):[0,5],
          (14,17):[2,3],(14,18):[0,5],(15,17):[3],(15,18):[0,5],
          (11,20):[1],(12,20):[0,1],(13,20):[3,4],(13,21):[0,1],(14,20):[3,4],(14,21):[0,1,2],
          (15,21):[4],(15,22):[3,4,5],(15,23):[0,1,4,5],(14,22):[1,2],(14,23):[1],(16,22):[2,3,4],
          (16,23):[0],(17,22):[3],(17,23):[0,1,5],(18,22):[3,4],(18,23):[0,1],(19,23):[4],
          (20,11):[2,3],(20,12):[0,4,5],(19,12):[2],(19,13):[1,2,3],(20,13):[5],(19,14):[0,4,5],
          (19,15):[5],(18,13):[2],(18,14):[1,2,3],(18,15):[0,4,5],(17,15):[2],(17,16):[1],}


class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "GAME_OVER"
        self.console_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 16)
        self.console = Console(self.screen, self.console_font, 1.0, 0.25)
        self.player = characters.Character('Cal Arath', 'male', 8, 9, 0, 2, randint(2,6), True)
        self.player_hex = choice([(1,1),(7,1),(9,1),(13,1),(15,1),(18,1)])
        '''camera and map are confined to the upper-left 3/4s of the screen'''
        self.camera = pygame.Rect((0, 0), (self.x * 0.75, self.y * 0.75)) #(self.x, self.y))
        self.party = []
        self.lovers = []
        self.party.append(self.player)
        self.trackers = {'Day': 1, 'Party': len(self.party), 'Rations': 0, 'Gold': self.player.gold, 'Speed': min(char.move_speed for char in self.party)}
        self.establish_data_path()

        self.player_icon = pygame.image.load(path.join(self.img_folder, 'player_icon_outline.png')).convert_alpha()
        self.player_rect = self.player_icon.get_rect()
        self.player_rect.center = (HEX_RADIUS, HEX_RADIUS)

        self.map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
        self.map_surface_rect = self.map_surface.get_rect()

        self.terrain_spritesheet = pygame.image.load(path.join(self.img_folder, 'terrain_spritesheet.png')).convert_alpha()
        self.icon_spritesheet_color = pygame.image.load(path.join(self.img_folder, 'icon_spritesheet_color.png')).convert_alpha()
        self.knotwork = pygame.image.load(path.join(self.img_folder, 'knotwork.png')).convert_alpha()

        sword_maiden = characters.Character(None, 'female', 7, 7, 0, 0, true_love=True)
        wizard = characters.Character(wizard=True)
        priest = characters.Character(priest=True)
        self.party.append(sword_maiden)
        self.party.append(wizard)
        self.party.append(priest)

        self.show_inventory_screen = False
        self.hunt_bonus = 0

    def initialize(self):
        self.console.clear_console()
        self.console.create_log()
        self.player = characters.Character('Cal Arath', 'male', 8, 9, 0, 2, randint(2,6), True)
        self.party = []
        self.lovers = []
        self.party.append(self.player)
        sword_maiden = characters.Character(None, 'female', 7, 7, 0, 0, true_love=True)
        self.party.append(sword_maiden)
        wizard = characters.Character(wizard=True)
        self.party.append(wizard)
        priest = characters.Character(priest=True)
        self.party.append(priest)
        self.player_hex = choice([(1,1),(7,1),(9,1),(13,1),(15,1),(18,1)])
        self.trackers = {'Day': 1, 'Party': len(self.party), 'Rations': 0, 'Gold': self.player.gold, 'Speed': min(char.move_speed for char in self.party)}
        self.hunt_bonus = 0

    '''The camera to follow the player as they move around the game map'''
    def camera_follow(self, player_rect):
        self.player_rect.center = hexagon_dict[self.player_hex]

        self.camera.centerx = player_rect.centerx
        self.camera.centery = player_rect.centery

        self.camera.x = max(0, min(self.camera.x, MAP_WIDTH - self.camera.width))
        self.camera.y = max(0, min(self.camera.y, MAP_HEIGHT - self.camera.height))

        if self.camera.right > MAP_WIDTH:
            self.camera.x -= self.camera.right - MAP_WIDTH
        if self.camera.bottom > MAP_HEIGHT:
            self.camera.y -= self.camera.bottom - MAP_HEIGHT

    '''This method determines which hex the mouse is hovering over or clicking in'''
    def hex_contains(self, point, hex_center):
        adjusted_point = (point[0] + self.camera.x, point[1] + self.camera.y)
        dx = adjusted_point[0] - hex_center[0]
        dy = adjusted_point[1] - hex_center[1]
        return abs(dy) <= HEX_RADIUS and abs(dx) <= HEX_SIDE_LENGTH / 2 and HEX_SIDE_LENGTH * abs(dy) + HEX_RADIUS * abs(dx) <= HEX_RADIUS * HEX_SIDE_LENGTH

    '''This method outlines a hex to highlight it'''
    def draw_outline(self, hex_center):
        pygame.draw.polygon(self.map_surface, outline_color, [
            (hex_center[0] + cos(angle) * (HEX_RADIUS + 2), hex_center[1] + sin(angle) * (HEX_RADIUS + 2))
            for angle in [0, pi / 3, 2 * pi / 3, pi, 4 * pi / 3, 5 * pi / 3]
        ], 4)

    '''This method determines if a hex is adjacent to the one the player is currently in'''
    def adjacent_hex(self, player_hex):
        adjacent_hexagons = []
        if player_hex[0] % 2 == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif i == -1 and j == -1:
                        continue
                    elif i == 1 and j == -1:
                        continue
                    neighbor_hex = (player_hex[0] + i, player_hex[1] + j)
                    if neighbor_hex in hexagon_dict:
                        adjacent_hexagons.append(neighbor_hex)
        elif player_hex[0] % 2 == 1:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif i == -1 and j == 1:
                        continue
                    elif i == 1 and j == 1:
                        continue
                    neighbor_hex = (player_hex[0] + i, player_hex[1] + j)
                    if neighbor_hex in hexagon_dict:
                        adjacent_hexagons.append(neighbor_hex)
        return adjacent_hexagons

    '''This handles mouse clicks, keystrokes, and other events'''
    def get_event(self, event):       
        if event.type == pygame.QUIT:
            self.quit = True

        if self.player.alive is False:
            self.console.display_message('Sadly, O Prince, your life and your quest end here.', True)
            if event.type == pygame.KEYDOWN:
                self.done = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] <= self.x * 0.75 and mouse_pos[1] <= self.y * 0.75:
                for hex_key, hex_center in hexagon_dict.items():
                    if self.hex_contains(mouse_pos, hex_center):
                        if hex_key in self.adjacent_hex(self.player_hex):
                            self.player_rect.center = hex_center
                            self.player_hex = hex_key
                            self.camera_follow(self.player_rect)
                            break

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] <= self.x * 0.75 and mouse_pos[1] <= self.y * 0.75:
                for hex_key, hex_center in hexagon_dict.items():
                    if self.hex_contains(mouse_pos, hex_center):
                        self.player_rect.center = hex_center
                        self.player_hex = hex_key
                        self.camera_follow(self.player_rect)
                        break

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DELETE:
                self.done = True
            if event.key == pygame.K_ESCAPE:
                self.quit = True
            if event.key == pygame.K_1:
                events.e057(self.party, self.console)
            if event.key == pygame.K_2:
                events.e032(self.party, self.console)
            if event.key == pygame.K_3:
                num_foes = 4
                foes = []
                for _ in range(num_foes):
                    foes.append(characters.Character(name='Orc Warrior', combat_skill=4, endurance=5, wealth_code=1))
                game_actions.combat(self.party, foes, self.console)
            if event.key == pygame.K_9:
                self.party[0].gold += 50
            if event.key == pygame.K_0:
                for char in self.party:
                    char.flying = True
        
        player_input = self.console.handle_input(event)

        self.daily_cycle(player_input)

        # if player_input in ['nw','n','ne','sw','s','se']:
        #     direction = player_input
        #     self.player_hex = game_actions.move(direction, self.player_hex, hexagon_dict, self.console)
        #     self.camera_follow(self.player_rect)
        #     self.location_message()
        #     #game_actions.encounter(self.player_hex, self.console)
        #     game_actions.hunt(self.party, self.player_hex, self.console, castles, temples, towns, deserts, mountains, farmlands)
        #     game_actions.eat_meal(self.party, self.player_hex, self.console, castles, temples, towns, deserts, oasis)
            
        #     self.count_rations()
        #     self.update_trackers()
        #     for character in self.party:
        #         character.update()
        #         if not character.alive and not character.heir:
        #             self.console.display_message(f'{character.name} has died!')
        #             self.party.remove(character)
        #     game_actions.true_love(self.party, self.lovers, self.console)

        # if player_input == 'i':
        #     self.show_inventory_screen = not self.show_inventory_screen

        # if player_input == 't':
        #     if self.player_hex in ruins:
        #         game_actions.search_ruins(self.party, self.player_hex, self.console)
        #         game_actions.hunt(self.party, self.player_hex, self.console, castles, temples, towns, deserts, mountains, farmlands)
        #         game_actions.eat_meal(self.party, self.player_hex, self.console, castles, temples, towns, deserts, oasis)
        #         self.count_rations()
        #         self.update_trackers()
        #         for character in self.party:
        #             character.update()
        #             if not character.alive and not character.heir:
        #                 self.console.display_message(f'{character.name} has died!')
        #                 self.party.remove(character)
        #         game_actions.true_love(self.party, self.lovers, self.console)

        # if player_input == 'r':
        #     game_actions.hunt(self.party, self.player_hex, self.console, castles, temples, towns, deserts, mountains, farmlands, game_actions.rest(self.party, self.player_hex, self.console))
        #     game_actions.eat_meal(self.party, self.player_hex, self.console, castles, temples, towns, deserts, oasis)
        #     self.count_rations()
        #     self.update_trackers()
        #     for character in self.party:
        #         character.update()
        #         if not character.alive and not character.heir:
        #             self.console.display_message(f'{character.name} has died!')
        #             self.party.remove(character)
        #     game_actions.true_love(self.party, self.lovers, self.console)

    '''This method counts the rations in the party and updates the tracker'''
    def count_rations(self):
        ration_count = 0
        for character in self.party:
            ration_count += character.possessions.count('ration')
        self.trackers['Rations'] = ration_count

    '''This method updates the Gold, Day, Party, and Item trackers'''
    def update_trackers(self):
        self.trackers['Gold'] = self.party[0].gold
        self.trackers['Day'] += 1
        self.trackers['Party'] = len(self.party)
        #self.trackers['Items'] = len(self.player.possessions)
        self.trackers['Speed'] = min(char.move_speed for char in self.party)

    '''This method draws each hexagon and then gives it a color, and image, and any icons it may have'''
    def draw_hexagon(self, surface, center, key):
        hexagon_points = []
        for i in range (6):
            angle = radians(60 * i)
            x = center[0] + HEX_RADIUS * cos(angle)
            y = center[1] + HEX_RADIUS * sin(angle)
            hexagon_points.append((x, y))

        if key in plains:
            terrain_color = plains_green
        elif key in farmlands:
            terrain_color =farmlands_brown
        elif key in forests:
            terrain_color = forests_green
        elif key in hills:
            terrain_color = hills_red
        elif key in mountains:
            terrain_color = mountains_gray
        elif key in deserts:
            terrain_color = deserts_yellow
        elif key in swamps:
            terrain_color = swamps_blue
        else:
            terrain_color = (0, 0, 0)

        pygame.draw.polygon(surface, terrain_color, hexagon_points)
        
        if key in plains:
            grass = self.get_terrain_image()
            surface.blit(grass, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
        elif key in farmlands:
            furrows = self.get_terrain_image(y=80)
            surface.blit(furrows, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
        elif key in forests:
            woods = self.get_terrain_image(y=160)
            surface.blit(woods, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
        elif key in hills:
            badlands = self.get_terrain_image(y=240)
            surface.blit(badlands, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
        elif key in mountains:
            peaks = self.get_terrain_image(y=320)
            surface.blit(peaks, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
        elif key in deserts:
            sand_dunes = self.get_terrain_image(y=400)
            surface.blit(sand_dunes, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
        elif key in swamps:
            mires = self.get_terrain_image(y=480)
            surface.blit(mires, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))

        if key in rivers:
            self.draw_river_segment(surface, hexagon_points, rivers[key])

        if key in roads:
            self.draw_road_segment(surface, center, roads[key])

        if key in oasis:
            image = self.icon_spritesheet_color.subsurface(pygame.Rect(0, 480, 80, 80))
            surface.blit(image, (center[0] - HEX_RADIUS * 1.1, center[1] - HEX_RADIUS * 0.65))

        if key in castles:
            self.get_icon_image(castles, key, center, surface)
        elif key in ruins:
            self.get_icon_image(ruins, key, center, surface)
        elif key in temples:
            self.get_icon_image(temples, key, center, surface)
        elif key in towns:
            self.get_icon_image(towns, key, center, surface)

        pygame.draw.polygon(surface, "red", hexagon_points, 2)

        text = self.font.render(f'{key[0]:02d}{key[1]:02d}', True, "red")
        text_rect = text.get_rect(center=(center[0], center[1] - (HEX_RADIUS * .5)))
        surface.blit(text, text_rect)

    '''This method creates the grid of hexagons and offsets each column so they align properly, it also creates the dict{}'''
    def draw_hex_grid(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                x_offset = col * (3/2) * HEX_RADIUS
                y_offset = row * HEX_SIDE_LENGTH
                if col % 2 == 1:
                    y_offset += HEX_SIDE_LENGTH / 2

                #key = f'{(col + 1):02d}{(row + 1):02d}'
                key = (col + 1, row + 1)
                hexagon_dict[key] = (HEX_RADIUS + x_offset, HEX_RADIUS + y_offset)
                self.draw_hexagon(surface, (HEX_RADIUS + x_offset, HEX_RADIUS + y_offset), key)

    '''This method gets the terrain image from the terrain spritesheet'''
    def get_terrain_image(self, x=0, y=0, w=80, h=80):
        image = self.terrain_spritesheet.subsurface(pygame.Rect(x, y, w, h))
        image = pygame.transform.scale(image, (HEX_RADIUS * 1.9, HEX_RADIUS * 1.9))
        return image
    
    '''This method gets the icon image and text for towns, temples, ruins, and castles'''
    def get_icon_image(self, dict, key, center, surface):
        icon = self.icon_spritesheet_color.subsurface(dict[key][1])
        self.font = pygame.font.Font(None, 16)
        icon_text = self.font.render(f'{dict[key][0]}', True, "red", "black")
        icon_text_rect = icon_text.get_rect(center=(center[0], center[1] - HEX_RADIUS * 0.1))
        surface.blit(icon, (center[0] - HEX_RADIUS * 0.6, center[1] - HEX_RADIUS * 0.25))
        surface.blit(icon_text, icon_text_rect)

    '''This method draws all river segments along the sides of a hex'''
    def draw_river_segment(self, surface, key, directions):
        for direction in directions:
            start = key[(direction - 1) % 6]
            end = key[(direction - 2) % 6]
            pygame.draw.line(surface, "blue", start, end, 16)
            pygame.draw.circle(surface, "blue", start, 8)
            pygame.draw.circle(surface, "blue", end, 8)

    '''This method draws all road segments within a hex'''
    def draw_road_segment(self, surface, key, directions):
        for direction in directions:
            start = key
            end = self.get_hex_side_center(key, direction)
            pygame.draw.line(surface, (120, 70, 40), start, end, 16)
            pygame.draw.circle(surface, (120, 70, 40), start, 8)
            pygame.draw.circle(surface, (120, 70, 40), end, 8)
    
    '''This method creates the end points for roads at the midpoint of one of the hex sides'''
    def get_hex_side_center(self, key, direction):
        angle = radians(60 * direction)
        x = key[0] + ((HEX_RADIUS * 0.9) * cos(angle + radians(-90)))
        y = key[1] + ((HEX_RADIUS * 0.9) * sin(angle + radians(-90)))
        return int(x), int(y)
 
    '''This method displays a message for the player when they arrive in a hex containing a feature'''
    def location_message(self):
        if self.player_hex in castles:
            self.console.display_message(f'You arrive at the imposing fortifications of {castles[self.player_hex][0]}')
        elif self.player_hex in towns:
            self.console.display_message(f'You arrive at the town of {towns[self.player_hex][0]}')
        elif self.player_hex in temples:
            self.console.display_message(f'You arrive at the holy site of {temples[self.player_hex][0]}')
        elif self.player_hex in ruins:
            self.console.display_message(f'You arrive at the desolate remnants of {ruins[self.player_hex][0]}')

    '''This method displays a message for the player on certain days'''
    def time_message(self):
        e001_text = "Evil events have overtaken your Northlands Kingdom. Your father, the old king, is dead - assassinated by rivals to the throne. These usurpers now hold the palace with their mercenary royal guard. You have escaped, and must collect 500 gold pieces to raise a force to smash them and retake your heritage. Furthermore, the usurpers have powerful friends overseas. If you can't return to take them out in ten weeks, their allies will arm and you will lose your kingdom forever. To escape the mercenary royal guard, your loyal body servant Ogab smuggled you into a merchant caravan to the southern border. Now, at dawn you roll out of the merchant wagons into a ditch, dust off your clothes, loosen your swordbelt, and get ready to start the first day of your adventure. Important Note: if you finish actions for a day on any hex north of the Tragoth River, the mercenary royal guardsmen may find you."
        day70_text = "Ten weeks have passed, and you have been unable to raise sufficient funds or forces to retake your kingdom.  Perhaps the fates may offer you another chance in the future, but for now you must remain in exile."

        if self.trackers["Day"] == 1:
            self.console.display_message(e001_text)
            self.location_message()
        
        if self.trackers["Day"] > 7 and (self.trackers["Day"] - 1) % 7 == 0:
            self.console.display_message(f'A week has passed. You have {10 - int((self.trackers["Day"] - 1) / 7)} weeks remaining.')
                
        if self.trackers["Day"] == 71:
            self.console.display_message(day70_text)

    '''This method draws all the map elements to the screen and highlights hexes adjacent to the player'''
    def draw(self, surface):
        self.map_surface.fill("black")
        self.draw_hex_grid(self.map_surface)

        for hex_center in hexagon_dict.values():
            pygame.draw.polygon(self.map_surface, (0, 0, 0), [
                (hex_center[0] + cos(angle) * HEX_RADIUS, hex_center[1] + sin(angle) * HEX_RADIUS)
                for angle in [0, pi / 3, 2 * pi / 3, pi, 4 * pi / 3, 5 * pi / 3]
            ], 1)

            if self.hex_contains(pygame.mouse.get_pos(), hex_center):
                self.draw_outline(hex_center)

        for neighbor in self.adjacent_hex(self.player_hex):
            if neighbor in hexagon_dict:
                self.draw_outline(hexagon_dict[neighbor])

        #player = pygame.draw.rect(self.map_surface, pygame.Color("red"), self.player_rect)
        self.map_surface.blit(self.player_icon, self.player_rect)
        self.camera_follow(self.player_rect)

        surface.blit(self.map_surface, self.map_surface_rect)
        surface.blit(self.map_surface.subsurface(self.camera), (0, 0))

        ### side info panel ###
        self.side_panel = pygame.Surface((self.x * 0.25, self.y * 0.75))
        self.side_panel.fill(parchment_color)
        surface.blit(self.side_panel, (self.x - self.x * 0.25, 0))
        self.sp_rect = pygame.draw.rect(surface, "black", (self.x - self.x * 0.25, 0, self.x - self.x * 0.75, (self.y - self.y * 0.25) + 20), 20)
        surface.blit(self.knotwork, (self.x - self.x * 0.25, 0))

        y_coord = 110
        for key, value in self.trackers.items():
            tracker_font = pygame.font.Font(pygame.font.match_font('couriernew', True), 36)
            tracker_text = tracker_font.render(f'{key:<7}: {value:>3}', True, [80, 80, 80])
            surface.blit(tracker_text, (self.x - self.x * 0.22, y_coord))
            y_coord += tracker_font.get_linesize()
        y_coord += 20
        char_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 16)
        attribute_y_coord = y_coord
        for attribute in self.player.__str__():
            if attribute != self.player.title:
                char_text = char_font.render(attribute, True, [80, 80, 80])
                surface.blit(char_text, (self.x - self.x * 0.22, attribute_y_coord))
                attribute_y_coord += char_font.get_linesize()
        item_y_coord = y_coord
        for item in self.player.possessions:
            item_text = char_font.render(f'{item.title()}', True, [80, 80, 80])
            surface.blit(item_text, (self.x - self.x * 0.11, item_y_coord))
            item_y_coord += char_font.get_linesize()
        character_y_coord = attribute_y_coord + 20
        party_text = char_font.render('Party Members:', True, [80, 80, 80])
        surface.blit(party_text, (self.x - self.x * 0.22, character_y_coord))
        character_y_coord += char_font.get_linesize()
        for character in self.party[1:]:
            character_text = char_font.render(f'{character.name} ({len(character.possessions)}/{character.max_carry})', True, [80, 80, 80])
            surface.blit(character_text, (self.x - self.x * 0.22, character_y_coord))
            character_y_coord += char_font.get_linesize()


        ### party stats and inventory screen ###
        if self.show_inventory_screen:
            inventory_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 16)
            self.inventory_screen = pygame.Surface((self.x * 0.75, self.y * 0.75))
            self.inventory_screen.fill(parchment_color)
            surface.blit(self.inventory_screen, (0, 0))
            x_coord, y_coord = 20, 20
            for character in self.party:
                attribute_y_coord = y_coord
                for attribute in character.__str__():
                    char_text = inventory_font.render(attribute, True, [80, 80, 80])
                    surface.blit(char_text, (x_coord, attribute_y_coord))
                    attribute_y_coord += inventory_font.get_linesize()
                item_y_coord = attribute_y_coord
                item_counts = {}
                for item in character.possessions:
                    item_counts[item] = item_counts.get(item, 0) + 1
                for item, count in item_counts.items():
                    if count > 1:
                        item_text = inventory_font.render(f'{item.title()} x {count}', True, [80, 80, 80])
                    else:
                        item_text = inventory_font.render(f'{item.title()}', True, [80, 80, 80])
                    surface.blit(item_text, (x_coord, item_y_coord))
                    item_y_coord += inventory_font.get_linesize()
                x_coord += 150
        
        '''black border for console panel'''
        pygame.draw.rect(surface, "black", (0, self.y - self.y * 0.25, self.x, self.y - self.y * 0.75), 20)
        # self.knotwork = pygame.transform.scale(self.knotwork, (636, 84))
        # surface.blit(self.knotwork, (0, self.y - 84))

        self.time_message()        
        self.console.render()


    '''This method handles the daily cycle of game play (choose actions, encounters, hunt, eat meals, etc.)'''
    def daily_cycle(self, player_input):
        if player_input in ['nw','n','ne','sw','s','se','i','t','r','o','p','h','q','c']:
            daily_action_done = False
            if not daily_action_done:
                ### morning ###
                daily_action_done = self.choose_daily_action(player_input)

            if daily_action_done:
                ### afternoon ###
                game_actions.hunt(self.party, self.player_hex, self.console, castles, temples, towns, deserts, mountains, farmlands, self.hunt_bonus)

                ### evening ###
                game_actions.eat_meal(self.party, self.player_hex, self.console, castles, temples, towns, deserts, oasis)

                ### daily updates ###
                self.count_rations()
                self.update_trackers()
                for character in self.party:
                    character.update()
                    if not character.alive and not character.heir:
                            self.console.display_message(f'{character.name} has died!')
                            self.party.remove(character)
                game_actions.true_love(self.party, self.lovers, self.console)


    '''This method handles the choice of action in the daily cycle'''
    def choose_daily_action(self, player_input):
        if player_input in ['nw','n','ne','sw','s','se']:
            direction = player_input
            self.player_hex = game_actions.move(direction, self.player_hex, hexagon_dict, self.console)
            self.camera_follow(self.player_rect)
            self.location_message()
            return True
            
            
        if player_input == 'i':
            self.show_inventory_screen = not self.show_inventory_screen
            return False

        if player_input == 't':
            if self.player_hex in ruins:
                game_actions.search_ruins(self.party, self.player_hex, self.console)
                return True
            return False            

        if player_input == 'r':
            self.hunt_bonus = game_actions.rest(self.party, self.player_hex, self.console)
            return True
            
        if player_input == 'o':
            if self.player_hex in temples:
                game_actions.make_offering(self.party, self.player_hex, self.console)
                return True
            return False
        
        if player_input == 'p':
            if any(self.player_hex in key for key in [temples, towns, castles]):
                game_actions.seek_audience(self.party, self.player_hex, self.console)
                return True
            return False
        
        if player_input == 'h':
            if any(self.player_hex in key for key in [towns, castles]):
                game_actions.hire_followers(self.party, self.player_hex, self.console)
                return True
            return False
        
        if player_input == 'q':
            if any(self.player_hex in key for key in [temples, towns, castles]):
                game_actions.seek_news_and_information(self.party, self.player_hex, self.console)
                return True
            return False
        
        if player_input == 'c':
            if 'cache' in self.player_hex:
                game_actions.cache_locate()
                return True
            else:
                game_actions.cache_place()
                return True