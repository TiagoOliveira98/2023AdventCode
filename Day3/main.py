file = open('data.txt', 'r')
lines = file.readlines()

numbers = '1234567890'

# Preparing the data structure
content = [['.' for i in range(len(lines[0])+1)]]

for line in lines:
    content.append((['.']+[x for x in line]))

content[-1]=content[-1]+['\n']
content.append(['.' for i in range(len(lines[0])+1)])

# Actually searching for adjacent numbers
flag = False
sum = 0
for y in range(1,len(content)-1):
    x = 1
    number = ''
    while x < len(content[0])-1:
        if content[y][x] in numbers:
            while content[y][x] in numbers:
                if (content[y-1][x] != '.' and content[y-1][x] != '\n' and content[y-1][x] not in numbers) or (content[y+1][x] != '.' and content[y+1][x] != '\n' and content[y+1][x] not in numbers) or (content[y][x-1] != '.' and content[y][x-1] != '\n' and content[y][x-1] not in numbers) or (content[y][x+1] != '.' and content[y][x+1] != '\n' and content[y][x+1] not in numbers) or (content[y-1][x-1] != '.' and content[y-1][x-1] != '\n' and content[y-1][x-1] not in numbers) or (content[y-1][x+1] != '.' and content[y-1][x+1] != '\n' and content[y-1][x+1] not in numbers) or (content[y+1][x-1] != '.' and content[y+1][x-1] != '\n' and content[y+1][x-1] not in numbers) or (content[y+1][x+1] != '.' and content[y+1][x+1] != '\n' and content[y+1][x+1] not in numbers):
                    flag = True
                number += content[y][x]
                x+=1  
            if flag == True:
                sum += int(number)
            number = ''
            flag = False
        else:
            x += 1
print(sum)
            