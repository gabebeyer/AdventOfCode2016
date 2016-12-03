example = [5,10,25]

def isTriangle(triangle):

	counter = 0
	othersides = {0: [triangle[1],triangle[2]],
				  1:  [triangle[0],triangle[2]],
				  2:  [triangle[0],triangle[1]]}		
	
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
	
	return triangles

def part2():
	
	for triangle in part1():
		print triangle


part2()