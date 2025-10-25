a = 6
action = Items.Fertilizer
plant_up = Entities.Bush
plant_down = Entities.Bush
def going_up_untill_end():
	for i in range(a):
		if get_entity_type() != plant_up:
			plant(plant_up)
		else:
			if can_harvest():
				harvest()
				plant(plant_up)
			else:
				use_item(action)
		if get_pos_y() < a - 1:
			move(North)
		else:
			move(East)
			
def going_down_until_end():
	for i in range(a):
		if get_ground_type() != Grounds.Soil:
			till()
		else:
			harvest()
		plant(plant_down)
		use_item(action)		
		if get_pos_y() > 0:
			move(South)
		else:
			move(East)