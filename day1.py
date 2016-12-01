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
direction = 'north'

for instruction in instructions:
	
	#turn
	if instruction[0] == 'R':
		if direction == 'north':direction = 'east'
		elif direction == 'east':direction = 'south'
		elif direction == 'south':direction = 'west'
		elif direction == 'west':direction = 'north'
	elif instruction[0] == 'L':
		if direction == 'north':direction = 'west'
		elif direction == 'west':direction = 'south'
		elif direction == 'south':direction = 'east'
		elif direction == 'east':direction = 'north'

	#move
	if direction   == 'east':		
		for x in xrange(int(instruction[1:])):
			location = (location[0] + 1,location[1])
			if location in locations_visited:
				locations_visited_twice.append(location)
			locations_visited.append(location)
	elif direction == 'west':
		for x in xrange(int(instruction[1:])):
			location = (location[0] - 1,location[1])
			if location in locations_visited:
				locations_visited_twice.append(location)
			locations_visited.append(location)
	elif direction == 'north':
		for x in xrange(int(instruction[1:])):
			location = (location[0] ,location[1] + 1)
			if location in locations_visited:
				locations_visited_twice.append(location)
			locations_visited.append(location)
	elif direction == 'south':
		for x in xrange(int(instruction[1:])):
			location = (location[0] ,location[1]- 1)
			if location in locations_visited:
				locations_visited_twice.append(location)
			locations_visited.append(location)

print abs(location[0]) + abs(location[1])
print abs(locations_visited_twice[0][0]) + abs(locations_visited_twice[0][1])


  

