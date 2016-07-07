import time
import enemies
import weapons
import sys
print("Welcome to Zombieland. Please, introduce your name")
NameOfCaracter=raw_input("Name of the caracter?")
print("Well, "+NameOfCaracter +", are you ready to start this adventure? ")

def Attack(Enemy,weapon):
    zombie(Enemy)-FiveSeven(weapons)
    print("*You killed the zombie*")

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.05)


delay_print("Loading... ")
time.sleep(5)

delay_print("The instructions are simple; escape from the island. ")
time.sleep(2)

delay_print("You may find some weapons that will be really useful. ")
time.sleep(2)

delay_print("If you die, you will have to start from the beginning. ")
delay_print("So, lets begin! ")
time.sleep(2)
delay_print("Location: Alcatraz, San Francisco ")
time.sleep(2)
delay_print("Loading...")
time.sleep(5)
delay_print("You find yourself in one of the cells. As soon as you wake up, there is a zombie trying to enter the cell. ")
delay_print("He looks like one of the guards of the prison, and has a key on his neck. ")

    
CellKey= raw_input("Take the key? ")
if CellKey == "Yes":
        delay_print("*Obtained cell key* ")
        delay_print("You killed the zombie by taking his head off, and took his weapon. ")   
        delay_print("* Obtained Five Seven *")
delay_print("As soon as you leave the cell, you notice that everything has changed... ")
time.sleep(2) 
delay_print(" Some routes are blocked, and most of the prison is in ruins. ")
delay_print("All the cells are opened... Parts of dead bodies are found inside the cell. The lights are not working, neither any of the electric devices in the prison. ")       
delay_print("Therefore, the Gondola is not working either.You will have to activate the electricity in order to make the gondola work! ")



