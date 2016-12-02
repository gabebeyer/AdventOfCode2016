instructions = '''R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, 
R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, 
L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, 
R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, 
R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, 
R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, 
L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, 
R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1'''

instructions = instructions.replace(",", "").split()
location = (0,0)
locations_visited = []
locations_visited_twice = []
direction = 0

for instruction in instructions:
	print direction

	#turn
	if instruction[0] == 'R':

		direction += 1

		if direction == 3:
			direction = 0


	
	elif instruction[0] == 'L':
		if direction == 0:
			direction = 3
		direction -= 1

	

	#move
	if direction  ==  0:		
		for x in xrange(int(instruction[1:])):
			location = (location[0],location[1]+1)
			if location in locations_visited:
				locations_visited_twice.append(location)
			locations_visited.append(location)

	if direction  ==  1:		
		for x in xrange(int(instruction[1:])):
			location = (location[0]+1,location[1])
			if location in locations_visited:
				locations_visited_twice.append(location)
			locations_visited.append(location)	

	if direction  ==  2:		
		for x in xrange(int(instruction[1:])):
			location = (location[0],location[1]-1)
			if location in locations_visited:
				locations_visited_twice.append(location)
			locations_visited.append(location)

	if direction  ==  4:		
		for x in xrange(int(instruction[1:])):
			location = (location[0]-1,location[1])
			if location in locations_visited:
				locations_visited_twice.append(location)
			locations_visited.append(location)			























print abs(location[0]) + abs(location[1])

print abs(locations_visited_twice[0][0]) + abs(locations_visited_twice[0][1])


  

