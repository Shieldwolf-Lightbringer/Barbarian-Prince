def e002(current_hex_key): #Mercenary Royal Guardsmen
	mrg = (101,201,301,302,401,501,502,601,701,801,901,1001,1101,1201,1301,1501,1601,1701,1801,1901,2001)
	if current_hex_key in mrg:
		mrg_event = (d6(1) - 3)
		if current_hex_key in {101,1501}:
			mrg_event += 1
		if mrg_event >= 1:
			mrg_num = d6(1)
			print(f"{mrg_num} Mercenary thugs, dressed by the usurpers as their royal guardsmen, are riding toward you!")
			for i in range(mrg_num):
				enemy_profile = Character("Merc Royal Guard", 5, 4, 0, 4)
				enemy_instance_party.update({i: enemy_profile})
			for key, value in enemy_instance_party.items(): 
				print("enemy:",key+1, vars(value))
			print("=" * 80)
			enemy_party = enemy_instance_party
			action = input("\nDo you wish to attempt to:\n(1) Negotiate\n(2) Evade\n(3) Fight\n > ")
			if action == "1":
				print("Negotiate")
			elif action == "2":
				print("Evade")
			elif action == "3":
				combat()
			else:
				combat()
'''Roll one die, subtract three (-3), then add one (+1) if you are in Ogon (0101) or Weshor (1501). If the result is one (1) or more, this event occurs. If the result is zero (0) or less, no event occurs.
Mercenary thugs, dressed by the usurpers as their royal guardsmen, are riding toward you! Roll one die for the number of men, each of which has combat skill 5, endurance 4, wealth 4. Your options are:
die roll negotiate *evade fight
1 pass r327 attacked r307 surprise r300
2 pass r328 attack r306 surprise r301
3 pass r329 attack r304 surprise r303
4 bribe to pass (15) r323 hide r318 attack r304
5 bribe to pass (25) r323 escape r311 attack r305
6 attacked r306 escape mtd r312 attacked r306
7 — escape mtd r312 —
* if your party all winged mounts, you can use a flying escape r313 instead of rolling for the evade option; if your entire party has mounts, add one (+1) to die roll. You can abandon un-mounted members of the party for this.'''

def e003(): # Swordsman
	print("You meet a swordsman adventurer. He is mounted on a horse with combat skill 6, endurance 6, and wealth 7. Sitting there on his horse he takes an active interest in your party.")
	action = input("Your options are:\n(1) Talk\n(2) evade\n(3) Fight\n > ")

'''die roll talk *evade fight
1 converse r341 escape mtd r312 surprise r303
2 converse r341 escape r315 attack r304
3 looter r340 hide r317 attack r305
4 hireling r339 bribe (5) r322 attacked r306
5 hireling r333 pass r325 attacked r307
6 bribe (10) r332 pass r325 surprised r308
* if your party has winged mounts and/or flying ability, you can use escape flying (r313) instead of rolling the die for the evade option.'''

e004 Mercenary Band
You observe a small band of mercenaries approaching. The leader is mounted on a horse, with combat skill 6,
endurance 6, wealth 50. Roll one die for the number of men with him, each having combat skill 5, endurance 4, wealth 4. Troopers are mounted if there are one or two, on foot otherwise. Your options are:
die roll talk *evade fight
1 conversation r341 hide r319 surprise r301
2 bribe to hire (20) r332 pass r328 surprise r302
3 hirelings r338 pass r329 surprise r303
4 hirelings r339 hide r317 attack r304
5 looters r340 pass r327 attack r305
6 attacked r306 escape mtd r312 attack r306
* if your party has any mounts, add one (+1) to your die roll for this option, results higher than 6 are
considered 6; if your party all have winged mounts and/or flying ability, you can use escape flying (r313)
instead of rolling the die for the evade option.

e005 Amazons
You see a group of Amazon warriors approaching, all on foot. The number in the group is one die roll plus one (+1). All are combat skill 6, endurance 5, wealth 4. They are blood-sisters, and will always hire out together, serve together, and if any are abandoned or left behind all will desert you. Your options are:
die roll talk *evade fight
1 conversation r341 escape r311 surprise r302
2 hirelings r338 escape r314 surprise r303
3 hirelings r339 escape r315 attack r304
4 looters r340 hide r119 attack r305
5 pass r327 pass r328 attacked r306
6 attacked r306 hide r317 battle r330
* if your party has mounts, you may use escape mounted (r312) instead of rolling the die when using the evade option.

e006 Dwarf
You encounter a Dwarf Warrior with combat skill 6, endurance 7, and wealth 21. First select one of the three options below (talk, evade, fight). Then, before rolling a die to resolve the option, first roll one die to see if he is alone or accompanied by friends:
1,2,3 Dwarf is alone
4 Dwarf has one friend with him, combat skill 5, endurance 6, wealth 12.
5 Dwarf has a number of friends with him equal to one die roll, each is combat skill 5, endurance 6, wealth 12.
6 Dwarf is leader of a band, see e058 for the number of dwarves in it, and use the option selected to resolve the event in that section.
die roll* talk ** evade fight
1 surprised r308 bribe (5) r322 surprised r308
2 bribe to hire (10) r322 pass r328 attacked r306
3 looter r340 escape r314 attacked r306
4 hirelings r339 escape r315 attack r305
5 hirelings r333 escape r311 attack r305
6 †conversation r341 attacked r306 attack r304
7 †ally r334 escape r311 surprise r303
* if Dwarf Warrior is alone, add one (+1) to the die roll.
** if your party has mounts, you may use escape mounted r312 instead of rolling the die to resolve the evade option.
† if Dwarf(s) join your party as a result of this, they will reveal to you the location of ancient Mines, roll one die
for direction (1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW) and a second for the distance in hexes. When you arrive
there, after normal travel events (if any), roll one die for what you find: 1,2 -e059; 3,4-e064; 5-e056; 6-
e028.

e007 Elf
You encounter an Elf on foot, with combat skill 5, endurance 5, wealth 15. In addition, after you select your option (from the three below), roll one die to determine his additional characteristics, if any:
1 No additional characteristics.
2 He is actually leader of an Elven Band, see e071 and using the option already selected, resolve the event using that section instead of this (also use e071 to determine how many additional elves in the band will now appear).
3 He is a magician with a nerve gas bomb e190 (if he is forced to fight, he will use the bomb if allowed a surprise attack in combat, r220).
4 He is a magician carrying a vial that cures poison (e181), and has an assistant with combat skill 3, endurance 3, wealth 2.
5 He is a priest of an Elvish forest cult with a healing potion (e180).
6 He has a friend traveling with him, who is combat skill 4, endurance 4, wealth 7.
Due to the greater wisdom of Elves, subtract one (-1) from your own wit & wiles throughout this event or encounter. However, if the Elf joins your party, add one (+1) to your wit & wiles while he is in the party, due to his sage advice and extensive knowledge. Your options are:
die roll* talk **evade fight
1 inquiry r342 hide r317 surprise r302
2 conversation r341 hide r318 attack r305
3 inquiry r342 escape r314 attacked r306
4 conversation r341 escape r315 attacked r306
5 escapee r335 escape r315 surprised r308
6 plead comrades r336 pass r326 battle r330
7 pass r328 pass r329 surprised r309
8 pass r329 surprised r310 surprised r310
* if the event occurs in a forest, add two (+2) to the die roll.
** if the party is not in forest, you may use escape mounted r312 instead of rolling the die for the evade option.

e008 Halfling
You encounter a halfling with combat skill 3, endurance 6, and wealth 4. You can attack him, talk with him, or pass by and end the encounter. If you attack him, you strike first in combat (r220), but after each round roll one die, a "2" or higher means the halfling has escaped into the brush if still alive, the combat is over. If you pause to talk with him, you find he is a long-winded fellow like most halflings, and you cannot travel further today, and any other daily actions still undone will remain undone. To resolve the results of the talk, roll one die:
1 Banal conversation and many irrelevancies waste your time, nothing is accomplished.
2 Halfling tells you location of his village, which is in an adjacent hex, roll one die for the direction (1-N,2-NE, 3-SE, 4-&, 5-SW, 6-NW). If you enter that hex, see e070 after any normal travel events are finished.
3 General inquiries are needed, see r342.
4-5 Extended conversation results, see e341.
6 Halfling has choice gossip and very useful information, roll one die again, 1,2,3-e147; 4,5,6-e162.
Regardless of the outcome of the conversation, the halfling will wander off, ending the encounter.

e009 Farm
You spot a small farm ahead. You may detour around it, but that will consume the rest of the day, ending all travel for today. Alternately, you can go up to it. If you approach the farm, you must decide whether to make it a friendly approach, or a raid. After you make this choice, then roll two dice 2-e012; 3-e012; 4-e011; 5-e014; 6-e010; 7-e011; 8-e013; 9-e015; 10-e012; 11-e016;12-e016.
If you select a raid, and remain in this hex at the end of today, you may be attacked by a revengeful mob tomorrow morning, before you have a chance to select your daily action. At that time roll one die, if a 5 or higher results see e017. If any other number occurs, there is no mob or event.

e010 Starving Farmer
Friendly Approach: farmer had a ruined harvest, his family is now starving. He begs the charity of 5 food units from you. If you refuse this although you have them, all your followers are disgusted by your evil temper, roll one die for each at the start of tomorrow, a 3 or higher means that follower deserts you. If you grant the charity, or don't have 5 food units, there is no special event and the encounter ends.
Raid: farmer and his family are quickly killed, no combat is necessary, but you find he was poor and starving, no food or money are gained.

e011 Peaceful Farmer
Friendly Approach: farmer is generous, provides food and lodging for your entire party tonight at no cost. Tomorrow morning, he will sell you food units at the rate of 4 units per gold piece, and will sell as much as you wish to buy. Finally, when you finally leave the hex, roll one die, if the result is 6 the farmer's youngest son joins you for the adventurous life. He is combat skill 3, endurance 4, wealth 0, and can act as a guide within two hexes of the location of the farm.
Raid: farmer and his family fight back. Together they count as combat skill 4, endurance 7, wealth 1, see r330 for combat situation. If you kill them all, you gain four times (4x) one die roll in food units as plunder.

e012 Farmer with Protector
Friendly Approach: farmer warns you off his land, but will sell you food at 2 units per gold piece, in any
quantity you desire. Regardless of whether you buy or not, the event will then end and you continue on your
way.
Raid: farmer and his family bolt doors and send smoke signals, Farmer and family count combat skill 4,
endurance 7, wealth 2 in combat (r220) where your party strikes first. However, after each round roll one die, a "3" or higher means the Protector arrives with his men. If they arrive, on the next round they strike first. They are five men strong, the Protector himself is combat skill 6, endurance 5, wealth 25, and his four men each are combat skill 5, endurance 5, wealth 4. If you kill all your opponents in the raid, you can find the treasure the farmer tried to hide, see e040.

e013 Rich Peasant Family
Friendly Approach: family provides food and lodging as if you are in town (see r215 food and r217 lodging for costs), with the same penalties if you refuse to pay. Family may have stables, roll one die, result of "4" or more means they do. If they have stables, roll again for number of horses available for sale, then roll one die again and double it for the price per horse. They will sell horses at this rate, and will also sell food at 2 food units per gold piece (an unlimited amount of food is for sale).
Raid: family has four retainers, each with combat skill 4, endurance 4, wealth 1. You must fight these in combat (r306), and if you kill them, then you must fight a second battle against the family itself (r305), which overall has a combat skill of 5, endurance 6, wealth 30. If you kill everyone, then you gain six times (6x) one die roll in food units as bonus plunder.

e014 Hostile Reaver Clan
Roll one die and add two (+2) for the number of clan members. The leader is combat skill 5, endurance 5, wealth 10; other clan members are combat skill 4, endurance 4, wealth 4.
Friendly Approach: if clan equals or outnumbers your party, they will attempt a surprise attack, see r307. If you outnumber the clan, they will bar the house and bid you pass on. You can then either pass on, or make general inquiries. If you select the latter, see r342, but any reavers who do not join your party will automatically attempt a surprise attack, see r307. If they do, those reavers who joined will not participate in that combat.
Raid: there is a battle between your party and the clan, see r330.

e015 Friendly Reaver Clan
Roll one die and add one (+1) for the number of clan members. The leader is combat skill 5, endurance 4, wealth 7; other clan members are combat skill 4, endurance 4, wealth 4.
Friendly Approach: clan leader will discuss terms with you, see r342. Unless combat results, he will also sell food at 2 units per gold piece, and horses at 6 gold pieces each, regardless of whether he joins your party or not.
Raid: There is a battle between your party and the clan, see r330.

e016 Magician's Home
Friendly Approach: magician insists you stay the night and tell him of your adventures to date. You must
provide your own food for the day, as he has a small larder. He may be willing to discuss joining your party, he is combat skill 3, endurance 5, see r342 if you wish to try. If you don't, or do and avoid a combat situation, he will give you a magic gift, roll once on line "B" of the Treasure Table (r226) for the item received.
Raid: magician calls upon his powers to defeat and destroy your party. Roll one die for the number of wounds you suffer, one of which is poisoned. All your followers die or flee, deserting you. You must abandon everything you cannot carry yourself. You will save any mount you are riding, and its loads, but no other mounts can be saved. If you have the Resistance Talisman (el84) you can stop his powers and destroy the magician in battle at the cost of destroying the talisman. If you do, roll one die for the wealth code of the magician: 1-5; 2,3-25; 4,5-60; 6-110.

e017 Peasant Mob in Hot Pursuit
A large mob of angry farmers and villagers are after you! You are trapped and must fight your way out. Roll two dice and double the sum. This is the number of men in the mob. One of these is the leader, with combat skill 3, endurance 2, wealth 2; all the others are combat skill 2, endurance 2. See r330 for the exact combat situation.

e018 Priest
You encounter a local Priest riding on a donkey (equivalent to a horse as a mount), with combat skill 3,
endurance 3, wealth 25. He seems aloof and not disposed to conversation, but he may be afraid of you . . . You can let him pass, ending this encounter, or select one of the two options below:
die roll talk fight
1 plead comrade r336 surprise r301
2 plead comrade r336 surprise r303
3 plead comrade r337 attack r304
4 conversation r341 attack r305
5 inquiry r342 attack r305
6 pass r325 attack r306
Note: if you do fight the Priest in combat, and kill him, roll one die. If a 5 or 6 results, he casts upon you the "mark of Cain". You must immediately roll once for each follower in your party, and any time the roll is greater than your wit & wiles the follower will immediately desert you. In addition, all Monks and Priests in the future will recognize the mark, and will not join your party. You can never attempt an audience (r211) with the high priest of any temple marked on the map, but may with high priests of any secret unmarked temples that you find.

e019 Hermit Monk
You encounter a hermit monk meditating in the wilderness, with combat skill 3, endurance 6, wealth 0. He seems to be ignoring you. You can select one of the options below;
die roll talk avoid fight
1 inquiry r342 pass r325 attack r305
2 conversation r341 pass r325 attack r305
3 *plead comrades r336 pass r325 attacked r306
4 *plead comrades r336 pass r326 attacked r306
5 pass r325 surprised r310 attacked r307
6 pass r325 **monk e022 surprised r308
* unless a Priest or Monk is with your party, reduce your wit & wiles by one (-1) temporarily when resolving these events, hermit monks listen poorly.
** monk is not what he seemed, see this event for what you really encountered, select a new option, and resolve the event accordingly.

e020 Travelling Monk
You encounter a travelling monk, who has combat skill 4, endurance 5, wealth 4. Roll one die, if the result is 5
or 6 he is accompanied by a companion monk of equal abilities. He seams eager to talk, your options are:
die roll talk evade fight
1 conversation r341 pass r325 surprise r302
2 conversation r341 pass r325 attack r304
3 inquiry r342 pass r326 attack r305
4 plead comrades r336 inquiry r342 attack r305
5 plead comrades r337 inquiry r342 attacked r306
6 surprised r309 escape r311 attacked r306

e021 Warrior Monks
You encounter a party of Monks belonging to a powerful military order, who have weapons and armor. Each monk is combat skill 6, endurance 6, wealth 10. Roll two dice and halve the total (rounding fractions up) for the number in the group. Roll one die again, if the result is 4 or higher they are all mounted as well. Your options
are:
die roll talk *evade fight
1 conversation r341 pass r325 surprise r301
2 inquiry r342 hide r317 surprise r302
3 pass r329 hide r319 attack r304
4 bribe to pass (10) r323 escape r315 attack r305
5 attacked r306 bribe (10) r324 attacked r306
6 roll again pass r329 attacked r306
* if your party has mounts, and the warrior monks do not, you may use escape mounted r312 instead of rolling the die for the evade option; if your party has winged mounts, you may escape flying r313 instead of rolling the die for the evade option, if you wish.

e022 Monks — reference
You have encountered a monk or monks, roll one die again for the event: 1,2-e019; 3,4-e020; 5,6-e021.

e023 Wizard
You meet a Wizard with combat skill 4, endurance 4, and wealth 60. A henchman with combat skill 5, endurance 4, and wealth 4 accompanies him. Roll one die, if the result is 3 or higher, they are mounted on horses. The wizard seems old, but still active and perhaps quite powerful. Your options:
die roll *talk evade fight
1 inquiry r342 pass r325 attack r305
2 inquiry r342 pass r325 attacked r306
3 conversation r341 bribe-pass (5) r321 see e024
4 see e024 escape r314 see e024
5 pass r328 escape r313 surprised r308
6 ally r334 see e024 attacked r307
* if the wizard joins your party, see also e025.
Wizard Fireballs: if you get into combat (r220) with the wizard, he may strike at your party with fireballs, instead of making a normal strike. Before each strike by the wizard, roll one die. If the result is 5 or 6, he strikes with a fireball spell. When the spell strikes, roll one die, that is the number of wounds each character in your party suffers, including yourself. If the wizard has any wounds, he will automatically escape when the fireball strikes. Otherwise, he will remain and allow the battle to continue.

e024 Wizard attack
Wizard attempts to use magic and take control of you and your party. Roll one die; if the result equals or exceeds your wit & wiles, his attack is successful. All your followers become slaves of the wizard and are lost to you. He captures all their wealth, possessions, and mounts also. If he fails to capture them, your entire party escapes instead (r218).
If your followers became slaves, roll one die again, if the result exceeds your wit & wiles, you too are captured by the wizard. If not, you escape (r218). If you are captured, you lose all your possessions, wealth, and mount.
Each day you are a slave, instead of a normal daily action, you can do nothing — you are being moved around
by the Wizard. Roll one die for the direction of his travel (1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW), he will only move one hex per day. For every three days you spend as a wizard's slave, you suffer one wound as a result of starvation and overwork. At the end of each day as a slave (including the end of the day you are captured), you can roll one die for an escape attempt. If the result is 6 you escape (r218) immediately. If the result is 1 you are caught trying to escape and suffer one extra wound due to his cruel punishments. Any other result is no effect, because no suitable escape opportunity has arisen. If you finally escape, you do so only with yourself and your weapons, without any money, food or followers

e025 Wizard Advice
The wizard, now a member of your party, confides during the evening meal that he knows of a valuable treasure. According to his information, the treasure is in a certain direction (roll one die: 1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW) and a certain distance away (roll one die for distance in hexes). Once you reach that hex, consult e026 for how to find the treasure.

e026 Search for Treasure
You believe you have found the proper location of a treasure. You now must spend one day searching for the
precise spot, as if you were trying, to Find a cache (see r214). At the end of that day, roll one die: 1-e027; 2-e028; 3-e029; 4,5-bogus information, nothing is found; 6-clues suggest the treasure is in an adjacent hex, roll one die to determine which direction (1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW). After you arrive there, you can apply this event again.

e027 Ancient Treasure
You find an ancient treasure, long lost. It is wealth code 110, see r225.

e028 Cave Tombs
Amid the howling winds on a craggy cliff you find caves, and within the caves the tombs of an ancient race. You can decide to avoid them, ending this event, or you can continue inward and investigate the tombs. If you continue inward, roll one die: 1-e030, 2-e031, 3-e032, 4-e033, 5-e034, 6-e029.

e029 Danger & Treasure
You sense that both danger and treasures are near. Roll one die and see that event: 1-e028; 2-e032; 3-e036;
4-e037; 5-e038; 6-e044.

e030 Mummies
You discover dried mummies of a long lost race. Although a scholar may be interested, you aren't, because amid the dust and rot you find just one (1) gold piece!

e031 Looted Tomb
You find a partially looted tomb of a dead Prince. Under his sarcophagus you find a secret compartment, but it has a trap lock. Roll one die, if your wit & wiles exceed the die roll, you have outwitted the trap, otherwise see r227 for injuries it may inflict. In either case, you find a treasure with wealth code 50, plus a Gift of Charm (e182). However, the Gift of Charm is very old, roll one die, if the result is 5 or 6 it turns to dust as you lift it from the compartment, and is therefore worthless.

e032 Ghosts
A group of ghosts surprise you in combat (r220), roll one die and add one (+1) for the number of ghosts, each of which is combat value 4, endurance 2. They are guarding an ancient altar. If you kill all the ghosts, you can investigate the altar if you wish. If you do, roll one die: 1-e037; 2-e039; 3-e041; 4-e042; 5-e044; 6-nothing.

e033 Warrior Wraiths
Wraiths of long dead super warriors assault your party, and strike first in combat (r220) against you. Roll one die for the number of wraiths, which is always two or more (die roll of one is considered two instead). Each Wraith has a combat value of 6, endurance 9. If all are killed, you find they are guarding plunder from an ancient battle, roll one die to determine the wealth code of this treasure: 1-25; 2-50; 3-60; 4-70; 5,6-100. Seer225 for details.

e034 Spectre of the Inner Tomb
Looking around the atrium of an old tomb, you notice a hidden passage to the interior. You pass within, but it is a long hall, taking the rest of the day to explore. You sense the presence of a Spectre. You can either retreat now, or continue. If you retreat, the event ends.
If you continue, at the end of the day, before the evening meal, you finally reach the inner tomb, and find the Spectre. It has combat value 7, endurance 3, but is only hurt by poison wounds (normal wounds have no effect) or by wounds from a magic sword. Any priest, monk, magician, wizard, or witch will have magical weapons that are poison to the Spectre.
If you kill the Spectre, roll one die to determine the wealth code of the treasure it guarded: 1-5; 2-12; 3,4-25; 5-60; 6-110; see r225 for details.

e035 Spell of Chaos
A guardian spell of chaos is activated as your party passes within. You and your entire party become mindless idiots. All wander away, so you lose all followers and possessions except for your own mount, and any wealth and possessions you personally carry. You do not eat an evening meal, and begin to suffer the effects of starvation (r216). At the start of tomorrow, roll one die and subtract one (-1) for the number of days you remain mindless and wandering. If the result is zero, you have recovered. If the result is any other number, each day roll one die for the direction you wander (1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW), at one hex per day. You have no travelling events while wandering, and will not eat. When your mind finally returns, you can begin to function normally again at the start of the next day.

e036 Golem at the Gate
You become separated from the rest of your party during the search. You notice the gateway of a ruined temple, and pass through it. A huge golem appears before you, made entirely of living stone. It raises its sword and strikes first in combat (r220). It is combat skill 6, endurance 8.
If you kill the Golem, roll one die for the next event: 1-e038; 2-e040; 3-e043, 4-e044; 5-e046; 6-e027.
If you escape (r220e) from the Golem in combat, you lose the rest of your followers and all mounts, only you, your possessions and your wealth on your body survive. If you defeat the Golem and survive subsequent events without making an escape (r218) you will rejoin your party at the evening meal (r215).

e037 Broken Chest
You find a chest with a broken and cracked lid. Sorting through old mouldering cloths, you find (roll one die): 1-e180; 2-e181; 3-e182; 4-e184; 5-e186; 6-e189.

e038 Cache under Stone
By chance you overturn a stone slab, jumping back as it crashes to the ground. You see that it uncovers an old cache of rotting food and other items. Roll one die: 1-e180; 2-e181; 3-e182; 4-e185; 5-e187; 6-e190.

e039 Treasure Chest
You find a locked chest. You know the lock may be trapped. If you decide to open it, roll one die, if the result is 3 or higher it does have a trap lock, see r227. If you survive the trap (if any), and open the chest, roll one die. If the result is 6 the chest is empty. Otherwise it has a treasure with a wealth of 60. This may include a special possession, but if that possession is a pegasus winged mount, it is actually an item with a pegasus emblem, roll again with one die and consult line A on the Treasure Table (r225) for the actual item found.

e040 Treasure Chest
You find a locked treasure chest protected by a trap. You can either ignore it, or attempt to open it anyway. If you try to open it, roll one die, if the die roll exceeds your wit & wiles you have bungled and sprung the trap, see r227. If you survive the sprung trap (if any), you can now open it, roll one die to determine the wealth code of the contents: 1-5; 2-25; 3-50; 4-60; 5-70; 6-100. See r225 for details. Any result that includes a pegasus winged mount as a possession actually is a pegasus talisman which you can keep. Whenever you have any magician, wizard, witch, priest or monk in your party, they can help you use the talisman to call upon an actual pegasus winged mount, which will immediately appear and serve as your mount (see r204 for details on airborne travel and the use of winged mounts).

e041 Vision Gem
You find a large, fixed stone with multiple facets. You gaze into it without thinking, and find you can look elsewhere. Roll one die for what you discover: 1-e143; 2-e144; 3-e145; 4-e146; 5-e147; 6-nothing of value.

e042 Alcove of Sending
You find a small alcove inscribed with runes. If your party includes a magician, wizard or witch the runes can be deciphered, and the alcove's secret put to use. Otherwise, this event ends. The secret of the alcove is simple: it sends voices and thoughts. Using it you can command an audience with either a High Priest (e155), the Mayor of a Town (e156), the Lady Aeravir of Aeravir Castle (e160), or Count Drogat of Drogat Castle (e161). For the audience you are temporarily transported to that location, and will return at the end of that day, just before the evening meal, regardless of where you are. Followers given from an audience cannot return with you, and are lost. After use the alcove needs many months to recharge, so it cannot be used again during the game (another alcove, if found, could be used).

e043 Small Altar
You find a small altar, on which is displayed (roll one die): 1-e186; 2-e189; 3-e191; 4-e192; 5-e193; 6-e194. However, there is also a magic spell shimmering around the altar. If your party includes a magician, wizard, or witch you can determine the nature of the spell by rolling one die and looking at the list below. Otherwise, you only discover the spell by actually risking it to reach the altar. Alternately, you can avoid the altar and end this event without ever trying to recover the item on the altar. 1,2 Magic shock field spell, no one can pass through and reach the altar, and anyone who tries automatically suffers one wound when repulsed. 3,4 Magic fire, roll one die and suffer that many wounds entering the spell. You can then retreat without reaching the altar, or can brave the fire further, recover the item, and roll one die again for the wounds suffered due to this prolonged exposure. 5 Poison air, roll one die and suffer that many poison wounds, but the item on the altar can be recovered in the process. 6 Fear spell, it has made your party afraid that an evil spell protects the altar, while in reality the fear spell can do you no harm. You walk to the altar, recover the item and return without injury.

e044 High Altar
You find a high altar of godly power. If any character in your party is a priest or monk, he will know the invocations to use at this altar. You may ask him to make the invocation, and roll one die to see what happens. If you don't ask him, or your party lacks such a follower, the event ends.
1 Monk or priest is engulfed in godly fires and dies.
2 Lightning and earthquakes destroy the high altar, roll one die for each character in your party, and suffer that many wounds due to flying stones and fire.
3 Monk or priest struck with one wound, discovers it was the altar to the wrong god, and more invocations are impossible there.
4 Voice of the gods sounds forth, and gives you an impossible riddle, and a prophecy none can understand. No more invocations are possible.
5 Voices of the gods give a prophecy that seems to promise a treasure, see e147.
6 One of the gods appears, issuing thunderbolts and flames, pledging support to your cause. In an astral vision you see the gods striking down the usurpers to your throne, and telling Northlands priests that your reign shall be holy. You will regain your throne and win the game if you can return alive to the northlands (any hex north of the Tragoth River) within the next 30 days. However, experiencing the power of the gods directly has weakened your human frame, your endurance is permanently reduced by one ( -1). In gratitude for the godly support, you must give all your money away to the gods of the altar instantly, or be struck down dead.

e045 Arch of Travel
You find a metal-banded archway inscribed with runes. If any character in your party is a magician, wizard or witch the runes can be read, and the arch used if you wish. Otherwise, the event ends. If you can use the arch, you can travel through it instead of making a normal daily travel action (see r204). Travel through the arch allows you to make a magical transfer to any other hex on the map, as you wish. However, you travel forward in time as well, so when you use the arch, roll one die and that is the number of extra days which pass when you use the arch, advance the time track by that many days and continue play (by determining if any travel events occur, etc. see r204). You cannot get lost by travelling through the arch. As long as your party continues to have a magician, wizard or witch you can return to this hex and use the arch again and again. However, arch travel is only one-way, from the arch to another hex. You cannot travel from any hex to the arch!

e046 Gateway to Darkness
You have found one of the dreaded black portals. Any follower in your party who joined you south of the Tragoth River will instantly recognize it. If you cannot recognize it, or decide not to use it, this event ends. The Gateway to Darkness feeds on death, and is timeless. If you enter it, you must abandon all your followers and mounts, since it only accepts one living creature at a time. As you step in, a guardian creature with combat skill 7, endurance 7 strikes first at you in combat (r220). You must fight to the death, you cannot escape. If you kill the guardian, you can then re-emerge from the other side of the gateway into the same hex you left. However, you have travelled backwards in time. Roll two dice and subtract the total from the number of days elapsed in the game. You have lost your followers because they are stuck in the future, in another part of the time stream, even though you have travelled backwards in time, all the gold, possessions, etc. you acquired still apply. The gateway thrives on paradoxes. You can enter the portal more than once, if you wish. However, each time you enter there is one additional guardian waiting within, plus all previously dead ones have come back to life. Therefore, the second time you enter there are always two guardians, the third time there are always three guardians, etc. Having once entered the portal, you know its secret too, and can use it even if you have no followers from south of the Tragoth.

e047 Mirror of Reversal
You see an old mirror, and looking into it, discover yourself twisted into evil shape. This thing leaps from the mirror and attacks you, getting the first strike in combat (r220). It has the same combat skill and endurance as yourself, and has the same possessions and gold. If you have any followers, you can call for their aid in the battle, but for each strike a follower makes, roll one die, a 5 or 6 means the follower strikes you by accident (mistaking you for your double). If you kill the mirror-thing, the battle ends, and you permanently add one (+1) to your wit & wiles, due to gaining a fuller understanding of yourself in this contest. In addition, you will (of course) double your possessions and wealth, by gaining that of the mirror-thing.

e048 Fugitive
You encounter a person trying to avoid local justice. He or she will join your party as an ally, but will desert whenever you encounter any Constables (unless your party elects to fight them, and kills them all) or whenever you enter any town, castle or temple. Instead, you can immediately elect to fight the character encountered, see r300. Roll one die to see exactly who you meet:
1 Swordsman adventurer, combat skill 7, endurance 7, wealth 1. Roll one die again, a 6 means she is a
swordswoman with endurance 6 and wealth 4, and you become lovers (r228).
2 Runaway slave, combat skill 2, endurance 4, wealth 0. Roll one die again, a 6 means she is a slave woman and you become lovers (r228). She can act as a local guide with 5 hexes of where you found her.
3 Priest, combat skill 3, endurance 3, wealth 10. He gives you half his wealth in gratitude (r225) and can act as a guide for you if you desire.
4 Magician, combat skill 3, endurance 2, wealth 5. He will give you free advice as well, see e025.
5 Merchant, combat skill 2, endurance 3, wealth 0. He can act as a guide if you desire, and will help you bargain properly for purchases as long as he remains with the party. As a result, you only end up paying half the normal price for anything you buy, or any bribes you make (round fractions upwards). Hiring and paying followers must still be at the normal rates. Roll one die again, 5 or higher means he has a horse as his mount as well.
6 Army deserter, combat skill 4, endurance 4, wealth 2. Roll one die again, a 5 or higher means he has a horse as his mount also.

e049 Travelling Minstrel
You meet a musician. You can ignore him and end this event, or invite him to dinner (r215). In the latter case, you must give him one food unit or he deserts, but if fed he will sing a tale that night that prevents any of your party from deserting, no matter what events happened today, even if you followers are not properly feed or lodged. After the songs and the meal, you may start a conversation if you wish, see e341. If he ends up joining your party, his ability to prevent desertions can be used just once more during the game, on any day you wish.

e050 Local Constabulary
This event only applies if you are within three (3) hexes of a town, castle, or temple. Otherwise there is no event. If the nearest town/castle/temple is Ogon (0101) or Weshor (1501), see e002 instead. You encounter local law enforcements officers. First roll one die to see if they are mounted, a 5 or higher roll means they are. Next roll one die to see how many you encounter, add one (+1) to the roll if they are mounted, add three (+3) to the roll if they are on foot. Each constable is combat skill 5, endurance 4, wealth 4. Now select your option, and roll the die. Add two (+2) to the die roll if you have visited the nearest town, castle, or temple before and did not leave it by an escape (r218). If you escaped, you cannot add two because you are undoubtedly a "wanted" man. If you have never visited the nearest town/ castle/temple before, you can add one (+1) to the die roll.
die roll negotiate * evade fight
1 surprised r308 attacked r306 surprised r308
2 attacked r306 hide r320 attacked r307
3 bribe-pass (10) r322 escape r311 attacked r306
4 bribe-pass (15) r323 escape r315 attack r305
5 pass r329 hider318 attacked r304
6 attacked r306 attacked r305 surprise r303
7 pass r325 pass r325 surprise r302
8 pass r326 pass r325 surprise r301
* if your party has mounts, and the constabulary does not, you may use escape mounted r312 instead of rolling the die for this option. If your party has winged mounts or can fly, you may use escape flying r313 instead of rolling the die for this option.

e051 Bandits
You are ambushed by bandits, who surprise you in combat (r220). The number of bandits exceeds the number of characters in your party by two. One of the bandits is the leader, with combat skill 6, endurance 6, wealth 15. The rest are combat skill 5, endurance 4, wealth 1.

e052 Goblins
You sight a band of Goblins in the distance. Roll two dice for the number in the band, each is combat skill 3, endurance 3, wealth 1. In addition, they are lead by an additional Hobgoblins with combat skill 6, endurance 5, wealth 5. You saw them first, so you can either escape (r218) from the area, or attempt to follow them (r219). If you follow them, after the follow movement (r219) roll one die. If the result exceeds your wit & wiles the band discovers you and attacks, but your party will get the first strike in combat (r220). If they do not discover you, roll one die to see where they lead you: 1-e054; 2,3,4,5,6-e053.

e053 Campsite
Roll two dice for the campsite location. You may now elect to fight the characters encountered at the campsite, or not. If you don't, unless otherwise indicated in a previous event, you must hide (r218) in the hex until tomorrow. If you elect to fight, the characters encountered, and kill them, you gain control of their campsite.
Campsite locations are:
2 Campsite at a small altar, when you gain control see e043.
3 Campsite at previously unknown ruins, if you gain control see e064.
4 Campsite at the entrance to cave tombs, if you gain control see e028.
5 Campsite is rendezvous with another group of the same size, group encountered is now double its original size; you must roll one die, if it exceeds your wit & wiles they discover you and attack, although you get the first strike in combat (r220); if they don't discover you, roll two dice again and once more refer to this listing (which could lead to this result again, causing another doubling and check for possible discovery).
6,7,8 Campsite in open ground, no special event as aspect of site.
9 Campsite hidden by terrain and vegetation, if you gain control of it, roll again to see exactly where it is (if this result occurs again, roll again until some other result occurs).
10 Campsite is at a small building, if you gain control you can investigate, roll one die for event 1- e042; 2-e037; 3-e038;4-e039; 5,6-nothing. You need not investigate if you prefer to play it safe.
11 Campsite is near a place where you sense magic, if you gain control of it you must immediately roll one die: 1-e032; 2-e036; 3-e043; 4-e044; 5-e045;6-e046.
12 Campsite is near a place of hidden magic. If you gain control of the site, and have a priest, monk, magician, wizard or witch in your party, roll one die: 1-e022; 2-e036; 3-e043; 4-e044; 5-e045;6- e046.

e054 Goblin Keep
You see a fortified tower keep of a Goblin King. The area is swarming with hundreds of Goblins. You decide you should escape, but a band of Goblins has already seen you. They charge forward with screams and howls.
If you are unable to escape from this hex for any reason (see r218) or decide not to resist, you are captured, see e061.
If you try to escape, first make your escape move (r218). Then roll one die to see if you elude the pursuing Goblins. If your wit & wiles is greater than the die roll, you lose them and the event ends. Otherwise, you must either surrender (go to e061 and return to the keep hex), or fight them. If you fight, roll one die three times for the number of Goblins, each is combat skill 3, endurance 3, and wealth 1. In addition, there is one Hobgoblin leader with combat skill 6, endurance 5, and wealth 4. You can strike first in combat (r220). You cannot escape from combat, you must kill or be killed. If you kill them all, your escape is made good, and this event ends. If you return to the hex with the Goblin King's keep any time later in the game, you will be captured automatically by the Goblins, see e061.

e055 Orcs
You sight a band of Orcs in the distance. Roll two dice for the number in the band. One is a chieftain with combat skill 5, endurance 6, and wealth 7. The rest are warriors, combat skill 4, endurance 5, and wealth 1. You can either escape (r218) from the area, or attempt to follow them (r219). If you follow them, after the follow movement roll one die. If the result exceeds your wit & wiles the Orcs discover you and attack, but your party gets first strike in combat (r220). If they don't discover you, roll one die to see where they lead you: 1-Orc Tower e056; 2,3,4,5,6-Campsite e053. If they lead you to a campsite, you can either avoid them by escaping to an adjacent hex (r218) or you can make a surprise attack in combat (r220) against them at their campsite.

e056 Orc Tower
You see the dark tower of an Orc Warlord. The area is full of Orcs and worse things. An Orc war-patrol led by a demi-Troll of combat skill 8, endurance 7, and wealth 10 spots you. Roll one die and add one (+1) for the number of Orcs in the patrol also, each has combat skill 5, endurance 5, wealth 2. You can either surrender to them (go to e061) or try to escape.

e057 Troll
A huge stone-skinned Troll confronts your party. Roll one die, if the troll exceeds your wit & wiles, then it strikes first in combat (r220), otherwise you strike first. The Troll is combat skill 8, endurance 8, wealth 15. Furthermore, the Troll skin has regenerative properties. It automatically cures one wound at the end of each combat round you fight against it. If you kill the troll, its stone-skin is a valuable item. Whenever you have an opportunity to buy food at a town, castle, temple, or from merchants you can sell the skin for 50 gold. It is also known that Count Drogat, of Drogat Castle, will treasure the gift should you manage to get a personal audience with him.

e058 Band of Dwarves
You encounter a group of dwarves. Each dwarf is combat skill 5, endurance 6, wealth 10. Roll one die and add one (+1) for the number of dwarves in the band. If your party has fewer members than the dwarf band, you spot them first, and can either follow them (r219), hide or escape from them (r218) as you wish, or meet them, using one of the three options below. If your party is equal in size or larger, they spot you first, you must meet them, and select one of the options below:
die roll talk *evade fight
1 inquiry r342 escape r311 surprise r302
2 bribe-join (30) r331 escape r314 surprise r303
3 bribe-hire (10) r332 escape r315 attack r304
4 hirelings r339 hide r317 attack r305
5 pass r328 hide r319 attacked r306
6 attacked r306 attacked r306 surprised r308
* if your party has any mounts, you can use mounted escape r312 instead of rolling the die if you select the evade option.
Following: if you follow the dwarves, after follow movement (r219) roll one die. If the result equals or exceeds your wit & wiles the dwarves discover you and attack, striking first in combat (r220). If they don't discover you, roll one die to see where they end the day: 1-Dwarf Mines see e059; 2.3.4.5,6-Campsite see e053.

e059 Dwarf Mines
You see a great underground castle inhabited by Dwarves. Dwarven constables and patrols intercept your
party. Roll one die. If the die roll exceeds your wit & wiles, you and your party are arrested immediately, see e060. Otherwise, you are passed, and enter the castle mines. There you can undertake any actions and activities normally allowed in a castle (r203). This includes seeking an audience with the Dwarf King who rules there (r211, use Huldra castle table). Like any castle, you must spend the normal amounts for food (r215) and lodging (r217).

e060 Arrested
You and your party are arrested by an overwhelming force, and cannot resist. You are put into jail, roll one die for the gravity of the offence: 1 (or less)-e061; 2-e06 2; 3,4-e06 3; 5,6-see next paragraph (e060a). e060a Minor Offence: you are held overnight, along with your entire party, although the jailers provide food and "lodging" for all. Tomorrow you are assessed 10 gold pieces fine, plus jailing cost of 2 gold pieces per character (including yourself) and 1 gold piece per mount. Any whom you pay for are released. Any whom you do not pay for are left in jail and lost. If you cannot pay for anyone's release (not even yourself), you and your party are imprisoned, see e063.

e061 Marked for Death
You and your party have committed a very grave offence. The death penalty is demanded. Until then, you and your party are imprisoned. All your money, possessions and mounts are confiscated and permanently lost. You are provided with food and lodging while in prison. At the start of each day in prison roll one die: 1 means you manage to escape (see below for details), 6 means you must finally meet the headsman and are put to death. Any other die roll means you continue to languish in prison.
Escapes: if you escape from prison, roll one die for each other character in your party, who were imprisoned near you: 1,2-they are part of the escape and join you; 3,4,5,6-they are unable to join the escape, or have already been executed. Now that the size of your party is determined, use the escape rules (r218) to determine where you end up. The escape takes the entire day, after it you must prepare for the evening meal (r215).

e062 Thrown in the Dungeon
You are thrown into a deep dungeon. Other members of your party are imprisoned or sold as slaves, and therefore are permanently lost (unless a lover, see r228). You lose all your wealth, possessions and mounts. While in the dungeon, you are provided with food and lodging (of a sort). At the start of each day in the dungeon roll two dice, a result of 2 or 3 means you escape (see r218) that day, any other result means you continue to languish in captivity. Every full week (seven days) you spend in the Dungeon inflicts one poisoned wound on you, due to unhealthy conditions, disease, and gradual weakness and starvation. If you escape, it takes the entire day. After it, you must find food for your evening meal (r215).

e063 Imprisoned
You and your party are imprisoned. All your money, possessions and mounts are confiscated and lost. While in prison, you are provided with food and lodging. At the start of each day roll one die, 1 means you escape, any other result means you continue to remain captive. If you escape, roll one die again for each character in your party, another 1 means they escape with you, any other result means they cannot escape and are lost. When you escape, including any followers, see r218 for procedure. The escape takes the entire day, after it you must find food for the evening meal (r215).

e064 Ruins
You discover hidden ruins. You can undertake a search action in them (r208) on any following day you are in the hex, just as if they were ruins marked on the map.

e065 Hidden Town
You discover a previously unknown town. You can undertake any normal actions there, as if it were a town on the map (r203). You are also in a town for food (r215) and lodging (r217). However, due to the isolation of this town, you cannot seek news and information (r209) here.

e066 Secret Temple
You find a secret temple, of an obscure and feared cult. Before you can do anything a large group of guardian monks surrounds you. Roll one die: if the result equals or exceeds your wit & wiles you and your party are arrested, see e060 and subtract one (-1) from the die roll when resolving that event. If the result is less than your wit & wiles you talk your way past the guardians, and you can stay at the temple as if it were a normal temple marked on the map. Thus the rules for food (r215) and lodging (r217) at a temple apply, as well as your ability to undertake daily actions allowed at a temple (r203). If you later return to this temple, the guardians will continue to permit you free entrance, with no new die rolls needed/However, if you kill anyone while in this temple hex, or escape from it, the next time you enter you must begin this event afresh, including a new die roll.

e067 Abandoned Mines
You come across apparently abandoned mines. It looks like they were once inhabited by dwarves. You can avoid them, ending this event, or you can enter them and investigate further. If you enter, roll one die: 1-e059; 2-e051; e-e046; 4-e045; 5,6-e028.

e068 Wizard's Abode
You come across a wizard's home. Roll one die: 1,2-e023; 3-e024; 4-e016 and roll die for your approach (even is friendly, odd is a raid); 5,6-see e068a in the paragraph below:
e068a Wizard Tower: a great wizard's tower looms before you. It is just like a castle for all game purposes, including food (r215) and lodging (r217). However, the ruling wizard is jealous, and will tolerate no rivals. Any magicians, wizards or witches in your party will either desert or be arrested, unless you elect to have your whole party escape (r218) from the hex. If you stay, on subsequent days you can perform any daily actions normally allowed at a castle (r203), but if you seek an audience with the ruler (r211) use the temple and high priest tables.

e069 Wounded Warrior
You come across a heroic fighter near death. He was combat skill 7, endurance 6, wealth 0, but he has five wounds. If you remain with him while he rests and heals, or carry him while he heals, as part of your party, he will join your party as an ally, at no cost except food (r215) and lodging (r217) as necessary.

e070 Halfling Town
You come across a hidden and unknown town of halflings. You can undertake any normal actions (r203) in this town, but normal rules for food (r215) and lodging (r217) apply. However, halflings have a great love of gossip, news and new faces; any day you spend doing a seek news and information action (r209), you and your party will be wined and dined so much that you need not buy any food for your evening meal, you've already had more than enough! If you kill any character while in the halfling town, or must escape from the town, for the rest of the game the halflings will dislike you. You will no longer be wined and dined when seeking news and information. Any time you seek news and information (r209), hire followers (r210), or seek and audience (r211) in the town, you must suffer an extra minus one (-1) to your dice roll when resolving these actions.

e071 Elven Band
You encounter a band of elves. Roll one die and add one (+1) for the number of elves in the band. Each elf is combat skill 5, endurance 4, and wealth 7. You have three options:
die roll talk evade fight
0 follow e072 passr325 surprise r301
1 inquiry r342 escape-fly r313 surprise r302
2 inquiry r342 escape r315 attack r305
3 conversation r341 hide r318 attacked r306
4 pass r325 hide r320 attacked r307
5 follow e072 attacked r306 surprised r308
6 surprised r309 surprised r309 surprised r310
7 surprised r309 escape-fly r313 attack r305
Note: if your party includes an elf, subtract one (-1) from your die roll; if your party includes a dwarf, add one (+1) to your die roll.
e072 Following an Elven Band
The elves bid that you follow them. If you do not, refer back to e071 and select either the ‘evade’ or ‘fight’ option. If you do follow the elves, after making a follow move (r219) roll one die to see where you end the day: 1-Elven Town e165; 2-Elven Castle e166; 3,4,5,6-Campsite e053. If you end up at a campsite, you may peacefully share the campsite with the elves, eating your own food (r215, including hunting where possible). On the follow day you can select any daily action, or you can continue to follow the elves instead. If you follow them, make the follow move (r219) and roll again for where you end up. Thus you could follow the elves for a number of days before arriving at a town or castle. Alternately, you can fight the elves for control of their campsite at the end of any day (before the evening meal r215). The elves are able to strike first in this combat (r220).

e073 Witch
You encounter a witch with combat skill 1, endurance 3, wealth 5. Roll one die, if it exceeds your wit & wiles she is hostile; if the roll is equal she ignores you and the event ends; if the roll is less she is friendly. Hostile Witch: your party must escape (r218) immediately. Roll one die for each character in the party, including yourself. If a 6 occurs the character was turned into a frog before he or she escaped, and is lost. If you are turned into a frog, any lover, magician, wizard, or friendly witch surviving in your party can turn you back. Otherwise, you will remain a frog for years, and lose the game. Friendly Witch: roll one die to determine her actions: 1,2-she joins your party as an ally (r334); 3,4-she can be hired to join your party (r333); 5,6-she gives you a gift, see e195.

e074 Spiders
Giant spiders trap you, roll one die for the number of spiders. Their webs trap your party, and the combat skill of each character is reduced by one. Each spider has combat skill 4, endurance 3, and inflicts only poisoned wounds. It is very likely that you are surprised also, see r309.

e075 Wolves
This event is postponed until after your finish your evening meal (r215). Ignore this event if in any town, castle or temple. At night a hunting pack of wolves attacks your party. Roll three dice for the number of wolves, each of which is combat skill 3, endurance 3. They may surprise you, see r309. At the end of each combat round, if any wolves are still left alive, one of your mounts will be killed by the wolves. Since materials being transported (r206) by the mount have been unloaded for the night, only the mount itself is lost, not what it carries. You cannot escape from the wolf attack.

e076 Great Hunting Cat
Ignore this event if you are in a town, castle or temple. You are surprised by a great hunting cat, with combat skill 6, endurance 3. It surprises you in combat (r220) and selects one victim (see r341). As soon as the cat kills this victim it disappears into the wilds, carrying off the victim and any wealth or possessions the victim might carry. The victim's mount (if any) is killed, but left behind. When in combat with the cat, the victim cannot escape, but the rest of your party may escape combat.

e077 Herd of Wild Horses
Ignore this event if you are in a town, castle, temple or swamp hex. You surprise a herd of wild horses. Each character in your party can capture one, giving you that many additional mounts. However, you must spend tomorrow resting (r203) in order to train the captures. If you have a magician, wizard or witch in your party, that character can cast a spell that trains the animals instantly, no extra day of rest is needed.

e078 Bad Going
Ignore this event unless your party is travelling on mounts without wings (r204) such as horses. Ignore this event regardless of mounts if your party travelled along a road, or entered a village, castle or temple. Terrain is difficult for horses. You must either halt for the day to explore alternate routes, or you risk injuries. If you continue normal travel today, roll one die and subtract three (-3). If the result is 1 or more, that many horses have broken legs or thrown shoes, and are lost as mounts after the move. This may require you to reorganize transport loads (r206) and/or cache items your are carrying (r214). If this event occurs after your last travel move for the day, the difficult terrain applies for any travel (r204) on the following day. If some other action (r203) than travel is selected for tomorrow, you are presumed to explore alternate routes in the course of that other action, thus ending this event.

e079 Heavy Rains
Cold, driving rains hinder man and beast. You must stop moving today, and roll one die for each character in your party. If the result is 5 or 6, the character catches cold, and suffers one wound. At the start of tomorrow, roll one die. A result of 4 or higher means the rains continue, if you use any mounts they may catch pneumonia, roll once for each, they fail sick and die on a 5 or 6. You can lead animals at walking speed, including animals used to transport loads (r206) without risk. If you travel at all (r204) any characters who haven't yet caught cold must risk it. At the start of the day after tomorrow the weather will clear and the rain will stop, unless this event occurs again in the meantime.

e080 Pixies
A group of small, flying sprites called Pixies appear and dance around you and your party. Unless you have a magician, wizard, witch, elf or halfling in your party they will dance away and end the encounter. If your party includes any one of these characters, the pixies, may stop to grant you a boon, roll one die: 1-nothing of use; 2-advice see e025; 3-lead you to ancient cache see e038; 4,5-provide magic gift, see e195; 6-give you a winged pegasus mount see e188.

e081 Mounted Patrol
You encounter a mounted patrol of soldiers. Roll one die for the number in the patrol, each of which is combat skill 6, endurance 5, wealth 4. One of the men is the leader, and has wealth 10 instead. Your options are:
die roll talk *evade fight
1 inquiry r342 escape-mid r312 surprise r302
2 pass r327 escape-mtd r312 attack r305
3 bribe-pass (10) r322 escape r314 attack r305
4 bribe-pass (8) r324 hide r318 attacked r306
5 attacked r306 attacked r306 attacked r306
6 surprised r308 surprised r308 surprised r308
* if you have any winged mounts or ability to fly, you may use a flying escape r313 instead of rolling the die to resolve the evade option.

e082 Spectre
An unearthly spectre from the astral plane appears in the midst of your party, casting a hideous miasma in all directions. One character in your party is the spectre's victim (r343, magicians, wizards, witches, priests and monks must be first choices as victims). The victim is turned to smoke and taken by the spectre to the astral plane, never to be seen again, if you are the victim, you are lost, the game ends. However, a spectre is a magical being, and can be stopped using any possession that protects against magic attacks or injury.

e083 Wild Boar Charges
A huge wild boar charges toward your party. It has surprised you in combat (r220). The boar normally has combat skill 5, endurance 4, but its surprise strike is made with combat skill 8 because of its fearsome charge. Determine which character in your party is the target of this charge (r343). The boar continues selecting victims until you escape or kill it. If you kill the boar, roll two dice for the number of food units it provides (boar is quite delicious!).

e084 Bear Comes to Dinner
Ignore this event if you are in a town, castle, temple, friendly farm, in desert, or guest of any character who provides a free meal. You are about to sit down for a meal when a large, black bear wanders into your campsite! The bear will randomly attack one character (r343) after another in your party until all are killed, the bear is killed, or you escape. The bear strikes first in combat (r220), and has combat skill 5, endurance 5.

e085 Narrow Ledges
Your party is passing along narrow ledges and paths that overhang cliffs that plunge into deep gorges. Roll two dice for each character on foot in the party. If a "12" is rolled that character slips and falls to his death. Roll one die for each mount in your party without wings, a 6 means the mount stumbles and falls to its death, carrying away any rider and loads on it. If you entered the hex mounted, your entire party must be considered on mounts for this purpose. If you personally slip, or your mount falls over the edge, you are presumed to catch a ledge somewhere down the cliff and survive, but roll one die and add one (+1) for the numbers of wounds suffered in the fall. Next roll one die to see if your party finds you, a 5 or higher indicates they do, the wounds are the only effect. Any lower roll means the rest of your party does not find you, and disappears with all the mounts, possessions and wealth they were carrying.

e086 High Pass
In order to leave the hex by any direction except that which you entered, you must travel through a very high, alpine pass. On your next travel action (r204) (unless you leave by the hex you entered the hex), you must take the high pass as long as you aren't lost. When you travel the high pass, roll two dice for the effects of high winds, sub-freezing temperatures, snow, etc.
Dice once for your party:
7 (or less) no effect, travel is not hindered.
8 each character in party suffers 1 wound due to cold.
9 each character suffers 2 wounds, mounts die, no caches*.
10 each character suffers 3 wounds, mounts die, no caches*.
11 each character suffers 4 wounds, mounts die, no caches*.
12 each character suffers 4 wounds and 1 poison wound, mounts die, no caches*.
* Due to terrible conditions, if your transport ability (r206) is reduced due to loss of characters or mounts, you cannot cache spare wealth and possessions. They must be abandoned in the snows and lost entirely.

e087 Impassable Woods
You find the forest becomes thicker and thicker along this route, until further travel is impossible. You can only leave this hex by travelling to the hex from which you came (r204). In other words, any further moves must be "backwards." However, if entered from another direction this hex could be passable.

e088 Rock fall
As you travel along through a steep-sided gorge a rock fall beings, threatening your entire party. Roll one die for each character, mounts without riders are rolled for separately:
1,2,3,4 rocks miss, no effect.
5 character suffers one wound from flying rock chips; mount without a rider is caught by rolling boulder, breaks a leg, must be killed.
6 character hit by heavy rock, roll one die and add one (+1) for wounds suffered, mount without a rider is hit and killed instantly, and all its load buried beneath the rocks and also lost.

e089 Impassable Morass
You discover the swamp turns into an impassable morass of weeds, quicksand, water and muck. You can leave this hex only by moving to the hex you came from (r204). In other words, your next move must be "backwards." However, the hex might be passable if entered from another direction. Only this particular route is blocked.

e090 Quicksand
Your party stumbles into quicksand. Roll one die for each character or mount. If a character is riding a mount, you can either roll for both together as a character, or the character can sacrifice the mount and its load in order to jump from it to safety. Die roll results are:
1, 2, 3 character or mount struggles out of the quicksand without harm. 
4-character or mount escapes only if another character or mount is already free (to pull it out), otherwise it sinks and dies.
5 character struggles outward using vines and tree routes, but a mount is lost with everything it carries.
6 character or mount is trapped in deepest part, cannot win free, and automatically is lost with everything carried.

e091 Poison Snake
Your party unknowingly walks over the lair of a poison snake. One character (use r343 to select victim) suffers snakebite poison wounds, roll one die for the number of poison wounds received.

e092 Flood
Rains swell the water level of the marsh and cause flooding. You and your party are stranded on a small knoll, unable to travel further today. At the start of tomorrow, roll one die. If the result is 5 or higher, the waters subside so you can travel again (r204), otherwise you remain stranded and cannot make any travel (r204), escape (r218) or follow (r219) actions that day. Keep on rolling the die at the start of each day until travel is possible once more.

e093 Poison Plants
You notice poison plants around you today, often a sign of greater evil. You cannot hunt for food (r215) today, and roll one die for an additional event: l-e034; 2-e032; 3-e033;4-e074;5,6-no additional event.

e094 Crocodiles
Very large and very hungry crocodiles attack your party. Roll one die for the number of "crocs," each of which is combat skill 4, endurance 6. If you are in a swamp, you cannot escape from them in battle. The crocs always strike first in combat (r220), and in swamp achieve surprise as well.

e095 Mounts at Risk
The strain of travelling is exhausting your mounts. Roll one die for each mount in your party:
1, 2, 3, 4 mount still in fair condition, no special effect.
5 mount failing, unless it is allowed to rest (r203) one day, it will die after tomorrow.
6 mount in serious condition, cannot continue further, must be killed.

e096 Mounts Die
The adverse conditions finally take their toll on your mounts. All the mounts, including winged ones, must roll at the end of each day until they die or recover. One die is used:
1 mount recovering, do not roll any further for it.
2 mount recovering if it did not travel today, do not roll further; if the mount did travel today, it is still failing, roll again at the end of tomorrow.
3 mount still failing, but not dead yet, roll again at the end of tomorrow.
4, 5, 6 mount dies now.

e097 Marsh Gas and Rot
Your entire party has unwittingly travelled into an area full of flesh-rot disease and mind-destroying marsh gas. Roll one die for each character. If a 1 results the character escapes, any other result means the character dies a mindless and raving idiot while his flesh rots from his bones before his eyes. Roll for yourself first, since if you die the game ends, regardless of the fate of the rest in your party.

e098 Dragon
You encounter a huge, winged, fire-breathing Dragon with combat skill 10 and endurance 11. Roll one die, if the result is 1 or 2 you have found it at its lair, which has wealth 110 and wealth 60 both. With any other roll, it has only wealth 30. If you must fight it in combat (r220) you cannot escape. Your options are:
die roll evade fight
1 escape flying r313 surprise r302
2 escape r315 surprise r303
3 hide r318 attack r305
4 hide r320 attacked r306
5 attacked r306 surprised r308
6 surprised r308 surprised r309
Note: if you kill the Dragon, the Dragon's eye is greatly valued by high priests of the temples throughout the land, and may be of assistance in gaining an audience. Carrying the Dragon's eye counts as one load for transport purposes (r206).

e099 Roc
You encounter the Roc, a gigantic bird, which swoops down on your party. The roc is combat skill 9, endurance 8, and wealth 10. Your options are:
die roll evade fight
1 escape flying r313 surprise r301
2 escape flying r313 surprise r303
3 hide r317 attack r304
4 hide r319 attack r305
5 attack r305 attacked r306
6 surprised r308 surprised r308
Note: if you kill the Roc, you can cut off its beak and transport it as one load (r206). Count Drogat of Drogat Castle especially prizes this item, and it may help you gain an audience with him. In addition, the beak can be sold to any merchant, or in any town, castle, or temple whenever you buy food. The beak is worth 35 gold.

e100 Griffon
You meet a winged Griffon, which has combat skill 7, endurance 6, wealth 12. The Griffon is intelligent, and could serve both as a member of your party and as a winged mount for another character. However, Griffons are normally quite independent and ferocious, and this one looks especially unfriendly, if not hostile! Your
options are:
die roll talk *evade fight
1 inquiry r342 escape-fly r313 surprise r303
2 plead comrades r337 escape r315 attack r305
3 attacked r306 hide r317 attack r305
4 attacked r307 hide r318 attacked r306
5 surprised r308 pass r325 attacked r306
6 surprised i309 attacked r306 surprised r308
Note: if you kill the Griffon, you can remove its claws and carry them as an extra possession. They are especially valued by Lady Aeravir of Aeravir Castle, and may help you gain an audience with her.

e101 Harpy
You encounter a Harpy, a bird-woman with combat skill 5, endurance 4, and wealth 4. Harpies are known as dirty, nasty things, but occasionally have allied with humans for mutual gain. Your options are: 
die roll talk evade fight
1 inquiry r342 escape-fly r313 surprise r302
2 *pass r329 pass r325 attack r304
3 looter r340 pass r326 attack r305
4 looter r340 pass r327 attack r305
5 surprised r308 pass r328 attack r306
6 surprised r310 pass r329 surprised r309
If the Harpy joins your party, she has her own wings, and can travel airborne without a winged mount if desired. She also counts as travelling on a normal mount because the wings allow her to make long "airlifted" hops as well.

e102 Light Rainstorm
You must land immediately, and cannot travel further today due to low ceiling, heavy cloud cover, and bad
weather.

e103 Bad Headwinds
You cannot move faster than two hexes flying today. If this even occurs after you have travelled to the third hex today, you must land in the last hex (second hex entered) instead, and end your travel there.

e104 Good Tailwinds
You can fly one extra hex today if you wish. Normal travel rules (r204) apply when moving into this extra fourth hex.

e105 Storm Clouds Ahead
You can land immediately, in the hex you just entered, and avoid any risk. Alternately, if you continue flying today (assuming you have airborne travel remaining, if not this event means nothing), before checking for lost or a travel event, roll one die for what happens as you try to fly on: 1-e103; 2-e102; 3-e079; 4,5-no effect; 6-see e105a below.
e105a Violent Weather: your party is blown out of control by gigantic winds. Roll one die for the direction you are blown, instead of making your normal travel move: 1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW, and then roll one die again and halve the number (round fractions up) for the number of hexes your are blown. Then you crash into the final Rex, your flying mount is killed and you roll one die for wounds suffered. All other members of your party are blown off course and lost to you.

e106 Heavy Overcast
Thick, black clouds obscure your vision. You realize you are becoming lost. Roll one die for direction (1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW), and move one hex in that direction. Now roll one die for each additional character or unridden mount in your party, a 6 means that character/mount disappears into the overcast and is lost from your party. Finally, the overcast will force you and the remainder of your party to land in the new hex, no further travel today is possible.

e107 Falcon Scout
A friendly Falcon joins your party if you offer it one unit of food (r215) right now. For the rest of today you cannot get lost. Tonight, at the evening meal (r215), if you offer it a second food unit, and then roll anything other than a 6 on one die, the Falcon will remain throughout tomorrow with your part as a guide also. This can continue day after day provided you feed it a food unit at the evening meal and roll anything but a six. The falcon can only act as a guide, it has no combat skill or endurance value, any wound will kill it

e108 Hawkmen Attack
You encounter a group of hawkmen who swoop down on your party. Roll one die for the number of hawkmen, each is combat skill 7, endurance 5, wealth 7. They surprise your party in combat (r220). You cannot escape from combat, but must fight to the death.

e109 Wild Pegasus
You encounter a wild pegasus. Each character in your party is allowed one attempt to capture it, roll one die. If the result is 5 or higher the character captures the pegasus, you may add it as a winged mount to your party.

e110 Air Spirit
You encounter an air spirit, but will only recognize it if a magician, wizard, witch, priest or monk is in your party. If you can't recognize it, this event ends. If you recognize, you can attempt communication if you wish. To talk to the air spirit, roll one die. If the roll equals or exceeds your wit & wiles, communication fails, the air spirit becomes confused and blows you off course. Roll one die for the direction (1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW) and then roll one die for the number of hexes you are blown in that direction. Move your party to this new hex, and continue with your daily actions (r203). If the die roll is less than your wit & wiles, you successfully talk with the air spirit. It will help you in your journey. Roll two dice, and move up to that many hexes immediately, without risk of getting lost, and with no new travel events except for the last hex (where a normal travel event must be determined).

e111 Storm Demon
You encounter a powerful Demon of storms, which attacks your party. If you have any magicians, wizards, witches, priests, or monks in your party, each can attempt to stop the demon by rolling one die. A 6 means the demon attack is blocked, any other result means no effect on the attack. If you are unable to block the attack, your entire party is blown away to be lost or killed. You crash in an adjacent hex (roll one die to determine which one: 1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW), where your winged mount is killed, and you roll one die for the number of wounds suffered. Your wealth and possessions you carried are intact, but that of the rest of your party is lost.

e112 Meet Eagle Clan
While airborne you encounter eagles in flight, roll one die for the number of eagles. Each is combat skill 4, endurance 3, and wealth 1. Your options are listed below. If your party has a character type or mount other than humans, elves, and/or pegasus mounts, you must select the evade or fight option. Wizards, witches, magicians, priests and monks are presumed human unless specified as some other race when first encountered.
die roll evade *follow fight
1 pass r325 ambush e113 attack r304
2 pass r325 hunt e114 attacked r305
3 pass r326 hunt e114 attacked r306
4 pass r326 lair e115 attacked r306
5 conversation r341 help e116 surprised r308
6 inquiry r342 allies e117 surprised r309
*if you select follow, see r319 for procedure for a follow move today, and then consult the event listed. If you elect to follow, you must abandon all members of your party without winged mounts or ability to fly.

e113 Eagle Ambush
The eagles lead you to a craggy area, when more eagles suddenly appear, roll one die for the additional eagles who arrive. All of these make a surprise attack on your party, causing combat (r220).

e114 Eagle Hunt
Eagles are hunting, and they join your party for the hunt. This ends all travel today, and for the evening meal (r215) you can hunt regardless of hex type, and add one to your normal combat skill when doing so. You and the eagles will camp on a high crag, and do not count as landing in this hex for the day. Tomorrow the eagles leave, ending the event. You can either land in the hex (consult travel table for possible event immediately, r204 & r207) before pursuing any action you wish (r203), or you can leave the hex by travel (r204). If you leave the hex, instructions from the eagles act as if you had a guide for tomorrow only.

e115 Eagle Lair
The eagles lead you to their lair, where you meet family and make friends. Tonight you receive free food (r215) for your entire party. Do not roll for landing in the hex, the eagle lair replaces the normal landing event. Later in the game you can return to the eagle lair for free food, but only if you make airborne travel into the lair hex, and do not make a normal landing (but instead land in the lair).

e116 Eagle Help
Same as e115 (see that event), plus when you leave the lair the eagles provide one of themselves to join your party and act as a guide, combat skill 4 and endurance 3. The eagle is able to feed itself each day "on the wing," but will leave you whenever you end a day in a town, castle, or temple.

e117 Eagle Allies
The eagles lead you to their high council, and after hearing your tale, decide to support your quest for the Northlands kingdom. They give you 50 gold to help with expenses, plus a warrior band of eagles to join your party. Roll two dice for the number of eagles in the warrior band, each is combat skill 4, endurance 3. Any may act as guides if you wish. In addition, after the council tonight your entire party is feasted, your evening meal's food (r215) is entirely provided by the eagles.

e118 Giant
You encounter a 12-foot tall giant, carrying a very big club. He is combat skill 9, endurance 8, wealth 10. Your options are:
die roll talk evade fight
1 inquiry r342 escape-fly r313 surprise r301
2 plead comrades r337 escape-mid r312 surprise r302
3 looter r340 hide r316 attack r304
4 pass r328 hide r317 attack r305
5 attacked r306 hide r319 attacked r306
6 surprised r308 hide r320 attacked r306
If the giant joins your party, he is too big to be carried on any mount, so you can't use mounted travel (r204) while he is with your party. In addition, he eats double the normal amount of food (r215) each day.

e119 Flash Flood
Your party is travelling down a shallow depression, a wadi. Suddenly there is a roaring, and a wall of water rushes toward you. Rains elsewhere have caused a flash flood. Roll one die for each member of your party, 5 or 6 means the character can't scramble up the bank fast enough, and is carried away by the flood. This includes the character, any mount, and any wealth or possessions. Those carried away are permanently lost. If you are carried away in the flood, any mount of yours is killed, roll one die for the number of wounds you suffer, and you can only "rescue" one load of material from that which you were carrying (r206). All the rest is lost, and you are so far separated from your party that they give you up for dead and disappear also.

e120 Exhaustion
The burning days and freezing nights sap the strength of your party. Mounts cannot be ridden, and the load capacity of all men and mounts (r206) is halved. Each character in your party suffers one wound. No rest or healing of wounds (r222) is allowed until you leave the desert, or are in an oasis hex. Mounts recover normal abilities whenever your leave the desert and rest one day, or rest a day at an oasis.

e121 Sunstroke
The heat of the sun is unexpected. Roll one die for each character and mount in your party. A 6 means he or it collapses from sunstroke. Mounts that collapse, must be left to die. Characters that collapse must be carried if possible, even if that means other loads must be abandoned, see r206. If you suffer sunstroke, other characters in the party will carry you if possible, otherwise they leave you behind and disappear. If you suffer sunstroke and are not carried for the rest of the day, you suffer wounds equal to one die roll, and revive in time for the evening meal (r215). However, you are unable to hunt. If your party continues, carrying any sunstroke victims, there is no special effect except that sunstroke victims cannot participate in hunting. All characters recover from sunstroke at the evening meal.

e122 Raftsmen
You meet raftsmen at the side of the river, (or 1 gold piece they will transport you across, along with any
members of your party and mounts that you wish. Alternately, starting tomorrow, you can hire them for travel up or down the river. See r213 for details.

e123 Knight at the Bridge
You find a small bridge that will permit crossing the river. However, a knight in armour stands at the opposite end, challenging any who wish to cross. You can only cross if you personally engage him in combat (r220), the knight is combat skill 8, endurance 8, wealth 30. You may refuse the combat and end travel for the day, but roll one die for each character in your party, a "6" indicates he deserts due to your cowardice. If you engage in combat, roll one die at the start of each round, you strike first if the roll is 4 or more, the knight strikes first if the roll is 3 or less. If either you or the knight is knocked unconscious, the duel ends. If you are knocked unconscious crossing is prohibited, and travel ends for the day. If the knight is knocked unconscious you can either, leave him here and continue to travel, or you can halt for the day, treat his wounds, and allow him to join your party (no wages need be paid, but food r215 and lodging r21 7 must be supplied). You may give up the combat and end travel for the day after any combat round, without invoking the usual escape procedure.

e124 Raft
You cross the river using a quickly built raft. Roll one die to determine if any unfortunate incident occurs during the crossing: 1,2-nothing; 3-e094; 4-e125; 5-e126; 6-e127.

e125 Raft Overturns
The raft is caught in an eddy, hits a rock, and overturns. Everyone in your party, including mounts, swims to shore. However, all wealth and all possessions are lost.

e126 Raft caught in Current
Your raft is swept downriver, move one hex downriver (see r213 for definition of downriver). Then roll one die for each mount and the characters in your party, a "6" indicates it is lost overboard and drowns. If you fall overboard you can swim to shore, losing all your wealth, possessions and mount, while your party disappears downriver on the raft and is lost to you.

e127 Raft in Rough Water
Your raft hits white water, all food stores piled on it are lost overboard. All characters, mounts, wealth and possessions are saved. Raft continues its journey safely and you land or continue (as appropriate to your action) without further incident.

e128 Merchant
You meet a friendly merchant. You can either pass by and ignore him, ending this encounter, or you can stop to chat and barter. If you stop, roll two dice and consult the chart below:
2 Merchant has pegasus mount for sale, 50 gold.
3 Merchant mentions cave tombs in this hex, if you go to look, see e028
4 Merchant has cure-poison vials for sale, each costs 10 gold (see e181 for details of its use).
5 Merchant mentions a farm nearby in this hex, if you investigate see e009
6 Merchant has food for store, 1 gold per 2 food units, up to a maximum of eight (8) units may be purchased
7 Merchant may outwit you, roll one die, if it exceeds your wit & wiles you spend 10 gold needlessly (or all your money, if you have less)
8 Merchant has healing potions for sale, each costs 5 gold (see e180 for use)
9 Merchant has two horses for sale, 6 gold pieces each
10 Merchant has coffle of slaves for sale, see e163
11 Merchant provides some final clues about a treasure, see e147.
12 Learn unique secrets from the merchant, see e162.

e129 Merchant Caravan
You meet a merchant caravan camped for the night. You may halt for the day with them to talk and trade, or you can ignore them and end if this event. If you stop, roll two dice and consult the chart below:
2 Learn unique secrets from various caravan members, see el62
3 Learn of a monastery in this hex, if you go to look see e022.
4 Merchants have anti-poison talisman/amulet for sale for 25 gold, for details of its use sec el 87.
5 Merchants noticed farms in this hex, if you go to look sec e009.
6 Meet an independent merchant in the caravan, see e128.
7 Caravan guards become hostile, you must flee the hex, see escape r218.
8 Caravan healer has potions for sale, 6 gold each, for use see e180.
9 Caravan has up to six spare horses for sale, 7 gold pieces each.
10 Caravan has coffle of slaves for sale, see e163.
11 Talk with caravan guards give you hints to a treasure, see e147.
12 Caravan passed a nearby ruin yesterday, roll one die for which adjacent hex contains the ruins (1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW).

e130 Meet a High Lord
You meet a high and powerful lord of the land. Roll one die for identity: 1-Baron of Huldra Castle; 2-Count Drogat of Drogat Castle; 3-Lady Aeravir of Aeravir Castle; 4-High Priest of a Temple; 5,6-Town Mayor. The Lord has a bodyguard, roll two dice and add one (+1) for the number of guards, each of which is combat skill 6, endurance 6. Your options are:
die roll talk evade fight
1 pass r327 escape-mtd r312 surprise r303
2 pass r329 escape r314 attack r305
3 *arrested e060 escape r315 attacked r306
4 **audience hide r317 attacked r306
5 ***inquiry r342 hide r319 attacked r307
6 attacked r307 attacked r306 surprised r309
*If arrested, you are jailed at the Lord's residence, which is either the appropriate castle, nearest temple for the High Priest, or nearest town for Mayor. Advance time by one day, to represent time spent reaching jail (which may be by a magical means, if the distance was long).
**If you achieve an audience with Baron Huldra, roll one die: 1,2-nothing; 3,4-e150; 5-e151, 6-e152; if you gain an audience with Count Drogat see e161; if you gain an audience with Lady Aeravir see e160; if you gain an audience with the High Priest see e155; if you gain an audience with a Town Mayor see e156.
***Any inquiry results that normally allow hiring a character instead permit you to bribe the bodyguards with 10 gold for an audience. If you pay this, see **Audience notes above. If you don't, nothing happens, event ends. +If you fight and kill all the guards, the Lord must automatically grant you an **Audience (see above). However, you must still suffer any adverse results from the audience (presumably due to additional guards in the area, magic protection or powers of the Lord, etc.). Alternately, instead of an audience, you can rob the Lord, who is wealth 100. However, if you rob Baron Huldra, Count Drogat, or Lady Aeravir you can never enter the castle hex where they rule

e131 Empty Ruins
You spend the entire day fruitlessly searching the ruins, and find nothing.

e132 Organized Search
If alone, you spend the day fruitlessly searching the ruins, find nothing. If there are other characters in your party, roll one die. If the roll is less than the number of characters in your party (including yourself) the organized search helps, roll again immediate in rules section r208.

e133 Plague
After considerable searching during the day, you and your party find a variety of items worth 50 gold pieces in all, among many skeletons. Tonight, just before you start to eat (r215), a plague of mind-madness begins to affect your party, due to an ancient curse on this place. Roll one die for each character in your party, a 3 or higher means madness has destroyed the mind and the character crumples into a heap and soon dies, foaming at the mouth. All surviving members of the party immediately escape from the hex (r218) and camp elsewhere for the night (r215). Mounts are affected, so survivors can bring mounts, possessions, and wealth of the entire party with them. If you are victim of the madness yourself, your northern blood helps you to survive. You will awake the next morning, having gone without food (r216), and find all your surviving followers dead or escaped with all your wealth and possessions. You can now decide what action to take for the new day, all normal actions are allowed (r203).

e134 Unstable Ruins
In the ruins are many unstable walls and rocks, making your search very dangerous. You can either give up searching these ruins, doing nothing else today, or you can continue. If you continue, roll one die for each character in your party, if a 6 or higher results he is injured in the rubble, roll two dice for the wounds suffered. If any character survives the day unwounded, the search might yield results, see r208 and immediately roll again (which can result in this again, meaning the ruins are doubly dangerous, etc.).
Note this result applies to this ruins, each day you search this ruins all characters in your party must risk the rubble, as described in the previous paragraph.

e135 Broken Columns
Along a palisade of broken columns, you find an altar with an ancient inscription. If your party includes a
magician, wizard, witch, priest, and/or monk, the inscription can be deciphered and one die rolled for its
meaning: 1-e042; 2-e043; 3-e044; 4-e045; 5-e046; 6-e047. If none can decipher the inscription, this result is no event.

e136 Hidden Treasures
You uncover the remains of a palace treasure room, roll one die for the contents: 1-e037; 2-e038; 3-e039; 4-e044; 5-500 gold; 6-nothing.

e137 Inhabitants
You encounter things living in the ruins, roll one die: 1-e032; 2-e051; 3-e052; 4-e055; 5-e057; 6-e082.

e138 Unclean
The ruins are unclean, and have horrible, gruesome creatures populating them. Roll one die for what you encounter: 1-e032; 2-e033; 3-e034; 4-e056; 5-e082; 6-e098. If you survive this encounter, you can immediately consult r208 again to continue your search today, or you can end the searching for the day and have your evening meal (r215).

e139 Minor Treasures
You uncover a minor treasure, roll one die: 1-wealth 25; 2-wealth 60; 3-e038; 4-e039; 5-e040; 6-e140.

e140 Magic Box
You find a magic box. You can only open it if you have a magician, wizard or witch in your party. Until then, you can carry it with you, since it is relatively light. Once such a person is in your party, you can open it and examine the contents. Roll one die: 1-e141; 2-e142; 3-wealth 60; 4-wealth 110; 5-e195; 6-nothing but rubbish.

e141 Hydra's Teeth
Roll two dice for the number of Hydra's teeth inside. The magician/ wizard/witch explains that whenever you scatter these teeth on the ground, that number of undead warriors will rise and fight in your party for one combat (r220) at your command. These undead teeth-warriors are combat skill 5, endurance 4, and wealth 0. They will only last for that combat, and then disappear. However, you can scatter the teeth at any instant to use them that one time, including at the start or during any combat.

e142 Gems
The box contains a horde of gems worth wealth 200 (consult for wealth 100 twice). If you have a magician, wizard or witch in your party they also recognize one as a vision gem, see e041.

e143 Secret of the Temples
You learn the secret of all temple priests - for the Chaga drug. This is available in any town where you buy food, for 2 gold pieces a serving. If you buy a serving and offer it to a temple priest, while making a normal offering (r212), you can add one (+1) to the dice roll when determining the results of that offering. Similarly, if you give it to the high priest when seeking an audience with him (r211) you can add one (+1) to that dice roll also.

e144 Secret of the Baron Huldra
You learn that the Baron of Huldra is actually a double Bastard, and has imprisoned the true heir to the castle with a hill tribe in the Wredwrock Badlands, in hex 1611. You can attempt to rescue the heir and install him as the rightful Baron at Huldra if you wish. To do so, you must travel to hex 1611 and defeat the hill tribe. This requires that you have a magician, wizard or priest in your party (to cast a spell), that you have a magic sword (e186) or shield of light (e193) to impress the tribesmen, or a charisma talisman (e189) to walk among them, or a nerve gas bomb (e190) to kill them. Alternately, you can simply fight through the guards of the heir, making a surprise attack in combat (r220) on them, roll three dice and add one (+1) for the number of guards, each of which is combat skill 4, endurance 5. You then escape (r218) from the hex with the true heir, who is combat skill 5, endurance 7. You then travel with the heir, and if you reach Huldra Castle, your party-and the heir have two options. First, you can seek an audience with the current Baron (r211), and if you roll a "10" or higher (after any modifiers) you can reveal the true heir at the audience and depose the current Baron instantly. Alternately, you can make a sneak attack on the Baron at night, surprising in combat (r220) his traditional six bodyguards, each of which is combat skill 6, endurance 6, and then go on to attack the Baron, who is combat skill 6, endurance 8, and who strikes first in combat. If you succeed in disposing of the original Baron, the heir will take the throne and will return the favour by marching his army with you back to the Northlands, to help you regain your throne. You have won the game, due to the aid of the new Baron Huldra!
 
e145 Secret of Lady Aeravir
The Lady of Aeravir Castle is the priestess of a local temple cult that requires virginity. You discover that she is actually quite promiscuous, and can use this to advantage if you gain an audience with her. Add one (+1) when attempting to gain an audience (r211) with her, and if you gain it, you can roll twice for the results of the audience, and select whichever result you prefer most. However, the Lady dislikes blackmail, and you must escape from the hex at the end of the day when you use this secret knowledge. You can never return.

e146 The Secret of Count Drogat
You learn that Count Drogat, lord of Drogat Castle, is actually an undead creature who lives from the suffering, pain, and death of others. This explains why he so often tortures and dismembers felons in his realm, and often goes into rages that leave his lands in a reign of terror. However, he is very vulnerable to foulbane, a rare plant which only be purchased from the food merchants at Duffyd Temple (hex 2018) for 1 gold piece. Using the foulbane, when you attempt to gain an audience (r211) with Count Drogat you add one (+1) to your dice roll, and if you gain an audience you can ignore the first audience result die roll and try again if you wish. However, you must abide by the second result regardless of what it is. Finally, using the foulbane in Drogat Castle you can spend a day, instead of a normal daily action, in arranging for a special theft of the Count's personal jewels. At the end of the day you escape from the hex (r218) with wealth 110, but can never return to the castle hex (due to the Count's anger). In the process of the theft you might acquire magic items (part of the wealth 110).

e147 Clue to Treasure
You gain information about a nearby treasure. Roll one die for direction (1-N, 2-NE, 3-SE, 4-S, 5-SW, 6-NW) and roll another die for the distance (in hexes) in that direction where the treasure lies. When you reach that hex, and spend a day searching for it like a cache (r214) you can then roll two dice to see what you find: 2- e066; 3-e037; 4-e038; 5-e039; 6-e040; 7-e030; 8-wealth 110 (see r225); 9-e139; 10-e140; 11-e136; 12-e054.

e148 Seneschal Requires Bribe
You must pay a bribe to the seneschal to gain an audience with the lord. Roll one die and multiply by five (5) in a town or temple, by ten (10) in a castle, for the number of gold pieces needed in the bribe. If you pay this bribe, add ten (+10) and roll for seeking an audience (r211) once more. If you don't pay the bribe, you cannot attempt an audience with the lord in this hex for the rest of the game.

e149 Must Learn Court Manners
Your northern ways brand you as a boor. You are turned away as unpresentable. After you spend 10 gold pieces for better clothes in any town, castle, or temple you can try again for an audience. Until then, you cannot seek any further audiences in this hex. Once you have spent for better clothes, this event can still occur again, indicating that you must spend yet wore to improve your appearance!

e150 Pay Your Respects
You gain an audience with the Lord or Lady, pay your respects, tell your tales, and receive a purse of wealth 50. You cannot seek an audience with that same lord tomorrow, but after that you could try again.

e151 Find Favour 
You gain an audience and are heard favourably. Your entire party is given food (r215) and lodging (r217) free tonight. Tomorrow you are given a gift of gold, roll one die and multiply by 100 for the amount, plus an escort of cavalryman that guides you and remains with you during the day you leave the hex. The escort is so strong that you will automatically defeat and kill anything you meet in combat, without using the normal combat procedure.

e152 Noble Ally
You gain an audience and are heard with interest. The Lord decides to support your cause fully, and prepares to march his army to the Northlands with you, to help you regain your throne. You have fulfilled your quest and won the game!

e153 Master of the Household
You encounter the Master of the Household, who prevents you from receiving an audience. If you bribe him with 10 gold pieces, you can try for an audience on some future day. Otherwise, he takes a dislike to you, and you can never attempt to seek audiences in this hex again.

e154 Meet Lord's Daughter
You meet the ruler's beautiful daughter; roll one die for her attitude:
1,2 she hates you, see e060, and you cannot seek an audience again in this hex.
3 you dally with her, but she is reserved, this attempt to seek an audience ends with no result whatsoever, but you can try again another day.
4 she is reserved, you bow and pass on, roll again for seeking an audience (r211) immediately.
5 she takes a liking to you in conversation, and this seems to be of some help, roll again immediately for seeking an audience (r211) and add one (+1) to your dice roll.
6 she falls in love with you (r228), roll again immediately for seeking an audience (r211) and add four (+4) to your dice roll. After resolving that, if you leave the hex, she will leave with you. You will be accused of kidnapping, and are wanted throughout the land. It is as if you had killed someone in every town, temple and castle south of the Tragoth River. However, to help you in your quest, your new lover has acquired horses for your entire party (giving everyone mounts) and brings along her personal jewellery, worth wealth 200 (r225, consult wealth 100 twice).

e155 Audience with High Priest
You have private discussion with the high priest. Roll one die:
1 he is insulted, see e060 immediately.
2 he hears your pleas, but remains unmoved by your difficulties. Event ends, and you cannot seek another audience in this hex until next week.
3 he hears your pleas, and suggests you try offerings at the temple (r212) tomorrow or on some later day. You cannot seek another audience in this hex until you make this offering. If you have made an offering at a temple within the last three days, roll again.
4 he listens to your tale and offers to help you with your offerings at the temple tomorrow (r212). If you agree, and make the offerings tomorrow, add two (+2) to your dice roll when resolving that action. You cannot seek another audience in this hex until you make an offering in this hex.
5 he decides to provide modest support for you quest, and gives you wealth 110 (see r225). You cannot seek an audience again in this hex.
6 he decides to provide full support for your quest and ventures, he gives you 200 in gold plus wealth 110. You cannot seek an audience again here.

e156 Audience with Town Mayor
You have private discussions with the mayor. Roll one die:
1 he is insulted, see e060 immediately.
2 he hears your story, but remains stone-faced, unwilling or unable to help. However, you are free to seek audiences with him again any day.
3 he hears your story and gives you free food and lodging for tonight, as a distinguished (if dispossessed) visitor from the north. You are free to seek audiences with him again any day.
4 he hears your pleas with favour, and gives you a letter recommendation to the Lord of the nearest castle (el57). You cannot seek another audience with him until next week, at the earliest.
5 he hears your story with interest, gives you a letter of recommendation to the Lord of the nearest castle (el57) and 50 gold for expenses. You cannot seek another audience with him until you have used the letter.
6 if your party includes a monk or priest, he will support your cause for religious reasons. If not, he dismisses you, and refuses any further audiences until you have such a character in your party. If he supports your cause, he will provide a letter of recommendation to any castle or temple you request, will give you wealth 100, and his trusted assistant as a member of your party. This assistant is combat skill 4, endurance 4. You cannot seek another audience with him until you have used the letter or the assistant is killed or leaves your party (other than by you voluntarily dismissing him).

e157 Letter of Recommendation
You are given a properly signed and sealed letter that provides an introduction to the appropriate Lord (see previous section). This allows you to add two (+2) to your dice roll when seeking an audience (r211) with that lord in his hex of residence.

e158 Hostile Guards
You leave the rest of your party in an atrium, and are then confronted by two hostile guards. Each is combat skill 5, endurance 6, and wealth 7. If you pay 20 gold as a bribe they will let you pass, roll again on the appropriate seeking audience table (r211). Otherwise, they will attack you, getting the first strike in combat (r220). Regardless of whether you win or lose, the combat means you must immediately escape from this hex (r218).

e159 Must Purify Yourself
You must make an offering at a temple (r212) before you can attempt another audience in this hex. The offering must be made at any temple. This result does not prevent you from attempting audiences elsewhere before making this offering. If you do make the required offering, and then try for another audience in this hex, your devotion is noted and you can add two (+2) to the dice roll when seeking the audience (r211).

e160 Audience with Lady Aeravir
You are allowed a semi-private interview with the ruler of Aeravir Castle. Roll one die for the result:
1 she listens graciously, but has no interest in Northlands problems, you cannot seek another audience with her, and this results in nothing.
2 she listens but seems distracted, audience ends without result, but you cannot seek an audience again some other day.
3 she takes pity on you, and gives you a gift of wealth 60 to help in your quest, but decrees that you
cannot seek another audience with her.
4 she finds you favourably endowed with virtue. You and your entire party can eat (r215) and lodge (r217) at her castle for as long as you wish, whenever you wish. In addition, she provides you with a gift of wealth 110 to help you on your quest. However, you cannot seek another audience with her.
5 she has seductive charms; roll one die for the number of days that pass before you come to your senses again! After the time track is advanced, roll one die on this table again to see what the Lady thinks. Meantime, your entire party has been living in the castle, but any true love (r228) has deserted in despair, and you cannot roll for her return until after you leave this hex.
6 the Lady decides to support your cause fully. She gives you one die roll times 150 in gold, and an escort of three stalwart knights, each of which is combat skill 7, endurance 6, mounts for your entire party, and one spare pack-horse. Tonight she will hold a grand feast for you and all your party, providing food (r215) and lodging (r217) free. If any party members have wounds, her healers will cure all wounds tonight as well, even poisoned wounds.

e161 Audience with Count Drogat
You are allowed a semi-private interview with the ruler of Drogat Castle. Roll one die for the result, and add one (+1) if you have a Trollskin and give it to the Count.
1 Count's eyes glow like red coals - you are his next victim, see e061!
2 Count listens with half an ear, audience ends with no result, but you can seek another audience some other day.
3 Count is in a humorous mood, gives you flippant advice and sends you forth. You must leave Drogat Castle tomorrow, and are advised to never seek an audience with the Count again unless you carry a Letter of Recommendation.
4 Count takes an interest in your situation, and provides you with 100 gold and a treasure worth wealth 110 to further your cause.
5 if you have killed (personally) at least five men or creatures the Count takes an interest in you. Otherwise you are dismissed, and cannot seek an audience again with the Count until you have killed five. If the Count takes an interest, he will go so far as to provide 500 gold, a treasure of wealth 110, and two winged pegasus mounts. You are advised to never seek an audience with the Count again, since he is in one of his rare good moods.
6 the Count listens to your story with interest. Upon leaning the names of the northern usurpers he declares that they were the very ones who did him ill deeds many years ago. He immediately rallies his army to your cause, and uses his powerful magic to transport you, your party, him, and his army to the Northland capital to retake your throne. You immediately win.

e162 Learn Secrets
You finally accumulate enough hints and bits of unrelated information to learn of the important secrets of this region, roll one die: 1,2-e143; 3,4-e144; 5-e145; 6-e146.

e163 Slave Market
You can purchase slaves at the auction block. Porter slaves are available; roll one die to establish cost in gold per porter. These slaves need not be paid wages, and will function even if not fed (r215), but each day without food halves their carrying capacity, round fractions down. When their capacity reaches zero they die. See r206 to use porters. Slave girls are available, roll two dice and add two (+2) for the cost of each. Each slave girl functions as a Gift of Charm (e182) as long as she is fed properly (r215), and can be given as such. Slave girls who are not fed lose this ability until they are fed regularly for as many days as they missed meals. In addition, each day without food for the girl, normal starvation risks (r216) apply. Finally, for each girl you buy, roll two dice. If the result is "12" exactly you fall in love, freeing her to be your mate, see r228. Finally, on the market you find an old warrior. Only you spot his hidden qualities. Roll one die to establish the price in gold. Add two (+2) to this price if you didn't buy any porters or slave girls. If you buy him, he becomes a willing member of your party at no pay as soon as you free him. Then roll one die to determine his combat skill and one to determine his endurance. He fights with you like any other member of your party.

e164 Giant Lizard
A huge, giant lizard that shakes the earth as it walks attacks you. It is combat skill 10, endurance 12, but you strike first in combat (r220). Escape is only possible if you have mounts, those without cannot escape.

e165 Elven Town
You discover a hidden town inhabited by elves. Roll one die, subtracting one (-1) if your party includes an elf, magician, wizard, or witch, and adding one (+1) if your party includes a dwarf. If the roll exceeds your wit & wiles the elves decide you are untrustworthy, you are immediately arrested see e060. Otherwise, the elves allow you to visit their town. If you are given permission to visit the town, treat it just like a normal town marked on the map for all purposes, including selection of daily actions (r203), food (r215), and lodging (r217). Any followers hired in the town (r210) will be elves. If you return to the hex later in the game, you must roll again to see if the elves still give you permission to visit, or arrest you.

e166 Elven Fortress
You discover a hidden castle inhabited by elves. Roll one die, subtracting one (-1) if your party includes an elf, magician, wizard, or witch, and adding one (+1) if your party includes a dwarf. If the roll equals or exceeds your wit & wiles, the elves decide you are unworthy, and your entire party including yourself are arrested see e060. Otherwise, you may visit the castle. If you can visit, treat the castle like a normal castle marked on the map for all purposes, including selection of daily actions (r203), food (r215), and lodging (r217). Any followers hired in the castle (r210) will be elves. If you return to the hex later in the game, you must roll again to see if the elves still give you permission to visit, or arrest you.
