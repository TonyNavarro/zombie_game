import time
import sys
print("Welcome to Zombieland. Please, introduce your name")
NameOfCaracter=raw_input("Name of the caracter?")
print("Well, "+NameOfCaracter+" would you like to start the game ?")

def Attack(zombie, damage):
    zombie -= damage
    print("*You killed the zombie*")

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.10)


Start=raw_input("Yes or not ")
if Start == "Yes":
    delay_print("Loading...")

    delay_print("The instructions are simple; To escape from the island. ")
    time.sleep(2)

    delay_print("You may find some weapons that will ne really useful. ")
    time.sleep(2)

    delay_print("If you die, you will have to start from the beginning. ")
    delay_print("So, lets begin! ")
    time.sleep(5)
    delay_print("Location: Alcatraz, San Francisco ")
    time.sleep(2)
    delay_print("Loading...")
    time.sleep(5)
    delay_print("You find yourself in one of the cells. As soon as you wake up, there is a zombie trying to enter the cell.")
    delay_print("He looks like one of the guards of the prison, and has a key on his neck")
else:
    print("restart the game") 
    
CellKey= raw_input("Take the key?")
if CellKey == "Yes":
        print("Obtained cell key")
        print("You killed the zombie by taking his head off, and took his weapon ")   
        print("* Obtained Five Seven *")

DQ1=raw_input("Go to the right or left?")

if DQ1 == "right":
    print("You found a Zombie!")
    
    Attack(Zombie, 5)
else:
    left()


