import itertools

def isTriangle(triangle):
	counter = 0
	othersides = {0:[triangle[1],triangle[2]],1:[triangle[0],triangle[2]],2:[triangle[0],triangle[1]]}		
	
	for side in enumerate(triangle):
		if side[1] < sum(othersides[side[0]]):
			counter += 1
	
	return True if counter == 3 else False

def part1():
	totalTriangles = 0	
	triangles = []
	
	for line in open('day3input.txt').readlines():
		line = line.strip().split()
		line = map(int, line)
		if(isTriangle(line)):
			triangles.append(line)
			totalTriangles += 1
	
	return totalTriangles

def part2():
	totalTriangles = 0
	triangles = []
	
	with open('day3input.txt') as f:
		
		while True:
			
			clean = []#stackoverflow for 3 lines at a time 
			next_n_lines = list(itertools.islice(f, 3))			
			if not next_n_lines:break
			
			for line in next_n_lines:
				clean.append(line.strip().split())

			if isTriangle(map(int,[clean[0][0],clean[1][0],clean[2][0]])):
				totalTriangles += 1
			if isTriangle(map(int,[clean[0][1],clean[1][1],clean[2][1]])):
				totalTriangles += 1
			if isTriangle(map(int,[clean[0][2],clean[1][2],clean[2][2]])):
				totalTriangles += 1

	return totalTriangles

print part1()
print part2()