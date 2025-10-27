import till_farm
import hay_farm
import tree_farm

while True:
	if get_time() < 3500:
		hay_farm.full_route()
	else:
		till_farm()	
	
	