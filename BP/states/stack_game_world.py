import pygame
import os
import stack_map_generator
from states.stack_base_state import BaseState
from states.stack_pause_menu import PauseMenu

class GameWorld(BaseState):
    def __init__(self, game):
        BaseState.__init__(self, game)
        self.player = Player(self.game)
        self.grass_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "grass.png"))
        #self.grass_img = pygame.transform.scale(self.grass_img, (self.game.GAME_W, self.game.GAME_H))
        self.map = stack_map_generator.HexMap(self.game)

    def update(self,delta_time, actions):
        # Check if the game was paused 
        if actions["start"]:
            new_state = PauseMenu(self.game)
            new_state.enter_state()
        self.player.update(delta_time, actions)
        
    def render(self, display):
        screen_width, screen_height = display.get_size()
        grass_width, grass_height = self.grass_img.get_size()

        for y in range(0, screen_height, grass_height):
            for x in range(0, screen_width, grass_width):
                display.blit(self.grass_img, (x, y))
        
        self.player.render(display)
        self.map.create_map(display)
        

class Player():
    def __init__(self,game):
        self.game = game
        self.load_sprites()
        self.position_x, self.position_y = 200,200
        self.current_frame, self.last_frame_update = 0,0
        

    def update(self,delta_time, actions):
        # Get the direction from inputs
        direction_x = actions["right"] - actions["left"]
        direction_y = actions["down"] - actions["up"]
        # Update the position
        self.position_x += 100 * delta_time * direction_x
        self.position_y += 100 * delta_time * direction_y
        # Animate the sprite
        self.animate(delta_time,direction_x,direction_y)


    def render(self, display):
        display.blit(self.curr_image, (self.position_x,self.position_y))

    def animate(self, delta_time, direction_x, direction_y):
        # Compute how much time has passed since the frame last updated
        self.last_frame_update += delta_time
        # If no direction is pressed, set image to idle and return
        if not (direction_x or direction_y): 
            self.curr_image = self.curr_anim_list[0]
            return
        # If an image was pressed, use the appropriate list of frames according to direction
        if direction_x:
            if direction_x > 0: self.curr_anim_list = self.right_sprites
            else: self.curr_anim_list = self.left_sprites
        if direction_y:
            if direction_y > 0: self.curr_anim_list = self.front_sprites
            else: self.curr_anim_list = self.back_sprites
        # Advance the animation if enough time has elapsed
        if self.last_frame_update > .15:
            self.last_frame_update = 0
            self.current_frame = (self.current_frame +1) % len(self.curr_anim_list)
            self.curr_image = self.curr_anim_list[self.current_frame]

    def load_sprites(self):
        # Get the diretory with the player sprites
        self.sprite_dir = os.path.join(self.game.sprite_dir, "player")
        self.front_sprites, self.back_sprites, self.right_sprites, self.left_sprites = [],[],[],[]
        # Load in the frames for each direction
        for i in range(1,5):
            self.front_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_front" + str(i) +".png")))
            self.back_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_back" + str(i) +".png")))
            self.right_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_right" + str(i) +".png")))
            self.left_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_left" + str(i) +".png")))
        # Set the default frames to facing front
        self.curr_image = self.front_sprites[0]
        self.curr_anim_list = self.front_sprites