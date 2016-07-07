import enemies
import weapons 
class Player():
	def __init__(self):
		self.inventory=[Weapon.FiveSeven()]
		self.hp=100
		#self.location=
		self.victory= false
	def is_alive(self):
		return self.hp >0
	def print_inventory (self):
		for item in self.inventory:
			print (item, '\n')



	

