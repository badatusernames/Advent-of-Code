# import itertools as itertools
#
#find which range is larger
def moveCrate(puzzlelist,number,fromStack,toStack):
    #set Variables
    number = int(number)
    fromStack = int(fromStack)-1
    toStack = int(toStack)-1
    puzzlelist = puzzlelist
    temp = []

    #execute crate moves
    for x in range(0,number):
        if len(puzzlelist[fromStack]) > 0: #make sure the stack is not NULL
            crateToMove = puzzlelist[fromStack].pop() #remove crate from top of stack
            temp.insert(0,crateToMove) #insert at the beginning of stack to keep the order correct
        else:
            break

    puzzlelist[toStack].extend(temp) #extend the toStack with the temp crate configuration

    return puzzlelist

#assign variables
puzzleStart = []
puzzlelist = []
mylist = []
movelist = []

#Read puzzle state into list
#Then loop through lines and split on comma
with open('puzzle.txt','r') as p:
    puzzleStart = p.read().splitlines()
    print(puzzleStart)
    for line in puzzleStart:
        line = line.split(",")
        print(line)
        puzzlelist.append(line)
    print(puzzlelist)
    print("\n")

#Read the file and output the result into a list with no newlines
#Then Loop through lines and split on spaces
with open('input.txt','r') as f:
    mylist = f.read().splitlines()
    for line in mylist:
        line = line.split(" ")
        print(line)
        movelist.append(line)
    print(movelist)
    print("\n")

#process the list of moves one by one
for move in movelist:
    moveCrate(puzzlelist,move[1],move[3],move[5])
    print(puzzlelist)

#print the ending crate configuration
print("\n")
print("\n")
for x in puzzlelist:
    print(x)
