import random
import os
import time
import pyfiglet
valid_choices = ["left", "right", "straight", "back"]
valid_YorN = ["yes", "no"]
class clearScreen():
    def clearTheScreen():
        try:
            os.system('cls||clear')
        except:
            pass
player_inventory = [0, 3, 2, 1]
small_potions = player_inventory[1]
medium_potions = player_inventory[2]
large_potions = player_inventory[3]
player_name = input("The Dungeon awaits Adventurer, What is your name? ? ?")
if player_name == "Fleur":
    print("I've heard this name before...")
if player_name == "Bitch":
    print("I cannot believe that is your real name...")
if player_name == "Hana":
    print("I've heard about you, Hana...")
print("{name}, The name of a true hero...".format(name = player_name))

class Character:
    def __init__(self, health, mana, defense, attack, level, experience, gold, weapon):
        self.health = 100
        self.mana = 100
        self.defense = 3
        self.attack = level * 2
        self.level = 1
        self.experience = experience
        self.gold = gold
        self.weapon = Sword
    def Die(self):
        if health != 0:
            self.health = 0
        print("Your adventure ends here, Better luck next time. . .")
    def __repr__(self):
        print("These are in your inventory")
        for weapon in weapons:
            print(weapons)
        return ("Your currently holding {weapon}".format(weapon = self.weapons[self.current_weapon].name))
    def switch_weapon(self, new_weapon):
        if new_weapon < len(self.weapons) and new_weapon >= 0:
            print("hi")
        elif new_weapon == current_weapon:
            print("Youre already holding that. . .")
        else:
            player_current_weapon.append(new_weapon)
            print("new weapon equipped!")
            
class Ranger(Character):
    def __init__(self, health = 150, defense = 2.5, mana = 30, weapon = "Bow"):
        super().__init__(attack = attack,
                         level = level,
                         experience = experience,
                         gold = gold)
    INITIAL_MANA = 30
    INITIAL_HEALTH = 150
    stat_up_points = 0 
    in_the_battle = False
    player_class = "RANGER"
    
class Mage(Character):
    def __init__ (self, health = 125, defense = 2.5, weapon = "Staff"):
        super().__init__(mana = mana,
                         attack = attack,
                         defense = defense,
                         level = level,
                         experience = experience,
                         gold = gold)
    INITIAL_MANA = 100
    INITIAL_HEALTH = 120
    statUpPoints  = 0 
    inTheBattle = False
    playerClass = "MAGE"
    
class Knight(Character):
    def __init__ (self, health = 175, defense = 4, mana = 15, weapon = "Sword"):
        super().__init__(level = level,
                         experience = experience,
                         gold = gold,
                         attack = attack)
    INITITAL_MANA = 50
    INITITAL_HEALTH = 175
    statUpPoints  = 0 
    inTheBattle = False
    playerClass = "KNIGHT"

rangerinfo = [150, 3, 50]
mageinfo = [125, 2, 100]
knightinfo = [175, 4, 25]
while True:
    print("\n1: Ranger - Health:",rangerinfo[0],"Defense:",rangerinfo[1],"Mana:",rangerinfo[2])
    print("2: Mage - Health:",mageinfo[0],"Defense:",mageinfo[1],"Mana:",mageinfo[2])
    print("3: Knight - Health:",knightinfo[0],"Defense:",knightinfo[1],"Mana:",knightinfo[2])
    player_class = input("Select your Class... 1, 2, or 3? ")
    if player_class == "1":
        print("A nimble Ranger, a perfect balance of stealth and power.")
        break
    if player_class == "2":
        print("Seeking power through knowledge I see?")
        break
    if player_class == "3":
        print("A noble Knight, Seeking a grand adventure perhaps?")
        break
    if player_class == "Fleur":
        print("Ahh, The Jackalope? I've heard rumors of their art...")
    if player_class == "Bitch":
        print("Well I never...")
    if player_class == "Hana":
        print("Holy shit, its Hana")
    else:
        print("Please select a valid Class...")
        continue
    
boss = ["Narfi, The Betrayer King", "Tormod, The Desecrator", "Muxus, Goblin Grandee"] 
randombosses = random.choice(boss)    
player_heal_max = player_class[0]        
print("You step to the entrance of the Dungeon, looking down to your hand you re-read the notice the guard handed you..")
print("\nW A N T E D") 
print(randombosses)
print("B O U N T Y")
print(random.randint(0,10000))

ascii_banner = pyfiglet.figlet_format("The Adventure Begins")
print(ascii_banner)

def prompt_for_input(prompt: valid_choices):
  while True:
    choice = input(prompt)
    if choice in valid_choices:
      return choice
    print("not a valid choice...try again!")

def prompt_for_YorN(prompt: valid_YorN):
  while True:
    choice = input(prompt)
    if choice in valid_YorN:
      return choice
    print("not a valid choice...try again!")
    
def Roll_D20():
    print(random.randint(1,20))
    return

print("You reassure yourself and press on.")
choice = prompt_for_input("The inside of the Crypt is cold and dark, three paths lay ahead of you... Which Direction will you go?? straight, Back, Left or Right?")
if choice == "straight":
    print("You walk straight ahead. The faint light from the torches is barely enough for you to see.. On your left side you see a torch that looks like it can be removed from its cage")
    choice = prompt_for_YorN("attempt to remove?")
    if choice == "yes":
        print("You reach towards the torch and give it a slight tug, it requires a little more strength than you originally thought..")
    choice = prompt_for_YorN("Try harder?")
    if choice == "yes":
        print("You grab the torch and forcibly remove it from its cage. you feel accomplished until the cage falls to the ground making a BANG. You hear a loud screech coming from the other end of the hallway youre in.")
        print("You hear shuttling in the darkness infront of you, the noise sound familiar....Bones??!")
    if choice == "no":
        print("You choose to continue your journey in the dark. Fear slowly creeps over you as you continue down the hallway")


if choice == "back":
    print("You decide. In this moment. That you would like to live, So you crumble up the notice and walk away")
    print ("""\
    L*L L L L*L L*L L
    L L*L L*L L*L L*L
    L*L L*L L*L L*L L
    L L*L L*L L*L L*L
    L*L L*L L*L L*L L
    L L*L L*L L*L L*L
    L*L L*L L*L L*L L
    L L*L L*L L*L L*L
    L*L L*L L*L L*L L
    L L*L L*L L*L L*L
    L*L L*L L*L L*L L
    L L*L L*L L*L L*L
    L*L L*L L*L L*L L
    L L*L L*L L*L L*L
    L*L L*L L*L L*L L*L L*L L*L L*L L*L L*L L
    L L*L L*L L*L L*L L*L L*L L*L L*L L*L L*L
    L*L L*L L*L L*L L*L L*L L*L L*L L*L L*L L
    L L*L L*L L*L L*L L*L L*L L*L L*L L*L L*L
    L*L L*L L*L L*L L*L L*L L*L L*L L*L L*L L
    L L*L L*L L*L L*L L*L L*L L*L L*L L*L L*L
                                                """)
    

if choice == "left":
    print("You glance left, then right, then decide to go Left. Along the cobblestone walls you see cracks and dust, the faint smell of old fabric starts to hit your nose, but you continue forth. on the leftside wall you see one door slightly ajar,")
    choice = prompt_for_YorN("Will you open the door?")
    if choice == "yes":
        print("Curiosity gets the better of you as you slowly open the door, you see a room in complete disarray, the bed is completely broken, all painting are ripped to shreds. Some floor boards are cracked or even broken in half")
    choice = prompt_for_YorN("Continue to Explore?")
    if choice == "no":
        print("You ignore the room for now, continuing down the hallway you reach the end, to your left is a big pile of debris, obviously from a cave-in of some sort..")
        choice = prompt_for_input("Which Direction will you go? STRAIGHT up the hallway you just enetered... Or BACK the way you came? ")
        if choice == "straight":
            print("You head through the long hallway, paying close attention to noises you hear in the various cracks in the walls and floors below.the light seems to fade the further down the hallway you venture.")
        if choice == "back":
            print("You choose to head back the way you came and regroup.")
    if choice == "yes":
        print("You begin to rummage through the drawers that are still left unscatched. you find 50 Gold!!")
        print("You now have {gold} gold!".format(gold = 50).append(player_inventory))
    if choice == "no":
        print("You ignore the room and continue moving foward")






if choice == "right":
    print("Without question you head to the right, heading down the hallway you hear the faint creaking of the chandeliers that hang above. You find yourself at the end of a hallway, to your left, a long hallway where only a faint light can be seen at the end. on your right, a shorter hallway with a cracked wooden door at the end.")    
    choice = prompt_for_input("Which Direction?? left, right, or back")
    if choice == "left":
        print("You decide to go left, as you go steadily down the hallway, you hear faint clinking, almost like bottles tapping together. You can see the light coming through a broken hole in the wall, as you approach your foot snags on a tripwire!!")
        print("Roll to see if you can stop the trap in time")
        choice = input("press ENTER to roll")
        D20 = Roll_D20()
        
        if Roll_D20 != 13:
            print("You react quickly, grabbing the rope before it dropped the rocks")
        else:
            print("The trap triggers and a bucket of rocks falls from above, alerting the enemy mage who gets the first blow.")
        
        choice = prompt_for_YorN("Continue foward??")
        if choice == "yes":
            print("You press foward unscatched at the dangers ahead, you see the outline of a body starting to stand up in the distance. As you walk a little foward you see its an Undead!")
    if choice == 'right':
        print("You decide to head to the right, Dark hallways aren't your thing anyway. Approaching the door you hear rattling, it almost sounds like..Bones?")
        choice = prompt_for_YorN("Open the door??")
    if choice == 'back':
        print("You decide to retrace your steps and head back the way you came to re-group")
    



