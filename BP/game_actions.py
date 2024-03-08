import characters
import events
import travel_events
from hexmap import overland_map
from collections import Counter
from random import choice, randint

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

def encounter(hex, console, terrain_type=None):
    '''this still needs to account for roads, river rafting, and river crossings'''
    if terrain_type is None:
        terrain_type = getattr(travel_events, overland_map[hex][0])
    encounter_dice = randint(1,6) + randint(1,6)
    if encounter_dice >= terrain_type['event']:
        row_dice = randint(1,6)
        column_dice = randint(0,5)
        event = terrain_type[row_dice][column_dice]
        console.display_message(f'You encounter event {event} in the {overland_map[hex][0]}!')

def get_lost(hex, console, terrain_type=None):
    '''this still needs to account for roads, river rafting, and river crossings'''
    if terrain_type is None:
        terrain_type = getattr(travel_events, overland_map[hex][0])
    get_lost_dice = randint(1,6) + randint(1,6)
    if get_lost_dice >= terrain_type['lost']:
        console.display_message(f'You have gotten lost attempting to enter the {overland_map[hex][0]}.  Maybe you will find your way tomorrow.')
        return True

def follow_road(direction, player_hex, console):
    has_road ={
		"n" : "1",
		"ne": "2",
		"se": "3",
		"s" : "4",
		"sw": "5",
		"nw": "6"}
    
    if overland_map[player_hex][3] is not None:
        if has_road[direction] in overland_map[player_hex][3]:
            console.display_message('You follow the road.')
            terrain_type = getattr(travel_events, "Road")
            return terrain_type
        else:
            return None

def cross_river(direction, player_hex, console):
    has_river ={
		"n" : "1",
		"ne": "2",
		"se": "3",
		"s" : "4",
		"sw": "5",
		"nw": "6"}
    
    if overland_map[player_hex][2] is not None:
        if has_river[direction] in overland_map[player_hex][2]:
            terrain_type = getattr(travel_events, "Cross_River")
            if not follow_road(direction, player_hex, console):
                console.display_message("You are attempting to cross a river.")
                can_cross = randint(1,6) + randint(1,6)
                if can_cross >= terrain_type["lost"]:
                    console.display_message("However, you are unable to find a suitable place to cross the river today.")
                    return False
                
                else: #pass the river
                    console.display_message("You have successfully made it across the river.")
                    river_event = randint(1,6) + randint(1,6)
                    if river_event >= terrain_type['event']:
                        row_dice = randint(1,6)
                        column_dice = randint(0,5)
                        event = terrain_type[row_dice][column_dice]
                        console.display_message(f'You encounter event {event} while crossing the river!')
                    return True
                
        return True
    return True

def raft_river():
    pass

def move(input, player_hex, hexagon_dict, console):
    if player_hex[0] % 2 == 0:
        dir = {
            'nw': (-1, +0),
            'n' : (+0, -1),
            'ne': (+1, +0),
            'sw': (-1, +1),
            's' : (+0, +1),
            'se': (+1, +1)
            }
    elif player_hex[0] % 2 == 1:
        dir = {
            'nw': (-1, -1),
            'n' : (+0, -1),
            'ne': (+1, -1),
            'sw': (-1, +0),
            's' : (+0, +1),
            'se': (+1, +0)
            }
    if input in dir:
        v = dir[input]
        if (player_hex[0] + v[0], player_hex[1] + v[1]) in hexagon_dict:
            if cross_river(input, player_hex, console):
                if get_lost((player_hex[0] + v[0], player_hex[1] + v[1]), console, follow_road(input, player_hex, console)):
                    player_hex = player_hex
                else:
                    player_hex = (player_hex[0] + v[0], player_hex[1] + v[1])
                    encounter(player_hex, console, follow_road(input, player_hex, console))
            else:
                player_hex = player_hex
        else:
            player_hex = player_hex
    else:
        player_hex = player_hex

    return player_hex

def combat(party, enemies, console, has_surprise=None, has_first_strike=None):
    killed = 0
    loot = []
    rounds = 0
    if has_surprise == 'enemy':
        console.display_message('The enemy has taken you by surprise!')
        party_strike_flag = False
        party_first_strike_flag = False
        enemy_strike_flag = True
        enemy_first_strike_flag = True
    elif has_surprise == 'player':
        console.display_message('You have taken the enemy by surprise!')
        party_strike_flag = True
        party_first_strike_flag = True
        enemy_strike_flag = False
        enemy_first_strike_flag = False
    else:
        battle_begin_message = 'All combatants array themselves for battle. '
        party_strike_flag = True
        enemy_strike_flag = True
        if has_first_strike == 'enemy':
            battle_begin_message += 'Enemy has first strike.'
            party_first_strike_flag = False
            enemy_first_strike_flag = True
        else:
            battle_begin_message += 'Party has first strike.'
            party_first_strike_flag = True
            enemy_first_strike_flag = False
        console.display_message(battle_begin_message)

    while party[0].alive and enemies:
        if rounds == 0:
            console.display_message('*---Combat begins---*')
        elif rounds > 0:
            console.display_message('*---A new round of combat begins---*')
        if party_strike_flag or party_first_strike_flag:
            for character in party:
                if character.alive and character.awake:
                    valid_targets = [enemy for enemy in enemies if enemy.alive]
                    if not valid_targets:
                        break
                    target = choice(valid_targets)
                    combat_strike(character, target, console)
                    
        if enemy_strike_flag or enemy_first_strike_flag:
            for enemy in enemies:
                if enemy.alive and enemy.awake:
                    valid_enemy_targets = [character for character in party if character.alive]
                    if not valid_enemy_targets:
                        break
                    enemy_target = choice(valid_enemy_targets)
                    combat_strike(enemy, enemy_target, console)
                    
        for character in party:
            character.update()
            if not character.alive and not character.heir:
                console.display_message(f'{character.name} has been slain!')
                party[0].gold += character.gold
                party.remove(character)
            if not character.alive and character.heir:
                console.display_message(f'{character.name} has been slain!')
                return False

        for enemy in enemies:
            enemy.update()
            if enemy.regenerates and enemy.alive:
                console.display_message(f'{enemy.name} has regenerated a wound!')
            if not enemy.alive:
                console.display_message(f'{enemy.name} has been slain!')
                loot.append(enemy.wealth_code)
                enemies.remove(enemy)
                killed += 1

        party_strike_flag = True
        enemy_strike_flag = True
        rounds += 1

        if killed > 0 and killed > len(enemies):
            rout = randint(1, 6)
            if rout == 6:
                console.display_message(f"The enemy has routed! {len(enemies)} foes have fled!")
                for enemy in enemies:
                    enemies.remove(enemy)

        console.display_message('Do you wish to Fight or Escape?', True)
        player_input = console.handle_player_response()

        if player_input == 'f':
            console.display_message('You continue the battle...')
            continue
        if player_input == 'e':
            escape_roll = randint(1,6)
            if escape_roll >= 4:
                console.display_message('Combat has ended. You have escaped from your enemies.')
                break
            else:
                console.display_message('You have failed to escape your enemies!')
                party_strike_flag = False
                continue

    if not enemies:
        console.display_message(f'Combat has ended. After {rounds} rounds of combat, {party[0].name}, you are victorious!  You have slain {killed} opponents.')
        total_gold = 0
        for wealth_code in loot:
            gold, item = roll_treasure(wealth_code)
            total_gold += gold
            if item:
                party[0].add_item(item)
                console.display_message(f'You find a {item}!')
        console.display_message(f'You find {total_gold} gold!')
        party[0].gold += total_gold
        return True
    elif not party[0].alive:
        console.display_message(f'Combat has ended. {party[0].name}, you have been defeated!')
        return False


def combat_strike(attacker, target, console):
    console.clear_console()
    miss_set = {-6, -5, -4, -3, -2, 0, 1, 2, 4, 6, 7, 9, 15}
    hit_map = {-1: 1,
                3: 1,
                5: 1,
                8: 1,
                11: 1,
                10: 2,
                12: 2,
                13: 2,
                17: 2,
                14: 3,
                16: 5,
                18: 5,
                19: 5,
                20: 6}
    strike = randint(1,6) + randint(1,6) + attacker.combat_skill - attacker.fatigue - target.combat_skill
    if attacker.total_wounds > 0:
        strike -= 1
        if attacker.total_wounds >= attacker.endurance / 2:
            strike -= 1
    if target.total_wounds >= target.endurance / 2:
        strike += 2

    if strike in miss_set:
        console.display_message(f'{attacker.name} missed the enemy {target.name}!')
    else:
        if attacker.magical and target.unearthly:
            console.display_message(f'Hit! {attacker.name} struck the enemy {target.name} for {hit_map[strike]} damage!')
            target.poison_wounds += hit_map[strike]
        elif not attacker.magical and target.unearthly:
            console.display_message(f'Hit! {attacker.name} struck the enemy, but {target.name} is not vulnerable to mortal weapons!  You must use poison or magic!')
        else:
            console.display_message(f'Hit! {attacker.name} struck the enemy {target.name} for {hit_map[strike]} damage!')
            target.wounds += hit_map[strike]


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
            #rations = ["ration"] * hunt_result
            rations = hunt_result // len(party)
            extra_rations = hunt_result % len(party)
            console.display_message(f'{hunter.name} brings back {hunt_result} rations from hunting.')

            for character in party:
                for _ in range(rations):
                    if len(character.possessions) <= character.max_carry:
                        character.add_item('ration')
            for _ in range(extra_rations):
                party[randint(0, len(party) - 1)].add_item('ration')

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
    food_message = ""
    if any(player_hex in key for key in [castles, temples, towns]):
        lodging(party, console)
        for character in reversed(party):
            if 'ration' in character.possessions:
                food_message += f'{character.name} has eaten. '
                #console.display_message(f'{character.name} has eaten.')
                character.possessions.remove('ration')
                character.has_eaten = True
                if character.max_carry < 10:
                    character.max_carry = min(character.max_carry * 2, 10)
                if character.fatigue > 0:
                    character.fatigue -= 1
            elif party[0].gold >= 1 + gold_spent:
                gold_spent += 1
                food_message += f'{character.name} has purchased a meal. '
                #console.display_message(f'{character.name} has purchased a meal.')
                character.has_eaten = True
            else:
                console.display_message(f'{party[0].name} does not have enough gold to purchase a meal for {character.name}!')
                starvation(character, party, console)
        party[0].gold -= gold_spent
                
    elif player_hex in deserts and player_hex not in oasis:
        for character in reversed(party):
            ration_count = Counter(character.possessions)
            if ration_count['ration'] >= 2:
                food_message += f'{character.name} has eaten. '
                #console.display_message(f'{character.name} has eaten.')
                character.possessions.remove('ration')
                character.possessions.remove('ration')
                character.has_eaten = True
                if character.max_carry < 10:
                    character.max_carry = min(character.max_carry * 2, 10)
                if character.fatigue > 0:
                    character.fatigue -= 1
            else:
                starvation(character, party, console)

    else:
        for character in reversed(party):
            if 'ration' in character.possessions:
                food_message += f'{character.name} has eaten. '
                #console.display_message(f'{character.name} has eaten.')
                character.possessions.remove('ration')
                character.has_eaten = True
                if character.max_carry < 10:
                    character.max_carry = min(character.max_carry * 2, 10)
                if character.fatigue > 0:
                    character.fatigue -= 1
            else:
                starvation(character, party, console)

    console.display_message(food_message)

def starvation(character, party, console):
    starvation_message = ""
    if not character.has_eaten:
        character.max_carry = max(character.max_carry // 2, 1)
        character.fatigue += 1
        starvation_message += f'{character.name} has gone without food! '
        #console.display_message(f'{character.name} has gone without food!')
        character.check_carry_capacity()
    console.display_message(starvation_message)
    desertion(character, party, console, 'hunger')
    '''Need to implement mount starvation'''

def desertion(character, party, console, reason):
    if not character.heir or character.true_love:
        desertion_dice = randint(1,6) + randint(1,6) - party[0].wits
        if desertion_dice >= character.loyalty:
            console.display_message(f'{character.name} has grown weary of {reason} and has abandoned you!')
            party.remove(character)
        else:
            console.display_message(f'Despite {reason}, {character.name} has decided to remain your companion!')

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
        console.display_message(f'{party[0].name} does not have enough gold to rent rooms and the party is forced to sleep in the street!')
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
        console.display_message(f'{character.name} was struck by a poisoned needle for 1 poison wound!')
        character.poison_wounds += 1
    elif trap_roll == 2:
        acid_damage = randint(1,6)
        console.display_message(f'{character.name} was struck by a burning acid explosion for {acid_damage} wounds!')
        character.wounds += acid_damage
    elif trap_roll == 3:
        gas_damage = randint(1,6)
        console.display_message(f'Poison gas envelops {character.name} and inflicts {gas_damage} poison wounds!')
        character.poison_wounds += gas_damage
    elif trap_roll == 4:
        console.display_message(f'Plague dust inflicts sickness on {character.name}!')
        character.plague = True
    elif trap_roll == 5:
        sharp_damage = randint(4,9)
        console.display_message(f'Flying spikes and knives explode toward {character.name} and deal {sharp_damage} wounds!')
        character.wounds += sharp_damage
    else:
        console.display_message(f'Trap malfunctions! No injury to {character.name}!')

def true_love(party, lovers, console):
    love = []
    for character in party:
        if character.true_love:
            lovers.append(character)
            love.append(character)

    if love in party and len(love) == 1:
        party[0].wits_bonus = 1
    else:
        party[0].wits_bonus = 0
        
    for character in lovers:
        return_message = ''
        if character not in party and character.alive:
            love_roll = randint(1,6) + randint(1,6)
            console.display_message(f'{character.name} is searching for you! {love_roll}')
            if love_roll == 12:
                console.display_message(f'{character.name} visits you in your dreams, and you know your love has left this world.')
                character.alive = False
                lovers.remove(character)
                #love.remove(character)
            if 12 > love_roll >= 10:
                return_message += f'{character.name} has found you and rejoined your party! '
                has_mount_roll = randint(1,6) + randint(1,6)
                if has_mount_roll >= 9:
                    return_message += 'They found a mount while you were separated. '
                    character.mounted = True
                    if has_mount_roll == 12:
                        return_message += "It's a pegasus!"
                        character.flying = True
                console.display_message(return_message)
                party.append(character)
            else:
                return

    '''True love will not abandon party, regardless of money/food situation.  If forced to separate, character will
    return at end of day on roll of 10 or 11 on 2d6; a 12 means they died.  If they find you again, a roll of 9+ on
    2d6 means they return with a horse; a 12 means they return with a pegasus.  
    While true love is in party, you get +1 wits.  Cannot have true love with more than one character at a time.
    Maybe develop a loyalty or boon companion mechanic?'''


'''actions available in any hex'''
def rest(party, player_hex, console):
    encounter(player_hex, console)
    rest_message = ""
    for character in party:
        if character.wounds > 0:
            character.wounds -= 1
            #console.display_message(f'{character.name} has rested for the day and healed a wound.')
            rest_message += f'{character.name} has rested for the day and healed a wound. '
        else:
            #console.display_message(f'{character.name} has rested for the day.')
            rest_message += f'{character.name} has rested for the day. '
    hunt_bonus = int(len(party) - 1)
    rest_message += f'You have a +{hunt_bonus} bonus to hunting today.'
    console.display_message(rest_message)
    return hunt_bonus

def cache_locate():
    pass

def cache_place():
    pass


'''actions available in certain hexes'''

def seek_news_and_information(party, player_hex, console): #town, temple, or castle
    gather_info_roll = randint(1,6) + randint(1,6) #+ character.info_bonus[player_hex]
    console.display_message(f'Initial roll: {gather_info_roll}')
    if party[0].gold >= 5:
        console.display_message('Do you wish to spend 5 gold to loosen tongues? (y/n)') #need to handle choice
        party[0].gold -= 5
        gather_info_roll += 1
        console.display_message(f'Plus bribe bonus: {gather_info_roll}')
    if party[0].wits >= 5:
        gather_info_roll += 1
        console.display_message(f'Plus wits bonus: {gather_info_roll}')

    if gather_info_roll == 2:
        console.display_message('Your inquiries uncover no news of note; nothing seems to be happening.')
    
    elif gather_info_roll == 3:
        console.display_message("You discover a thieves' den and pillage it while they are out.  You gain 50 gold.")
        party[0].gold += 50
    
    elif gather_info_roll == 4:
        temples = {(7,11):"Branwyn's Temple",
                   (10,21):'Sulwyth Temple',
                   (13,9):"Donat's Temple",
                   (18,5):'Temple of Zhor',
                   (20,18):'Temple of Duffyd'}
        secret_rites = choice(temples)
        console.display_message(f'You learn of secret rites at {secret_rites}.  You gain a small advantage when making offerings there.')
        if secret_rites in party[0].offering_bonus:
            party[0].offering_bonus[secret_rites] += 1
        else:
            party[0].offering_bonus[secret_rites] = 1
            
    elif gather_info_roll == 5:
        console.display_message('Your inquiries uncover no news of note; but you feel at home in this place and gain a small bonus when seeking information or hirelings.')
        if player_hex in party[0].info_bonus:
            party[0].info_bonus[player_hex] += 1
        else:
            party[0].info_bonus[player_hex] = 1
        if player_hex in party[0].hiring_bonus:
            party[0].hiring_bonus[player_hex] += 1
        else:
            party[0].hiring_bonus[player_hex] = 1
    
    elif gather_info_roll == 6:
        console.display_message('A large caravan is in town.  You may visit them today, if you wish.')
        events.e129(console)
    
    elif gather_info_roll == 7:
        console.display_message('Discover cheaper lodgings and food, pay half the normal price here.')
    
    elif gather_info_roll == 8:
        console.display_message('A cutpurse picks your pocket, stealing half your gold!')
        party[0].gold //= 2
    
    elif gather_info_roll == 9:
        console.display_message('You attract the attention of the local constabulary.')
        events.e050(console)
    
    elif gather_info_roll == 10:
        console.display_message('You discover the residence of a local magician.')
        events.e016(console)
    
    elif gather_info_roll == 11:
        console.display_message("You discover the local thieves' guild and are 'invited' to join.  If you do, you participate in a theft tonight and then flee the hex.  If you pay the guild their cut, you may return to this hex in the future. ")
        party[0].gold += 200
    
    elif gather_info_roll >= 12:
        console.display_message('A secret informant offers you valuable information for 10 gold.')
        if party[0].gold >= 10:
            party[0].gold -= 10
            secret_info = choice(['bogus secrets that prove worthless', 'event e147', 'event e143', 'event e144', 'event e145', 'event e146'])
            console.display_message(f'The informant reveals {secret_info} before slipping away into the crowds.')


def hire_followers(party, player_hex, console): #town or castle
    hiring_roll = randint(1,6) + randint(1,6) #+ party[0].hiring_bonus[player_hex]
    
    if hiring_roll == 2:
        console.display_message("A Freeman joins your party at no cost (except food and lodging).")
        freeman = characters.Character(name='Freeman', combat_skill=3, endurance=4)
        party.append(freeman)
    elif hiring_roll == 3:
        console.display_message("A Lancer with a horse can be hired for 3 gold per day.")
        lancer = characters.Character(name='Lancer', combat_skill=5, endurance=5, daily_wage=3, mounted=True)
        party.append(lancer)
    elif hiring_roll == 4:
        console.display_message("One or two mercenaries can be hired for 2 gold per day each.")
        mercenary = characters.Character(name='Mercenary', combat_skill=4, endurance=4, daily_wage=2)
        mercenaries_hired = console.handle_input()
        for _ in range(max(mercenaries_hired, 2)):
            party.append(mercenary)
    elif hiring_roll == 5:
        console.display_message("Horse dealer in area, you can buy horses (for mounts) at 10 gold each.")
    elif hiring_roll == 6:
        console.display_message("Local guide available, hire for 2 gold per day.")
        guide = characters.Character(name='Guide', combat_skill=2, endurance=3, daily_wage=2, guide=True)
        party.append(guide)
    elif hiring_roll == 7:
        console.display_message("Henchmen available, roll one die for the number available for hire, at 1 gold per day each.")
        henchmen_roll = randint(1,6)
        henchmen = characters.Character(None, None, combat_skill=3, endurance=3, daily_wage=1)
        henchmen_hired = console.handle_input()
        for _ in range(max(henchmen_hired, henchmen_roll)):
            party.append(henchmen)
    elif hiring_roll == 8:
        console.display_message("Slave market, see event e163")
    elif hiring_roll == 9:
        console.display_message("Nothing available, but you gain some news and information, see r209 but subtract one (-1) from your dice roll there.")
    elif hiring_roll == 10:
        console.display_message("Honest horse dealer in area, can buy horses (for mounts) at 7 gold each.")
    elif hiring_roll == 11:
        console.display_message("Runaway boy or girl joins your party at no cost (except food and lodging), has combat skill 1, endurance 3.")
        runaway = characters.Character(name='Runaway Urchin', combat_skill=1, endurance=3)
        party.append(runaway)
    elif hiring_roll >= 12:
        console.display_message("Porters, in any quantity desired, are available to hire for ½ gold each per day. In addition, a local guide can be hired for 2 gold per day.")
        porters = characters.Character(name='Porter', combat_skill=1, endurance=2, daily_wage=0.5)
        guide = characters.Character(name='Guide', combat_skill=1, endurance=2, daily_wage=2, guide=True)
        porters_hired = console.handle_input()
        for _ in range(porters_hired):
            party.append(porters)
        party.append(guide)


def seek_audience(party, player_hex, console): #town, temple, or castle
    pass
    # if current_hex_key in (101, 109, 216, 419, 422, 719, 916, 1004, 1009, 1415, 1501, 1720):
	# 	audience_town = d6(2)
	# 	if audience_town == 2:
	# 		# 2 Grievously insult the town council, e062.
	# 		# 3 A slanderous aside about the mayor's wife is blamed on you, e060.
	# 		# 4 Meet hostile guards, e158.
	# 		# 5 Encounter the Master of the Household, e153.
	# 		# 6,7,8 Audience refused today, you may try again.
	# 		# 9,10 Audience permitted, el56.
	# 		# 11 Meet daughter of the mayor, e154.
	# 		# 12 Audience permitted, e156.

	# if current_hex_key in (711, 1021, 1309, 1805, 2018):
	# 	audience_temple = d6(2)
	# 	if audience_temple == 2:
	# 		# 2 Anger temple guards, e063.
	# 		# 3 Priestess resents a lewd remark, e060.
	# 		# 4 Encounter hostile guards, e158.
	# 		# 5 Audience refused today, you may try again.
	# 		# 6 Must purify yourself, e159
	# 		# 7 Audience refused today, you may try again.
	# 		# 8 Allowed audience if you give temple a Dragon's eye, go to e155; otherwise you must deal with the Master of the Household, e153.
	# 		# 9 Permitted to pay your respects, e250
	# 		# 10 You must purify yourself, e159.
	# 		# 11+ Audience permitted, e155

	# if current_hex_key == 323:
	# 	audience_drogat = d6(2)
	# 	if audience_drogat == 2:
	# 		# 2 You are the Count's next victim; see e061.
	# 		# 3 The Captain of the Guard dislikes your haircut; see e062.
	# 		# 4 Meet the daughter of the Count, e154.
	# 		# 5 Encounter the Master of the Household, e153.
	# 		# 6 Confronted by hostile guards, e158.
	# 		# 7 Gain an audience (e161) if you give the Roc's Beak to the Doorman; otherwise you are deemed unworthy and unwise, and are arrested (e060).
	# 		# 8 Seneschal requires a bribe, e148.
	# 		# 9 Must learn court manners, e149.
	# 		# 10 Find favour in the eyes of the Count, e151.
	# 		# 11+ Audience granted with Count, e161.

	# if current_hex_key == 1212:
	# 	audience_huldra = d6(2)
	# 	if audience_huldra == 2:
	# 		# 2 Audience permanently refused, cannot try again.
	# 		# 3 Meet Baron's Daughter, e154.
	# 		# 4 Must learn court manners, e149.
	# 		# 5 Confronted by hostile guards, e158.
	# 		# 6,7 Audience refused today, you may try again.
	# 		# 8 Encounter the Master of the Household, e153.
	# 		# 9 Seneschal requires a bribe, e148.
	# 		# 10,11 Pay your respects to the Baron, e150.
	# 		# 12 Find favour in the eyes of the Baron, e151.
	# 		# 13+ Baron becomes your Noble ally, e152.

	# if current_hex_key == 1923:
	# 	audience_aeravir = d6(2)
	# 	if audience_aeravir == 2:
	# 		# 2 You insult the Lady's dignity, arrested e060.
	# 		# 3 You must purify yourself first, e159.
	# 		# 4 Untoward remark makes the guards hostile, e158.
	# 		# 5 Must learn better court manners, e149.
	# 		# 6 Meet the Master of the Household, e153.
	# 		# 7 Gain an audience (e160) if you give the Griffon's Claw, otherwise audience refused but you may try again.
	# 		# 8 Audience refused, but you may try again.
	# 		# 9 Seneschal requires a bribe, e148.
	# 		# 10 Audience granted, e160.
	# 		# 11 Meet daughter of the Lady Aeravir, e154.
	# 		# 12+ Audience granted, e160.


def make_offering(party, player_hex, console): #temple
    offering_roll = randint(1,6) + randint(1,6) #+ party[0].offering_bonus[player_hex]
    console.display_message('You must spend 1 gold for proper herbs and sacrifice to make an offering.')
    if party[0].gold >= 10:
        console.display_message('If you wish, you may spend 10 gold on fine herbs and sacrifices for the offering. (y/n)?') #need to handle choice
        if 'yes':
            party[0].gold -= 10
            offering_roll += 1
    else:
        party[0].gold -= 1
    
    console.display_message('You spend the day preparing, waiting in line, and finally giving an offering at the temple altar.') 

    if offering_roll == 2:
        console.display_message('You commit a magnificent error in the rites, the entire temple becomes impure and abandoned, no longer functions as a temple for the rest of the game. You are arrested and sentenced to death, e061.')
    if offering_roll == 3:
        console.display_message('Good Omens, but no special result.')
    if offering_roll == 4:
        console.display_message('Bad Omens, you are travelling under a curse. Roll one die for each of your followers, any result except a 1 means they believe the omens and immediately desert you. You cannot seek to hire any followers (r210) in this hex for the rest of the game.')
    if offering_roll == 5:
        console.display_message('High Priest insulted by your northern manners, arrested e060.')
    if offering_roll == 6:
        console.display_message('Good Omens, you get free food (r215) and lodging (r217) tonight.')
    if offering_roll == 7:
        console.display_message('Favourable Omens for further worship, if you try this Offerings action again tomorrow, you can add one (+1) to your dice roll. Otherwise no effect.')
    if offering_roll == 8:
        console.display_message('Gods favour your questions, priests assign a monk to your party. The monk has combat skill 2, endurance 3, serves as a guide when leaving this or any adjacent hex only.')
        monk = characters.Character(None, None, 2, 3, monk=True)
        party.append(monk)
    if offering_roll == 9:
        console.display_message('Special omen and riddle provides a clue to treasures, see e147.')
    if offering_roll == 10:
        console.display_message('Fall in love with priestess (see r229). You immediately escape (r218) with her and can never return to this hex. She is combat skill 2, endurance 4, and has wealth 100 in temple treasures she has stolen!')
        priestess_love = characters.Character(None, 'female', 2, 4, wealth_code=100, priest=True, true_love=True)
        party.append(priestess_love)
    if offering_roll == 11:
        console.display_message('The High Priest requires an audience with you; see e155.')
    if offering_roll == 12 or offering_roll == 13:
        console.display_message('High Priest spends afternoon talking with you, provides you with final clues to some secret information, roll one die: 1,2-e144; 3,4-e145; 5,6-e146. Alternately, instead of the secret information, you can use his influence in attempting Offerings again tomorrow, and add three (+3) to your dice roll here.')
    if offering_roll >= 14:
        console.display_message('Gods declare your cause a religious crusade, and the Staff of Command is passed into your hands. If you bring this possession to any hex north of the Tragoth River you will command instant obedience throughout the Northlands, regain your throne and win the game. In the meantime you are given a pair of warrior monks (combat skill 5, endurance 6) with mounts to join your party and help you return northward.')
        party[0].add_item('Staff of Command')
        for _ in range(2):
            warrior_monk = characters.Character(None, None, 5, 6, monk=True, mounted=True)
            party.append(warrior_monk)


def search_ruins(party, player_hex, console): #ruins
    ruin_results = {2: ['e133', 'Plague'], 3: ['e135', 'Broken Columns'], 
                    4: ['e136', 'Hidden Treasures'], 5: ['e137', 'Inhabitants'], 
                    6: ['e139', 'Minor Treasures'], 7: ['e131', 'Empty Ruins'],
                    8: ['e132', 'Organized Search'], 9: ['e134', 'Unstable Ruins'], 
                    10: ['e138', 'Unclean'], 11: ['e135', 'Broken Columns'], 
                    12: ['e035', 'Spell of Chaos']}
    ruin_search_roll = randint(1,6) + randint(1,6)
    ruin_event = ruin_results[ruin_search_roll]
    console.display_message(f'Your search of the ruins has uncovered {ruin_event[1]}!')
    if ruin_event[0] == 'e131':
        events.e131(console)
    elif ruin_event[0] == 'e132':
        events.e132(party, player_hex, console)
    elif ruin_event[0] == 'e133':
        events.e133(party, console)
    elif ruin_event[0] == 'e134':
        events.e134(party, player_hex, console)
    elif ruin_event[0] == 'e135':
        events.e135(party, console)
    elif ruin_event[0] == 'e136':
        events.e136(party, console)
    elif ruin_event[0] == 'e137':
        events.e137(party, console)
    elif ruin_event[0] == 'e138':
        events.e138(party, console)
    elif ruin_event[0] == 'e139':
        events.e139(party, console)
    elif ruin_event[0] == 'e035':
        events.e035(party, player_hex, console)

        