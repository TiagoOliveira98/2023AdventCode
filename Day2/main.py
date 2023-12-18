file = open('data.txt', 'r')
lines = file.readlines()

sum = 0

for idx,line in enumerate(lines):
    for play in [line.split(":")[1]]:
        flag = True
        x = play.split(' ')
        i = 1
        while i < len(x)-1 and flag:
            if ('red' in x[i+1] and int(x[i]) > 12) or ('green' in x[i+1] and int(x[i]) > 13) or ('blue' in x[i+1] and int(x[i]) > 14):
                flag = False
            i+=2
        if flag== False:
            sum -= (idx+1)
            break
    sum += (idx+1)

print(sum)
