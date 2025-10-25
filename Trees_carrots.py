def trees_carrots():
	a = 6
	action = Items.Water
	
	for i in range(a):
		if get_entity_type() != Entities.Tree:
			plant(Entities.Tree)
		else:
			if can_harvest():
				harvest()
				plant(Entities.Tree)
			else:
				use_item(action)
		if get_pos_y() < a - 1:
			move(North)
		else:
			move(East)
			

	for i in range(a):
		if get_ground_type() != Grounds.Soil:
			till()
		else:
			harvest()
		plant(Entities.Carrot)
		use_item(action)		
		if get_pos_y() > 0:
			move(South)
		else:
			move(East)