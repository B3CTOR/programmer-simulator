from ursina import *
from shop import *

class Player(Entity):
	def __init__(self, texture):
		super().__init__(
			model = Quad(),
			texture = texture,
			scale = 10,
			ignore_paused = True,
			)

		self.money = 0
		self.multiplier = 1


#		setattr(Player, 'money', int(getattr(Player, 'money')) + 5 * player.multiplier)
