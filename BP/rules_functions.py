def search_ruins():
	print("You spend the day searching through the ruins.")
	ruin_result = d6(2)
	if ruin_result == 2:
		e133()
	elif ruin_result == 3:
		e135()
	elif ruin_result == 4:
		e136()
	elif ruin_result == 5:
		e137()
	elif ruin_result == 6:
		e139()
	elif ruin_result == 7:
		e131()
	elif ruin_result == 8:
		e132()
	elif ruin_result == 9:
		e134()
	elif ruin_result == 10:
		e138()
	elif ruin_result == 11:
		e135()
	elif ruin_result == 12:
		e035()


def seek_news():
	print("You spend the day talking with people in taverns, streets, and the market, hoping to learn some useful news or information.")
	news_result = d6(2)
	if prince.Wits >= 5:
		news_result += 1
	if prince.Wealth >= 5:
		spend_gold = input("Do you wish to spend 5 gold to loosen people's tongues? > ").lower()
		if spend_gold == "y":
			prince.Wealth -= 5
			news_result += 1
	if news_result <= 2:
		print("No news of note; nothing seems to be happening today.")
	elif news_result == 3:
		print(" You discover a thieves' den and pillage it while they're out, gain 50 gold.")
		prince.Wealth += 50
	elif news_result == 4:
		temple = random.choice["Sulwyth", "Branwyn", "Zhor", "Donat", "Duffyd"]
		print(f"You hear rumours of secret rites at {temple} temple. When making offerings there, add one (+1) to your dice roll from now on.")
		temple_flag = temple.append()
		return temple_flag
	elif news_result == 5:
		print("You feel at home. You learn nothing today, but in the future always add one (+1) whenever seeking News or Hirelings in this hex.")
	elif news_result == 6:
		caravan = input("A large caravan is in town. Would you like to visit them today? > ").lower()
		if caravan == "y":
			e129()
	elif news_result == 7:
		print("You discover cheaper lodgings and food, pay half normal price in this hex from now on.")
	elif news_result == 8:
		print("At some point today a cutpurse picked your pocket; you have lost half your wealth.")
		prince.Wealth = (prince.Wealth // 2)
	elif news_result == 9:
		print("You attract attention of local constabulary.")
		e050()
	elif news_result == 10:
		magician = input("You discover residence of a local magician. Do you wish to visit him today? > ").lower() 
		if magician == "y":
			approach = "friendly"
			e016(approach)
	elif news_result == 11:
		guild_invite = input("You discover the local thieves guild and are invited to join.  Do you wish to accept? > ").lower()
		if guild_invite == "y":
			print("You participate in a theft of 200 gold this very evening, after dinner. You must escape tonight after the job.")
			guild_cut = input("Do you wish to give the guild their cut of 10% before you leave? > ").lower()
			if guild_cut == "y":
				prince.Wealth += 180
				print("The guild is pleased with your performance. You may return to this hex in the future.")
			if guild_cut == "n":
				prince.Wealth += 200
				print("You have angered the guild.  If you value your safety, you should never return to this hex.")
	elif news_result >= 12:
		if prince.Wealth >= 10:
			secret_info = input("A secret informant offers you valuable information for 10 gold.  Do you wish to pay for it? > ").lower()
			if secret_info == "y":
				prince.Wealth -= 10
				info_result = d6(1)
				if info_result == 1:
					print("These secrets are bogus and ultimately prove worthless.  Fortunately it comes to no greater detriment than your pride and your coin purse.")
				elif info_result == 2:
					e147()
				elif info_result == 3:
					e143()
				elif info_result == 4:
					e144()
				elif info_result == 5:
					e145()
				elif info_result == 6:
					e146()


def hire_followers():
	print ("You spend the day posting notices, visiting agents and merchants, and inquiring at taverns about the availability of hired help.")
	hire_result = d6(2)
	if hire_result == 2:
		print("A Freeman joins your part at no cost (except food and lodging), he is combat skill 3, endurance 4.")
	elif hire_result == 3:
		print("A Lancer with a horse can be hired for 3 gold per day, he is combat skill 5, endurance 5.")
	elif hire_result == 4:
		print("One or two mercenaries can be hired for 2 gold per day each. Each is combat skill 4, endurance 4")
	elif hire_result == 5:
		print("Horse dealer in area, you can buy horses (for mounts) at 10 gold each.")
	elif hire_result == 6:
		print("Local guide available (see r205), hires for 2 gold per day, has combat skill 2, endurance 3.")
	elif hire_result == 7:
		print("Henchmen available, roll one die for the number available for hire, each is combat skill 3, endurance 3, and costs 1 gold per day each.")
	elif hire_result == 8:\
		print("Slave market")
		e163()
	elif hire_result == 9:
		print("Nothing available, but you gain some news and information, see r209 but subtract one (-1) from your dice roll there.")
	elif hire_result == 10:
		print("Honest horse dealer in area, can buy horses (for mounts) at 7 gold each.")
	elif hire_result == 11:
		print("Runaway boy or girl joins your party at no cost (except food and lodging), has combat skill 1, endurance 3.")
	elif hire_result >= 12:
		print("Porters in any quantity available, hire for ½ gold each per day. In addition, a local guide (r205) can be hired for 2 gold per day, has combat skill 1, endurance 2.")


def seek_audience():
	if current_hex_key in (101, 109, 216, 419, 422, 719, 916, 1004, 1009, 1415, 1501, 1720):
		audience_town = d6(2)
		if audience_town == 2:
			# 2 Grievously insult the town council, e062.
			# 3 A slanderous aside about the mayor's wife is blamed on you, e060.
			# 4 Meet hostile guards, e158.
			# 5 Encounter the Master of the Household, e153.
			# 6,7,8 Audience refused today, you may try again.
			# 9,10 Audience permitted, el56.
			# 11 Meet daughter of the mayor, e154.
			# 12 Audience permitted, e156.

	if current_hex_key in (711, 1021, 1309, 1805, 2018):
		audience_temple = d6(2)
		if audience_temple == 2:
			# 2 Anger temple guards, e063.
			# 3 Priestess resents a lewd remark, e060.
			# 4 Encounter hostile guards, e158.
			# 5 Audience refused today, you may try again.
			# 6 Must purify yourself, e159
			# 7 Audience refused today, you may try again.
			# 8 Allowed audience if you give temple a Dragon's eye, go to e155; otherwise you must deal with the Master of the Household, e153.
			# 9 Permitted to pay your respects, e250
			# 10 You must purify yourself, e159.
			# 11+ Audience permitted, e155

	if current_hex_key == 323:
		audience_drogat = d6(2)
		if audience_drogat == 2:
			# 2 You are the Count's next victim; see e061.
			# 3 The Captain of the Guard dislikes your haircut; see e062.
			# 4 Meet the daughter of the Count, e154.
			# 5 Encounter the Master of the Household, e153.
			# 6 Confronted by hostile guards, e158.
			# 7 Gain an audience (e161) if you give the Roc's Beak to the Doorman; otherwise you are deemed unworthy and unwise, and are arrested (e060).
			# 8 Seneschal requires a bribe, e148.
			# 9 Must learn court manners, e149.
			# 10 Find favour in the eyes of the Count, e151.
			# 11+ Audience granted with Count, e161.

	if current_hex_key == 1212:
		audience_huldra = d6(2)
		if audience_huldra == 2:
			# 2 Audience permanently refused, cannot try again.
			# 3 Meet Baron's Daughter, e154.
			# 4 Must learn court manners, e149.
			# 5 Confronted by hostile guards, e158.
			# 6,7 Audience refused today, you may try again.
			# 8 Encounter the Master of the Household, e153.
			# 9 Seneschal requires a bribe, e148.
			# 10,11 Pay your respects to the Baron, e150.
			# 12 Find favour in the eyes of the Baron, e151.
			# 13+ Baron becomes your Noble ally, e152.

	if current_hex_key == 1923:
		audience_aeravir = d6(2)
		if audience_aeravir == 2:
			# 2 You insult the Lady's dignity, arrested e060.
			# 3 You must purify yourself first, e159.
			# 4 Untoward remark makes the guards hostile, e158.
			# 5 Must learn better court manners, e149.
			# 6 Meet the Master of the Household, e153.
			# 7 Gain an audience (e160) if you give the Griffon's Claw, otherwise audience refused but you may try again.
			# 8 Audience refused, but you may try again.
			# 9 Seneschal requires a bribe, e148.
			# 10 Audience granted, e160.
			# 11 Meet daughter of the Lady Aeravir, e154.
			# 12+ Audience granted, e160.


def offering():
	pass
# You spend the day preparing, waiting in line, and finally giving an offering at the temple altar. This action is only permitted at a temple. You must spend at least one gold piece for proper herbs and sacrifice. If you spend ten gold pieces for exceptionally fine herbs and sacrifices, add one (+1) to your dice roll result. To determine the result, roll two dice:
# 2 You commit a magnificent error in the rites, the entire temple becomes impure and abandoned, no longer functions as a temple for the rest of the game. You are arrested and sentenced to death, e061.
# 3 Good Omens, but no special result.
# 4 Bad Omens, you are travelling under a curse. Roll one die for each of your followers, any result except a 1 means they believe the omens and immediately desert you. You cannot seek to hire any followers (r210) in this hex for the rest of the game.
# 5 High Priest insulted by your northern manners, arrested e060.
# 6 Good Omens, you get free food (r215) and lodging (r217) tonight.
# 7 Favourable Omens for further worship, if you try this Offerings action again tomorrow, you can add one (+1) to your dice roll. Otherwise no effect.
# 8 Gods favour your questions, priests assign a monk to your party. The monk has combat skill 2, endurance 3, serves as a guide when leaving this or any adjacent hex only.
# 9 Special omen and riddle provides a clue to treasures, see e147.
# 10 Fall in love with priestess (see r229). You immediately escape (r218) with her and can never return to this hex. She is combat skill 2, endurance 4, and has wealth 100 in temple treasures she has stolen!
# 11 The High Priest requires an audience with you; see e155.
# 12, 13 High Priest spends afternoon talking with you, provides you with final clues to some secret information, roll one die: 1,2-e144; 3,4-e145; 5,6-e146. Alternately, instead of the secret information, you can use his influence in attempting Offerings again tomorrow, and add three (+3) to your dice roll here.
# 14+ Gods declare your cause a religious crusade, and the Staff of Command is passed into your hands. If you bring this possession to any hex north of the Tragoth River you will command instant obedience throughout the Northlands, regain your throne and win the game. In the meantime you are given a pair of warrior monks (combat skill 5, endurance 6) with mounts to join your party and help you return northward.


def heal_hunt(wounds, food):
	pass


def cache_items(inventory):
	pass