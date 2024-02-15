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
            if get_lost((player_hex[0] + v[0], player_hex[1] + v[1]), console):
                player_hex = player_hex
            else:
                player_hex = (player_hex[0] + v[0], player_hex[1] + v[1])
        return player_hex


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
        if desertion_dice >= 4:
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
    console.display_message(rest_message)
    return hunt_bonus

def cache_locate():
    pass

def cache_stash():
    pass


'''actions available in certain hexes'''

def seek_news_and_information(character, player_hex, console): #town, temple, or castle
    gather_info_roll = randint(1,6) + randint(1,6) + character.info_bonus[player_hex]
    if character.gold >= 5:
        console.display_message('Do you wish to spend 5 gold to loosen tongues? (y/n)') #need to handle choice
        character.gold -= 5
        gather_info_roll += 1
    if character.wits >= 5:
        gather_info_roll += 1

    if gather_info_roll == 2:
        console.display_message('Your inquiries uncover no news of note; nothing seems to be happening.')
    
    elif gather_info_roll == 3:
        console.display_message("You discover a thieves' den and pillage it while they are out.  You gain 50 gold.")
        character.gold += 50
    
    elif gather_info_roll == 4:
        temples = {(7,11):"Branwyn's Temple",
                   (10,21):'Sulwyth Temple',
                   (13,9):"Donat's Temple",
                   (18,5):'Temple of Zhor',
                   (20,18):'Temple of Duffyd'}
        secret_rites = choice(temples)
        console.display_message('You learn of secret rites at {secret_rites}.  You gain a small advantage when making offerings there.')
        if secret_rites in character.offering_bonus:
            character.offering_bonus[secret_rites] += 1
        else:
            character.offering_bonus[secret_rites] = 1
            
    elif gather_info_roll == 5:
        console.display_message('Your inquiries uncover no news of note; but you feel at home in this place and gain a small bonus when seeking information or hirelings.')
        if player_hex in character.info_bonus:
            character.info_bonus[player_hex] += 1
        else:
            character.info_bonus[player_hex] = 1
        if player_hex in character.hiring_bonus:
            character.hiring_bonus[player_hex] += 1
        else:
            character.hiring_bonus[player_hex] = 1
    
    elif gather_info_roll == 6:
        console.display_message('A large caravan is in town.  If you wish to visit them today, see event e129.')
    
    elif gather_info_roll == 7:
        console.display_message('Discover cheaper lodgings and food, pay half the normal price here.')
    
    elif gather_info_roll == 8:
        console.display_message('A cutpurse picks your pocket, stealing half your gold!')
        character.gold /= 2
    
    elif gather_info_roll == 9:
        console.display_message('You attract the attention of the local constabulary, see event e050.')
    
    elif gather_info_roll == 10:
        console.display_message('You discover the residence of a local magician, see event e016.')
    
    elif gather_info_roll == 11:
        console.display_message("You discover the local thieves' guild and are 'invited' to join.  If you do, you participate in a theft tonight and then flee the hex.  If you pay the guild their cut, you may return to this hex in the future. ")
        character.gold += 200
    
    elif gather_info_roll >= 12:
        console.display_message('A secret informant offers you valuable information for 10 gold.')
        secret_info = choice(['bogus secrets that prove worthless', 'event e147', 'event e143', 'event e144', 'event e145', 'event e146'])


def hire_followers(party, player_hex, console): #town or castle
    hiring_roll = randint(1,6) + randint(1,6) + party[0].hiring_bonus[player_hex]
    
    if hiring_roll == 2:
        console.display_message("A Freeman joins your party at no cost (except food and lodging).")
        freeman = characters.Character(None, None, 3, 4)
        party.append(freeman)
    elif hiring_roll == 3:
        console.display_message("A Lancer with a horse can be hired for 3 gold per day.")
        lancer = characters.Character(None, None, 5, 5, daily_wage=3, mounted=True)
        party.append(lancer)
    elif hiring_roll == 4:
        console.display_message("One or two mercenaries can be hired for 2 gold per day each.")
        mercenary = characters.Character(None, None, 4, 4, daily_wage=2)
        party.append(mercenary)
    elif hiring_roll == 5:
        console.display_message("Horse dealer in area, you can buy horses (for mounts) at 10 gold each.")
    elif hiring_roll == 6:
        console.display_message("Local guide available (see r205), hires for 2 gold per day.")
        guide = characters.Character(None, None, 2, 3, daily_wage=2)
        party.append(guide)
    elif hiring_roll == 7:
        console.display_message("Henchmen available, roll one die for the number available for hire, at 1 gold per day each.")
        henchmen = characters.Character(None, None, 3, 3, daily_wage=1)
        party.append(henchmen)
    elif hiring_roll == 8:
        console.display_message("Slave market, see event e163")
    elif hiring_roll == 9:
        console.display_message("Nothing available, but you gain some news and information, see r209 but subtract one (-1) from your dice roll there.")
    elif hiring_roll == 10:
        console.display_message("Honest horse dealer in area, can buy horses (for mounts) at 7 gold each.")
    elif hiring_roll == 11:
        console.display_message("Runaway boy or girl joins your party at no cost (except food and lodging), has combat skill 1, endurance 3.")
        runaway = characters.Character(None, None, 1, 3)
        party.append(runaway)
    elif hiring_roll >= 12:
        console.display_message("Porters in any quantity available, hire for ½ gold each per day. In addition, a local guide (r205) can be hired for 2 gold per day, has combat skill 1, endurance 2.")
        porters = characters.Character(None, None, 1, 2, daily_wage=0.5)
        guide = characters.Character(None, None, 1, 2, daily_wage=2)
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
    offering_roll = randint(1,6) + randint(1,6) + party[0].offering_bonus[player_hex]
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


def search_ruins(party, console): #ruins
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
        events.e132(party, console)
    elif ruin_event[0] == 'e133':
        events.e133(party, console)
    elif ruin_event[0] == 'e134':
        events.e134(party, console)
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
        events.e035(party, None, console)

        