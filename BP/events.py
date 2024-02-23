import characters
import game_actions
from hexmap import overland_map
from random import choice, randint

# Not yet fully implemented
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


def e032(party, console): # Ghosts
    num_ghosts = randint(1,6) + 1
    ghost_party = []
    for _ in range(num_ghosts):
        ghost_party.append(characters.Character(name='Ghost', combat_skill=4, endurance=2))
    console.display_message(f'A group of {num_ghosts} ghosts surprise your party. They are guarding an ancient altar. If you kill all the ghosts, you can investigate the altar if you wish.')
    game_actions.combat(party, ghost_party, console, has_surprise='enemy')
    
    console.display_message('With the ghosts defeated, you turn to investigate the altar they guarded.')
    ghost_altar_roll = randint(1,6)
    ghost_altar = {1:'e037', 2:'e039', 3:'e041', 4:'e042', 5:'e044', 6:'nothing'}
    ghost_altar_event = ghost_altar[ghost_altar_roll]
    if ghost_altar_event == 'nothing': 
        console.display_message(f'The altar is broken and the inscriptions are too weathered; any magic this once held has long since dissipated.  At least you have put the {num_ghosts} ghosts to rest.')
    elif ghost_altar_event == 'e037': # Broken Chest
        e037(party, console)
    elif ghost_altar_event == 'e039': # Treasure Chest
        e039(party, console)
    elif ghost_altar_event == 'e041': # Vision Gem
        e041(party, console)
    elif ghost_altar_event == 'e042': # Alcove of Sending
        e042(party, console)
    elif ghost_altar_event == 'e044': # High Altar
        e044(party, console)


def e033(party, console): # Warrior Wraiths
    num_wraiths = randint(2,6)
    wraith_party = []
    for _ in range(num_wraiths):
        wraith_party.append(characters.Character(name='Wraith', combat_skill=6, endurance=9))
    console.display_message(f'A group of {num_wraiths} wraiths, the remnants of long dead super warriors, swiftly assault your party!  They strike first in combat against you.')
    game_actions.combat(party, wraith_party, console, has_first_strike='enemy')

    console.display_message('With the wraiths defeated, you discover that they were guarding plunder from an ancient battle.')
    wraith_plunder_roll = randint(1,6)
    wraith_plunder = {1:25, 2:50, 3:60, 4:70, 5:100, 6:100}
    wraith_plunder_value = wraith_plunder[wraith_plunder_roll]
    gold, item = game_actions.roll_treasure(wraith_plunder_value)
    party[0].gold += gold
    console.display_message(f'You find {gold} gold!')
    if item:
        party[0].add_item(item)
        console.display_message(f'You find a {item}!')


def e034(party, console): # Spectre of the Inner Tomb
    spectre_party = []
    spectre_party.append(characters.Character(name='Spectre', combat_skill=7, endurance=3, unearthly=True))
    console.display_message('Looking around the atrium of an old tomb, you notice a hidden passage to the interior. You pass within, but it is a long hall, taking the rest of the day to explore. You sense the malevolent presence of a Spectre. You can either retreat now, or continue.')
    console.display_message('Choosing to press onward, at the end of the day, before the evening meal, you finally reach the inner tomb, and find the Spectre. Normal weapons have no effect on the spectre!  It is only hurt by poison wounds or wounds from a magic sword!  Any priest, monk, magician, wizard, or witch will have magical weapons that are poison to the Spectre.')
    game_actions.combat(party, spectre_party, console)

    console.display_message('With the spectre defeated, you turn to investigate the treasure it guarded.')
    spectre_plunder_roll = randint(1,6)
    spectre_plunder = {1:5, 2:12, 3:25, 4:25, 5:60, 6:110}
    spectre_plunder_value = spectre_plunder[spectre_plunder_roll]
    gold, item = game_actions.roll_treasure(spectre_plunder_value)
    party[0].gold += gold
    console.display_message(f'You find {gold} gold!')
    if item:
        party[0].add_item(item)
        console.display_message(f'You find a {item}!')


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


def e037(party, console): # Broken Chest
    broken_chest_items = {'e180': 'healing potion',
                          'e181': 'cure poison vial',
                          'e182': 'gift of charm',
                          'e184': 'resistance talisman',
                          'e186': 'magic sword',
                          'e189': 'charisma talisman'}
    item = choice(['e180','e181','e182','e184','e186','e189'])
    special_item = broken_chest_items[item]
    console.display_message(f'You find a chest with a broken and cracked lid. Sorting through old mouldering cloths, you find a {special_item.title()}.')
    party[0].add_item(special_item)


def e038(party, console): # Cache under Stone
    stone_cache_items = {'e180': 'healing potion',
                         'e181': 'cure poison vial',
                         'e182': 'gift of charm',
                         'e185': 'poison drug',
                         'e187': 'anti-poison amulet',
                         'e190': 'nerve gas bomb'}
    item = choice(['e180','e181','e182','e185','e187','e190'])
    special_item = stone_cache_items[item]
    console.display_message(f'By chance you overturn a stone slab, jumping back as it crashes to the ground. You see that it uncovers an old cache of rotting food and other items. You find a {special_item.title()}.')
    party[0].add_item(special_item)


def e039(party, console): # Treasure Chest
    console.display_message('You find a locked chest. You know the lock may be trapped. You can either ignore it, or attempt to open it anyway.')
    trap_roll = randint(1,6)
    if trap_roll >= 3:
        game_actions.trap_lock(party[0], console)
    chest_roll = randint(1,6)
    if chest_roll == 6:
         console.display_message('Unbelievable! The chest is empty!')
    else:
        gold, item = game_actions.roll_treasure(60)
        party[0].gold += gold
        console.display_message(f'You find {gold} gold!')
        if item:
            party[0].add_item(item)
            console.display_message(f'You find a {item}!')


def e040(party, console): # Trapped Treasure Chest
    console.display_message('You find a locked treasure chest protected by a trap. You can either ignore it, or attempt to open it anyway.')
    trap_roll = randint(1,6)
    if trap_roll > party[0].wits:
        game_actions.trap_lock(party[0], console)

    chest_roll = randint(1,6)
    chest_contents = {1:5, 2:25, 3:50, 4:60, 5:70, 6:100}
    chest_result = chest_contents[chest_roll]
   
    gold, item = game_actions.roll_treasure(chest_result)
    party[0].gold += gold
    console.display_message(f'You find {gold} gold!')
    if item:
        party[0].add_item(item)
        console.display_message(f'You find a {item}!')


def e041(party, console): # Vision Gem
    console.display_message('You find a large, fixed stone with multiple facets. You gaze into it without thinking, and find you can look elsewhere.')
    vision_roll = randint(1,6)
    vision_gem_secrets = { 1:'e143', 2:'e144', 3:'e145', 4:'e146', 5:'e147', 6:'nothing of value'}
    vision_event = vision_gem_secrets[vision_roll]
    if vision_event == 'nothing of value': 
        console.display_message('While fascinating, your observations of far off people and places produce nothing you can use.')
    elif vision_event == 'e143': # Secret of the Temples
        e143(party, console)
    elif vision_event == 'e144': # Secret of Baron Huldra
        e144(party, console)
    elif vision_event == 'e145': # Secret of Lady Aeravir
        e145(party, console)
    elif vision_event == 'e146': # Secret of Count Drogat
        e146(party, console)
    elif vision_event == 'e147': # Clue to Treasure
        e147(party, console)


# Not yet fully implemented
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


# Not yet fully implemented
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
                                 

# Not yet fully implemented
def e046(party, console): # Gateway to Darkness
    console.display_message('In a passage near the altar, you have found one of the dreaded black portals. The darkness within the archway absorbs all light and reflects no image, yet seems to pulse and undulate.')
    # Abandon all followers and mounts, fight guardian (7,7), travel backwards in time 2d6 days.
    # Portal is permanent once discovered and can be reused.  Each time, there is an additional guardian.


# Not yet fully implemented
def e047(party, console): # Mirror of Reversal
    console.display_message('Propped against a column near the altar you see an old mirror.  Looking into it, you see an image of yourself twisted into an evil shape.  This creature leaps from the mirror and attacks you!')
    evil_twin = party[0]
    # game_actions.combat(party, evil_twin), any followers accidentally strike you on d6 5+, if you win, gain wits += 1 and all wealth and possessions


# Not fully implemented, need to loot after battle.  Maybe in combat function?
def e051(party, console): # Bandits
    num_bandits = len(party) + 2
    console.display_message(f'You are ambushed by {num_bandits} bandits, who surprise you in combat.')
    bandit_party = []
    bandit_party.append(characters.Character(name='Bandit Chief', combat_skill=6, endurance=6, wealth_code=15))
    for _ in range(num_bandits - 1):
        bandit_party.append(characters.Character(name='Bandit', combat_skill=5, endurance=4, wealth_code=1))
    game_actions.combat(party, bandit_party, console, has_surprise='enemy')


# Not fully implemented
def e052(party, console): # Goblins
    num_goblins = randint(1,6) + randint(1,6)
    console.display_message(f'You sight a band of {num_goblins} goblins, lead by a Hobgoblin, in the distance.  You can either escape the area or attempt to follow them.')
    goblin_party = []
    goblin_party.append(characters.Character(name='Hobgoblin', combat_skill=6, endurance=5, wealth_code=5))
    for _ in range(num_goblins):
        goblin_party.append(characters.Character(name='Goblin', combat_skill=3, endurance=3, wealth_code=1))
    #game_actions.escape()
    #game_actions.follow_characters()
    '''If you follow them, after the follow movement (r219) roll one die. If the result exceeds your wit & wiles the band
discovers you and attacks, but your party will get the first strike in combat (r220). If they don't discover you, roll
one die to see where they lead you: 1-e054; 2,3,4,5,6-e053.'''


def e053(party, other_party, console): # Campsite
    pass


def e054(party, console): # Goblin Keep
    pass


def e055(party, console): # Orcs
    num_orcs = randint(1,6) + randint(1,6)
    console.display_message(f'You sight a band of {num_orcs} orcs, lead by a chieftan, in the distance.  You can either escape the area or attempt to follow them.')
    orc_party = []
    orc_party.append(characters.Character(name='Chieftan', combat_skill=5, endurance=6, wealth_code=7))
    for _ in range(num_orcs):
        orc_party.append(characters.Character(name='Orc Warrior', combat_skill=4, endurance=5, wealth_code=1))
    #game_actions.escape()
    #game_actions.follow_characters()
    '''If you follow them, after the follow movement roll one die. If the result exceeds your wit & wiles the Orcs
discover you and attack, but your party gets first strike in combat (r220). If they don't discover you, roll one die
to see where they lead you: 1-Orc Tower e056; 2,3,4,5,6-Campsite e053.
If they lead you to a campsite, you can either avoid them by escaping to an adjacent hex (r218) or you can
make a surprise attack in combat (r220) against them at their campsite.'''


def e056(party, console): # Orc Tower
    num_orcs = randint(1,6) + 1
    console.display_message(f'You see the dark tower of an Orc Warlord.  This area is full of orc and worse things.  A war-patrol of {num_orcs} orcs, led by a demi-Troll warchief, spots you!.  You can either surrender to them or attempt to escape.')
    orc_party = []
    orc_party.append(characters.Character(name='Warchief', combat_skill=8, endurance=7, wealth_code=10))
    for _ in range(num_orcs):
        orc_party.append(characters.Character(name='Orc Warrior', combat_skill=5, endurance=5, wealth_code=2))
    #game_actions.escape()
    #surrender e061()


def e057(party, console): # Troll
    console.display_message('A huge stone-skinned Troll confronts your party.')
    troll_party = []
    troll_party.append(characters.Character(name='Troll', combat_skill=8, endurance=8, wealth_code=15, regenerates=True))
    game_actions.combat(party, troll_party, console, has_surprise='enemy')

    console.display_message('If you kill the troll, its stone-skin is a valuable item. Whenever you have an opportunity to buy food at a town, castle, temple, or from merchants you can sell the skin for 50 gold. It is also known that Count Drogat, of Drogat Castle, will treasure the gift should you manage to get a personal -audience with him.')
    party[0].add_item('troll stone-skin')


def e082(party, console): # Spectre
    console.display_message('An unearthly spectre from the astral plane appears in the midst of your party, casting a hideous miasma in all directions.')
    target = choice(party)
    console.display_message(f"{target.name} is the spectre's victim!  {target.name} is turned to smoke and taken by the spectre to the astral plane, never to be seen again!")
    if not target.heir:
        target.alive = False
        party.remove(target)
    elif target.heir:
        target.alive = False
    '''However, a spectre is a magical being, and can be stopped using any possession that protects against magic attacks or injury.'''


def e098(party, console): # Dragon
    console.display_message('You encounter a huge, winged, fire-breathing Dragon!')
    dragon_party = []
    lair_roll = randint(1,6)
    if lair_roll <= 2:
        dragon_party.append(characters.Character(name='Dragon', combat_skill=10, endurance=11, wealth_code=0, flying=True))
        console.display_message('You have found the mighty beast at its lair, surrounded by treasure!')
        gold, item = game_actions.roll_treasure(110)
        gold2, item2 = game_actions.roll_treasure(60)
        party[0].gold += gold 
        party[0].gold += gold2
        console.display_message(f'You find {gold} gold!')
        if item:
            party[0].add_item(item)
            console.display_message(f'You find a {item}!')
        if item2:
            party[0].add_item(item2)
            console.display_message(f'You find a {item2}!')
    else:
        dragon_party.append(characters.Character(name='Dragon', combat_skill=10, endurance=11, wealth_code=30, flying=True))
    ''' If you must fight it in combat (r220) you cannot escape. Your options are:
die roll evade fight
1 escape flying r313 surprise r302
2 escape r315 surprise r303
3 hide r318 attack r305
4 hide r320 attacked r306
5 attacked r306 surprised r308
6 surprised r308 surprised r309'''
    '''Note: if you kill the Dragon, the Dragon's eye is greatly valued by high priests of the temples throughout the
land, and may be of assistance in gaining an audience. Carrying the Dragon's eye counts as one load for
transport purposes (r206).'''


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
        e131(console) # Empty Ruins


# Not yet fully implemented
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


# Not yet fully implemented
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
            if inscription_event == 'e042': # Alcove of Sending
                e042(party, console)
            elif inscription_event == 'e043': # Small Altar
                e043(party, console)
            elif inscription_event == 'e044': # High Altar
                e044(party, console)
            elif inscription_event == 'e045': # Arch of Travel
                e045(party, console)
            elif inscription_event == 'e046': # Gateway to Darkness (time portal)
                e046(party, console)
            elif inscription_event == 'e047': # Mirror of Reversal
                e047(party, console)
    else:
        console.display_message('With none able to decipher the inscriptions, you are forced to leave empty-handed.')


def e136(party, console): # Hidden Treasures
    console.display_message('You uncover the remains of a palace treasure room!')
    treasure_room_roll = randint(1,6)
    treasure_rooms = {1:'e037', 2:'e038', 3:'e039', 4:'e044', 5:'500 gold', 6:'nothing'}
    hidden_treasure_event = treasure_rooms[treasure_room_roll]
    if hidden_treasure_event == 'nothing':
        console.display_message('Unfortunately, the treasure room was looted long ago.  You find nothing of value.')
    elif hidden_treasure_event == '500 gold':
        console.display_message('You find piles of gold coins!  There is enough here to raise your army and retake your kingdom!')
        party[0].gold += 500
    elif hidden_treasure_event == 'e037': # Broken Chest
        e037(party, console)
    elif hidden_treasure_event == 'e038': # Cache under Stone
        e038(party, console)
    elif hidden_treasure_event == 'e039': # Treasure Chest
        e039(party, console)
    elif hidden_treasure_event == 'e044': # High Altar
        e044(party, console)


def e137(party, console): # Inhabitants
    console.display_message('You encounter creatures in the ruins!')
    inhabitants_roll = randint(1,6)
    ruin_inhabitants = {1:'e032', 2:'e051', 3:'e052', 4:'e055', 5:'e057', 6:'e082'}
    inhabitants_event = ruin_inhabitants[inhabitants_roll]
    if inhabitants_event == 'e032':   # Ghosts
        e032(party, console)
    elif inhabitants_event == 'e051': # Bandits
        e051(party, console)
    elif inhabitants_event == 'e052': # Goblins
        e052(party, console)
    elif inhabitants_event == 'e055': # Orcs
        e055(party, console)
    elif inhabitants_event == 'e057': # Troll
        e057(party, console)
    elif inhabitants_event == 'e082': # Spectre
        e082(party, console)    


# Not yet fully implemented
def e138(party, console): # Unclean
    console.display_message('The ruins are unclean, and have horrible, gruesome creatures populating them!')
    unclean_roll = randint(1,6)
    unclean_inhabitants = {1:'e032', 2:'e033', 3:'e034', 4:'e056', 5:'e082', 6:'e098'}
    unclean_event = unclean_inhabitants[unclean_roll]
    if unclean_event == 'e032':   # Ghosts
        e032(party, console)
    elif unclean_event == 'e033': # Warrior Wraiths
        e033(party, console)
    elif unclean_event == 'e034': # Spectre of the Inner Tomb
        e034(party, console)
    elif unclean_event == 'e056': # Orc Tower
        e056(party, console)
    elif unclean_event == 'e082': # Spectre
        e082(party, console)
    elif unclean_event == 'e098': # Dragon
        e098(party, console)  

def e139(party, console): # Minor Treasures
    minor_treasures = {1:25, 2:60, 3:'e038', 4:'e039', 5:'e040', 6:'e140'}
    minor_treasure_roll = randint(1,6)
    minor_treasure_event = minor_treasures[minor_treasure_roll]
    if minor_treasure_event == 25:
        gold, item = game_actions.roll_treasure(25)
        party[0].gold += gold
        console.display_message(f'You find {gold} gold!')
        if item:
            party[0].add_item(item)
            console.display_message(f'You find a {item}!')
    elif minor_treasure_event == 60:
        gold, item = game_actions.roll_treasure(60)
        party[0].gold += gold
        console.display_message(f'You find {gold} gold!')
        if item:
            party[0].add_item(item)
            console.display_message(f'You find a {item}!')
    elif minor_treasure_event == 'e038': # Cache under Stone
        e038(party, console)
    elif minor_treasure_event == 'e039': # Treasure Chest
        e039(party, console)
    elif minor_treasure_event == 'e040': # Trapped Treasure Chest
        e040(party, console)
    elif minor_treasure_event == 'e140': # Magic Box
        e140(party, console)


# Not yet fully implemented
def e140(party, console): # Magic Box
    console.display_message('You find a magic box!')
    pass


# Not yet fully implemented
def e143(party, console): # Secret of the Temples
    console.display_message('You learn the secret of all temple priests - for the Chaga drug. This is available in any town where you buy food, for 2 gold pieces a serving.')
    pass


# Not yet fully implemented
def e144(party, console): # Secret of Baron Huldra
    console.display_message('You learn the secret of Baron Huldra.')
    pass


# Not yet fully implemented
def e145(party, console): # Secret of Lady Aeravir
    console.display_message('You learn the secret of Lady Aeravir.')
    pass


# Not yet fully implemented
def e146(party, console): # Secret of Count Drogat
    console.display_message('You learn the secret of Count Drogat.')
    pass


# Not yet fully implemented
def e147(party, console): # Clue to Treasure
    console.display_message('You learn the secret location of a nearby treasure.')
    pass


events_dict = {'e002': e002}