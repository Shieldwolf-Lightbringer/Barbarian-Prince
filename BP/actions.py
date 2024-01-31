from random import randint

'''general actions'''
def roll_treasure(wealth_code):
    wealth_dice = randint(0,5)
    if isinstance(treasure_table[wealth_code][wealth_dice], list):
        gold_value = treasure_table[wealth_code][wealth_dice][0]
        item_row = treasure_table[wealth_code][wealth_dice][1]
        item_dice = randint(0,5)
        item = item_table[item_row][item_dice]
        return gold_value, item
    else:
        return treasure_table[wealth_code][wealth_dice], None

treasure_table = {1:[0, 0, 1, 1, 2, 2],
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

# item_table = {'A':['e180', 'e181', 'e182', 'e183', 'e184', 'e185'],
#               'B':['e180', 'e186', 'e187', 'e188', 'e190', 'e193'],
#               'C':['e186', 'e188', 'e189', 'e191', 'e192', 'e194'],}

item_table = {'A':['healing potion', 'cure poison vial', 'gift of charm', 'endurance sash', 'resistance talisman', 'poison drug'],
              'B':['healing potion', 'magic sword', 'anti-poison amulet', 'pegasus mount', 'nerve gas bomb', 'shield of light'],
              'C':['magic sword', 'pegasus mount', 'charisma talisman', 'resistance ring', 'ressurection necklace', 'royal helm of the northlands'],}

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

def encounter(hex):
    '''this needs to check what terrain the player is in, then roll on the appropriate table'''
    terrain_type = hex
    row_dice = randint(1,6)
    column_dice = randint(0,5)
    if hex in terrain_type:
        event = terrain_type[row_dice][column_dice]
    pass

def get_lost():
    pass

def talk():
    pass

def evade():
    pass

def fight():
    pass


'''actions available in any hex'''
def rest():
    pass

def cache_locate():
    pass

def cache_stash():
    pass


'''actions available in certain hexes'''

def gather_info():
    pass

def hire_followers():
    pass

def seek_audience():
    pass

def make_offering():
    pass

def search_ruins():
    pass