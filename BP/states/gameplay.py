import pygame
from .base import BaseState
from os import path
from math import cos, sin, pi, sqrt, radians
from random import randint

ROWS = 23
COLUMNS = 20
HEX_RADIUS = 60  # if below 60, subsurface outside surface area
HEX_SIDE_LENGTH = int(HEX_RADIUS * sqrt(3))
MAP_WIDTH = (HEX_RADIUS * 3/2) * COLUMNS + (HEX_RADIUS * .55)
MAP_HEIGHT = (HEX_RADIUS * 2) * (ROWS - 3) + (HEX_RADIUS * .70)
hexagon_dict = {}
outline_color = (255, 255, 0)
# plains = ['0101','0102','0104','0108','0109','0110','0112','0113','0119','0120','0121','0122',
#           '0208','0209','0210','0211','0212','0219','0223',
#           '0305','0308','0311','0316','0318','0320','0321',
#           '0410','0412','0413','0415','0416','0417',
#           '0502','0507',
#           '0601','0602','0604',
#           '0701','0702','0704']
plains = [(1,1),(1,2),(1,4),(1,8),(1,9),(1,10),(1,12),(1,13),(1,19),(1,20),(1,21),(1,22)]
plains_green = (217, 217, 90)
farmlands = []
forests = []
hills = []
#mountains = ['0103','0201','0301','0304','0403','0404','0405','0503','0504','0603','0703']
mountains = [(1,3),(2,1),(3,1),(3,4),(4,3),(4,4),(4,5),(5,3),(5,4),(6,3),(7,3)]
mountains_gray = (208, 200, 224)
deserts = [(1,6),(2,6),(3,6),(4,7),(13,8),(13,9),(14,8),(14,9),(15,7),(15,8),(15,9),(15,10),
           (16,6),(16,7),(16,8),(16,9),(17,7),(17,8),(17,10)]
deserts_yellow = (236, 236, 198)
swamps = []


class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.player_rect = pygame.Rect((0, 0), (HEX_RADIUS/2, HEX_RADIUS/2))
        self.player_rect.center = (HEX_RADIUS, HEX_RADIUS) #self.screen_rect.center
        self.player_hex = (1,1)
        self.camera = pygame.Rect((0, 0), (self.x, self.y))
        self.next_state = "GAME_OVER"
        self.load_data()

        self.map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
        self.map_surface_rect = self.map_surface.get_rect()

        self.terrain_spritesheet = pygame.image.load(path.join(self.img_folder, 'terrain_spritesheet.png')).convert_alpha()
        # self.grass = pygame.image.load(path.join(self.img_folder, 'grass_texture.png')).convert_alpha()
        # self.grass = pygame.transform.scale(self.grass, (HEX_RADIUS * 2, HEX_RADIUS * 2))
        # self.sand_dunes = pygame.image.load(path.join(self.img_folder, 'hills.png')).convert_alpha()
        # self.sand_dunes = pygame.transform.scale(self.sand_dunes, (HEX_RADIUS * 2, HEX_RADIUS * 2))
        

    def camera_follow(self, player_rect):
        self.player_rect.center = hexagon_dict[self.player_hex]
        # distance_to_left = player_rect.left
        # distance_to_right = self.x - player_rect.right
        # distance_to_top = player_rect.top
        # distance_to_bottom = self.y - player_rect.bottom

        # if (distance_to_left < 3 * HEX_SIDE_LENGTH / 2 or
        #     distance_to_right < 3 * HEX_SIDE_LENGTH / 2 or
        #     distance_to_top < 3 * HEX_RADIUS or
        #     distance_to_bottom < 3 * HEX_RADIUS
        #    ):

        self.camera.centerx = player_rect.centerx
        self.camera.centery = player_rect.centery

        self.camera.x = max(0, min(self.camera.x, MAP_WIDTH - self.camera.width))
        self.camera.y = max(0, min(self.camera.y, MAP_HEIGHT - self.camera.height))

        if self.camera.right > MAP_WIDTH:
            self.camera.x -= self.camera.right - MAP_WIDTH
        if self.camera.bottom > MAP_HEIGHT:
            self.camera.y -= self.camera.bottom - MAP_HEIGHT

    def hex_contains(self, point, hex_center):
        adjusted_point = (point[0] + self.camera.x, point[1] + self.camera.y)
        dx = adjusted_point[0] - hex_center[0]
        dy = adjusted_point[1] - hex_center[1]
        return abs(dy) <= HEX_RADIUS and abs(dx) <= HEX_SIDE_LENGTH / 2 and HEX_SIDE_LENGTH * abs(dy) + HEX_RADIUS * abs(dx) <= HEX_RADIUS * HEX_SIDE_LENGTH

    def draw_outline(self, hex_center):
        pygame.draw.polygon(self.map_surface, outline_color, [
            (hex_center[0] + cos(angle) * (HEX_RADIUS + 2), hex_center[1] + sin(angle) * (HEX_RADIUS + 2))
            for angle in [0, pi / 3, 2 * pi / 3, pi, 4 * pi / 3, 5 * pi / 3]
        ], 4)

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

    def get_event(self, event):
        if self.player_hex[0] % 2 == 0:
            dir = {
                pygame.K_q: (-1, +0),
                pygame.K_w: (+0, -1),
                pygame.K_e: (+1, +0),
                pygame.K_a: (-1, +1),
                pygame.K_s: (+0, +1),
                pygame.K_d: (+1, +1)
                }
        elif self.player_hex[0] % 2 == 1:
            dir = {
                pygame.K_q: (-1, -1),
                pygame.K_w: (+0, -1),
                pygame.K_e: (+1, -1),
                pygame.K_a: (-1, +0),
                pygame.K_s: (+0, +1),
                pygame.K_d: (+1, +0)
                }
        
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for hex_key, hex_center in hexagon_dict.items():
                if self.hex_contains(mouse_pos, hex_center):
                    if hex_key in self.adjacent_hex(self.player_hex):
                        self.player_rect.center = hex_center
                        self.player_hex = hex_key
                        self.camera_follow(self.player_rect)
                        break

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = pygame.mouse.get_pos()
            for hex_key, hex_center in hexagon_dict.items():
                if self.hex_contains(mouse_pos, hex_center):
                    self.player_rect.center = hex_center
                    self.player_hex = hex_key
                    self.camera_follow(self.player_rect)
                    break

        elif event.type == pygame.KEYUP:
            if event.key in dir:
                v = dir[event.key]
                if (self.player_hex[0] + v[0], self.player_hex[1] + v[1]) in hexagon_dict:
                    self.player_hex = (self.player_hex[0] + v[0], self.player_hex[1] + v[1])
                    self.camera_follow(self.player_rect)
                else:
                    self.player_hex = self.player_hex
                    self.camera_follow(self.player_rect)
            
            elif event.key == pygame.K_SPACE:
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True


    def draw_hexagon(self, surface, center, key, spritesheet=None):
        hexagon_points = []
        for i in range (6):
            angle = radians(60 * i)
            x = center[0] + HEX_RADIUS * cos(angle)
            y = center[1] + HEX_RADIUS * sin(angle)
            hexagon_points.append((x, y))

        if key in plains:
            terrain_color = plains_green
        elif key in farmlands:
            pass
        elif key in forests:
            pass
        elif key in hills:
            pass
        elif key in mountains:
            terrain_color = mountains_gray
        elif key in deserts:
            terrain_color = deserts_yellow
        elif key in swamps:
            pass
        else:
            terrain_color = (0, 0, 0)

        pygame.draw.polygon(surface, terrain_color, hexagon_points)
        
        if key in plains:
            grass = self.terrain_spritesheet.subsurface(pygame.Rect(0, 0, 80, 80))
            grass = pygame.transform.scale(grass, (HEX_RADIUS * 1.9, HEX_RADIUS * 1.9))
            surface.blit(grass, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
        elif key in mountains:
            peaks = self.terrain_spritesheet.subsurface(pygame.Rect(0, 320, 80, 80))
            peaks = pygame.transform.scale(peaks, (HEX_RADIUS * 1.9, HEX_RADIUS * 1.9))
            surface.blit(peaks, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
        elif key in deserts:
            sand_dunes = self.terrain_spritesheet.subsurface(pygame.Rect(0, 400, 80, 80))
            sand_dunes = pygame.transform.scale(sand_dunes, (HEX_RADIUS * 1.9, HEX_RADIUS * 1.9))
            surface.blit(sand_dunes, (center[0] - HEX_RADIUS * 0.95, center[1] - HEX_RADIUS * 0.95))
            # sand_dunes = pygame.image.load(path.join(self.img_folder, 'hills.png')).convert_alpha()
            # sand_dunes = pygame.transform.scale(sand_dunes, (HEX_RADIUS * 1.5, HEX_RADIUS * 1.5))
            # surface.blit(sand_dunes, (center[0] - HEX_RADIUS * 0.75, center[1] - HEX_RADIUS * 0.75))

        
        '''
        if spitesheet:
            image_rect = spritesheet.get_rect()
            image_rect.center = center
            surface.blit(spritesheet, image_rect.topleft)
        '''

        pygame.draw.polygon(surface, "red", hexagon_points, 2)

        text = self.font.render(f'{key[0]:02d}{key[1]:02d}', True, "red")
        text_rect = text.get_rect(center=(center[0], center[1] - (HEX_RADIUS * .5)))
        surface.blit(text, text_rect)

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

    def draw(self, surface):
        # surface.fill(pygame.Color("black"))
        # surface.blit(self.map_img, self.map_img_rect)

        # self.draw_regular_polygon(surface, "black", 6, 80, (544, 493))
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

        pygame.draw.rect(self.map_surface, pygame.Color("red"), self.player_rect)

        surface.blit(self.map_surface, self.map_surface_rect)
        surface.blit(self.map_surface.subsurface(self.camera), (0, 0))


        