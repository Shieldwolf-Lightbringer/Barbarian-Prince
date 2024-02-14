import characters
import game_actions
from hexmap import overland_map
from random import choice, randint

def e002(party, hex, console):
    north_tragoth_river = [(1,1),(2,1),(3,1),(3,2),(4,1),(5,1),(5,2),(6,1),(7,1),(8,1),(9,1),
                           (10,1),(11,1),(12,1),(13,1),(15,1),(16,1),(17,1),(18,1),(19,1),(20,1),]
    if hex in north_tragoth_river:
        event_roll = randint(1,6) - 3
        if hex in [(1,1),(15,1)]:
            event_roll += 1
        if event_roll >= 1:
            thugs = randint(1,6)
            enemy_party = []
            console.display_message(f'{thugs} Mercenary thugs, dressed by the usurpers as their royal guardsmen, are riding towards you!')
            for _ in range(thugs):
                enemy_party.append(characters.Character('Thug Guardsman', 'male', 5, 4, wealth_code=4, mounted=True))
            console.display_message('You have the option to negotiate, evade, or fight them.')


def e035(party, player_hex, console): # Spell of Chaos
    console.display_message('A guardian spell of chaos is activated as your party passes within. You and your entire party become mindless idiots and wander away.')
    days_mindless = 0
    for character in party:
        character.mindless = True
        if not character.heir:
            party.remove(character)
    while party[0].mindless:
        if randint(1,6) - days_mindless < 0:
            party[0].mindless = False
            return days_mindless
        else:
            #game_actions.move(player_hex, console)
            game_actions.starvation(party[0], party, console)
            days_mindless += 1

def e131(console): # Empty Ruins
    console.display_message('You spend the entire day fruitlessly searching the ruins, and find nothing.')

def e132(party, console): # Organized Search
    if len(party) > 1:
        console.display_message('Your organized search might help uncover something.')
        if randint(1,6) < len(party):
            game_actions.search_ruins(party, console)
        else:
            console.display_message('Despite your thoroughness, you turn up nothing of use.')
    else:
        console.display_message('You spend the entire day fruitlessly searching the ruins, and find nothing.')

def e133(party, console): # Plague
    console.display_message('After considerable searching during the day, you find a variety of items worth 50 gold pieces in all, among many skeletons.')
    party[0].gold += 50
    console.display_message('Tonight, before you start to eat, a plague of mind-madness begins to affect your party, due to an ancient curse upon this place.') 
    for character in party:
        if randint(1,6) >= 3:
            if not character.heir:
                console.display_message(f'Madness has destroyed the mind of {character.name}!  They crumple to heap and soon die, foaming at the mouth!')
                party.remove(character)
            else:
                console.display_message(f'Madness has taken the mind of {character.name}, but your northern blood helps you to survive! You awaken the next morning and find youself alone.')
                character.gold = 0
                character.possessions = []
                game_actions.starvation(character, party, console)
                for character in party:
                    if not character.heir:
                        party.remove(character)
                break
    #game_actions.escape()
            
def e134(party, console): # Unstable Ruins
    console.display_message('In the ruins there are many unstable walls and rocks, making your search very dangerous.')
    console.display_message('You can either give up searching these ruins, doing nothing else today, or you can press on.')
    for character in party:
        if randint(1,6) == 6:
            character.wounds += (randint(1,6) + randint(1,6))
    game_actions.search_ruins(party, console)

def e135(party, console): # Broken Columns
    console.display_message('Along a palisade of broken columns, you find an altar with an ancient inscription.')
    if any(character.magical for character in party):
        console.display_message('One of your sorcerous companions is able to decipher the inscriptions!')
        # 1-e042; 2-e043; 3-e044; 4-e045; 5-e046; 6-e047
    else:
        console.display_message('With none able to decipher the inscriptions, you are forced to leave empty-handed.')

def e136(party, console): # Hidden Treasures
    console.display_message('You uncover the remains of a palace treasure room!')
    party[0].gold += 100
    #1-e037; 2-e038; 3-e039; 4-e044; 5-500 gold; 6-nothing

def e137(party, console): # Inhabitants
    console.display_message('You encounter living things in the ruins!')
    # 1-e032; 2-e051; 3-e052; 4-e055; 5-e057; 6-e082

def e138(party, console): # Unclean
    console.display_message('The ruins are unclean, and have horrible, gruesome creatures populating them!')
    # 1-e032; 2-e033; 3-e034; 4-e056; 5-e082; 6-e098

def e139(party, console): # Minor Treasures
    console.display_message('You uncover a minor treasure!')
    # 1-wealth 25; 2-wealth 60; 3-e038; 4-e039; 5-e040; 6-e140
    minor_treasure_roll = randint(1,2)
    if minor_treasure_roll == 1:
        gold, item = game_actions.roll_treasure(25)
        party[0].gold += gold
        if item:
            party[0].add_item(item)
    elif minor_treasure_roll == 2:
        gold, item = game_actions.roll_treasure(60)
        party[0].gold += gold
        if item:
            party[0].add_item(item)


events_dict = {'e002': e002}