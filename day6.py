from collections import Counter


colums = [[],[],[],[],[],[],[],[]]

for line in open('day6input.txt').readlines():
	
	line = line.strip()

	count = 0

	for letter in line:

		colums[count].append(letter)

		count += 1

#---------------------------------

awnserOne = ''

for colum in colums:

				# counts items in list and retruns list of (item, #)
	decoded = Counter(colum).most_common(1)[0][0]

	awnserOne += str(decoded)

print awnserOne


#---------------------------------

awnserTwo = ''

for colum in colums:

	decoded = Counter(colum).most_common()[-1][0]

	awnserTwo += str(decoded)

print awnserTwo

	


