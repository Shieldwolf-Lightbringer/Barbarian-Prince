import pygame
import events
import game_actions
import stack_map_generator
from characters import Character
from game_console import Console
from random import choice, randint
from states.stack_base_state import BaseState
from states.stack_pause_menu import PauseMenu

class GameWorld(BaseState):
    def __init__(self, game):
        BaseState.__init__(self, game)
        self.console_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 16)
        self.console = Console(self.game.game_canvas, self.console_font, 1.0, 0.25)
        self.player = Character(name='Cal Arath', sex='male', combat_skill=8, endurance=9, wealth_code=2, wits=randint(2,6), heir=True)
        self.party = []
        self.lovers = []
        self.party.append(self.player)
        self.trackers = {'Day': 1, 'Party': len(self.party), 'Rations': 0, 'Gold': self.player.gold, 'Speed': min(char.move_speed for char in self.party)}
        self.victory = False
        self.hunt_bonus = 0
        self.map = stack_map_generator.HexMap(self.game)
        self.player_hex = self.map.player_hex

        sword_maiden = Character(title='Swordmaiden', sex='female', combat_skill=7, endurance=7, true_love=True)
        wizard = Character(title= 'Wizard', wizard=True)
        priest = Character(title= 'Priest', priest=True)
        self.party.append(sword_maiden)
        self.party.append(wizard)
        self.party.append(priest)
        # self.player = Player(self.game)
        # self.grass_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "grass.png"))
        #self.grass_img = pygame.transform.scale(self.grass_img, (self.game.GAME_W, self.game.GAME_H))

    def update(self, delta_time, actions):
        # Check if the game was paused 
        if actions["space"]:
            new_state = PauseMenu(self.game, self.party)
            new_state.enter_state()
        # self.player.update(delta_time, actions)

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

    '''This method displays a message for the player when they arrive in a hex containing a feature'''
    def location_message(self):
        if self.player_hex in stack_map_generator.castles:
            self.console.display_message(f'You arrive at the imposing fortifications of {stack_map_generator.castles[self.player_hex][0]}. You may (h)ire followers, (p)etition for audience, or (q)uery news.')
        elif self.player_hex in stack_map_generator.towns:
            self.console.display_message(f'You arrive at the town of {stack_map_generator.towns[self.player_hex][0]}. You may (h)ire followers, (p)etition for audience, or (q)uery news.')
        elif self.player_hex in stack_map_generator.temples:
            self.console.display_message(f'You arrive at the holy site of {stack_map_generator.temples[self.player_hex][0]}.  You may make an (o)ffering, (p)etition for audience, or (q)uery news.')
        elif self.player_hex in stack_map_generator.ruins:
            self.console.display_message(f'You arrive at the desolate remnants of {stack_map_generator.ruins[self.player_hex][0]}. You may search for (t)reasure here.')

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

    '''This method renders the side information panel'''
    def render_side_panel(self, surface):
        self.side_panel = pygame.Surface((self.game.GAME_W * 0.25, self.game.GAME_H * 0.75))
        self.side_panel.fill(self.map.color_dict['parchment'])
        surface.blit(self.side_panel, (self.game.GAME_W - self.game.GAME_W * 0.25, 0))
        self.sp_rect = pygame.draw.rect(surface, "black", (self.game.GAME_W - self.game.GAME_W * 0.25, 0, self.game.GAME_W - self.game.GAME_W * 0.75, (self.game.GAME_H - self.game.GAME_H * 0.25) + 20), 20)
        #surface.blit(self.knotwork, (self.x - self.x * 0.25, 0))

        y_coord = 110
        for key, value in self.trackers.items():
            tracker_font = pygame.font.Font(pygame.font.match_font('couriernew', True), 36)
            tracker_text = tracker_font.render(f'{key:<7}: {value:>3}', True, [80, 80, 80])
            surface.blit(tracker_text, (self.game.GAME_W - self.game.GAME_W * 0.22, y_coord))
            y_coord += tracker_font.get_linesize()
        y_coord += 20
        char_font = pygame.font.Font(pygame.font.match_font('papyrus', True), 16)
        attribute_y_coord = y_coord
        for attribute in self.player.__str__():
            if attribute != self.player.title:
                char_text = char_font.render(attribute, True, [80, 80, 80])
                surface.blit(char_text, (self.game.GAME_W - self.game.GAME_W * 0.22, attribute_y_coord))
                attribute_y_coord += char_font.get_linesize()
        item_y_coord = y_coord
        for item in self.player.possessions:
            item_text = char_font.render(f'{item.title()}', True, [80, 80, 80])
            surface.blit(item_text, (self.game.GAME_W - self.game.GAME_W * 0.11, item_y_coord))
            item_y_coord += char_font.get_linesize()
        character_y_coord = attribute_y_coord + 20
        party_text = char_font.render('Party Members:', True, [80, 80, 80])
        surface.blit(party_text, (self.game.GAME_W - self.game.GAME_W * 0.22, character_y_coord))
        character_y_coord += char_font.get_linesize()
        for character in self.party[1:]:
            character_text = char_font.render(f'{character.name} ({character.total_wounds}/{character.endurance})', True, [80, 80, 80])
            surface.blit(character_text, (self.game.GAME_W - self.game.GAME_W * 0.22, character_y_coord))
            character_y_coord += char_font.get_linesize()


    def render(self, display):
        # screen_width, screen_height = display.get_size()
        # grass_width, grass_height = self.grass_img.get_size()

        # for y in range(0, screen_height, grass_height):
        #     for x in range(0, screen_width, grass_width):
        #         display.blit(self.grass_img, (x, y))
        
        # self.player.render(display)
        self.map.draw_map(display)

        ### side info panel ###
        self.render_side_panel(display)
        # self.side_panel = pygame.Surface((self.game.GAME_W * 0.25, self.game.GAME_H * 0.75))
        # self.side_panel.fill(self.map.color_dict['parchment'])
        # display.blit(self.side_panel, (self.game.GAME_W - self.game.GAME_W * 0.25, 0))
        # self.sp_rect = pygame.draw.rect(display, "black", (self.game.GAME_W - self.game.GAME_W * 0.25, 0, self.game.GAME_W - self.game.GAME_W * 0.75, (self.game.GAME_H - self.game.GAME_H * 0.25) + 20), 20)
        # #surface.blit(self.knotwork, (self.game.GAME_W - self.game.GAME_W * 0.25, 0))

        '''black border for console panel'''
        pygame.draw.rect(display, "black", (0, self.game.GAME_H - self.game.GAME_H * 0.25, self.game.GAME_W, self.game.GAME_H - self.game.GAME_H * 0.75), 20)
        # self.knotwork = pygame.transform.scale(self.knotwork, (636, 84))
        # surface.blit(self.knotwork, (0, self.y - 84))

        self.time_message()        
        self.console.render_area(display)
        self.console.render_text(display)
        

# class Player():
#     def __init__(self,game):
#         self.game = game
#         self.load_sprites()
#         self.position_x, self.position_y = 200,200
#         self.current_frame, self.last_frame_update = 0,0
        

#     def update(self,delta_time, actions):
#         # Get the direction from inputs
#         direction_x = actions["right"] - actions["left"]
#         direction_y = actions["down"] - actions["up"]
#         # Update the position
#         self.position_x += 100 * delta_time * direction_x
#         self.position_y += 100 * delta_time * direction_y
#         # Animate the sprite
#         self.animate(delta_time,direction_x,direction_y)


#     def render(self, display):
#         display.blit(self.curr_image, (self.position_x,self.position_y))

#     def animate(self, delta_time, direction_x, direction_y):
#         # Compute how much time has passed since the frame last updated
#         self.last_frame_update += delta_time
#         # If no direction is pressed, set image to idle and return
#         if not (direction_x or direction_y): 
#             self.curr_image = self.curr_anim_list[0]
#             return
#         # If an image was pressed, use the appropriate list of frames according to direction
#         if direction_x:
#             if direction_x > 0: self.curr_anim_list = self.right_sprites
#             else: self.curr_anim_list = self.left_sprites
#         if direction_y:
#             if direction_y > 0: self.curr_anim_list = self.front_sprites
#             else: self.curr_anim_list = self.back_sprites
#         # Advance the animation if enough time has elapsed
#         if self.last_frame_update > .15:
#             self.last_frame_update = 0
#             self.current_frame = (self.current_frame +1) % len(self.curr_anim_list)
#             self.curr_image = self.curr_anim_list[self.current_frame]

#     def load_sprites(self):
#         # Get the diretory with the player sprites
#         self.sprite_dir = os.path.join(self.game.sprite_dir, "player")
#         self.front_sprites, self.back_sprites, self.right_sprites, self.left_sprites = [],[],[],[]
#         # Load in the frames for each direction
#         for i in range(1,5):
#             self.front_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_front" + str(i) +".png")))
#             self.back_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_back" + str(i) +".png")))
#             self.right_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_right" + str(i) +".png")))
#             self.left_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_left" + str(i) +".png")))
#         # Set the default frames to facing front
#         self.curr_image = self.front_sprites[0]
#         self.curr_anim_list = self.front_sprites