import time
import sys
import random 

 


def delay_print(s): 
    for c in s:
        sys.stdout.write( '%s' % c ) 
        sys.stdout.flush()
        time.sleep(0.05)

def attack(weapon,enemy,player):
    enemy.hp =enemy.hp - weapon.damage
    while enemy.hp != 0:
        enemy.hp=enemy.hp - weapon.damage
        player.hp=player.hp-enemy.damage
        if enemy.hp>0:

            print("You used"+gun.name+ "against the zombie")
            print(-weapon.damage)
            print("Enemy health is")
            print("The enemy still alive!")
            print("The enemy hit you")
            print(enemy.damage)

        else:
            print("Zombie is dead")
            print(player.hp)
            break     

#///  PLAYER  \\\#

class Character():
    best_weapon=None 
    def __init__(self, hp):
        self.hp=100
        self.name= NameOfCharacter
        self.inventory=[item.FiveSeven(3)]
    def add_item(self,items):
            self.items[Weapons.Intervention(30)]=item 
    def modify_character(self, items):
            self.add_item(Character)
          
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')   
            
            


        
      
        

        

#///Enemies\\\#
class zombie():
    def __init__(self, hp, damage):
        self.hp=10
        self.damage=3

class MiniBoss():
    def __init__(self, hp, damage):
        self.hp=50
        self.damage=10
        

class FinalBoss():
    def __init__(self, hp, damage):
        self.hp=100
        self.damage=15        

def MysteryBox(): #This is a randomizer that will output a random weapon.
    weapons=["AK47","MP5","Nova","Intervention"]
    MysteryBox=random.choice(weapons)
    print(MysteryBox)
    def modify_character(self, Weapons):
            self.add_item(Character)
            inventory.add_item(Weapons(MysteryBox))

       

        

#///WEAPONS\\\#
class Weapons():
    def __init__(self, damage):
        self.name=name
        self.damag=damage



  

class FiveSeven():
    def __init__(self, damage):
        self.damage=3
        self.name = " Five Seven "

class AK47():
    def __init__(self,damage):
        self.damage=7
        self.name="AK47"

class MP5():
    def __init__(self,damage):
        self.damage=5
        self.name="MP5"
class Intervention():
    def __init__(self):
        self.damage=30
        self.name="Intervention"
class Nova():
    def __init__(self, damage):
        self.dmaage=10
        self.name="Nova"



"""delay_print("Welcome to Zombieland. Please, introduce your name ")
"""
NameOfCharacter=raw_input() 
"""
delay_print("Well,"+NameOfCaracter +", you are ready to start the game ")

delay_print("Loading... ")
time.sleep(5)#This will slow the next thing by many seconds as the brackets says 

delay_print("The instructions are simple; escape from the island. ")
time.sleep(2)

delay_print("You may find some weapons that will be really useful. ")
time.sleep(2)

delay_print("If you die, you will have to start from the beginning. ")
time.sleep(1)
delay_print("So, lets begin! ")
time.sleep(2)
delay_print("Location: Alcatraz, San Francisco ")
time.sleep(2)
delay_print("Loading...")
time.sleep(5)
delay_print("You find yourself in one of the most secured prison in the world; Alcatraz. As soon as you wake up, you feel that the environment has changed. There are candles on the corridor, and someone at the door... its a zombie!")
delay_print("He looks like one of the guards of the prison, and has a key on his neck. ")

CellKey= raw_input("Take the key? ")
if CellKey == "yes" or "Yes" or "ok":
        delay_print("*Obtained cell key* ")
        delay_print("You killed the zombie by taking his head off, and took his weapon. ")   
        delay_print("* Obtained Five Seven *")
delay_print("As soon as you leave the cell, you notice that the environment has changed... ")
time.sleep(2) 
delay_print(" The prison is in ruins, and some ways are blocked. ")
delay_print("All the cells are opened... Parts of dead bodies are found inside the cell. The lights are not working, neither any of the electric devices in the prison. ")       
delay_print("Therefore, the Gondola is not working either.You will have to activate the electricity in order to make the gondola work! ")
delay_print("Objective: Turn the power on. ")"""
delay_print("You are in the middle of the corridor, and you have two options, right, or left?")
Direction1=raw_input(" ")
gun=FiveSeven(3)
if Direction1=="right":
    delay_print("As soon as you see the end of the corridor, you turned to the left, where there is a long passage, and looks like there is someone there.")
    delay_print(" When you get close, you realize it's a zombie!")
    delay_print("*A Zombie appeared! ")
    enemy=zombie(10,3)
    gun=FiveSeven(3)
    player=Character(100)
    attack(gun,enemy,player)
else:
    print("As yoy continue walking, you notice a strange ligh coming out from one of the cells...")
    print("Its a mysstery box! Would you like to open it?")
    UseBox=raw_input("Use the box? ")
    if UseBox=="Yes" or "yes":
        print ("Yoy Obtained ")
        MysteryBox()
        
        

print("In order to move on to the next section, you need to kill the boss of the actual section. He will always be next to the stairs") 
print("The strongest enemy is in the last cell, wainting for you. Get ready for this important battle! ")   
print("*You found a miniboss*")
gun=MysteryBox
enemy=MiniBoss(50,10)
player=Character(91)
attack(gun,enemy,player)
        










   
 




