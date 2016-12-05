from hashlib import md5

inputText = "uqwqemis"

password = []

i = 0

while len(password) < 8:
    
    hexed = md5(inputText + str(i)).hexdigest()
  
    if hexed.startswith("00000"):

        val = hexed[5]

        password.append(val)

    i += 1

print password