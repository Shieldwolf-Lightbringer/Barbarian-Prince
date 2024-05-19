import os
import pygame
from math import cos, sin, pi, sqrt, radians
from random import randint, choice

plains = [(1,1),(1,2),(1,4),(1,8),(1,9),(1,10),(1,12),(1,13),(1,19),(1,20),(1,21),(1,22),(2,8),(2,9),(2,10),
          (2,11),(2,12),(2,19),(2,23),(3,5),(3,8),(3,11),(3,16),(3,18),(3,20),(3,21),(4,10),(4,12),(4,13),
          (4,15),(4,16),(4,17),(5,2),(5,7),(5,10),(5,12),(5,15),(5,17),(5,20),(5,21),(5,23),(6,1),(6,2),
          (6,4),(6,7),(6,8),(6,12),(6,13),(6,14),(6,15),(6,17),(6,20),(6,21),(6,22),(6,23),(7,1),(7,2),
          (7,4),(7,6),(7,7),(7,8),(7,14),(7,17),(7,18),(7,20),(7,22),(8,10),(8,17),(8,18),(8,19),(8,20),
          (8,21),(8,22),(8,23),(9,2),(9,5),(9,6),(9,7),(9,9),(9,10),(9,17),(9,19),(9,20),(9,21),(10,4),(10,5),
          (10,8),(10,12),(10,13),(10,14),(10,17),(11,4),(11,10),(11,15),(11,16),(11,18),(12,5),(12,13),(12,16),
          (12,17),(12,21),(13,1),(13,3),(13,5),(13,14),(13,15),(13,17),(13,18),(13,19),(13,20),(13,21),(13,22),
          (13,23),(14,2),(14,3),(14,16),(14,18),(14,20),(15,13),(15,14),(15,16),(16,2),(16,13),(16,14),(16,15),
          (16,16),(16,19),(16,20),(17,4),(17,14),(17,18),(17,20),(17,23),(18,3),(18,14),(18,19),(18,23),(19,5),
          (19,6),(19,11),(19,14),(19,15),(19,18),(19,19),(20,4),(20,14),(20,18),(20,19)] #complete

farmlands = [(2,16),(2,17),(2,22),(3,17),(3,19),(3,22),(3,23),(4,18),(4,19),(4,20),(4,22),(4,23),
             (5,19),(6,18),(6,19),(7,19),(8,16),(9,16),(10,9),(13,16),(14,14),(14,15),(15,1),(15,15),
             (16,1), (18,22),(19,21),(19,22),(19,23),(20,21),(20,22),(20,23)] #complete

forests = [(1,11),(1,16),(1,17),(1,18),(1,23),(2,2),(2,3),(2,15),(2,18),(2,20),(2,21),(3,2),(3,3),(3,9),(3,10),
           (3,14),(3,15),(4,1),(4,2),(4,8),(4,9),(4,14),(4,21),(5,1),(5,5),(5,8),(5,9),(5,13),(5,14),(5,16),(5,18),
           (5,22),(6,6),(6,10),(6,16),(7,5),(7,9),(7,11),(7,12),(7,15),(7,16),(7,21),(7,23),(8,2),(8,3),(8,5),(8,7),
           (8,8),(8,9),(8,11),(8,12),(8,13),(8,14),(8,15),(9,3),(9,8),(9,11),(9,13),(9,15),(9,18),(10,2),(10,7),
           (10,18),(11,17),(11,20),(12,1),(12,2),(12,18),(12,19),(12,20),(12,22),(13,4),(13,12),(14,4),(14,13),
           (14,17),(14,19),(15,3),(15,4),(15,17),(15,18),(15,19),(15,20),(15,21),(16,4),(16,18),(16,21),(17,16),
           (17,17),(17,22),(18,15),(18,17),(18,20),(18,21),(19,16),(19,17),(19,20),(20,15),(20,17),(20,20)] #complete

hills = [(1,5),(1,7),(2,4),(2,5),(2,7),(3,7),(4,6),(5,6),(6,5),(8,1),(8,6),(9,4),(9,12),(9,22),(9,23),
         (10,1),(10,3),(10,10),(10,11),(10,19),(10,23),(11,1),(11,2),(11,7),(11,8),(11,9),(11,12),(11,13),
         (12,3),(12,8),(12,9),(12,10),(12,15),(13,6),(13,9),(13,10),(14,5),(14,6),(14,7),(14,10),(14,11),
         (14,12),(15,11),(15,12),(16,10),(16,12),(17,1),(17,2),(17,9),(17,11),(17,13),(17,15),(17,19),
         (18,8),(18,11),(18,12),(18,13),(18,18),(19,4),(19,12),(19,13),(20,3),(20,5),(20,7),(20,9),(20,10),
         (20,13)] #complete

mountains = [(1,3),(2,1),(3,1),(3,4),(4,3),(4,4),(4,5),(5,3),(5,4),(6,3),(7,3),(8,4),(9,1),(10,6),
             (10,20),(10,21),(10,22),(11,5),(11,6),(11,11),(11,14),(11,21),(11,22),(11,23),(12,4),
             (12,6),(12,7),(12,11),(12,12),(12,14),(12,23),(13,7),(13,11),(13,13),(15,5),(15,6),
             (16,3),(16,5),(16,11),(17,3),(17,5),(17,6),(17,12),(18,1),(18,2),(18,4),(18,5),(18,6),
             (18,7),(18,9),(18,10),(19,1),(19,2),(19,3),(19,7),(19,8),(19,9),(19,10),(20,1),(20,2),
             (20,6),(20,8),(20,11),(20,12)] #complete

deserts = [(1,6),(2,6),(3,6),(4,7),(13,8),(14,8),(14,9),(15,7),(15,8),(15,9),(15,10),
           (16,6),(16,7),(16,8),(16,9),(17,7),(17,8),(17,10)] #complete

swamps = [(1,14),(1,15),(2,13),(2,14),(3,12),(3,13),(4,11),(5,11),(6,9),(6,11),(7,10),(7,13),(9,14),
          (10,15),(10,16),(11,3),(11,19),(13,2),(14,1),(14,21),(14,22),(14,23),(15,2),(15,22),(15,23),
          (16,17),(16,22),(16,23),(17,21),(18,16),(20,16)] #complete

### dict codes (hex_key):['name', spritesheet slice, food cost, room/stable cost, audience possible]
towns = {(1,1):['Ogon', (pygame.Rect(0, 240, 80, 80)), 1, 1, True],
         (1,9):['Angleae', (pygame.Rect(0, 240, 80, 80)), 1, 1, True],
         (2,16):['Galden', (pygame.Rect(0, 320, 80, 80)), 1, 1, True],
         (4,19):['Halowich', (pygame.Rect(0, 240, 80, 80)), 1, 1, True],
         (4,22):['Lower Drogat', (pygame.Rect(0, 320, 80, 80)), 1, 1, True],
         (7,19):['Brigud', (pygame.Rect(0, 320, 80, 80)), 1, 1, True],
         (9,16):['Erwyn', (pygame.Rect(0, 320, 80, 80)), 1, 1, True],
         (10,4):['Cumry', (pygame.Rect(0, 240, 80, 80)), 1, 1, True],
         (10,9):['Cawther', (pygame.Rect(0, 320, 80, 80)), 1, 1, True],
         (15,1):['Weshor', (pygame.Rect(0, 320, 80, 80)), 1, 1, True],
         (14,15):['Tulith', (pygame.Rect(0, 240, 80, 80)), 1, 1, True],
         (17,20):['Lullwyn', (pygame.Rect(0, 240, 80, 80)), 1, 1, True]}
castles = {(3,23):['Drogat Castle', (pygame.Rect(0, 400, 80, 80)), 1, 1, True],
           (12,12):['Huldra Castle', (pygame.Rect(0, 400, 80, 80)), 1, 1, True],
           (19,23):['Aeravir Castle', (pygame.Rect(0, 400, 80, 80)), 1, 1, True]}
temples = {(7,11):["Branwyn's Temple", (pygame.Rect(80, 320, 80, 80)), 1, 1, True],
           (10,21):['Sulwyth Temple', (pygame.Rect(80, 80, 80, 80)), 1, 1, True],
           (13,9):["Donat's Temple", (pygame.Rect(80, 240, 80, 80)), 1, 1, True],
           (18,5):['Temple of Zhor', (pygame.Rect(80, 0, 80, 80)), 1, 1, True],
           (20,18):['Temple of Duffyd', (pygame.Rect(80, 160, 80, 80)), 1, 1, True]}
oasis = [(2,6),(14,9),(16,7),(16,9)]
ruins = {(2,6):['The Dead Plains', (pygame.Rect(0, 80, 80, 80))],
         (9,1):["Jakor's Keep", (pygame.Rect(0, 0, 80, 80))],
         (20,9):['Ruins of Pelgar', (pygame.Rect(0, 160, 80, 80))]}
roads = {(1,9):[1,4],(2,7):[0,3],(2,8):[0,4],
        (2,16):[2],(3,17):[3,5],(3,18):[0,3],(3,19):[0,2],(4,19):[2,3,5],
        (4,20):[0,3],(4,21):[0,4],(3,22):[1,3],(3,23):[0,1,3],(4,22):[4],
        (5,20):[1,5],(6,19):[1,4],(7,19):[1,2,4],
        (8,18):[0,4],(8,17):[0,3],(8,16):[1,3],(9,16):[4],
        (8,19):[3,5],(8,20):[0,2],(9,21):[2,5],(10,21):[5],
        (12,8):[2,4],(11,9):[1,4],(10,9):[1,3],(10,10):[0,3],(10,11):[0,2],(11,12):[3,5],(11,13):[0,2],
        (12,13):[2,5],(13,14):[2,5],(14,14):[3,5],(14,15):[0,1,4],
        (13,16):[1,3],(13,17):[0,3],(13,18):[0,3],(13,19):[0,3],(13,20):[0,2],(14,20):[1,5],(15,20):[1,4],
        (16,19):[2,4],(17,20):[1,2,5],
        (18,19):[1,4],(19,19):[1,4],(20,18):[1,4],
        (18,20):[2,5],(19,21):[2,5],(20,21):[3,5],(20,22):[0,4],(19,23):[1,4],(18,23):[1,4],
        (15,15):[1,4],(16,14):[1,4],(17,14):[1,4],(18,13):[4],
        (19,12):[0],(19,11):[1,3],(20,10):[0,4],(20,9):[3],
        (18,3):[2],(19,4):[3,5],(19,5):[0,3],(19,6):[0,5],(18,5):[2],}
rivers = {(1,1):[3],(1,2):[0,1],(2,1):[3,4],(2,2):[0,1],(3,2):[2,3,4],(3,3):[0],
          (4,1):[3],(4,2):[0,1,5],(5,2):[2,3,4],(5,3):[0],(6,1):[2,3],(6,2):[0,5],
          (7,1):[3],(7,2):[0,1,5],(8,1):[2,3,4],(8,2):[0],(9,1):[3],(9,2):[0,1,5],
          (10,1):[2,3,4],(10,2):[0],(11,1):[3],(11,2):[0,1,5],(12,1):[2,3,4],(12,2):[0,2,3],
          (13,1):[2,3],(13,2):[0,2,3,5],(14,1):[0,1,2,3,5],(14,2):[0,5],(15,1):[3,4],(15,2):[0,1,5],
          (16,1):[2,3,4],(16,2):[0],(17,1):[3],(17,2):[0,1,5],(18,1):[2,3,4],(18,2):[0],
          (19,1):[3],(19,2):[0,1,5],(20,1):[3,4],(20,2):[0,1],
          (13,3):[0,5],(12,3):[0,5],(11,3):[2,3],(11,4):[0,4,5],(10,3):[2],(10,4):[1,2],
          (11,5):[4,5],(10,5):[1,2,3],(11,6):[5],(10,6):[0,5],(9,6):[2,3],(9,7):[0,5],
          (8,6):[2,3],(8,7):[0,5],(7,7):[2,3],(7,8):[0,4,5],(6,7):[2],(6,8):[1,2],
          (7,9):[3,4,5],(6,9):[1,2,3],(6,10):[0,5],(7,10):[0,1,2,5],(8,9):[4],(8,10):[4,5],
          (5,10):[2,3],(5,11):[0,5],(4,10):[2,3],(4,11):[0,4,5],(3,11):[2],(3,12):[1,2,3],
          (4,12):[5],(3,13):[0,5],(2,12):[2,3],(2,13):[0,4,5],(1,13):[2],(1,14):[1,2,3],
          (2,14):[5],(1,15):[0],
          (7,11):[1,2],(8,11):[3,4,5],(7,12):[1],(8,12):[0,1],(9,12):[3,4],(9,13):[0,1,2],
          (10,12):[4],(10,13):[4,5],(9,14):[1,2],(10,14):[4,5],(9,15):[1,2],(10,15):[4,5],
          (9,16):[1,2],(10,16):[3,4,5],(9,17):[1],(10,17):[0,1,2],(11,17):[4],(11,18):[3,4,5],
          (10,18):[1],(11,19):[0,1,2],(12,18):[2,3,4],(12,19):[0,3,4,5],(13,18):[2,3],(13,19):[0,5],
          (14,17):[2,3],(14,18):[0,5],(15,17):[3],(15,18):[0,5],
          (11,20):[1],(12,20):[0,1],(13,20):[3,4],(13,21):[0,1],(14,20):[3,4],(14,21):[0,1,2],
          (15,21):[4],(15,22):[3,4,5],(15,23):[0,1,4,5],(14,22):[1,2],(14,23):[1],(16,22):[2,3,4],
          (16,23):[0],(17,22):[3],(17,23):[0,1,5],(18,22):[3,4],(18,23):[0,1],(19,23):[4],
          (20,11):[2,3],(20,12):[0,4,5],(19,12):[2],(19,13):[1,2,3],(20,13):[5],(19,14):[0,4,5],
          (19,15):[5],(18,13):[2],(18,14):[1,2,3],(18,15):[0,4,5],(17,15):[2],(17,16):[1],}


'''for the river codes, the numbers correspond to the hex side the river runs along.
   for road codes, the numbers correspond to the hex side the road traves to.'''
compass_code = {'n' :'1',
                'ne':'2',
                'se':'3',
                's' :'4',
                'sw':'5',
                'nw':'6'}

#{hex:["terrain", "feature", "river code", "road code"]}
overland_map = {
	(1,1) : ["Plains", "Ogon", "4", None],
	(1,2) : ["Plains", None, "12", None],
	(1,3) : ["Mountains", None, None, None],
	(1,4) : ["Plains", None, None, None],
	(1,5) : ["Hills", None, None, None],
	(1,6) : ["Desert", None, None, None],
	(1,7) : ["Hills", None, None, None],
	(1,8) : ["Plains", None, None, None],
	(1,9) : ["Plains", "Angleae", None, "25"],
	(1,10) : ["Plains", None, None, None],
	(1,11) : ["Forest", None, None, None],
	(1,12) : ["Plains", None, None, None],
	(1,13) : ["Plains", None, None, None],
	(1,14) : ["Swamp", None, "234", None],
	(1,15) : ["Swamp", None, "1", None],
	(1,16) : ["Forest", None, None, None],
	(1,17) : ["Forest", None, None, None],
	(1,18) : ["Forest", None, None, None],
	(1,19) : ["Plains", None, None, None],
	(1,20) : ["Plains", None, None, None],
	(1,21) : ["Plains", None, None, None],
	(1,22) : ["Plains", None, None, None],
	(1,23) : ["Forest", None, None, None],
	(2,1) : ["Mountains", None, None, None],
	(2,2) : ["Forest", None, None, None],
	(2,3) : ["Forest", None, None, None],
	(2,4) : ["Hills", None, None, None],
	(2,5) : ["Hills", None, None, None],
	(2,6) : ["Desert", ["The Dead Plains", "Oasis"], None, "4"],
	(2,7) : ["Hills", None, None, "14"],
	(2,8) : ["Plains", None, None, "15"],
	(2,9) : ["Plains", None, None, None],
	(2,10) : ["Plains", None, None, None],
	(2,11) : ["Plains", None, None, None],
	(2,12) : ["Plains", None, "34", None],
	(2,13) : ["Swamp", None, "156", None],
	(2,14) : ["Swamp", None, "6", None],
	(2,15) : ["Forest", None, None, None],
	(2,16) : ["Farmland", "Galden", None, "3"],
	(2,17) : ["Farmland", None, None, None],
	(2,18) : ["Forest", None, None, None],
	(2,19) : ["Plains", None, None, None],
	(2,20) : ["Forest", None, None, None],
	(2,21) : ["Forest", None, None, None],
	(2,22) : ["Farmland", None, None, None],
	(2,23) : ["Plains", None, None, None],
	(3,1) : ["Mountains", None, None, None],
	(3,2) : ["Forest", None, "345", None],
	(3,3) : ["Forest", None, "1", None],
	(3,4) : ["Mountains", None, None, None],
	(3,5) : ["Plains", None, None, None],
	(3,6) : ["Desert", None, None, None],
	(3,7) : ["Hills", None, None, None],
	(3,8) : ["Plains", None, None, None],
	(3,9) : ["Forest", None, None, None],
	(3,10) : ["Forest", None, None, None],
	(3,11) : ["Plains", None, None, None],
	(3,12) : ["Swamp", None, "234", None],
	(3,13) : ["Swamp", None, "16", None],
	(3,14) : ["Forest", None, None, None],
	(3,15) : ["Forest", None, None, None],
	(3,16) : ["Plains", None, None, None],
	(3,17) : ["Farmland", None, None, "46"],
	(3,18) : ["Plains", None, None, "14"],
	(3,19) : ["Farmland", None, None, "13"],
	(3,20) : ["Plains", None, None, None],
	(3,21) : ["Plains", None, None, None],
	(3,22) : ["Farmland", None, None, "24"],
	(3,23) : ["Farmland", "Drogat Castle", None, "124"],
	(4,1) : ["Forest", None, "4", None],
	(4,2) : ["Forest", None, "126", None],
	(4,3) : ["Mountains", None, None, None],
	(4,4) : ["Mountains", None, None, None],
	(4,5) : ["Mountains", None, None, None],
	(4,6) : ["Hills", None, None, None],
	(4,7) : ["Desert", None, None, None],
	(4,8) : ["Forest", None, None, None],
	(4,9) : ["Forest", None, None, None],
	(4,10) : ["Plains", None, "34", None],
	(4,11) : ["Swamp", None, "156", None],
	(4,12) : ["Plains", None, None, None],
	(4,13) : ["Plains", None, None, None],
	(4,14) : ["Forest", None, None, None],
	(4,15) : ["Plains", None, None, None],
	(4,16) : ["Plains", None, None, None],
	(4,17) : ["Plains", None, None, None],
	(4,18) : ["Farmland", None, None, None],
	(4,19) : ["Farmland", "Halowich", None, "346"],
	(4,20) : ["Farmland", None, None, "14"],
	(4,21) : ["Forest", None, None, "15"],
	(4,22) : ["Farmland", "Lower Drogat", None, "5"],
	(4,23) : ["Farmland", None, None, None],
	(5,1) : ["Forest", None, None, None],
	(5,2) : ["Plains", None, "345", None],
	(5,3) : ["Mountains", None, "1", None],
	(5,4) : ["Mountains", None, None, None],
	(5,5) : ["Forest", None, None, None],
	(5,6) : ["Hills", None, None, None],
	(5,7) : ["Plains", None, None, None],
	(5,8) : ["Forest", None, None, None],
	(5,9) : ["Forest", None, None, None],
	(5,10) : ["Plains", None, "34", None],
	(5,11) : ["Swamp", None, "16", None],
	(5,12) : ["Plains", None, None, None],
	(5,13) : ["Forest", None, None, None],
	(5,14) : ["Forest", None, None, None],
	(5,15) : ["Plains", None, None, None],
	(5,16) : ["Forest", None, None, None],
	(5,17) : ["Plains", None, None, None],
	(5,18) : ["Forest", None, None, None],
	(5,19) : ["Farmland", None, None, None],
	(5,20) : ["Plains", None, None, "26"],
	(5,21) : ["Plains", None, None, None],
	(5,22) : ["Forest", None, None, None],
	(5,23) : ["Plains", None, None, None],
	(6,1) : ["Plains", None, "34", None],
	(6,2) : ["Plains", None, "16", None],
	(6,3) : ["Mountains", None, None, None],
	(6,4) : ["Plains", None, None, None],
	(6,5) : ["Hills", None, None, None],
	(6,6) : ["Forest", None, None, None],
	(6,7) : ["Plains", None, "3", None],
	(6,8) : ["Plains", None, "23", None],
	(6,9) : ["Swamp", None, "234", None],
	(6,10) : ["Forest", None, "16", None],
	(6,11) : ["Swamp", None, None, None],
	(6,12) : ["Plains", None, None, None],
	(6,13) : ["Plains", None, None, None],
	(6,14) : ["Plains", None, None, None],
	(6,15) : ["Plains", None, None, None],
	(6,16) : ["Forest", None, None, None],
	(6,17) : ["Plains", None, None, None],
	(6,18) : ["Farmland", None, None, None],
	(6,19) : ["Farmland", None, None, "25"],
	(6,20) : ["Plains", None, None, None],
	(6,21) : ["Plains", None, None, None],
	(6,22) : ["Plains", None, None, None],
	(6,23) : ["Plains", None, None, None],
	(7,1) : ["Plains", None, "4", None],
	(7,2) : ["Plains", None, "126", None],
	(7,3) : ["Mountains", None, None, None],
	(7,4) : ["Plains", None, None, None],
	(7,5) : ["Forest", None, None, None],
	(7,6) : ["Plains", None, None, None],
	(7,7) : ["Plains", None, "34", None],
	(7,8) : ["Plains", None, "156", None],
	(7,9) : ["Forest", None, "456", None],
	(7,10) : ["Swamp", None, "1236", None],
	(7,11) : ["Forest", "Branwyn's Temple", "23", None],
	(7,12) : ["Forest", None, "2", None],
	(7,13) : ["Swamp", None, None, None],
	(7,14) : ["Plains", None, None, None],
	(7,15) : ["Forest", None, None, None],
	(7,16) : ["Forest", None, None, None],
	(7,17) : ["Plains", None, None, None],
	(7,18) : ["Plains", None, None, None],
	(7,19) : ["Farmland", "Brigud", None, "235"],
	(7,20) : ["Plains", None, None, None],
	(7,21) : ["Forest", None, None, None],
	(7,22) : ["Plains", None, None, None],
	(7,23) : ["Forest", None, None, None],
	(8,1) : ["Hills", None, "345", None],
	(8,2) : ["Forest", None, "1", None],
	(8,3) : ["Forest", None, None, None],
	(8,4) : ["Mountains", None, None, None],
	(8,5) : ["Forest", None, None, None],
	(8,6) : ["Hills", None, "34", None],
	(8,7) : ["Forest", None, "16", None],
	(8,8) : ["Forest", None, None, None],
	(8,9) : ["Forest", None, "5", None],
	(8,10) : ["Plains", None, "56", None],
	(8,11) : ["Forest", None, "456", None],
	(8,12) : ["Forest", None, "12", None],
	(8,13) : ["Forest", None, None, None],
	(8,14) : ["Forest", None, None, None],
	(8,15) : ["Forest", None, None, None],
	(8,16) : ["Farmland", None, None, "24"],
	(8,17) : ["Plains", None, None, "14"],
	(8,18) : ["Plains", None, None, "15"],
	(8,19) : ["Plains", None, None, "46"],
	(8,20) : ["Plains", None, None, "13"],
	(8,21) : ["Plains", None, None, None],
	(8,22) : ["Plains", None, None, None],
	(8,23) : ["Plains", None, None, None],
	(9,1) : ["Mountains", "Jakor's Keep", "4", None],
	(9,2) : ["Plains", None, "126", None],
	(9,3) : ["Forest", None, None, None],
	(9,4) : ["Hills", None, None, None],
	(9,5) : ["Plains", None, None, None],
	(9,6) : ["Plains", None, "34", None],
	(9,7) : ["Plains", None, "16", None],
	(9,8) : ["Forest", None, None, None],
	(9,9) : ["Plains", None, None, None],
	(9,10) : ["Plains", None, None, None],
	(9,11) : ["Forest", None, None, None],
	(9,12) : ["Hills", None, "45", None],
	(9,13) : ["Forest", None, "123", None],
	(9,14) : ["Swamp", None, "23", None],
	(9,15) : ["Forest", None, "23", None],
	(9,16) : ["Farmland", "Erwyn", "23", "5"],
	(9,17) : ["Plains", None, "2", None],
	(9,18) : ["Forest", None, None, None],
	(9,19) : ["Plains", None, None, None],
	(9,20) : ["Plains", None, None, None],
	(9,21) : ["Plains", None, None, "36"],
	(9,22) : ["Hills", None, None, None],
	(9,23) : ["Hills", None, None, None],
	(10,1) : ["Hills", None, "345", None],
	(10,2) : ["Forest", None, "1", None],
	(10,3) : ["Hills", None, "3", None],
	(10,4) : ["Plains", "Cumry", "23", None],
	(10,5) : ["Plains", None, "234", None],
	(10,6) : ["Mountains", None, "16", None],
	(10,7) : ["Forest", None, None, None],
	(10,8) : ["Plains", None, None, None],
	(10,9) : ["Farmland", "Cawther", None, "24"],
	(10,10) : ["Hills", None, None, "14"],
	(10,11) : ["Hills", None, None, "13"],
	(10,12) : ["Plains", None, "5", None],
	(10,13) : ["Plains", None, "56", None],
	(10,14) : ["Plains", None, "56", None],
	(10,15) : ["Swamp", None, "56", None],
	(10,16) : ["Swamp", None, "456", None],
	(10,17) : ["Plains", None, "123", None],
	(10,18) : ["Forest", None, "2", None],
	(10,19) : ["Hills", None, None, None],
	(10,20) : ["Mountains", None, None, None],
	(10,21) : ["Mountains", "Sulwyth Temple", None, "6"],
	(10,22) : ["Mountains", None, None, None],
	(10,23) : ["Hills", None, None, None],
	(11,1) : ["Hills", None, "4", None],
	(11,2) : ["Hills", None, "126", None],
	(11,3) : ["Swamp", None, "34", None],
	(11,4) : ["Plains", None, "156", None],
	(11,5) : ["Mountains", None, "56", None],
	(11,6) : ["Mountains", None, "6", None],
	(11,7) : ["Hills", None, None, None],
	(11,8) : ["Hills", None, None, None],
	(11,9) : ["Hills", None, None, "25"],
	(11,10) : ["Plains", None, None, None],
	(11,11) : ["Mountains", None, None, None],
	(11,12) : ["Hills", None, None, "46"],
	(11,13) : ["Hills", None, None, "13"],
	(11,14) : ["Mountains", None, None, None],
	(11,15) : ["Plains", None, None, None],
	(11,16) : ["Plains", None, None, None],
	(11,17) : ["Forest", None, "5", None],
	(11,18) : ["Plains", None, "456", None],
	(11,19) : ["Swamp", None, "123", None],
	(11,20) : ["Forest", None, "2", None],
	(11,21) : ["Mountains", None, None, None],
	(11,22) : ["Mountains", None, None, None],
	(11,23) : ["Mountains", None, None, None],
	(12,1) : ["Forest", None, "345", None],
	(12,2) : ["Forest", None, "134", None],
	(12,3) : ["Hills", None, "16", None],
	(12,4) : ["Mountains", None, None, None],
	(12,5) : ["Plains", None, None, None],
	(12,6) : ["Mountains", None, None, None],
	(12,7) : ["Mountains", None, None, None],
	(12,8) : ["Hills", None, None, "35"],
	(12,9) : ["Hills", None, None, None],
	(12,10) : ["Hills", None, None, None],
	(12,11) : ["Mountains", None, None, None],
	(12,12) : ["Mountains", "Huldra Castle", None, None],
	(12,13) : ["Plains", None, None, "36"],
	(12,14) : ["Mountains", None, None, None],
	(12,15) : ["Hills", None, None, None],
	(12,16) : ["Plains", None, None, None],
	(12,17) : ["Plains", None, None, None],
	(12,18) : ["Forest", None, "345", None],
	(12,19) : ["Forest", None, "1456", None],
	(12,20) : ["Forest", None, "12", None],
	(12,21) : ["Plains", None, None, None],
	(12,22) : ["Forest", None, None, None],
	(12,23) : ["Mountains", None, None, None],
	(13,1) : ["Plains", None, "34", None],
	(13,2) : ["Swamp", None, "1346", None],
	(13,3) : ["Plains", None, "16", None],
	(13,4) : ["Forest", None, None, None],
	(13,5) : ["Plains", None, None, None],
	(13,6) : ["Hills", None, None, None],
	(13,7) : ["Mountains", None, None, None],
	(13,8) : ["Desert", None, None, None],
	(13,9) : ["Desert", "Donat's Temple", None, None],
	(13,10) : ["Hills", None, None, None],
	(13,11) : ["Mountains", None, None, None],
	(13,12) : ["Forest", None, None, None],
	(13,13) : ["Mountains", None, None, None],
	(13,14) : ["Plains", None, None, "36"],
	(13,15) : ["Plains", None, None, None],
	(13,16) : ["Farmland", None, None, "24"],
	(13,17) : ["Plains", None, None, "14"],
	(13,18) : ["Plains", "Bridge", "34", "14"],
	(13,19) : ["Plains", "Bridge", "16", "14"],
	(13,20) : ["Plains", None, "45", "13"],
	(13,21) : ["Plains", None, "12", None],
	(13,22) : ["Plains", None, None, None],
	(13,23) : ["Plains", None, None, None],
	(14,1) : ["Swamp", None, "12346", None],
	(14,2) : ["Plains", None, "16", None],
	(14,3) : ["Plains", None, None, None],
	(14,4) : ["Forest", None, None, None],
	(14,5) : ["Hills", None, None, None],
	(14,6) : ["Hills", None, None, None],
	(14,7) : ["Hills", None, None, None],
	(14,8) : ["Desert", None, None, None],
	(14,9) : ["Desert", "Oasis", None, None],
	(14,10) : ["Hills", None, None, None],
	(14,11) : ["Hills", None, None, None],
	(14,12) : ["Hills", None, None, None],
	(14,13) : ["Forest", None, None, None],
	(14,14) : ["Farmland", None, None, "46"],
	(14,15) : ["Farmland", "Tulith", None, "125"],
	(14,16) : ["Plains", None, None, None],
	(14,17) : ["Forest", None, "34", None],
	(14,18) : ["Plains", None, "16", None],
	(14,19) : ["Forest", None, None, None],
	(14,20) : ["Plains", None, "45", "26"],
	(14,21) : ["Swamp", None, "123", None],
	(14,22) : ["Swamp", None, "23", None],
	(14,23) : ["Swamp", None, "2", None],
	(15,1) : ["Farmland", "Weshor", "45", None],
	(15,2) : ["Swamp", None, "126", None],
	(15,3) : ["Forest", None, None, None],
	(15,4) : ["Forest", None, None, None],
	(15,5) : ["Mountains", None, None, None],
	(15,6) : ["Mountains", None, None, None],
	(15,7) : ["Desert", None, None, None],
	(15,8) : ["Desert", None, None, None],
	(15,9) : ["Desert", None, None, None],
	(15,10) : ["Desert", None, None, None],
	(15,11) : ["Hills", None, None, None],
	(15,12) : ["Hills", None, None, None],
	(15,13) : ["Plains", None, None, None],
	(15,14) : ["Plains", None, None, None],
	(15,15) : ["Farmland", None, None, "25"],
	(15,16) : ["Plains", None, None, None],
	(15,17) : ["Forest", None, "4", None],
	(15,18) : ["Forest", None, "16", None],
	(15,19) : ["Forest", None, None, None],
	(15,20) : ["Forest", None, None, "25"],
	(15,21) : ["Forest", None, "5", None],
	(15,22) : ["Swamp", None, "456", None],
	(15,23) : ["Swamp", None, "1256", None],
	(16,1) : ["Farmland", None, "345", None],
	(16,2) : ["Plains", None, "1", None],
	(16,3) : ["Mountains", None, None, None],
	(16,4) : ["Forest", None, None, None],
	(16,5) : ["Mountains", None, None, None],
	(16,6) : ["Desert", None, None, None],
	(16,7) : ["Desert", "Oasis", None, None],
	(16,8) : ["Desert", None, None, None],
	(16,9) : ["Desert", "Oasis", None, None],
	(16,10) : ["Hills", None, None, None],
	(16,11) : ["Mountains", None, None, None],
	(16,12) : ["Hills", None, None, None],
	(16,13) : ["Plains", None, None, None],
	(16,14) : ["Plains", None, None, "25"],
	(16,15) : ["Plains", None, None, None],
	(16,16) : ["Plains", None, None, None],
	(16,17) : ["Swamp", None, "6", None],
	(16,18) : ["Forest", None, None, None],
	(16,19) : ["Plains", None, None, "35"],
	(16,20) : ["Plains", None, None, None],
	(16,21) : ["Forest", None, None, None],
	(16,22) : ["Swamp", None, "345", None],
	(16,23) : ["Swamp", None, "1", None],
	(17,1) : ["Hills", None, "4", None],
	(17,2) : ["Hills", None, "126", None],
	(17,3) : ["Mountains", None, None, None],
	(17,4) : ["Plains", None, None, None],
	(17,5) : ["Mountains", None, None, None],
	(17,6) : ["Mountains", None, None, None],
	(17,7) : ["Desert", None, None, None],
	(17,8) : ["Desert", None, None, None],
	(17,9) : ["Hills", None, None, None],
	(17,10) : ["Desert", None, None, None],
	(17,11) : ["Hills", None, None, None],
	(17,12) : ["Mountains", None, None, None],
	(17,13) : ["Hills", None, None, None],
	(17,14) : ["Plains", None, None, "25"],
	(17,15) : ["Hills", None, "3", None],
	(17,16) : ["Forest", None, "2", None],
	(17,17) : ["Forest", None, None, None],
	(17,18) : ["Plains", None, None, None],
	(17,19) : ["Hills", None, None, None],
	(17,20) : ["Plains", "Lullwyn", None, "236"],
	(17,21) : ["Swamp", None, None, None],
	(17,22) : ["Forest", None, "4", None],
	(17,23) : ["Plains", None, "126", None],
	(18,1) : ["Mountains", None, "345", None],
	(18,2) : ["Mountains", None, "1", None],
	(18,3) : ["Plains", None, None, "3"],
	(18,4) : ["Mountains", None, None, "12"],
	(18,5) : ["Mountains", "Temple of Zhor", None, "3"],
	(18,6) : ["Mountains", None, None, None],
	(18,7) : ["Mountains", None, None, None],
	(18,8) : ["Hills", None, None, None],
	(18,9) : ["Mountains", None, None, None],
	(18,10) : ["Mountains", None, None, None],
	(18,11) : ["Hills", None, None, None],
	(18,12) : ["Hills", None, None, None],
	(18,13) : ["Hills", None, "3", "5"],
	(18,14) : ["Plains", None, "234", None],
	(18,15) : ["Forest", None, "156", None],
	(18,16) : ["Swamp", None, None, None],
	(18,17) : ["Forest", None, None, None],
	(18,18) : ["Hills", None, None, None],
	(18,19) : ["Plains", None, None, "25"],
	(18,20) : ["Forest", None, None, "36"],
	(18,21) : ["Forest", None, None, None],
	(18,22) : ["Farmland", None, "45", None],
	(18,23) : ["Plains", "Bridge", "12", "25"],
	(19,1) : ["Mountains", None, "4", None],
	(19,2) : ["Mountains", None, "126", None],
	(19,3) : ["Mountains", None, None, None],
	(19,4) : ["Hills", None, None, "46"],
	(19,5) : ["Plains", None, None, "14"],
	(19,6) : ["Plains", None, None, "16"],
	(19,7) : ["Mountains", None, None, None],
	(19,8) : ["Mountains", None, None, None],
	(19,9) : ["Mountains", None, None, None],
	(19,10) : ["Mountains", None, None, "34"],
	(19,11) : ["Plains", None, None, "24"],
	(19,12) : ["Hills", None, "3", "1"],
	(19,13) : ["Hills", None, "234", None],
	(19,14) : ["Plains", None, "156", None],
	(19,15) : ["Plains", None, "6", None],
	(19,16) : ["Forest", None, None, None],
	(19,17) : ["Forest", None, None, None],
	(19,18) : ["Plains", None, None, None],
	(19,19) : ["Plains", None, None, "25"],
	(19,20) : ["Forest", None, None, None],
	(19,21) : ["Farmland", None, None, "36"],
	(19,22) : ["Farmland", None, None, None],
	(19,23) : ["Farmland", "Aeravir Castle", "5", "25"],
	(20,1) : ["Mountains", None, "45", None],
	(20,2) : ["Mountains", None, "12", None],
	(20,3) : ["Hills", None, None, None],
	(20,4) : ["Plains", None, None, None],
	(20,5) : ["Hills", None, None, None],
	(20,6) : ["Mountains", None, None, None],
	(20,7) : ["Hills", None, None, None],
	(20,8) : ["Mountains", None, None, None],
	(20,9) : ["Hills", "Ruins of Pelgar", None, "4"],
	(20,10) : ["Hills", None, None, "15"],
	(20,11) : ["Mountains", None, "34", None],
	(20,12) : ["Mountains", None, "156", None],
	(20,13) : ["Hills", None, "6", None],
	(20,14) : ["Plains", None, None, None],
	(20,15) : ["Forest", None, None, None],
	(20,16) : ["Swamp", None, None, None],
	(20,17) : ["Forest", None, None, None],
	(20,18) : ["Plains", "Temple of Duffyd", None, "25"],
	(20,19) : ["Plains", None, None, None],
	(20,20) : ["Forest", None, None, None],
	(20,21) : ["Farmland", None, None, "46"],
	(20,22) : ["Farmland", None, None, "15"],
	(20,23) : ["Farmland", None, None, None],
}


class HexMap():
    def __init__(self, game):
        self.game = game

        self.ROWS = 23
        self.COLUMNS = 20
        self.HEX_RADIUS = 60  # if below 60, subsurface outside surface area
        self.HEX_SIDE_LENGTH = int(self.HEX_RADIUS * sqrt(3))
        self.MAP_WIDTH = (self.HEX_RADIUS * 3/2) * self.COLUMNS + (self.HEX_RADIUS * .55)
        self.MAP_HEIGHT = (self.HEX_RADIUS * 2) * (self.ROWS - 3) + (self.HEX_RADIUS * .70)
        self.hexagon_dict = {}
        self.color_dict = {'outline': (255, 255, 0),
                           'parchment': (220, 215, 175),
                           'plains_green' : (217, 217, 90),
                           'farmlands_brown' : (190, 171, 167),
                           'forests_green' : (56, 109, 93),
                           'hills_red' : (175, 79, 90),
                           'mountains_gray' : (208, 200, 224),
                           'deserts_yellow' : (236, 236, 198),
                           'swamps_blue' : (213, 236, 244)}
        
        self.player_icon = pygame.image.load(os.path.join(self.game.img_folder, 'player_icon_outline.png')).convert_alpha()
        self.player_rect = self.player_icon.get_rect()
        self.player_rect.center = (self.HEX_RADIUS, self.HEX_RADIUS)
        self.player_hex = choice([(1,1),(7,1),(9,1),(13,1),(15,1),(18,1)])
        '''camera and map are confined to the upper-left 3/4s of the screen'''
        self.camera = pygame.Rect((0, 0), (self.game.GAME_W * 0.75, self.game.GAME_H * 0.75)) #(self.game.GAME_W, self.game.GAME_H))

        self.map_surface = pygame.Surface((self.MAP_WIDTH, self.MAP_HEIGHT))
        self.map_surface_rect = self.map_surface.get_rect()

        self.terrain_spritesheet = pygame.image.load(os.path.join(self.game.img_folder, 'terrain_spritesheet.png')).convert_alpha()
        self.icon_spritesheet_color = pygame.image.load(os.path.join(self.game.img_folder, 'icon_spritesheet_color.png')).convert_alpha()
        self.knotwork = pygame.image.load(os.path.join(self.game.img_folder, 'knotwork.png')).convert_alpha()


        '''The camera to follow the player as they move around the game map'''
    def camera_follow(self, player_rect):
        self.player_rect.center = self.hexagon_dict[self.player_hex]

        self.camera.centerx = player_rect.centerx
        self.camera.centery = player_rect.centery

        self.camera.x = max(0, min(self.camera.x, self.MAP_WIDTH - self.camera.width))
        self.camera.y = max(0, min(self.camera.y, self.MAP_HEIGHT - self.camera.height))

        if self.camera.right > self.MAP_WIDTH:
            self.camera.x -= self.camera.right - self.MAP_WIDTH
        if self.camera.bottom > self.MAP_HEIGHT:
            self.camera.y -= self.camera.bottom - self.MAP_HEIGHT

    '''This method determines which hex the mouse is hovering over or clicking in'''
    def hex_contains(self, point, hex_center):
        adjusted_point = (point[0] + self.camera.x, point[1] + self.camera.y)
        dx = adjusted_point[0] - hex_center[0]
        dy = adjusted_point[1] - hex_center[1]
        return abs(dy) <= self.HEX_RADIUS and abs(dx) <= self.HEX_SIDE_LENGTH / 2 and self.HEX_SIDE_LENGTH * abs(dy) + self.HEX_RADIUS * abs(dx) <= self.HEX_RADIUS * self.HEX_SIDE_LENGTH

    '''This method outlines a hex to highlight it'''
    def draw_outline(self, hex_center):
        pygame.draw.polygon(self.map_surface, self.color_dict['outline'], [
            (hex_center[0] + cos(angle) * (self.HEX_RADIUS + 2), hex_center[1] + sin(angle) * (self.HEX_RADIUS + 2))
            for angle in [0, pi / 3, 2 * pi / 3, pi, 4 * pi / 3, 5 * pi / 3]
        ], 4)

    '''This method determines if a hex is adjacent to the one the player is currently in'''
    def adjacent_hex(self, player_hex):
        adjacent_hexagons = []
        if player_hex[0] % 2 == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif i == -1 and j == -1:
                        continue
                    elif i == 1 and j == -1:
                        continue
                    neighbor_hex = (player_hex[0] + i, player_hex[1] + j)
                    if neighbor_hex in self.hexagon_dict:
                        adjacent_hexagons.append(neighbor_hex)
        elif player_hex[0] % 2 == 1:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif i == -1 and j == 1:
                        continue
                    elif i == 1 and j == 1:
                        continue
                    neighbor_hex = (player_hex[0] + i, player_hex[1] + j)
                    if neighbor_hex in self.hexagon_dict:
                        adjacent_hexagons.append(neighbor_hex)
        return adjacent_hexagons
    
    '''This method draws each hexagon and then gives it a color, and image, and any icons it may have'''
    def draw_hexagon(self, surface, center, key):
        hexagon_points = []
        for i in range (6):
            angle = radians(60 * i)
            x = center[0] + self.HEX_RADIUS * cos(angle)
            y = center[1] + self.HEX_RADIUS * sin(angle)
            hexagon_points.append((x, y))

        if key in plains:
            terrain_color = self.color_dict['plains_green']
        elif key in farmlands:
            terrain_color = self.color_dict['farmlands_brown']
        elif key in forests:
            terrain_color = self.color_dict['forests_green']
        elif key in hills:
            terrain_color = self.color_dict['hills_red']
        elif key in mountains:
            terrain_color = self.color_dict['mountains_gray']
        elif key in deserts:
            terrain_color = self.color_dict['deserts_yellow']
        elif key in swamps:
            terrain_color = self.color_dict['swamps_blue']
        else:
            terrain_color = (0, 0, 0)

        pygame.draw.polygon(surface, terrain_color, hexagon_points)
        
        if key in plains:
            grass = self.get_terrain_image()
            surface.blit(grass, (center[0] - self.HEX_RADIUS * 0.95, center[1] - self.HEX_RADIUS * 0.95))
        elif key in farmlands:
            furrows = self.get_terrain_image(y=80)
            surface.blit(furrows, (center[0] - self.HEX_RADIUS * 0.95, center[1] - self.HEX_RADIUS * 0.95))
        elif key in forests:
            woods = self.get_terrain_image(y=160)
            surface.blit(woods, (center[0] - self.HEX_RADIUS * 0.95, center[1] - self.HEX_RADIUS * 0.95))
        elif key in hills:
            badlands = self.get_terrain_image(y=240)
            surface.blit(badlands, (center[0] - self.HEX_RADIUS * 0.95, center[1] - self.HEX_RADIUS * 0.95))
        elif key in mountains:
            peaks = self.get_terrain_image(y=320)
            surface.blit(peaks, (center[0] - self.HEX_RADIUS * 0.95, center[1] - self.HEX_RADIUS * 0.95))
        elif key in deserts:
            sand_dunes = self.get_terrain_image(y=400)
            surface.blit(sand_dunes, (center[0] - self.HEX_RADIUS * 0.95, center[1] - self.HEX_RADIUS * 0.95))
        elif key in swamps:
            mires = self.get_terrain_image(y=480)
            surface.blit(mires, (center[0] - self.HEX_RADIUS * 0.95, center[1] - self.HEX_RADIUS * 0.95))

        if key in rivers:
            self.draw_river_segment(surface, hexagon_points, rivers[key])

        if key in roads:
            self.draw_road_segment(surface, center, roads[key])

        if key in oasis:
            image = self.icon_spritesheet_color.subsurface(pygame.Rect(0, 480, 80, 80))
            surface.blit(image, (center[0] - self.HEX_RADIUS * 1.1, center[1] - self.HEX_RADIUS * 0.65))

        if key in castles:
            self.get_icon_image(castles, key, center, surface)
        elif key in ruins:
            self.get_icon_image(ruins, key, center, surface)
        elif key in temples:
            self.get_icon_image(temples, key, center, surface)
        elif key in towns:
            self.get_icon_image(towns, key, center, surface)

        pygame.draw.polygon(surface, "red", hexagon_points, 2)

        text = self.font.render(f'{key[0]:02d}{key[1]:02d}', True, "red")
        text_rect = text.get_rect(center=(center[0], center[1] - (self.HEX_RADIUS * .5)))
        surface.blit(text, text_rect)

    '''This method creates the grid of hexagons and offsets each column so they align properly, it also creates the dict{}'''
    def draw_hex_grid(self, surface):
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                x_offset = col * (3/2) * self.HEX_RADIUS
                y_offset = row * self.HEX_SIDE_LENGTH
                if col % 2 == 1:
                    y_offset += self.HEX_SIDE_LENGTH / 2

                #key = f'{(col + 1):02d}{(row + 1):02d}'
                key = (col + 1, row + 1)
                self.hexagon_dict[key] = (self.HEX_RADIUS + x_offset, self.HEX_RADIUS + y_offset)
                self.draw_hexagon(surface, (self.HEX_RADIUS + x_offset, self.HEX_RADIUS + y_offset), key)

    '''This method gets the terrain image from the terrain spritesheet'''
    def get_terrain_image(self, x=0, y=0, w=80, h=80):
        image = self.terrain_spritesheet.subsurface(pygame.Rect(x, y, w, h))
        image = pygame.transform.scale(image, (self.HEX_RADIUS * 1.9, self.HEX_RADIUS * 1.9))
        return image
    
    '''This method gets the icon image and text for towns, temples, ruins, and castles'''
    def get_icon_image(self, dict, key, center, surface):
        icon = self.icon_spritesheet_color.subsurface(dict[key][1])
        self.font = pygame.font.Font(None, 16)
        icon_text = self.font.render(f'{dict[key][0]}', True, "red", "black")
        icon_text_rect = icon_text.get_rect(center=(center[0], center[1] - self.HEX_RADIUS * 0.1))
        surface.blit(icon, (center[0] - self.HEX_RADIUS * 0.6, center[1] - self.HEX_RADIUS * 0.25))
        surface.blit(icon_text, icon_text_rect)

    '''This method draws all river segments along the sides of a hex'''
    def draw_river_segment(self, surface, key, directions):
        for direction in directions:
            start = key[(direction - 1) % 6]
            end = key[(direction - 2) % 6]
            pygame.draw.line(surface, "blue", start, end, 16)
            pygame.draw.circle(surface, "blue", start, 8)
            pygame.draw.circle(surface, "blue", end, 8)

    '''This method draws all road segments within a hex'''
    def draw_road_segment(self, surface, key, directions):
        for direction in directions:
            start = key
            end = self.get_hex_side_center(key, direction)
            pygame.draw.line(surface, (120, 70, 40), start, end, 16)
            pygame.draw.circle(surface, (120, 70, 40), start, 8)
            pygame.draw.circle(surface, (120, 70, 40), end, 8)
    
    '''This method creates the end points for roads at the midpoint of one of the hex sides'''
    def get_hex_side_center(self, key, direction):
        angle = radians(60 * direction)
        x = key[0] + ((self.HEX_RADIUS * 0.9) * cos(angle + radians(-90)))
        y = key[1] + ((self.HEX_RADIUS * 0.9) * sin(angle + radians(-90)))
        return int(x), int(y)
    
    def draw_map(self, surface):
        self.map_surface.fill("black")
        self.draw_hex_grid(self.map_surface)
        for hex_center in self.hexagon_dict.values():
            pygame.draw.polygon(self.map_surface, (0, 0, 0), [
				(hex_center[0] + cos(angle) * self.HEX_RADIUS, hex_center[1] + sin(angle) * self.HEX_RADIUS)
				for angle in [0, pi / 3, 2 * pi / 3, pi, 4 * pi / 3, 5 * pi / 3]
			], 1)
            if self.hex_contains(pygame.mouse.get_pos(), hex_center):
                   self.draw_outline(hex_center)
        for neighbor in self.adjacent_hex(self.player_hex):
            if neighbor in self.hexagon_dict:
                self.draw_outline(self.hexagon_dict[neighbor])

		#player = pygame.draw.rect(self.map_surface, pygame.Color("red"), self.player_rect)
        self.map_surface.blit(self.player_icon, self.player_rect)
        self.camera_follow(self.player_rect)
        surface.blit(self.map_surface, self.map_surface_rect)
        surface.blit(self.map_surface.subsurface(self.camera), (0, 0))
	
		