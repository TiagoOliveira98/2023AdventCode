file = open('data.txt', 'r')
lines = file.readlines()

spellNumbers ={"one":1, "two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9, "1":1, "2":2, "3":3, "4":4, "5":5 ,"6":6, "7":7, "8":8, "9":9}
all = []
sum = 0

for line in lines:
    init = 0
    last = 0
    aux = []
    while last < len(line):
        for i in spellNumbers:            
            if i in line[init:last+1]:
                if i not in ["1","2","3","4","5","6","7","8","9"]:
                    init = last
                else:
                    init = last + 1 
                aux.append(spellNumbers[i])
        last += 1
    sum += aux[0]*10 + aux[-1]
    all.append(sum)
print(sum) 