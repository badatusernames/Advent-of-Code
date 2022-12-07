#assign variables
charactersProcessed = 0
startOfPacketCharacter = 0
tempSet = []



#read the file into a string
with open('input.txt','r') as file:
    data = file.read()

print(data)

#loop through the string looking at sets of 14 characters
for x in range(0,len(data)):
    temp = data[x:x+14]
    print(temp)

    #creating a set of characters to deduplicate
    for i in temp:
        tempSet.append(i)

    print(set(tempSet))

    #check if set is equal to 14 (no deduplicates) else iterate the main loop
    if len(set(tempSet)) == 14:
        print("The packet start is: " + str(x+14))
        break
    else:
        print("Not 14 unique characters")
        temp = ""
        tempSet = []
