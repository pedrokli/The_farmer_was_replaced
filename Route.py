a = 6
action = Items.Weird_Substance
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
		use_item(action)
		use_item(action2)
		if get_pos_y() < a - 1:
			move(North)
		else:
			move(East)
			
def going_down_until_end(plant_down):
	for i in range(a):
		if get_ground_type() != Grounds.Soil:
			till()
		else:
			harvest()
		plant(plant_down)
		use_item(action)
		use_item(action2)			
		if get_pos_y() > 0:
			move(South)
		else:
			move(East)
			
def full_route():
	going_up_untill_end(Entities.Carrot)
	going_down_until_end(Entities.Carrot)
	