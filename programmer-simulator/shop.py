from ursina import *
from player import *



class Shop(Entity):

	def __init__(self, texture = '', **kwargs):
		super().__init__(
			model = 'quad',
			texture = texture,
			position = (0,0,1),
			scale = (.73,.47),
			)

class Item(Entity):
	def __init__(self, texture = '', price = 0, position = (0,0,0), **kwargs):
		super().__init__(
			model = 'cube',
			texture = texture,
			scale = (.049,.049,.00001),
			position = position,
			collider = 'box',
			ignore_paused = True
			)
		self.price = price

	def input(self, key):

		if self.hovered:
			if key == 'left mouse down':
				setattr(Player, 'money', self.price)




