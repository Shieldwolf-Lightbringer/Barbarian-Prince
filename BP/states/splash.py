import pygame
from .base import BaseState
from os import path


class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        self.font = pygame.font.Font(None, 128)
        self.title = self.font.render("BARBARIAN PRINCE", True, pygame.Color("red"))
        self.title_rect = self.title.get_rect(center=[self.screen_rect.centerx, 200])
        self.next_state = "MENU"
        self.time_active = 0
        self.establish_data_path() # this uses the method from the base class, so creates the paths to the asset folders

        self.background_img = pygame.image.load(path.join(self.img_folder, 'background.jpg')).convert_alpha()
        self.background_img = pygame.transform.scale(self.background_img, (self.x, self.y + 120))
        self.background_img_rect = self.background_img.get_rect(center=self.screen_rect.center)

        self.title_img = pygame.image.load(path.join(self.img_folder, 'bp_cover.png')).convert_alpha()
        self.title_img = pygame.transform.scale2x(self.title_img)
        self.title_img_rect = self.title_img.get_rect(center=(self.x / 4, self.y * .6))#(center=self.screen_rect.center)
        self.title_img2 = pygame.transform.flip(self.title_img, True, False)
        self.title_img_rect2 = self.title_img.get_rect(center=(self.x * .75, self.y * .6))

    # def startup(self, persistent):
    #     self.persist = persistent
    
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
            else:
                self.done = True

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 2500:
            self.done = True

    def draw(self, surface):
        # surface.fill(pygame.Color("red"))
        # self.rect = pygame.Rect((25, 25), (1390, 850))
        # self.rect.center = self.screen_rect.center
        # pygame.draw.rect(surface, pygame.Color('black'), self.rect)
        surface.blit(self.background_img, (0,0)) #self.background_img_rect)
        surface.blit(self.title_img, self.title_img_rect)
        surface.blit(self.title_img2, self.title_img_rect2)
        surface.blit(self.title, self.title_rect)