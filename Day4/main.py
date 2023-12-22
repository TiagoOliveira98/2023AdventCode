file = open('data.txt', 'r')
lines = file.readlines()

output = 0
for line in lines:
    line = line.replace('\n','')
    sum = 0
    for game in [line.split(":")[1]]:
        sep = game.split("|")
        print(sep[0].split(' '))
        print(sep[1].split(' '))
        for entry in sep[0].split(' '):
            if entry != '' and entry in sep[1].split(' '):
                sum += 1
    if sum != 0:
        output += 2**(sum-1)
print(output) 
