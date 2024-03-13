import pygame
from random import randint, choice

class Character:
    def __init__(self, name=None, sex=None, combat_skill=None, endurance=None, wounds=0, wealth_code=0, wits=None, heir=False,
                 daily_wage=0, guide=False, priest=False, monk=False, magician=False, wizard=False, witch=False, true_love=False,
                 mounted=False, flying=False, unearthly=False, regenerates=False):
        self.name = name if name else self.random_name()
        self.sex = sex if sex else choice(['male', 'female'])
        self.combat_skill = combat_skill if combat_skill else randint(1,5)
        self.fatigue = 0
        self.endurance = endurance if endurance else max((self.combat_skill + randint(0,2)), 2)
        self.wounds = wounds
        self.poison_wounds = wounds
        self.possessions = []
        self.max_carry = 10
        self.wits = wits if wits else 0
        self.wits_bonus = 0
        self.heir = heir
        self.gold = 0
        self.wealth_code = wealth_code
        self.determine_wealth(wealth_code)
        self.alive = True
        self.awake = True
        self.has_eaten = False
        self.loyalty = 4
        self.daily_wage = daily_wage
        self.guide = guide
        self.priest = priest
        self.monk = monk
        self.magician = magician
        self.wizard = wizard
        self.witch = witch
        self.magical = False
        if any([self.priest, self.monk, self.magician, self.wizard, self.witch]):
            self.magical = True
        self.true_love = true_love
        if self.true_love:
            self.loyalty = 20
        self.plague = False
        self.mindless = False
        self.move_speed = 1
        self.mounted = mounted
        self.flying = flying
        if self.heir:
            self.audience_bonus = {}
            self.hiring_bonus = {}
            self.info_bonus = {}
            self.offering_bonus = {}
            self.food_mod = {}
            self.room_mod = {}
        self.unearthly = unearthly
        self.regenerates = regenerates
        self.update()
        
    def determine_wealth(self, wealth_code):
        wealth_dice = randint(0,5)
        if isinstance(treasure_table[wealth_code][wealth_dice], list):
            gold_value = treasure_table[wealth_code][wealth_dice][0]
            item_row = treasure_table[wealth_code][wealth_dice][1]
            item_dice = randint(0,5)
            self.add_item(item_table[item_row][item_dice])
            self.gold += gold_value
        else:
            self.gold += treasure_table[wealth_code][wealth_dice]
        if self.gold > 0:
            self.add_item('pouch of gold')

    def random_name(self):
        syllables = ['a','aa','ad','ae','al','am','an','ar','at','ay','az',
                     'b','ba','be','bi','bo','bu',
                     'c','ca','ce','ck','co','cu','cy',
                     'd','da','de','di','do','du','dy',
                     'e','ee','ed','el','em','en','er','ex','ey','ez',
                     'f','fa','fe','fi','fo','fr','fu',
                     'g','ga','ge','gi','gn','go','gu',
                     'h','ha','he','hi','hn','ho','hu','hy',
                     'i','id','ie','il','im','in','io','ir','iu',
                     'j','ja','je','ji','jo','ju',
                     'k','ka','ke','ki','ko','ku',
                     'l','la','le','lf','li','lm','ln','lo','lu','ly',
                     'm','ma','me','mi','mm','mn','mo','mu','my',
                     'n','na','ne','ni','nn','no','nu','ny',
                     'o','ob','od','oe','of','og','oh','oi','ok','ol','om','on','oo','op','or','os','ot','ou','ow','oy','oz',
                     'p','pa','pe','pi','po','pp','pu','py',
                     'q','qu','qi',
                     'r','ra','re','ri','ro','rr','ru','ry',
                     's','sa','se','sh','si','so','ss','su','sy',
                     't','ta','te','th','ti','to','tt','tu','ty',
                     'u','ub','uc','ud','uf','ug','uh','uk','ul','um','un','up','ur','us','ut','ux','uz',
                     'v','va','ve','vi','vo','vu',
                     'w','wa','we','wi','wo','wu','wy',
                     'x','xa','xe','xi','xo','xu','xy',
                     'y','ya','ye','yi','yo','yu',
                     'z','za','ze','zi','zo','zu','zz']
        name = ''
        num_syllables = randint(1,5)

        for _ in range(num_syllables):
            syllable = choice(syllables)
            name += syllable
            if randint(0,2) == 0:
                name += ' '

        return name.strip().title()

    def __str__(self):
        self.title = ''
        if self.heir:
            self.title += 'Prince of the North'
        if self.true_love:
            self.title += 'the Beloved'
        if self.guide:
            self.title += 'Guide'
        if self.magical:
            self.title += 'the '
            if self.priest:
                self.title += 'Priest'
            if self.monk:
                self.title += 'Monk'
            if self.magician:
                self.title += 'Magician'
            if self.wizard:
                self.title += 'Wizard'
            if self.witch:
                self.title += 'Witch'
        return [f'{self.name}',
                self.title,
                f'Combat Skill: {max(self.combat_skill - self.fatigue, 0)}',
                f'Endurance: {self.endurance}',
                f'Wounds: {self.total_wounds}',
                f'Wits: {self.wits + self.wits_bonus}',
                f'Gold: {self.gold}',
                f'Possessions: {len(self.possessions)}/{self.max_carry}']
    
    def add_item(self, item):
        if len(self.possessions) <= self.max_carry:
            self.possessions.append(item)

    def plague_and_recovery(self):
        if self.plague and self.alive:
            self.wounds += randint(1,3) 
            recovery_roll = randint(1,6)
            if recovery_roll >= 4:
                self.plague = False

    def check_carry_capacity(self):
        while len(self.possessions) > self.max_carry:
            random_item = choice(self.possessions)
            self.possessions.remove(random_item)

    def update(self):
        self.total_wounds = self.wounds + self.poison_wounds

        if self.unearthly:
            if self.wounds > 0:
                self.wounds = 0

        if self.regenerates:
            if self.total_wounds >= self.endurance:
                self.awake = False
                self.alive = False
            else:
                self.awake = True
                if self.wounds > 0:
                    self.wounds -= 1
                elif self.poison_wounds > 0:
                    self.poison_wounds -= 1

        if self.total_wounds < self.endurance - 1:
            self.awake = True
        if self.total_wounds >= self.endurance - 1:
            self.awake = False
        if self.total_wounds >= self.endurance:
            self.alive = False

        self.has_eaten = False
        if self.fatigue > self.combat_skill:
            self.fatigue = self.combat_skill
        self.plague_and_recovery()
        pouches_of_gold = (self.gold // 100) + 1
        if self.possessions.count('pouch of gold') < pouches_of_gold:
            self.add_item('pouch of gold')
        elif self.possessions.count('pouch of gold') > pouches_of_gold:
            self.possessions.remove('pouch of gold')
        if self.gold == 0:
            while 'pouch of gold' in self.possessions:
                self.possessions.remove('pouch of gold')
        self.check_carry_capacity()
        if not self.mounted and not self.flying:
            self.move_speed = 1
        if self.mounted and not self.flying:
            self.move_speed = 2
        if self.flying:
            self.move_speed = 3


treasure_table = {0:[0, 0, 0, 0, 0, 0],
                  1:[0, 0, 1, 1, 2, 2],
                  2:[0, 1, 2, 2, 3, 4],
                  4:[2, 3, 4, 4, 5, 6],
                  5:[2, [3, 'A'], 4, [6, 'A'], 7, [8, 'A']],
                  7:[3, 4, 6, 8, 10, 11],
                  10:[6, 8, 9, 11, 12, 14],
                  12:[5, [9, 'C'], [11, 'A'], 12, [15, 'A'], 20],
                  15:[10, 12, 14, 16, 18, 20],
                  21:[15, 18, 20, 22, 24, 27],
                  25:[[20, 'A'], 22, [24, 'A'], 26, [28, 'A'], 30],
                  30:[23, 27, 29, 31, 33, 37],
                  50:[40, 45, 48, 52, 55, 60],
                  60:[[45, 'A'], [50, 'C'], 55, [60, 'B'], [70, 'A'], 80],
                  70:[55, 60, 65, 70, 80, 90],
                  100:[85, 90, 95, 100, 110, 120],
                  110:[[80, 'B'], [90, 'C'], [100, 'B'], [110, 'A'], [130, 'C'], [150, 'A']],}

item_table = {'A':['e180', 'e181', 'e182', 'e183', 'e184', 'e185'],
              'B':['e180', 'e186', 'e187', 'e188', 'e190', 'e193'],
              'C':['e186', 'e188', 'e189', 'e191', 'e192', 'e194'],}

# e180 healing potion
# e181 cure poison vial
# e182 gift of charm
# e183 endurance sash
# e184 resistance talisman
# e185 poison drug
# e186 magic sword
# e187 anti-poison amulet
# e188 pegasus mount
# e189 charisma talisman
# e190 nerve gas bomb
# e191 resistance ring
# e192 ressurection necklace
# e193 shield of light
# e194 royal helm of the northlands

# prince = Character('Cal Arath', 8, 9, 0, 2, randint(2,6))
# print(prince)


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