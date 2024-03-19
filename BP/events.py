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
                enemy_party.append(characters.Character(title='Usurper Thug', combat_skill=5, endurance=4, wealth_code=4, mounted=True))
            console.display_message('You have the option to negotiate, evade, or fight them.')


def e003(party, console): # Swordsman on horse
    pass


def e004(party, console): # Mercenary Band
    pass


def e005(party, console): # Amazons
    pass


def e006(party, console): # Dwarf
    pass


def e007(party, console): # Elf
    pass


def e008(party, console): # Halfling
    pass


def e009(party, console): # Farm
    console.display_message('You spot a small farm ahead. You may detour around it, but that will consume the rest of the day, ending all travel for today. Alternately, you can go up to it. If you approach the farm, you must decide whether to make it a friendly approach, or a raid.')
    approach = choice(['friendly', 'raid'])
    farm_type_roll = randint(1,6) + randint(1,6)
    if farm_type_roll in [2, 3, 10]:
        e012(party, console, approach)
    elif farm_type_roll in [4, 7]:
        e011(party, console, approach)
    elif farm_type_roll == 5:
        e014(party, console, approach)
    elif farm_type_roll == 6:
        e010(party, console, approach)
    elif farm_type_roll == 8:
        e013(party, console, approach)
    elif farm_type_roll == 9:
        e015(party, console, approach)
    elif farm_type_roll in [11, 12]:
        e016(party, console, approach)


def e010(party, console, approach=None): # Starving Farmer
    if approach == 'raid':
        console.display_message('The farmer and his family are quickly killed, no combat is necessary, but you find he was poor and starving, no food or money are gained.')
    else:
        console.display_message('The farmer has had a ruined harvest and his family is now starving. He begs the charity of 5 food units from you.')
        charity_option = choice(['yes', 'no'])
        if party[0].possessions.count('ration') < 5:
            console.display_message('However, without enough food to spare you are forced to leave the farmer and his family to their fate.')
        elif party[0].possessions.count('ration') >= 5:
            if charity_option == 'yes':
                console.display_message('You give the farmer and his family the rations they requested, and they praise you and bless you for your generosity.')
                for _ in range(5):
                    party[0].possessions.remove('ration')
            elif charity_option == 'no':
                console.display_message('Despite having the rations to spare, you refuse the farmer and his family.  All of your followers are disgusted by your evil temper.')
                for character in party:
                    game_actions.desertion(character, party, console, 'your evil temper')


### Need to correctly implement purchasing food
def e011(party, console, approach=None): # Peaceful Farmer
    if approach == 'raid':
        console.display_message('The farmer and his family attempt to fight off your raid!')
        farmer_party = []
        farmer_party.append(characters.Character(name='Farmer Clan', title='Farmer Clan', combat_skill=4, endurance=7, wealth_code=1))
        if game_actions.combat(party, farmer_party, console):
            food_plunder = randint(1,6) * 4
            console.display_message(f'Having slaughtered the entire family, you find {food_plunder} rations as plunder.')
            game_actions.distribute_rations(party, food_plunder)
    else:
        console.display_message('The farmer is generous, provides food and lodging for your entire party tonight at no cost. Tomorrow morning, he will sell you food units at the rate of 4 units per gold piece, and will sell as much as you wish to buy.')
        game_actions.purchase_rations(party, console, 4)
        if randint(1,6) == 6:
            console.display_message("As you are leaving, the farmer's youngest son joins you for a life of adventure.")
            party.append(characters.Character(title='Young Farmer', sex='male', combat_skill=3, endurance=4, guide=True))


### Need to correctly implement turn by turn reinforcement rolls and purchasing food
def e012(party, console, approach=None): # Farmer with Protector
    if approach == 'raid':
        console.display_message('The farmer and his family bolt the doors, send smoke signals, and attempt to fight off your raid.')
        farmer_party = []
        farmer_party.append(characters.Character(name='Farmer Clan', title='Farmer Clan', combat_skill=4, endurance=7, wealth_code=2))
        reinforcement_roll = randint(1,6)
        if reinforcement_roll >= 3:
            protector = characters.Character(title='Protector', combat_skill=6, endurance=5, wealth_code=25)
            farmer_party.append(protector)
            for _ in range(4):
                farmer_party.append(characters.Character(title='Man at Arms', combat_skill=5, endurance=5, wealth_code=4))
        if game_actions.combat(party, farmer_party, console, has_first_strike='player'):
            console.display_message('Having slaughtered the entire family, you discover the treasure they were attempting to hide.')
            e040(party, console)
    else:
        console.display_message('The farmer warns you off his land, but will sell you food at 2 units per gold piece, in any quantity you desire.  Afterwards, you continue on your way.')
        game_actions.purchase_rations(party, console, 2)


### Need to correctly implement purchasing food and horses
def e013(party, console, approach=None): # Rich Peasant Family
    if approach == 'raid':
        console.display_message('The family retainers rush to mount a defense against your raid!')
        retainer_party = []
        for _ in range(4):
            retainer_party.append(characters.Character(title='Retainer', combat_skill=4, endurance=4, wealth_code=1))
        if game_actions.combat(party, retainer_party, console):
            console.display_message('With their servants dead, the family takes up arms to resist you!')
            farmer_party = []
            farmer_party.append(characters.Character(name='Rich Farmer Clan', title='Rich Farmer Clan', combat_skill=5, endurance=6, wealth_code=30))
            if game_actions.combat(party, farmer_party, console):
                food_plunder = randint(1,6) * 6
                console.display_message(f'Having slaughtered the entire family, you find {food_plunder} rations as plunder.')
                game_actions.distribute_rations(party, food_plunder)
    else:
        console.display_message('The family provides food and lodging as if you are in town, with the same penalties if you refuse to pay.')
        stables_roll = randint(1,6)
        if stables_roll >= 4:
            horses_available = randint(1,6)
            price_per_horse = randint(1,6) * 2
            console.display_message(f'The family also has stables with {horses_available} horses avavalable to purchase at {price_per_horse} each.')
        console.display_message('They will sell you food at 2 units per gold piece, in any quantity you desire.')
        game_actions.purchase_rations(party, console, 2)


### Need to correctly implement general inquiries
def e014(party, console, approach=None): # Hostile Reaver Clan
    hostile_reaver_party = []
    hostile_reaver_party.append(characters.Character(title='Clan Leader', combat_skill=5, endurance=5, wealth_code=10))
    num_reavers = randint(1,6) + 1
    for _ in range(num_reavers):
        hostile_reaver_party.append(characters.Character(title='Clan Member', combat_skill=4, endurance=4, wealth_code=4))

    if approach == 'raid':
        console.display_message('You have encountered a hostile reaver clan!')
        game_actions.combat(party, hostile_reaver_party, console)
    else:
        if len(hostile_reaver_party) >= len(party):
            console.display_message('The reaver clan attempts a surprise attack!')
            game_actions.combat(party, hostile_reaver_party, console, has_first_strike='enemy')
        else:
            console.display_message('The reaver clan bars the house and bids you pass on. You can either pass on, or make general inquiries.')
            if 'general inquiries r342':
                game_actions.combat(party, hostile_reaver_party, console, has_first_strike='enemy')


## Need to correctly implement general inquiries and purchasing food and horses
def e015(party, console, approach=None): # Friendly Reaver Clan
    friendly_reaver_party = []
    friendly_reaver_party.append(characters.Character(title='Clan Leader', combat_skill=5, endurance=4, wealth_code=7))
    num_reavers = randint(1,6)
    for _ in range(num_reavers):
        friendly_reaver_party.append(characters.Character(title='Clan Member', combat_skill=4, endurance=4, wealth_code=4))

    if approach == 'raid':
        console.display_message('There is a battle between your party and the reaver clan.')
        game_actions.combat(party, friendly_reaver_party, console)
    else:
        console.display_message('The clan leader will discuss terms with you, see r342. Unless combat results, he will also sellvfood at 2 units per gold piece, and horses at 6 gold pieces each, regardless of whether he joins your party or not.')


def e016(party, console, approach=None): # Magician's Home
    if approach == 'raid':
        console.display_message('')
        '''magician calls upon his powers to defeat and destroy your party. Roll one die for the number of wounds
you suffer, one of which is poisoned. All your followers die or flee, deserting you. You must abandon everything
you cannot carry yourself. You will save any mount you are riding, and its loads, but no other mounts can be
saved. If you have the Resistance Talisman (el84) you can stop his powers and destroy the magician in battle
at the cost of destroying the talisman. If you do, roll one die for the wealth code of the magician: 1-5; 2,3-25;
4,5-60; 6-110.'''
    else:
        console.display_message('The magician insists you stay the night and tell him of your adventures to date. You must provide your own food for the day, as he has a small larder.')
        '''He may be willing to discuss joining your party, he
is combat skill 3, endurance 5, see r342 if you wish to try. If you don't, or do and avoid a combat situation, he
will give you a magic gift, roll once on line "B" of the Treasure Table (r226) for the item received.'''


def e017(party, console): # Peasant Mob in Hot Pursuit
    mob = (randint(1,6) + randint(1,6)) * 2
    console.display_message(f'A large mob of {mob} angry farmers and villagers are after you! You are trapped and must fight your way out.')
    mob_party = []
    mob_party.append(characters.Character(title='Peasant Leader', combat_skill=3, endurance=2, wealth_code=2))
    for _ in range(mob - 1):
        mob_party.append(characters.Character(title=choice(['Angry Farmer', 'Angry Peasant', 'Angry Villager']), combat_skill=2, endurance=2))
    game_actions.combat(party, mob_party, console)


def e018(party, console): # Priest
    pass


def e019(party, console): # Hermit Monk
    pass


def e020(party, console): # Travelling Monk
    pass


def e021(party, console): # Warrior Monks
    pass


def e022(party, console): # Random Monks
    random_monks_roll = randint(1,3)
    if random_monks_roll == 1:
        e019(party, console)
    elif random_monks_roll == 2:
        e020(party, console)
    elif random_monks_roll == 3:
        e021(party, console)


def e023(party, console): # Wizard
    pass


def e024(party, console): # Wizard Mind-Control Attack
    pass


def e025(party, console): # Wizard Advice
    pass


def e026(party, console): # Search For Treasure
    pass


def e027(party, console): # Ancient Treasure
    pass


def e028(party, console): # Cave Tombs
    pass


def e029(party, console): # Danger and Treasure
    pass


def e030(party, console): # Mummies
    pass


def e031(party, console): # Looted Tomb
    pass


def e032(party, console): # Ghosts
    num_ghosts = randint(1,6) + 1
    ghost_party = []
    for _ in range(num_ghosts):
        ghost_party.append(characters.Character(title='Ghost', race='Undead', combat_skill=4, endurance=2))
    console.display_message(f'A group of {num_ghosts} ghosts attack your party. They are guarding an ancient altar. If you kill all the ghosts, you can investigate the altar if you wish.')
    
    if game_actions.combat(party, ghost_party, console, has_surprise='enemy'):
    
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
        wraith_party.append(characters.Character(title='Warrior Wraith', race='Undead', combat_skill=6, endurance=9))
    console.display_message(f'A group of {num_wraiths} wraiths, the remnants of long dead super warriors, swiftly assault your party!  They strike first in combat against you.')
    
    if game_actions.combat(party, wraith_party, console, has_first_strike='enemy'):

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
    spectre_party.append(characters.Character(title='Spectre', race='Undead', combat_skill=7, endurance=3, unearthly=True))
    console.display_message('Looking around the atrium of an old tomb, you notice a hidden passage to the interior. You pass within, but it is a long hall, taking the rest of the day to explore. You sense the malevolent presence of a Spectre. You can either retreat now, or continue.')
    console.display_message('Choosing to press onward, at the end of the day, before the evening meal, you finally reach the inner tomb, and find the Spectre. Normal weapons have no effect on the spectre!  It is only hurt by poison wounds or wounds from a magic sword!  Any priest, monk, magician, wizard, or witch will have magical weapons that are poison to the Spectre.')
    
    if game_actions.combat(party, spectre_party, console):

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


def e036(party, console): # Golem at the Gate
    pass


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
                invoker.alive = False
                party.remove(invoker)
            elif invocations_roll == 2:
                console.display_message('Lightning and earthquakes destroy the high altar! Everyone is injured by flying stones and fire!')
                for character in party:
                    godly_wrath_roll = randint(1,6)
                    console.display_message(f'{character.name} suffers {godly_wrath_roll} wounds from flying stone and fire!')
                    character.wounds += godly_wrath_roll
            elif invocations_roll == 3:
                console.display_message(f'It was an altar to the wrong god, {invoker.name} suffers 1 wound for the transgression.')
                invoker.wounds += 1
            elif invocations_roll == 4:
                console.display_message('A voice of the gods sounds forth and gives you a riddle none can solve, and a prophecy none can understand.')
            elif invocations_roll == 5:
                console.display_message('Voices of the gods give a prophecy that seems to promise treasure!')
                e147(party, console)
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
    mirror_party = []
    console.display_message('Propped against a column near the altar you see an old mirror.  Looking into it, you see an image of yourself twisted into an evil shape.  This creature leaps from the mirror and attacks you!')
    evil_twin = party[0]
    mirror_party.append(evil_twin)
    # game_actions.combat(party, evil_twin), any followers accidentally strike you on d6 5+, if you win, gain wits += 1 and all wealth and possessions


def e048(party, console): # Fugitive
    pass


def e049(party, console): # Travelling Minstrel
    pass


def e050(party, console, bonus=0): # Local Constabulary
    constable_party = []
    if randint(1,6) > 5:
        mounted_constables = randint(1,6) + 1 + bonus
        for _ in range(mounted_constables):
            constable_party.append(characters.Character(title='Mounted Constable', combat_skill=5, endurance=4, wealth_code=4, mounted=True))
        console.display_message(f'You are confronted by {mounted_constables} mounted constables.')    
    else:
        constables = randint(1,6) + 3 + bonus
        for _ in range(constables):
            constable_party.append(characters.Character(title='Constable', combat_skill=5, endurance=4, wealth_code=4))
        console.display_message(f'You are confronted by {constables} constables.')

    game_actions.combat(party, constable_party, console)


# Not fully implemented, need to loot after battle.  Maybe in combat function?
def e051(party, console): # Bandits
    num_bandits = len(party) + 2
    console.display_message(f'You are ambushed by {num_bandits} bandits!')
    bandit_party = []
    bandit_party.append(characters.Character(title='Bandit Chief', combat_skill=6, endurance=6, wealth_code=15))
    for _ in range(num_bandits - 1):
        bandit_party.append(characters.Character(title='Bandit', combat_skill=5, endurance=4, wealth_code=1))
    
    game_actions.combat(party, bandit_party, console, has_surprise='enemy')


# Not fully implemented
def e052(party, console): # Goblins
    num_goblins = randint(1,6) + randint(1,6)
    console.display_message(f'You sight a band of {num_goblins} goblins, lead by a Hobgoblin, in the distance.  You can either escape the area or attempt to follow them.')
    goblin_party = []
    goblin_party.append(characters.Character(title='Commander', race='Hobgoblin', combat_skill=6, endurance=5, wealth_code=5))
    for _ in range(num_goblins):
        goblin_party.append(characters.Character(title='Skirmisher', race='Goblin', combat_skill=3, endurance=3, wealth_code=1))
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
    orc_party.append(characters.Character(title='Chieftan', race='Orc', combat_skill=5, endurance=6, wealth_code=7))
    for _ in range(num_orcs):
        orc_party.append(characters.Character(title='Warrior', race='Orc', combat_skill=4, endurance=5, wealth_code=1))
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
    orc_party.append(characters.Character(title='Warchief', race='demi-troll', combat_skill=8, endurance=7, wealth_code=10))
    for _ in range(num_orcs):
        orc_party.append(characters.Character(title='Warrior', race='Orc', combat_skill=5, endurance=5, wealth_code=2))
    #game_actions.escape()
    #surrender e061()


def e057(party, console): # Troll
    console.display_message('A huge stone-skinned Troll confronts your party.')
    troll_party = []
    troll_party.append(characters.Character(title='Brute', race='Troll', combat_skill=8, endurance=8, wealth_code=15, regenerates=True))
    troll_roll = randint(1,6)
    if troll_roll > party[0].wits:
        first_strike = 'enemy'
    else:
        first_strike = 'player'

    if game_actions.combat(party, troll_party, console, has_first_strike=first_strike):

        console.display_message('With the troll dead, you harvest its stone-skin as a valuable item. Whenever you have an opportunity to buy food at a town, castle, temple, or from merchants you can sell the skin for 50 gold. It is also known that Count Drogat, of Drogat Castle, will treasure the gift should you manage to get a personal audience with him.')
        party[0].add_item('trollskin')


def e058(party, console): # Band of Dwarves
    pass


def e059(party, console): # Dwarf Mines
    pass


def e060(party, console): # Arrested
    pass


def e061(party, console): # Marked For Death (Arrested)
    pass


def e062(party, console): # Thrown in the Dungeon (Arrested)
    pass


def e063(party, console): # Imprisoned (Arrested)
    pass


def e064(party, console): # Hidden Ruins
    pass


def e065(party, console): # Hidden Town
    pass


def e066(party, console): # Secret Temple
    pass


def e067(party, console): # Abandoned Mines
    pass


def e068(party, console): # Wizard's Abode
    pass


def e069(party, console): # Wounded Warrior
    pass


def e070(party, console): # Halfling Town
    pass


def e071(party, console): # Elven Band
    pass


def e072(party, console): # Following an Elven Band
    pass


def e073(party, console): # Witch
    pass


def e074(party, console): # Giant Spiders
    pass


def e075(party, console): # Pack of Wolves
    pass


def e076(party, console): # Great Hunting Cat
    pass


def e077(party, console): # Herd of Wild Horses
    pass


def e078(party, console): # Bad Going
    pass


def e079(party, console): # Heavy Rains
    pass


def e080(party, console): # Pixies
    pass


def e081(party, console): # Mounted Patrol
    pass


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


def e083(party, console): # Wild Boar Charge
    pass


def e084(party, console): # Bear Comes to Dinner
    pass


def e085(party, console): # Narrow Ledges
    pass


def e086(party, console): # High Pass
    pass


def e087(party, console): # Impassable Woods
    pass


def e088(party, console): # Rock Fall
    pass


def e089(party, console): # Impassable Morass
    pass


def e090(party, console): # Quicksand
    pass


def e091(party, console): # Poison Snake
    pass


def e092(party, console): # Flood
    pass


def e093(party, console): # Poison Plants
    pass


def e094(party, console): # Crocodiles
    pass


def e095(party, console): # Mounts at Risk
    pass


def e096(party, console): # Mounts Die
    pass


def e097(party, console): # Marsh Gas and Rot
    pass


def e098(party, console): # Dragon
    console.display_message('You encounter a huge, winged, fire-breathing Dragon!')
    dragon_party = []
    lair_roll = randint(1,6)
    if lair_roll <= 2:
        dragon_party.append(characters.Character(title='the Molten Fury', race='Dragon', combat_skill=10, endurance=11, wealth_code=0, flying=True))
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
        dragon_party.append(characters.Character(title='the Molten Fury', race='Dragon', combat_skill=10, endurance=11, wealth_code=30, flying=True))
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


def e099(party, console): # Roc
    pass


def e100(party, console): # Griffon
    pass


def e101(party, console): # Harpy
    pass


def e102(party, console): # Light Rainstorm (Flying)
    pass


def e103(party, console): # Bad Headwinds (Flying)
    pass


def e104(party, console): # Good Tailwinds (Flying)
    pass


def e105(party, console): # Storm Clouds Ahead (Flying)
    pass


def e106(party, console): # Heavy Overcast (Flying)
    pass


def e107(party, console): # Falcon Scout (Flying)
    pass


def e108(party, console): # Hawkmen Attack (Flying)
    pass


def e109(party, console): # Wild Pegasus (Flying)
    pass


def e110(party, console): # Air Spirit (Flying)
    pass


def e111(party, console): # Storm Demon (Flying)
    pass


def e112(party, console): # Meet Eagle Clan (Flying)
    pass


def e113(party, console): # Eagle Ambush (Flying)
    pass


def e114(party, console): # Eagle Hunt (Flying)
    pass


def e115(party, console): # Eagle Lair (Flying)
    pass


def e116(party, console): # Eagle Help (Flying)
    pass


def e117(party, console): # Eagle Allies (Flying)
    pass


def e118(party, console): # Giant
    pass


def e119(party, console): # Flash Flood
    pass


def e120(party, console): # Exhaustion
    pass


def e121(party, console): # Sunstroke
    pass


def e122(party, console): # Raftsmen
    pass


def e123(party, console): # Knight at the Bridge
    pass


def e124(party, console): # Raft
    console.display_message('')
    pass


def e125(party, console): # Raft Overturns
    console.display_message('')
    pass


def e126(party, console): # Raft Caught in Current
    console.display_message('')
    pass


def e127(party, console): # Raft in Rough Water
    console.display_message('')
    pass

# Not fully implemented
def e128(party, console): # Merchant
    console.display_message('You meet a friendly merchant. You can either pass by and ignore him, ending this encounter, or you can stop to chat and barter')
    merchant_roll = randint(1,6) + randint(1,6)
    merchant = {2  : 'Merchant has pegasus mount for sale, 50 gold.',
                3  : 'Merchant mentions cave tombs in this hex, if you go to look, see e028',
                4  : 'Merchant has cure-poison vials for sale, each costs 10 gold (see e181 for details of its use).',
                5  : 'Merchant mentions a farm nearby in this hex, if you investigate see e009',
                6  : 'Merchant has food for store, 1 gold per 2 food units, up to a maximum of eight (8) units may be purchased',
                7  : 'Merchant may outwit you, roll one die, if it exceeds your wit & wiles you spend 10 gold needlessly (or all your money, if you have less)',
                8  : 'Merchant has healing potions for sale, each costs 5 gold (see e180 for use)',
                9  : 'Merchant has two horses for sale, 6 gold pieces each',
                10 : 'Merchant has coffle of slaves for sale, see e163',
                11 : 'Merchant provides some final clues about a treasure, see e147.',
                12 : 'Learn unique secrets from the merchant, see e162.'}
    merchant_result = merchant[merchant_roll]
    console.display_message(f'{merchant_result}')


# Not fully implemented
def e129(party, console): # Merchant Caravan
    console.display_message('You meet a merchant caravan camped for the night. You may halt for the day with them to talk and trade, or you can ignore them and end if this event.')
    caravan_roll = randint(1,6) + randint(1,6)
    merchant_caravan = {2  :'Learn unique secrets from various caravan members, see el62',
                        3  :'Learn of a monastery in this hex, if you go to look see e022.',
                        4  :'Merchants have anti-poison talisman/amulet for sale for 25 gold, for details of its use sec el 87.',
                        5  :'Merchants noticed farms in this hex, if you go to look sec e009.',
                        6  :'Meet an independent merchant in the caravan, see e128.',
                        7  :'Caravan guards become hostile, you must flee the hex, see escape r218.',
                        8  :'Caravan healer has potions for sale, 6 gold each, for use see e180.',
                        9  :'Caravan has up to six spare horses for sale, 7 gold pieces each.',
                        10 :'Caravan has coffle of slaves for sale, see e163.',
                        11 :'Talk with caravan guards give you hints to a treasure, see e147.',
                        12 :'Caravan passed a nearby ruin yesterday, roll one die for which adjacent hex contains the ruins (1-N,2-NE, 3-SE, 4-S, 5-SW, 6-NW).'}
    caravan_result = merchant_caravan[caravan_roll]
    console.display_message(f'{caravan_result}')


def e130(party, console): # Meet a High Lord
    pass


def e131(party, console): # Empty Ruins
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
            if not character.alive and not character.heir:
                console.display_message(f'{character.name} is crushed to death!')
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


# Not yet fully implemented, need to be able to search again if desired after surviving encounter
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


# Not yet fully implemented, need to be able to carry it UNTIL party contains appropriate character
def e140(party, console): # Magic Box
    console.display_message('You find a magic box!')
    caster_in_party = any([character.magician, character.wizard, character.witch] for character in party)
    if caster_in_party:
        caster_character = [character for character in party if character.magician or character.wizard or character.witch]
        if caster_character:
            caster_companion = choice(caster_character)
            console.display_message(f'{caster_companion.name} knows the secrets to the box and is able to open it for you to examine the contents.')
            magic_box_roll = randint(1,6)
            if magic_box_roll == 1:
                e141(party, console)
            elif magic_box_roll == 2:
                e142(party, console)
            elif magic_box_roll == 3:
                gold, item = game_actions.roll_treasure(60)
                party[0].gold += gold
                console.display_message(f'You find {gold} gold!')
                if item:
                    party[0].add_item(item)
                    console.display_message(f'You find a {item}!')
            elif magic_box_roll == 4:
                gold, item = game_actions.roll_treasure(110)
                party[0].gold += gold
                console.display_message(f'You find {gold} gold!')
                if item:
                    party[0].add_item(item)
                    console.display_message(f'You find a {item}!')
            elif magic_box_roll == 5:
                e195(party, console)
            elif magic_box_roll == 6:
                console.display_message('The box contains nothing but rubbish.')


# Not yet fully implemented
def e141(party, console): # Hydra's Teeth
    hydra_teeth_quantity = randint(1,6) + randint(1,6)
    console.display_message(f'You find {hydra_teeth_quantity} hydra teeth.')
    party[0].possessions.append(f'{hydra_teeth_quantity} hydra teeth')
    '''The magician/ wizard/witch explains that whenever you
scatter these teeth on the ground, that number of undead warriors will rise and fight in your party for one
combat (r220) at your command. These undead teeth-warriors are combat skill 5, endurance 4, and wealth 0.
They will only last for that combat, and then disappear. However, you can scatter the teeth at any instant to use
them that one time, including at the start or during any combat.'''


def e142(party, console): # Gems
    console.display_message('The box contains a horde of gems!')
    gold1, item1 = game_actions.roll_treasure(100)
    gold2, item2 = game_actions.roll_treasure(100)
    party[0].gold += gold1, gold2
    console.display_message(f'The gems are worth {gold1 + gold2} gold!')
    caster_in_party = any([character.magician, character.wizard, character.witch] for character in party)
    if caster_in_party:
        caster_character = [character for character in party if character.magician or character.wizard or character.witch]
        if caster_character:
            caster_companion = choice(caster_character)
            console.display_message(f'{caster_companion.name} tells you that one of the gems is a Vision Gem and encourages you to peer into it.')
            e041(party, console)



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


def e148(party, console): # Seneschal Requires Bribe
    pass


def e149(party, console): # Must Learn Court Manners
    pass


def e150(party, console): # Pay Your Respects
    pass


def e151(party, console): # Find Favor
    pass


def e152(party, console): # Noble Ally
    pass


def e153(party, console): # Master of the Household
    pass


def e154(party, console): # Meet Lord's Daughter
    pass


def e155(party, console): # Audience with High Priest
    pass


def e156(party, console): # Audience with Town Mayor
    pass


def e157(party, console): # Letter of Recommendation
    pass


def e158(party, console): # Hostile Guards
    pass


def e159(party, console): # Must Purify Yourself
    console.display_message('')
    pass


def e160(party, console): # Audience with Lady Aeravir
    console.display_message('You are allowed a semi-private interview with the ruler of Aeravir Castle.')
    aeravir_roll = randint(1,6)
    aeravir_interview_results = '''
1
she listens graciously, but has no interest in Northlands problems, you cannot seek another
audience with her, and this results in nothing.
2
she listens but seems distracted, audience ends without result, and you cannot seek an audience
again some other day.
3
she takes pity on you, and gives you a gift of wealth 60 to help in your quest, but decrees that you
cannot seek another audience with her.
4
she finds you favourably endowed with virtue. You and your entire party can eat (r215) and lodge
(r217) at her castle for as long as you wish, whenever you wish. In addition, she provides you with a
gift of wealth 110 to help you on your quest. However, you cannot seek another audience with her.
5
she has seductive charms; roll one die for the number of days that pass before you come to your
senses again! After the time track is advanced, roll one die on this table again to see what the Lady
thinks. Meantime, your entire party has been living in the castle, but any true love (r228) has
deserted in despair, and you cannot roll for her return until after you leave this hex.
6
the Lady decides to support your cause fully. She gives you one die roll times 150 in gold, and an
escort of three stalwart knights, each of which is combat skill 7, endurance 6, mounts for your entire
party, and one spare pack-horse. Tonight she will hold a grand feast for you and all your party,
providing food (r215) and lodging (r217) free. If any party members have wounds, her healers will
cure all wounds tonight as well, even poisoned wounds.
'''


def e161(party, console): # Audience with Count Drogat
    console.display_message('You are allowed a semi-private interview with the ruler of Drogat Castle.')
    drogat_roll = randint(1,6)
    if 'trollskin' in party[0].possessions:
        drogat_roll += 1
        party[0].possessions.remove('trollskin')
    drogat_interview_results = '''
1 Count's eyes glow like red coals - you are his next victim, see e061!
2
Count listens with half an ear, audience ends with no result, but you can seek another audience
some other day.
3
Count is in a humorous mood, gives you flippant advice and sends you forth. You must leave Drogat
Castle tomorrow, and are advised to never seek an audience with the Count again unless you carry
a Letter of Recommendation.
4
Count takes an interest in your situation, and provides you with 100 gold and a treasure worth wealth
110 to further your cause.
5
 if you have killed (personally) at least five men or creatures the Count takes an interest in you.
Otherwise you are dismissed, and cannot seek an audience again with the Count until you have
killed five. If the Count takes an interest, he will go so far as to provide 500 gold, a treasure of wealth
110, and two winged pegasus mounts. You are advised to never seek an audience with the Count
again, since he is in one of his rare good moods.
6
the Count listens to your story with interest. Upon leaning the names of the northern usurpers he
declares that they were the very ones who did him ill deeds many years ago. He immediately rallies
his army to your cause, and uses his powerful magic to transport you, your party, him, and his army
to the Northland capital to retake your throne. You immediately win.'''


def e162(party, console): # Learn Secrets
    console.display_message('You finally accumulate enough hints and bits of unrelated information to learn of the important secrets of this region.')
    secrets_roll = randint(1,6)
    region_secrets = {1: e143(party, console),
                       2: e143(party, console),
                       3: e144(party, console),
                       4: e144(party, console),
                       5: e145(party, console),
                       6: e146(party, console)}
    secret_learned = region_secrets[secrets_roll]
    return secret_learned


def e163(party, console): # Slave Market
    pass


def e164(party, console): # Giant Lizard (Godzilla)
    giant_lizard_party = []
    console.display_message('A huge, giant lizard that shakes the earth as it walks attacks you!')
    giant_lizard = characters.Character(name='Giant Lizard', combat_skill=10, endurance=12)
    giant_lizard_party.append(giant_lizard)
    game_actions.combat(party, giant_lizard_party, console, has_first_strike='party')


def e165(party, console): # Hidden Elven Town
    pass


def e166(party, console): # Hidden Elven Fortress
    pass


### Items ###

def e180(party, console): # Healing Potion
    '''This potion can be applied once to any character (including yourself) at the end of the day, after the evening
meal (r215). The potion immediately cures all wounds except poison wounds.'''


def e181(party, console): # Cure Poison Vial
    '''Any character can drink this vial once during the evening meal (r215). It will cure all poison wounds overnight.
Only poison wounds are cured, it has no effect on regular wounds.'''


def e182(party, console): # Gift of Charm
    '''This is a small item of no real value, but with a magic aura. You can give this gift to any character(s) you
encounter as part of any talk or negotiate option. When you use it, you can then roll a second and a third time
for that option, and select whichever result you prefer. Once given away, the gift is gone and useless unless the
receiver later fights you in combat and you kill him. Then you can recover the gift as part of the defeated's
possessions.'''


def e183(party, console): # Endurance Sash
    '''You wear this sash around your waist, and its magic adds one (+1) to your normal endurance level. The effect
is permanent as long as you retain your possessions. You cannot wear more than one sash, additional ones
can be cached (r214) or given to other characters in your party.
'''


def e184(party, console): # Resistance Talisman
    '''This jewelled talisman allows you to resist all magic spells and attacks. Whenever magic is used, you can call
upon the talisman to negate it. However, the talisman may be unable to contain a strong spell, so each time it is
used roll one die, a result of 6 means the spell is stopped but the talisman is shattered and broken in the
process'''


def e185(party, console): # Poison Drug
    '''This drug can be applied to the weapons of any one character in your party. Its use means that whenever that
character strikes in combat (r220) and inflicts wounds, for each normal wound given, one extra poison wound is
also given.
After a combat where the poisoned weapon is used, roll one die. A 6 means the poison has worn off, and the
weapon returns to normal. Since a character often has multiple weapons, he has the option of using his
poisoned weapon, or a normal weapon, as desired.'''


def e186(party, console): # Magic Sword
    '''A character can carry this special sword among his weapons. The magic sword adds one (+1) to the combat
skill of the character with it. In addition, the blade's magic means that every wound it inflicts counts as poisoned
too.'''


def e187(party, console): # Anti-Poison Amulet
    '''This protects against all poison wounds. Any poison wound inflicted is ignored if the target has this amulet.
Normal wounds still take effect. When a poison wound is prevented, roll two dice. If the total is 12, the amulet
has reached its limit, cannot absorb more poison, and must be discarded.'''


def e188(party, console): # Pegasus Mount
    '''You have acquired a pegasus — a winged horse that allows you to travel airborne. The pegasus is like a
normal mount in all other respects, including the same transport ability (r206), food requirements (r215), and
lodging when in towns, castles, or temples (r217). You can use the pegasus as a normal mount on the ground,
if desired.'''


def e189(party, console): # Charisma Talisman
    '''The character that wears this talisman improves his "stature" and charisma in the eyes of others. If you wear it,
add one (+1) to your wit & wiles in any event or option that involves or results from talk or negotiation. This
talisman does not improve your wit & wiles when trying to evade, hide, attack, or surprise. Like many magical
devices, this talisman's spell may eventually wear out. After each use, roll two dice, if the total is 12 it has worn
out and must be discarded.'''


def e190(party, console): # Nerve Gas Bomb
    '''This sealed jar is filled with a deadly and quick-acting gas created by a master alchemist. If you surprise an
enemy in combat (r220), instead of your initial strikes, your entire party can stand off and let you hurl the bomb.
When you do, roll one die for each character encountered: 1,2,3,4-character killed by gas; 5-character flees
from gas, takes his wealth and possessions with him; 6-character unaffected by gas.
The jar with the gas is rather heavy, and counts as one (1) load to transport (r206).'''


def e191(party, console): # Resistance Ring
    '''This ring creates a magic aura around the wearer. Every time the wearer is wounded, roll two dice:
2 thru 8 blow warded by ring, ignore wounds.
9,10,11 blow skids around aura and strikes home, take normal wound result minus one wound
(deflected in the skidding)
12 ring fails, blow has normal effect, and ring melts on your finger, causing injury and one extra
wound.
The ring can be used to ward poison wounds like normal wounds. The ring can also be used to ward magic
attacks against the wearer, but will not protect others in the party. In a magic attack, two rolls must be made,
and the single worst result (to the wearer) is applied.'''


def e192(party, console): # Resurrection Necklace
    '''This necklace of black opals and tiny bones holds the secret of a second life. If the wearer dies for any reason,
including voluntary suicide, at the end of that day the character rises from the dead. The necklace disintegrates
as the character revives, and thus only works once. The resurrection occurs in the same hex, but the character
is now free to select any action on the next day.
A character revived by the necklace, having been left for dead, will have lost all possessions and money, and
the entire party will have scattered, although a lover might return (see r228). A character revived by the
necklace has a somewhat ghoulish cast, and is a bit weaker. Endurance is reduced by one. Such appearances
are favoured at Drogat Castle, you learn, and so you can add one (+1) if seeking an audience (r211) with Count
Drogat.'''


def e193(party, console): # Shield of Light
    '''This enchanted shield will flash and shine in the eyes of any attacker. When a character has this shield, any
opponent in combat has his combat skill reduced by one (-1). If the character with the shield dies, the shield will
dull and die, becoming useless. At the end of each combat where the shield is used, roll one die. If a 6 results,
the shield is so banged and damaged by battle that it is now useless.
To preserve the shield, you may elect to not use it in some combats. You can change your mind during the
battle, but must then check for damage after the battle anyway.'''


def e194(party, console): # Royal Helm of the Northlands
    '''This ancient and sacred treasure has long been lost. Myths and tales still relate the great exploits of its wearers.
Now you hold this treasure that gives you automatic and indisputable right to the Northlands throne.
If you return to either Ogon (0101) or Weshor (1501) towns with the helm, you will be instantly hailed as the
rightful King of the Northlands, and win the game.
In the meantime, possession of the helm increases your stature and self-confidence, so increase your wit &
wiles by one (+1).'''


def e195(party, console): # Random Items Reference
    random_item_roll = randint(1,6) + randint(1,6)
    random_items = {2 : e191(party, console),
                    3 : e186(party, console),
                    4 : e182(party, console),
                    5 : e184(party, console),
                    6 : e181(party, console),
                    7 : e180(party, console),
                    8 : e185(party, console),
                    9 : e193(party, console),
                    10: e183(party, console), 
                    11: e189(party, console), 
                    12: e192(party, console)}
    random_item_result = random_items[random_item_roll]
    return random_item_result





