'''
import hexmap

def starting_position():
	start_hex = d6(1)
	#print(start_hex)
	if start_hex == 1:
		start_hex_key = 101
		start_hex = hexmap.overland_map[101][1] if hexmap.overland_map[101][1] else hexmap.overland_map[101][0] #Ogon
	elif start_hex == 2:
		start_hex_key = 701
		start_hex = hexmap.overland_map[701][1] if hexmap.overland_map[701][1] else hexmap.overland_map[701][0] #Plains
	elif start_hex == 3:
		start_hex_key = 901
		start_hex = hexmap.overland_map[901][1] if hexmap.overland_map[901][1] else hexmap.overland_map[901][0] #Ruins
	elif start_hex == 4:
		start_hex_key = 1301
		start_hex = hexmap.overland_map[1301][1] if hexmap.overland_map[1301][1] else hexmap.overland_map[1301][0] #Plains
	elif start_hex == 5:
		start_hex_key = 1501
		start_hex = hexmap.overland_map[1501][1] if hexmap.overland_map[1501][1] else hexmap.overland_map[1501][0] #Weshor
	elif start_hex == 6:
		start_hex_key = 1801
		start_hex = hexmap.overland_map[1801][1] if hexmap.overland_map[1801][1] else hexmap.overland_map[1801][0] #Mountains
	print(f"\nNow, at dawn you roll out of the merchant wagons into a ditch, dust off your clothes, loosen your swordbelt, and get ready to start the first day of your adventure. Staying hidden until the caravan is out of sight, you find yourself in the {start_hex} north of the Tragoth river.")
	return start_hex_key


def travel(current_hex_key):
	###current_hex_key = starting_position()
	###current_hex_key = 1010
	current_hex = hexmap.overland_map[current_hex_key]
	print(f"\nYou are in the {current_hex[1] if current_hex[1] else current_hex[0]} of hex {current_hex_key}")

	heading = ('N','NE','SE','S','SW','NW')
	direction = input("\nWhich direction would you like to move?\nSelect: 'N','NE','SE','S','SW','NW' > ").upper()
	if direction not in heading:
		print("That is not a valid direction, please pick another.")
		travel(current_hex_key)
	else:
		#print(f"\nFrom {current_hex_key} you travel {direction} to {new_hex_key}\n")
		new_hex_key = hexmap.movement(current_hex_key, direction)
		print(f"\nFrom {current_hex_key} you attempt to travel {direction} to {new_hex_key}\n")
		river_crossed = hexmap.river_crossing(current_hex_key, direction)
		if river_crossed == False:
			current_hex_key = current_hex_key
			return current_hex_key
		else:
			leaving_hex = hexmap.overland_map[current_hex_key]
			lost = {'Farmland':10,'Plains':9,'Forest':8,'Hills':8,'Mountains':7,'Swamp':5,'Desert':6}
			is_lost = d6(2)
			if lost[leaving_hex[0]] <= is_lost:
				print("You have gotten lost in the wilderness and make no progress today.")
				current_hex_key = current_hex_key
				return current_hex_key
			else:
				current_hex_key = new_hex_key
				current_hex = hexmap.overland_map[current_hex_key]
				print(f"\nYou are in the {current_hex[1] if current_hex[1] else current_hex[0]} of hex {current_hex_key}")
				target_hex = current_hex
				event = {'Farmland':8,'Plains':9,'Forest':9,'Hills':10,'Mountains':10,'Swamp':10,'Desert':10}
				is_event = d6(2)
				if event[target_hex[0]] <= is_event:
					print("You have an encounter!")
			return current_hex_key
		return current_hex_key
	return current_hex_key
	

def daily_actions():
	print(f"\nAvailable options for today are:\n{'-'*32}\n1< Travel to a new hex\n2< Rest to recover wounds and improve hunting\n3< Search for a previously placed cache\n4< Seek news & information (in town, castle, temple)\n5< Seek to hire followers (in town, castle)\n6< Seek audience with lord (in town, castle, temple)\n7< Submit offering (temple)\n8< Search ruins (in ruins)")
	action = input("\nWhich action do you choose? > ")
	if action == "1":
		return travel(current_hex_key)
	elif action == "2":
		pass #heal_hunt(wounds, food)
	elif action == "3":
		pass #cache_items(inventory)
	elif action == "4":
		pass #seek_news() if in town, castle, temple
	elif action == "5":
		pass #hire_followers(), if in town, castle
	elif action == "6":
		pass #seek_audience() if in town, castle, temple
	elif action == "7":
		pass #offering() if in temple
	elif action == "8":
		pass #search_ruins() if in ruins

	#choose action
	#resolve action

	#end of day
	#hunt/provide food
		#hunt: food += hunter_CS + ((hunter_END - hunter_Wounds)/2) - d6(2)) + 1 per additional hunter + 1 per guide
		#food -= 1 + 1 per ally + 2 per mount(if unable to forage), double requirements in desert
	#provide lodging if in town, temple, castle
		#gold -= 1(+1 for food) + 1 per 2 allies(+1 per ally for food) + 1 per mount(+1 for feed)
		#time counter += 1 day

start_hex_key = starting_position() #this is the start
current_hex_key = start_hex_key
#current_hex_key = 2010  #this is for testing map

while True:
	
	current_hex_key = daily_actions()

# ally = Character()
# opponent = Character()
# print(vars(opponent))

#Need a way to keep track of all characters Combat Skill and Endurance values, plus any special modifiers
#Need to create barbarian allies party and incorporate them
#Need to assign attackers to targets --  Well, random assignment is technically assignment 
#shift to a new enemy once an enemy is defeated
#Need to generate results of 2d6, compare all modifiers and compute a total, then compare that total to the wounds table and subtract the result from the appropriate Endurance score
#Need to remove a character from combat once their Endurance is 1 or less
#Need to check if enemy characters Rout and flee combat
#Need to attempt to escape combat
#Need to handle surprise 
'''
# Need to solve turn order
# Step 1: determine surprise (grants 1 free strike, followed by first strike each round)
# Step 2: match opponents--must be 1 v 1 until everyone has 1 opponent, then extras assigned
# Step 3: determine if player wishes to attempt escape
# Step 4: make strikes, apply wounds, and remove characters
# Step 5: check if enemy Routs
# Step 6: repeat from Step 2 until one side is defeated or escapes/routs
'''

# The following lines randomly generate the number of allies and their attributes.
default_num_allies = d6(1) - 1
barbarian_instance_party = {}
num_allies = int((input("\nHow many allies do you have? ")) or default_num_allies)
print("\nYou have", num_allies, "allies!\n")
barbarian_instance_party.update({0: prince}) # adds Prince to the ally party
for i in range(num_allies):
	ally_profile = Character()
	#print(vars(ally_profile))
	#print("-" * 80)
	barbarian_instance_party.update({i+1: ally_profile}) #i+1 is for if the prince is in the party
for k, v in barbarian_instance_party.items():
	print("ally:",k+1, vars(v))
print("=" * 80)

barbarian_party = barbarian_instance_party
time.sleep(1)

# The following lines randomly generate the number of opponents and their attributes.
default_num_enemies = d6(2) - 1
enemy_instance_party = {}  # this is a dictionary
num_enemies = int((input("\nHow many enemies are you facing? ")) or default_num_enemies)
print("\nYou are facing", num_enemies, "enemies!\n")
for i in range(num_enemies):
	enemy_profile = Character()
	#print(vars(enemy_profile))
	#print("-" * 80)
	enemy_instance_party.update({i: enemy_profile})
for key, value in enemy_instance_party.items(): #I CAN'T GET THIS TO PRINT; FERESHTEH CAN THOUGH!
	print("enemy:",key+1, vars(value))
print("=" * 80)

enemy_party = enemy_instance_party
time.sleep(1)

# These two dictionaries govern the results of attacks.
miss_set = {-6, -5, -4, -3, -2, 0, 1, 2, 4, 6, 7, 9, 15}
hit_map = {
    -1: 1,
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
    20: 6
}

# -1,3,5,8,11 One wound
# 10,12,13,17 Two wounds
# 14 Three wounds
# 16,18,19 Five wounds
# 20 Six wounds

# The following code is for random and automatic surprise decisions:

# strike_flag = 1
# enemy_strike_flag = 1
# print()
# print("*" * 45)
# surprise_flag = d6(1)
# if surprise_flag == 1:
#     print("The barbarian party is surprised!")
#     strike_flag = False
#     enemy_strike_flag = 1
# elif surprise_flag == 6:
#     print("The enemy party is surprised!")
#     strike_flag = 1
#     enemy_strike_flag = 0
# else:
#     print("All combatants array themselves for battle.")
#     strike_flag = 1
#     enemy_strike_flag = 1
# print("*" * 45)

# The following code is for manual surprise decisions:

# barbarian_surprise_flag = input("Is the barbarian party surprised? Yes or No. ")
# if barbarian_surprise_flag == "y":
# 	strike_flag = False
# else:
# 	strike_flag = 1

# enemy_surprise_flag = input("Is the enemy party surprised? Yes or No. ")
# if enemy_surprise_flag == "y":
# 	enemy_strike_flag = 0
# else:
# 	enemy_strike_flag = 1

#treasure = 0
#k = 0  # variable governing which enemy you are striking and how many have been slain
	

def combat():
  print()
  print("*" * 45)
  surprise_flag = d6(1)
  if surprise_flag == 1:
    print("The barbarian party is surprised!")
    strike_flag = False
    enemy_strike_flag = 1
  elif surprise_flag == 6:
    print("The enemy party is surprised!")
    strike_flag = 1
    enemy_strike_flag = 0
  else:
    print("All combatants array themselves for battle.")
    strike_flag = 1
    enemy_strike_flag = 1
  print("*" * 45)
  treasure = 0
  k = 0
  while prince.Endurance - prince.Wounds > 1 and enemy_party:
      if strike_flag:
        for ally in barbarian_party: #all index mappings assume number of enemies > allies, something not right here
            if k >= num_enemies:
                break            
            b_target = list(enemy_party.keys()) 
            a_target = random.choice(b_target)

            if barbarian_party[ally].Wounds >= barbarian_party[ally].Endurance -1:
                continue
        #    if enemy_party[a_target].Wounds >= enemy_party[a_target].Endurance - 1:
	      #        a_target += 1
            ally_strike = d6(2) + barbarian_party[ally].Combat_skill - enemy_party[a_target].Combat_skill

            if barbarian_party[ally].Wounds > 0 and barbarian_party[ally].Endurance > barbarian_party[ally].Endurance - barbarian_party[ally].Wounds:
                print(f"The wounds hamper {barbarian_party[ally].Name}'s strike!")
                ally_strike += -1
                if barbarian_party[ally].Endurance / 2 <= barbarian_party[ally].Wounds:
                    print(f"The severe wounds hamper {barbarian_party[ally].Name}'s strike!")
                    ally_strike += -1
          
            if enemy_party[a_target].Endurance / 2 <= enemy_party[a_target].Wounds:
                print(f"The {enemy_party[a_target].Name}'s wounds help your attack!")
                ally_strike += 2

            if ally_strike in miss_set:
                print(f"{ally_strike} {barbarian_party[ally].Name} Missed the enemy {enemy_party[a_target].Name}")

            else:
                print(ally_strike, barbarian_party[ally].Name, "Hit! They deal", hit_map[ally_strike], "damage to", enemy_party[a_target].Name, "!")
                enemy_party[a_target].Wounds += hit_map[ally_strike]
                if enemy_party[a_target].Endurance - enemy_party[a_target].Wounds <= 1:
                    treasure = treasure + enemy_party[a_target].Wealth
                    print(enemy_party[a_target].Name, "is slain! Gold:", treasure)
                    enemy_party.pop(a_target)
                    k += 1

      print("+"*80)              
#	The following lines govern the enemy party members' attacks against the Prince.
      if enemy_strike_flag:
        for foe in enemy_party:
            e_target = list(barbarian_party.keys()) #foe%len(barbarian_party)
            if bool(e_target) == False:
              break
            target = random.choice(e_target)							
            if enemy_party[foe].Wounds >= enemy_party[foe].Endurance - 1:
              continue
          #  if barbarian_party[target].Wounds >= barbarian_party[target].Endurance -1:
          #    target += 1
            enemy_strike = d6(2) + enemy_party[foe].Combat_skill - barbarian_party[target].Combat_skill

            if enemy_party[foe].Wounds > 0 and enemy_party[foe].Endurance > enemy_party[foe].Endurance - enemy_party[foe].Wounds:
                print(f"The wounds hamper enemy {enemy_party[foe].Name}'s strike!")
                enemy_strike += -1
                if enemy_party[foe].Endurance / 2 <= enemy_party[foe].Wounds:
                    print(f"The severe wounds hamper enemy {enemy_party[foe].Name}'s strike!")
                    enemy_strike += -1

            if barbarian_party[target].Endurance / 2 <= barbarian_party[target].Wounds:
                print(f"{barbarian_party[ally].Name}'s' wounds help the enemy!")
                enemy_strike += 2

            if enemy_strike in miss_set:
                print(enemy_strike, "The enemy", enemy_party[foe].Name, "CS:", enemy_party[foe].Combat_skill, "END:", enemy_party[foe].Endurance - enemy_party[foe].Wounds, "Missed ally", barbarian_party[target].Name, "!" )

            else:
                print(enemy_strike, "Hit! The enemy", enemy_party[foe].Name, "CS:", enemy_party[foe].Combat_skill, "END:", enemy_party[foe].Endurance - enemy_party[foe].Wounds, "deals", hit_map[enemy_strike], "damage to", barbarian_party[target].Name,"!")
                barbarian_party[target].Wounds += hit_map[enemy_strike]
                if prince.Endurance - prince.Wounds <= 1:
                    print("fuck off Prince")
                if barbarian_party[target].Wounds >= barbarian_party[target].Endurance -1:
                    print(barbarian_party[target].Name, "is slain!")
                    treasure = treasure + barbarian_party[target].Wealth
                    print(f"{barbarian_party[target].Wealth} gold recovered.")
                    barbarian_party.pop(target)
              #  if target > len(barbarian_party):
              #      target = 0							
									
# The following lines reset strike flags for surprise and attempts to escape; they determine if the enemy routs (runs) from combat; they give the current status of the Prince and opponent he is fighting; they give the Prince to option to fight or attempt escape.
      strike_flag = 1
      enemy_strike_flag = 1
      if k > 0 and k < num_enemies:
        rout = random.randint(1, 6)
        if rout == 6:
            print("The enemy has routed!", num_enemies - k, "have fled!")
            break
      if k >= num_enemies or prince.Endurance - prince.Wounds <= 1:
        break
      print("\nYou have", prince.Endurance - prince.Wounds, "Endurance remaining. You have", len(barbarian_party)-1, "allies.  There are", num_enemies - k, "enemies remaining.") #, len(barbarian_party), barbarian_party.keys(), len(enemy_party), enemy_party.keys()) 
	
      next_round = input("Do you wish to Fight or Escape? ")
      print(" ")
      if next_round.lower() == 'f':
        os.system("clear")
        title_plate()
        continue
      elif next_round.lower() == 'e':
        os.system("clear")
        title_plate()
        escape = d6(1)
        if escape >= 4:
            print("You have escaped from combat!")
            break
        else:
            print("You have failed to escape your enemies!")
            strike_flag = 0
            continue
      else:
        os.system("clear")
        continue

# The lines below print the outcome of the combat.
  if prince.Endurance - prince.Wounds <= 1:
    print("You have been defeated!")
  elif not enemy_party:
    print("You have vanquished your foe!")

  print("-*-" * 25)
  print("Combat has ended! You have", prince.Endurance - prince.Wounds,
      "Endurance remaining. You have slain", k, "enemies.  You have", len(barbarian_party)-1, "allies.")
  if prince.Endurance - prince.Wounds > 1:
    prince.Wealth += treasure
    print(f"You collect {treasure} gold from fallen allies & enemies. You have {prince.Wealth} gold total.\n\n\n\n\n")


combat()
'''