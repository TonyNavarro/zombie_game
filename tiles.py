import weapons 
import enemies
import actions
import world 

class MapTile:
	def __init__(self, x, y):
		self.x=x
		self.y=y

class EmptyPath(MapTile):
	def intro_text(self):
		return""" just go fowards"""

class  StartinRoom(MapTile):
	def intro_text(self):
		return 
	def modify_player(self, player):
	
class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item=item
		super().__init__(x,y)
	def add_loot(self, player):
		player.inventory.append(self.item)
	def modify_player(self, player):
		self. add_loot(player)


class EnemyRoom(MapTile):
	def __init__(self, x, yx enemy):
		if self.enemy.is_alive():
			the_player.hp=the_player.hp-print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

		
class MinibossRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.MiniBoss())
		def intro_text(self):
			if self.enemy.is_alive():
				return """A Mini Boss appeared"""
			else: 
			return""" A dead body of a MiniBoss"""

class FinalBossRoom(EnemyRoom):
	def __init__(self, x, y ):
		super().__init__(x,y, enemies.FinalBoss())
		def intro.text(self)
		if self. enemy.is_alive():
			return"""The Final Boss Appeared"""
		else:
			return"""Dead body of the Final Boss"""



				
								
		
					
										
		




		