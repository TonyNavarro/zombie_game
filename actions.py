import player 
import enemies 
class Action():
	def __init__(self, method,name, hotkey, **kwargs):
		self.method= method
		self.hotkey= hotkey
		self.name= name	
		self.kwargs= kwargs
	def __str__(self):
		return  "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=Player.move_north, name='Move North', hotkey='w')

class MoveSourth(Action):
	def __init__(self):
		super().__init__(method=Player.mover_south, name='Move South', hotkey='s')

class MoveEast(Action):
	def __init__(self):
		super().__init__(method=Player.move_east, name='Move East', hotkey='d')

class MoveWest(Action):
	def __init__(self):
		super().__init__(method=Player.move_west, name= 'Move West ', hotkey='a')

			
class ViewInventory(Action):
	def __init__(self):
		super().__init__(method=Player.print_inventory, name='Open Invenroty ', hotkey='i')
		

class Attack(Action):
	def __init__(self, enemy):
		super().__init__(method=player.attack, name="Attack", hotkey='j')
	

		
fight=Action(player.attack, Attack,'j')