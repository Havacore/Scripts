from itertools import izip

directions = open('advent3_input.txt', 'r').read()

current_loc = (0, 0)
locations = [current_loc]

robot_loc = (0, 0)
is_robot = False

add_er_up = lambda xs, ys: tuple(x + y for x, y in izip(xs, ys))

for direction in directions:
	if direction == "^":
		if is_robot:
			robot_loc = add_er_up(robot_loc, (0, 1))
		else:
			current_loc = add_er_up(current_loc, (0, 1))
	elif direction == ">":
		if is_robot:
			robot_loc = add_er_up(robot_loc, (1, 0))
		else:
			current_loc = add_er_up(current_loc, (1, 0))
	elif direction == "<":
		if is_robot:
			robot_loc = add_er_up(robot_loc,(-1, 0))
		else:
			current_loc = add_er_up(current_loc, (-1, 0))
	elif direction == "v":
		if is_robot:
			robot_loc = add_er_up(robot_loc, (0, -1))
		else:
			current_loc = add_er_up(current_loc, (0, -1))

	is_robot = not is_robot

	if not is_robot:
		if current_loc not in locations:
			locations.append(current_loc)
	else:
		if robot_loc not in locations:
			locations.append(robot_loc)
	

print len(locations)