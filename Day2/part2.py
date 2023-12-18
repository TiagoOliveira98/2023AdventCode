file = open('data.txt', 'r')
lines = file.readlines()

dic = {'blue':0, 'red':0, 'green':0}

sum = 0

for idx,line in enumerate(lines):
    for play in [line.split(":")[1]]:
        x = play.split(' ')
        i = 1
        while i < len(x)-1:
            if 'red' in x[i+1]:
                if int(x[i]) > dic['red']:
                    dic['red'] = int(x[i])
            elif 'green' in x[i+1]:
                if int(x[i]) > dic['green']:
                    dic['green'] = int(x[i])
            elif 'blue' in x[i+1]:
                if int(x[i]) > dic['blue']:
                    dic['blue'] = int(x[i])
            i+=2

    result = 1
    for val in dic.values():
        result = result * val

    sum += result
    dic = {'blue':0, 'red':0, 'green':0}

print(sum)