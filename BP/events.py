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
    while len(party) > 1:
        for character in party:
            if not character.heir:
                party.remove(character)
    while party[0].mindless:
        if randint(1,6) - days_mindless < 0:
            party[0].mindless = False
            return days_mindless
        else:
            from states.gameplay import hexagon_dict
            random_move = choice(['n','ne','se','s','sw','nw'])
            player_hex = game_actions.move(random_move, player_hex, hexagon_dict, console)
            game_actions.starvation(party[0], party, console)
            days_mindless += 1


def e042(party, console): # Alcove of Sending
    console.display_message('Behind the altar, you find a small alcove inscribed with runes.')
    caster_in_party = any([character.magician, character.wizard, character.witch] for character in party)
    if caster_in_party:
        caster_character = [character for character in party if character.magician or character.wizard or character.witch]
        if caster_character:
            caster_companion = choice(caster_character)
            console.display_message(f'{caster_companion.name} informs you that this is an Alcove of Sending.  With it, you can send your astral form to compel audience with one of the mayors, high priests, or castle lords. However, you can only use this altar once and any companions granted by the audience cannot return through the astral realm with you.')  
        #need to implement astral audience


def e043(party, console): # Small Altar
    altar_items = {'e186':'Magic Sword',
                   'e189':'Charisma Talisman',
                   'e191':'Resistance Ring',
                   'e192':'Ressurection Necklace',
                   'e193':'Shield of Light',
                   'e194':'Royal Helm of the Northlands'}
    item = choice(['e186','e189','e191','e192','e193','e194'])
    special_item = altar_items[item]
    console.display_message(f'Upon the altar is displayed a {special_item}.  However, the air around the altar shimmers with magical energy.')
    altar_spell = choice(['magic shock field', 'magic shock field', 'magic fire', 'magic fire','poison air', 'fear'])
    caster_in_party = any([character.magician, character.wizard, character.witch] for character in party)
    if caster_in_party:
        caster_character = [character for character in party if character.magician or character.wizard or character.witch]
        if caster_character:
            caster_companion = choice(caster_character)
            console.display_message(f'{caster_companion.name} warns you that the altar is protected by a {altar_spell} spell!')
    else:
        console.display_message(f'Without any counsel on the nature of the magic, you must decide whether to risk it or abandon the {special_item}.')
    
    if altar_spell == 'magic shock field':
        console.display_message('Try as you might, you cannot pass through the field and reach the altar.  You are shocked for 1 wound in the process.')
        party[0].wounds += 1
    elif altar_spell == 'magic fire':
        fire1, fire2 = randint(1,6), randint(1,6)
        console.display_message(f'You are engulfed in magical flames, suffering {fire1} wounds.')
        party[0].wounds += fire1
        console.display_message(f'You retrieve the {special_item}, and suffer {fire2} more wounds as you make your way out of the flames with it.')
        party[0].wounds += fire2
        party[0].add_item(special_item)
    elif altar_spell == 'poison air':
        poison =  randint(1,6)
        console.display_message(f'The air is filled with poisonous vapors, you suffer {poison} poision wounds while retreiving the {special_item}.')
        party[0].poison_wounds += poison
        party[0].add_item(special_item)
    elif altar_spell == 'fear':
        console.display_message(f'Though your party members quake in fear of the evil spell protecting the altar, it can do you no harm. You recover the {special_item} without injury.')
        party[0].add_item(special_item)


def e044(party, console): # High Altar
    console.display_message('The inscriptions reveal this to be a high altar of godly power!')
    priest_monk_in_party = any([character.priest, character.monk] for character in party)
    if priest_monk_in_party:
        holy_character = [character for character in party if any([character.priest, character.monk])]
        if holy_character:
            invoker = choice(holy_character)
            console.display_message(f'One of your godly companions, {invoker.name} knows the invocations to use at this altar, and will attempt them if you wish.') 
            invocations_roll = randint(1,6)
            if invocations_roll == 1:
                console.display_message(f'{invoker.name} is incinerated in godly fires and dies!')
                party.remove(invoker)
            elif invocations_roll == 2:
                console.display_message('Lightning and earthquakes destroy the high altar! Everyone is injured by flying stones and fire!')
                for character in party:
                    character.wounds += randint(1,6)
            elif invocations_roll == 3:
                console.display_message(f'It was an altar to the wrong god, {invoker.name} suffers 1 wound for the transgression.')
                invoker.wounds += 1
            elif invocations_roll == 4:
                console.display_message('A voice of the gods sounds forth and gives you a riddle none can solve, and a prophecy none can understand.')
            elif invocations_roll == 5:
                console.display_message('Voices of the gods give a prophecy that seems to promise treasure! See event 147.')
                #e147(party, console)
            elif invocations_roll == 6:
                console.display_message('One of the gods appears, issuing thunderbolts and flames, pledging support to your cause. In an astral vision you see the gods striking down the usurpers to your throne, and telling Northlands priests that your reign shall be holy. You will regain your throne and win the game if you can return alive to the northlands (any hex north of the Tragoth River) within the next 30 days. However, experiencing the power of the gods directly has weakened your human frame, your endurance is permanently reduced by one.  In gratitude for the godly support, you must give all your money away to the gods of the altar instantly, or be struck down dead.')
                party[0].endurance -= 1
                party[0].gold = 0


def e045(party, console): # Arch of Travel
    console.display_message('Behind the altar, you find a metal-banded archway inscribed with runes.')
    caster_in_party = any([character.magician, character.wizard, character.witch] for character in party)
    if caster_in_party:
        caster_character = [character for character in party if character.magician or character.wizard or character.witch]
        if caster_character:
            caster_companion = choice(caster_character)
            console.display_message(f'{caster_companion.name} tells you that this is an Arch of Travel.  Your party may use it to magically transfer to any hex on the map, though time will contiue to pass.')
    # Arch is permanent when discovered (place icon on hex), and may be reused as long as you have a magical character in your party
    # Arch travel adds randint(1,6) days to the day tracker.  Travel is only one-way.
                                 

def e046(party, console): # Gateway to Darkness
    console.display_message('In a passage near the altar, you have found one of the dreaded black portals. The darkness within the archway absorbs all light and reflects no image, yet seems to pulse and undulate.')
    # Abandon all followers and mounts, fight guardian (7,7), travel backwards in time 2d6 days.
    # Portal is permanent once discovered and can be reused.  Each time, there is an additional guardian.


def e047(party, console): # Mirror of Reversal
    console.display_message('Propped against a column near the altar you see an old mirror.  Looking into it, you see an image of yourself twisted into an evil shape.  This creature leaps from the mirror and attacks you!')
    evil_twin = party[0]
    # game_actions.combat(party, evil_twin), any followers accidentally strike you on d6 5+, if you win, gain wits += 1 and all wealth and possessions


def e131(console): # Empty Ruins
    console.display_message('You spend the entire day fruitlessly searching the ruins, and find nothing.')


def e132(party, player_hex, console): # Organized Search
    if len(party) > 1:
        console.display_message('Your organized search might help uncover something.')
        if randint(1,6) < len(party):
            game_actions.search_ruins(party, player_hex, console)
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
                if len(party) > 1:
                    character.gold = 0
                    character.possessions = []
                game_actions.starvation(character, party, console)
                while len(party) > 1:
                    for character in party:
                        if not character.heir:
                            party.remove(character)
                
    #game_actions.escape()


def e134(party, player_hex, console): # Unstable Ruins
    console.display_message('In the ruins there are many unstable walls and rocks, making your search very dangerous. You can either give up searching these ruins, doing nothing else today, or you can press on.')
    for character in party:
        if randint(1,6) == 6:
            crushing_wounds = (randint(1,6) + randint(1,6))
            console.display_message(f'{character.name} is crushed by falling rocks for {crushing_wounds} wounds!')
            character.wounds += crushing_wounds
            if not character.alive:
                party.remove(character)
    game_actions.search_ruins(party, player_hex, console)


def e135(party, console): # Broken Columns
    console.display_message('Along a palisade of broken columns, you find an altar with an ancient inscription.')
    inscriptions_roll = randint(1,6)
    ancient_inscriptions = {1:'e042', 2:'e043', 3:'e044', 4:'e045', 5:'e046', 6:'e047'}
    inscription_event = ancient_inscriptions[inscriptions_roll]
    magical_in_party = any(character.magical for character in party)
    if magical_in_party:
        magical_character = [character for character in party if character.magical]
        if magical_character:
            sorcerous_companion = choice(magical_character)
            console.display_message(f'{sorcerous_companion.name} is able to decipher the inscriptions!')
            if inscription_event == 'e042':
                e042(party, console)
            elif inscription_event == 'e043':
                e043(party, console)
            elif inscription_event == 'e044':
                e044(party, console)
            elif inscription_event == 'e045':
                e045(party, console)
            elif inscription_event == 'e046':
                e046(party, console)
            elif inscription_event == 'e047':
                e047(party, console)
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
    # 1-wealth 25; 2-wealth 60; 3-e038; 4-e039; 5-e040; 6-e140
    minor_treasure_roll = randint(1,2)
    if minor_treasure_roll == 1:
        gold, item = game_actions.roll_treasure(25)
        party[0].gold += gold
        console.display_message(f'You find {gold} gold!')
        if item:
            party[0].add_item(item)
            console.display_message(f'You find a {item}!')
    elif minor_treasure_roll == 2:
        gold, item = game_actions.roll_treasure(60)
        party[0].gold += gold
        console.display_message(f'You find {gold} gold!')
        if item:
            party[0].add_item(item)
            console.display_message(f'You find a {item}!')


events_dict = {'e002': e002}