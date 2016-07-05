class Item():
	def __init__(self, name, description, value):
		self.name= name
		self.description=description
		self.value=value 
	def __str__(self):
		return "{}\n====\n{}\nValue: {}\n" . format(self.name, self.description, self.value)

class Weapon(Item):

	def __init__(self, name, description, value, damage):
		self.damage= damage
	def __str__(self):
		return "{}\n====\n{}\nValue: {}\nDamage". format(self.name, self.description, self.value, self.damage)

class FiveSeven(Weapon):
	def __init__(self):
		super().__init__(name="FiveSeven", description= "A secondary weapon with a normal fire rate", value=0, damage=3)

class AK47(Weapon):
	def __init__(self):
		super().__init__(name="AK47", description="A powerful assault rifle with a slighly different fire rate", value=0, damage=6)
	
class MP5(Weapon):
	def __init__(self):
		super().__init__(name="MP5", description="A SMG with a high fire rate", value=0, damage=4)

class Intervention(Weapon):
	def __init__(self):
		super().__init__(name="Intervention", description="A powerful sniper rifle, capable of killing a zombie with one shot", value=0, damage= 15)

class Nova(Weapon):
	def __init__(self):
		super().__init__(name="Nova", description="A one-shot shotgun, with a really low fire rate", value=0, damage=10)

	

		
	
		
		

								

		
	 
		
		



