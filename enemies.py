
class Enemy:
	def __init__(self, name, hp, damage):
		self.name=name
		self.hp=hp
		self.damage=damage
	def is_alive(self):
		return self.hp >0
def zombie(Enemy):
	def __init__(self):
		super().__intit__(name="Zombie ", hp=10, damage=3)

def MiniBoss(Enemy):
	def __init__(self):
		super().__init__(name="Mini Boss ", hp=75, damage=10)
		
def FinalBoss(Enemy):
	def __init__(self):
		super().__init__(name="Final Boss ", hp=180, damage=15)
		
								


				

		