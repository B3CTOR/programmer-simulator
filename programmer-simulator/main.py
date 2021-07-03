from ursina import *
from random import uniform
from shop import *
from player import Player

items = []
stop = False
automatic_bool = False

app = Ursina(fullscreen = True)

player = Player('assets/player.png')

upgrade_texture = load_texture('assets/upgrade.png')
player_texture = load_texture('assets/player.png')
player_texture_2 = load_texture('assets/player 2.png')
upgrade_texture = load_texture('assets/upgrade.png')
background_texture = load_texture('assets/background.png')
shop_background_texture = load_texture('assets/shop_background.png')
automatic_texture = load_texture('assets/automatic.png')

background = Entity(model = 'quad', position = (0,0,1), texture = background_texture, scale = (16,9))
shop_button = Button(text = 'Shop', scale = (.1,.1), color = color.rgb(250,110,100), position = (.6,.4), tooltip = Tooltip('Enter the shop'))
exit_shop_button = Button(text = 'Exit', scale = (.1,.1), color = color.rgb(250,110,100), position = (.6,.4), enabled = False, tooltip = Tooltip('Exit the shop'))
your_money = Text(text = f'Money: {player.money}', position = (.68,.41), background = True)
shop = Shop(shop_background_texture)
shop.disable()
upgrade = Item(upgrade_texture, 50, (.1,0,1), enabled = False)
upgrade_desc = Text(text = 'More money per click \n               50$', position = (.123,-.071,1), enabled = False)
automatic = Item(automatic_texture, 300, (-.1,0,1), enabled = False)
automatic_desc = Text(text = 'Automatic click \n         300$', position = (-.338,-.071,1), enabled = False)




def input(key):
	global stop
	global items

	if key == 'left mouse down' and not shop_button.hovered:

		if stop == False:
			Audio('assets/type.mp3')
			player.money += 2 * player.multiplier
			a = Text(text = f'+{2 * player.multiplier}$', position = (uniform(-.56,.56), uniform(-.34,.34)), scale = 1.4)
			a.fade_out(value=0, duration=.5)

			if player.texture == player_texture_2:
				player.texture = player_texture
			else:
				player.texture = player_texture_2

	if key == 'left mouse down' and shop_button.hovered:

		stop = True
		player.disable()
		background.disable()
		shop_button.disable()
		exit_shop_button.enable()
		shop.enable()
		upgrade.enable()
		upgrade_desc.enable()
		automatic.enable()
		automatic_desc.enable()
		camera.position = (0,0,0)
		if upgrade not in items:
			items.append(upgrade)
		if automatic not in items:
			items.append(automatic)



	if key == 'left mouse down' and exit_shop_button.hovered:
		for item in items:
			item.disable()
		shop.disable()
		player.enable()
		camera.position = (0,0,-20)
		stop = False
		exit_shop_button.disable()
		upgrade_desc.disable()
		automatic.disable()
		automatic_desc.disable()
		shop_button.enable()
		background.enable()

	for item in items:
		global automatic_bool
		if key == 'left mouse down' and item.hovered:
			if item.price <= player.money:
				if item == upgrade:	
					player.multiplier += 1
				if item == automatic:
					automatic_bool = True
				player.money -= item.price
				Audio('assets/buy.mp3')
				your_money.text = f'Money: {player.money}$'
			else:
				print_on_screen('Not enough money')
				Audio('assets/error.mp3')

def update():

	if automatic_bool:
		if stop == False:
			Audio('assets/type.mp3')
			player.money += 2 * player.multiplier
			a = Text(text = f'+{2 * player.multiplier}$', position = (uniform(-.56,.56), uniform(-.34,.34)), scale = 1.4)
			a.fade_out(value=0, duration=.5)

			if player.texture == player_texture_2:
				player.texture = player_texture
			else:
				player.texture = player_texture_2
	your_money.text = f'Money: {player.money}$'


app.run()