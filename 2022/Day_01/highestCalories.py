calorieTotal = 0
allElfs=[]
topThreeElfs = 0

with open('input.txt','r') as f:
    for line in f:
        if line == "\n":
            #print(calorieTotal)
            allElfs.append(calorieTotal)
            calorieTotal = 0
        else:
            calorieTotal = calorieTotal + int(line)

print(allElfs.sort())
print('Max value is: ' + str(max(allElfs)))
print(len(allElfs))
