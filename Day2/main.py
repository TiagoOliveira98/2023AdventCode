file = open('data.txt', 'r')
lines = file.readlines()

strings = ['12 red', '13 green', '13 blue']

# out = list([idx+1 if (strings[0] in line or strings[1] in line or strings[2] in line) else 0 for (idx,line) in enumerate(lines)])
# print(out)

print(list(map(lambda line: line.split(':')[1], lines)))
