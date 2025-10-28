import till_farm
import hay_farm
import tree_farm

while True:
	if get_time() < 10000:
		till_farm.full_route()
		
	else:
		tree_farm.full_route()	
	
	