#variable assignments
firstpart = ''
secondpart = ''
matchedItems = []
backpacksProcessed = 0
totalPriority = 0

#opens input file and reads each line
with open('input.txt','r') as f:
    for line in f:
        #splits each line into equal length strings
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]

        #Compare the characters in firstpart with each character in secondpart to find matches
        for element in firstpart:
            for element2 in secondpart:
                #print(element2)
                if element2 == element:
                    matchedItems += element2

        backpacksProcessed += 1
        print("Backpack " + str(backpacksProcessed) + " has completed processing.")
        #remove duplicate values from matchedItems
        matchedItems=list(set(matchedItems))
        print(matchedItems)

        #Convert the matchedItems into Unicode int and offset to match challenge priority values
        for match in matchedItems:
            value=ord(match)
            if value >= 97:
                value -= 96
            else:
                value -= 38
            #print(value)
            totalPriority = totalPriority + value

        matchedItems = []


print("The total Priority of the items is: " + str(totalPriority))
