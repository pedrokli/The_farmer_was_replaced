a = 8
action = Items.Fertilizer
action2 = Items.Water
plant_up = Entities.Tree
plant_down = Entities.Pumpkin
def going_up_untill_end(plant_up):
	for i in range(a):
		if get_ground_type() != Grounds.Soil:
			till()
		else:
			harvest()
		plant(plant_up)
		if get_water() < 0.4:
			
			use_item(action2)
		use_item(action)
		if get_pos_y() < a - 1:
			direction = North
		else:
			direction = East
		move(direction)
def going_down_until_end(plant_down):
	for i in range(a):
		if get_ground_type() != Grounds.Soil:
			till()
		else:
			harvest()
		plant(plant_down)

		if get_water() < 0.4:
			
			use_item(action2)	
					
		if get_pos_y() > 0:
			direction = South
		else:
			direction = East
		move(direction)
			
def full_route():
	going_up_untill_end(Entities.Carrot)
	going_down_until_end(Entities.Carrot)
	