import sys
import pygame
import random
from states.menu import Menu
from states.gameplay import Gameplay
from states.game_over import GameOver
from states.splash import Splash
from game import Game

pygame.init()
info = pygame.display.Info()
monitor_width = info.current_w
monitor_height = info.current_h

screen = pygame.display.set_mode((monitor_width, monitor_height))#((1440, 900))  # main monitor resolution
states = {
     "MENU": Menu(),
     "SPLASH": Splash(),
     "GAMEPLAY": Gameplay(),
     "GAME_OVER": GameOver(),
}

if __name__ == '__main__':
    game = Game(screen, states, "SPLASH")
    game.run()
    pygame.quit()
    sys.exit()


# names_list = ['Wolf', 'Mercenary', 'Peasant', 'Bandit', 'Goblin', 'Dwarf', 'Elf', 'Halfling', 'Amazon',
#               'Witch', 'Monk', 'Magician', 'Priest', 'Sprite', 'Orc', 'Sorcerer', 'Swordsman', 'Gnome', 'Barbarian']

# class Character:
# 	def __init__(self, Name=None, Combat_skill=None, Endurance=None, Wounds=None, Wealth=None):
# 		self.Name = Name if Name else f"{random.choice(names_list):^9}"
# 		self.Combat_skill = Combat_skill if Combat_skill else d6(1)
# 		self.Endurance = Endurance if Endurance else random.randint(2,6)
# 		self.Wounds = Wounds if Wounds else 0
# 		self.Wealth = Wealth if Wealth else d6(2) - 2


# class Player(Character):
#     def __init__(self, Name, Combat_skill, Endurance, Wounds, Wealth=None, Wits=None):
#         super().__init__(Name, Combat_skill, Endurance, Wounds, Wealth=None)
#         self.Name = Name if Name else "Cal Arath"
#         self.Wealth = Wealth if Wealth else random.randint(0,4)	
#         self.Wits = Wits if Wits else random.randint(2,6)

# def title_plate():
#     title = "BARBARIAN PRINCE"
#     decor = '%-' * len(title)
#     print(f'{decor}%\n%{title:^31}%\n{decor}%')
	
# # title_plate()

# def intro():
#     title_plate()
#     print('''\nEvil events have overtaken your Northlands Kingdom.\n
# Your father, the old king, is dead -- assassinated by rivals to the throne. These usurpers now hold the palace with their mercenary royal guard.
# To escape the mercenary royal guard, your loyal body servant Ogab smuggled you into a merchant caravan to the southern border.
# You have escaped, and must now collect 500 gold pieces to raise a force to smash them and retake your heritage.\n
# However, these usurpers have powerful friends overseas.
# If you cannot return to destroy them within ten weeks; their allies will arm, and you will lose your kingdom forever.''')
#     name = input("\nWhat is thy name, O Prince?: ")
#     prince = Player(name, 8, 9, 0)
#     print(f"\n{vars(prince)}")

# # intro()

# def d6(num_dice):
#     total_sum = 0
#     for die in range(num_dice):
#         total_sum += random.randint(1, 6)
#     return total_sum

# d6(2)

# if __name__ == '__main__':
#     #  intro()
#     #  for i in range(3):
#     #       foe = Character()
#     #       print(f"\n{vars(foe)}")
#     game = Game(screen, states, "SPLASH")
#     game.run()

#     pygame.quit()
#     sys.exit()