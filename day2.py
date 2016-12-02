def day2(fname):

	buttons_one  = [1,2,3,4,5,6,7,8,9]
	left_one     = [0,3,6]
	right_one    = [2,5,8]
	position_one = 4
	code_one     = ''

	buttons_two = buttons_one + ['A','B','C','D']
	code_two    = ''
	position_two = 4
	up_two      = [4,1,0,3,8]
	down_two    = [4,9,12,11,8]
	left_two    = [0,1,4,9,12]	
	right_two   = [0,3,8,11,12]

	for line in open(fname).readlines():
		line = line.strip()
		for char in line:
			butt = buttons_two[position_two]	
			
			if char == 'U':	
				
				if position_one > 2: position_one -= 3
				
				if position_two not in up_two:
					if butt == 3 or butt == 'D': position_two -= 2
					else: position_two -= 4

			if char == 'D':
				
				if position_one < 6: position_one += 3
				
				if position_two not in down_two:
					if butt == 1 or butt == 'B': position_two += 2
					else: position_two += 4

			if char == 'L':	
				
				if position_one not in left_one: position_one -= 1 
				
				if position_two not in left_two: position_two -= 1

			if char == 'R':				
				
				if position_one not in right_one: position_one += 1 
				
				if position_two not in right_two: position_two += 1
					

		code_one += str(buttons_one[position_one])
		code_two += str(buttons_two[position_two])
		
	print code_one 
	print code_two

day2('day2input.txt')















