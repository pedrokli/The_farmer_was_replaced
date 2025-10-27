a = 8
action = Items.Weird_Substance
action2 = Items.Water
plant_up = Entities.Tree
plant_down = Entities.Pumpkin
def going_up_untill_end():
	for i in range(a):
		if get_entity_type() != Entities.Tree:
			plant(plant_up)
		if can_harvest():
			harvest()
			plant(plant_up)
		else:
			use_item(action2)
		if get_pos_y() < a - 1:
			move(North)
		else:
			move(East)
			
def going_down_until_end():
	for i in range(a):
		if get_entity_type() != Entities.Tree:
			plant(plant_up)
		if can_harvest():
			harvest()
			plant(plant_up)
		else:
			if get_water() < 0.5:
				use_item(action2)
		if get_pos_y() > 0:
			move(South)
		else:
			move(East)
			
def full_route():
	going_up_untill_end()
	going_down_until_end()
	