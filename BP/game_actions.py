import travel_events
from hexmap import overland_map
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

def encounter(hex, console):
    '''this still needs to account for roads and river crossings'''
    terrain_type = getattr(travel_events, overland_map[hex][0])
    encounter_dice = randint(1,6) + randint(1,6)
    if encounter_dice >= terrain_type['event']:
        row_dice = randint(1,6)
        column_dice = randint(0,5)
        event = terrain_type[row_dice][column_dice]
        console.display_message(f'You encounter event {event}!')

def get_lost(hex, console):
    '''this still needs to account for roads and river crossings'''
    terrain_type = getattr(travel_events, overland_map[hex][0])
    get_lost_dice = randint(1,6) + randint(1,6)
    if get_lost_dice >= terrain_type['lost']:
        console.display_message(f'You have gotten lost attempting to enter the {overland_map[hex][0]}.  Maybe you will find your way tomorrow.')
        return True

def talk():
    pass

def evade():
    pass

def fight():
    pass

def dismiss_party_member(party):
    pass

def hunt(party, player_hex, console, castles, temples, towns, deserts, mountains, farmlands, bonus=0):
    hunter = party[0]
    if player_hex not in mountains and player_hex not in deserts:
        if not any(player_hex in key for key in [castles, temples, towns]):
            hunt_dice = randint(1,6) + randint(1,6)
            if hunt_dice == 12:
                injury = randint(1,6)
                console.display_message(f'{hunter.name} was injured while hunting, suffering {injury} wounds!')
                hunter.wounds += injury

            hunt_result = (hunter.combat_skill + int(hunter.endurance / 2) + bonus) - hunt_dice
            rations = ["ration"] * hunt_result
            console.display_message(f'{hunter.name} brings back {hunt_result} rations from hunting.')
            for ration in rations:
                for character in party:
                    character.add_item(ration) 
                    ### This is not dividing rations properly

            if player_hex in farmlands:
                encounter = randint(1,6)
                if encounter == 5:
                    mob = (randint(1,6) + randint(1,6)) * 2
                    console.display_message(f'You are pursued by a large mob of {mob} angry farmers and villagers!')
                    if hunter.combat_skill + randint(1,6) - hunter.fatigue < 10:
                        hunter.wounds += randint(1,3)
                elif encounter == 6:
                    constables = randint(6,11)
                    console.display_message(f'Your illegal hunting has attracted the attention of {constables} members of the local constabulary!')
                    if hunter.combat_skill + randint(1,6) - hunter.fatigue < 12:
                        hunter.wounds += randint(1,6)


def eat_meal(party, player_hex, console, castles, temples, towns, deserts, oasis):
    gold_spent = 0
    if any(player_hex in key for key in [castles, temples, towns]):
        lodging(party, console)
        for character in party:
            if 'ration' in character.possessions:
                console.display_message(f'{character.name} has eaten.')
                character.possessions.remove('ration')
                character.has_eaten = True
                if character.max_carry < 10:
                    character.max_carry = min(character.max_carry * 2, 10)
                if character.fatigue > 0:
                    character.fatigue -= 1
            elif party[0].gold >= 1 + gold_spent:
                gold_spent += 1
                console.display_message(f'{character.name} has purchased a meal.')
                character.has_eaten = True
            else:
                starvation(character, party, console)
        party[0].gold -= gold_spent
                
    elif player_hex in deserts and player_hex not in oasis:
        for character in party:
            for _ in range(2):
                if 'ration' in character.possessions:
                    console.display_message(f'{character.name} has eaten.')
                    character.possessions.remove('ration')
                    character.has_eaten = True
                    if character.max_carry < 10:
                        character.max_carry = min(character.max_carry * 2, 10)
                    if character.fatigue > 0:
                        character.fatigue -= 1
                else:
                    starvation(character, party, console)

    else:
        for character in party:
            if 'ration' in character.possessions:
                console.display_message(f'{character.name} has eaten.')
                character.possessions.remove('ration')
                character.has_eaten = True
                if character.max_carry < 10:
                    character.max_carry = min(character.max_carry * 2, 10)
                if character.fatigue > 0:
                    character.fatigue -= 1
            else:
                starvation(character, party, console)   

def starvation(character, party, console):
    if not character.has_eaten:
        character.max_carry = max(character.max_carry // 2, 1)
        character.fatigue += 1
        console.display_message(f'{character.name} has gone without food!')
    desertion(character, party, console, 'hunger')
    '''Need to implement mount starvation'''

def desertion(character, party, console, reason):
    if not character.heir or character.true_love:
        desertion_dice = randint(1,6) + randint(1,6) - party[0].wits
        if desertion_dice >= 4:
            console.display_message(f'{character.name} has grown weary of {reason} and has abandoned you!')
            party.remove(character)

def lodging(party, console):
    rooms = 0.0
    stables = 0
    for character in party:
        if any([character.heir, character.priest, character.monk, character.magician, character.wizard, character.witch]):
            rooms += 1
        else:
            rooms += 0.5
        if character.mounted:
            stables += 1

    rooms = int(rooms) + (rooms > int(rooms))
    if party[0].gold >= rooms + stables:
        console.display_message(f'You rent {rooms} rooms and {stables} stables for the night, costing you {rooms + stables} gold.')
        party[0].gold -= rooms + stables
    elif rooms + stables > party[0].gold >= rooms:
        console.display_message(f'You rent {rooms} rooms for the night, costing you {rooms} gold.')
        '''Need to implement mounts going missing on d6 of 4+'''
        party[0].gold -= rooms
    else:
        for character in party:
            desertion(character, party, console, 'poverty')

def escape():
    '''move randomly to adjacent hex, no new events.  Cannot cross river unless flying.'''
    pass

def hide():
    '''remain in hex, no hunting.  mounts can forage.  eat and lodge normally in towns, castles, or temples.'''
    pass

def follow_characters():
    pass

def trap_lock(character, console):
    trap_roll = randint(1,6)
    if trap_roll == 1:
        console.display_message(f'{character} was struck by a poisoned needle!')
        character.poison_wounds += 1
    elif trap_roll == 2:
        console.display_message(f'{character} was struck by a burning acid explosion!')
        character.wounds += randint(1,6)
    elif trap_roll == 3:
        console.display_message(f'Poison gas envelops {character}!')
        character.poison_wounds += randint(1,6)
    elif trap_roll == 4:
        console.display_message(f'Plague dust inflicts sickness on {character}!')
        character.plague = True
    elif trap_roll == 5:
        console.display_message(f'Flying spikes and knives explode toward {character}!')
        character.wounds += randint(4,9)
    else:
        console.display_message(f'Trap malfunctions! No injury to {character}!')

def true_love():
    '''True love will not abandon party, regardless of money/food situation.  If forced to separate, character will
    return at end of day on roll of 10 or 11 on 2d6; a 12 means they died.  If they find you again, a roll of 9+ on
    2d6 means they return with a horse; a 12 means they return with a pegasus.  
    While true love is in party, you get +1 wits.  Cannot have true love with more than one character at a time.
    Maybe develop a loyalty or boon companion mechanic?'''


'''actions available in any hex'''
def rest(party, console):
    for character in party:
        if character.wounds > 0:
            character.wounds -= 1
            console.display_message(f'{character.name} has rested for the day and healed a wound.')
        else:
            console.display_message(f'{character.name} has rested for the day.')
    hunt_bonus = int(len(party) - 1)
    return hunt_bonus

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

def search_ruins(console):
    ruin_results = {2: ['e133', 'Plague'], 3: ['e135', 'Broken Columns'], 
                    4: ['e136', 'Hidden Treasures'], 5: ['e137', 'Inhabitants'], 
                    6: ['e139', 'Minor Treasures'], 7: ['e131', 'Empty Ruins'],
                    8: ['e132', 'Organized Search'], 9: ['e134', 'Unstable Ruins'], 
                    10: ['e138', 'Unclean'], 11: ['e135', 'Broken Columns'], 
                    12: ['e035', 'Spell of Chaos']}
    ruin_search_dice = randint(1,6) + randint(1,6)
    event = ruin_results[ruin_search_dice]
    console.display_message(f'Your search of the ruins has uncovered {event[1]}!')

        