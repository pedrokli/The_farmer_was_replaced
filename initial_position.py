while True:	
	if get_pos_x() != 0 and get_pos_y() == 0:
		move(West)
	if get_pos_x() == 0 and get_pos_y() != 0:
		move(South)
	if get_pos_x() != 0 and get_pos_y() != 0:
		move(South)	
	elif get_pos_x() == 0 and get_pos_y() == 0:
		break