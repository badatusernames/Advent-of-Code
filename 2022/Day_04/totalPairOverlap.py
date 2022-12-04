import itertools as itertools

#splits mylist into groups of size 3 for comparison
def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

#find which range is larger
def determineLargerRange(arr1):
    largerSet = 0

    #find values between
    set1 = int(arr1[1])-int(arr1[0])
    set2 = int(arr1[3])-int(arr1[2])

    #set larger set
    if set1 >= set2:
        largerSet = 1
        return largerSet
    else:
        largerSet = 2
        return largerSet

#use larger set and see if the smaller set is in it
def determineOverlap(arr1, largerSet):
    #set ranges from input
    set1Low = int(arr1[0])
    set1High = int(arr1[1])
    set2Low = int(arr1[2])
    set2High = int(arr1[3])

    #see if the smaller set is within larger
    if largerSet == 2:
        if set2Low <= set1Low and set2High >= set1High:
            return True
        else:
            return False
    else:
        if set1Low <= set2Low and set1High >= set2High:
            return True
        else:
            return False

#assign variables
pairlist = []
assignmentlist = []
thereIsOverlap = False
overlappingSections = 0

#Read the file and output the result into a list with no newlines
with open('input.txt','r') as f:
    mylist = f.read().splitlines()
    print(mylist)
    print("\n")

#Read list and split on ","
for pair in mylist:
    pair=pair.split(",")
    pairlist.extend(pair)
print(pairlist)
print("\n")

#Read list and split on "-"
for assignment in pairlist:
    assignment=assignment.split("-")
    assignmentlist.extend(assignment)
print(assignmentlist)
#Determine if length matches expected
print(len(assignmentlist))

#Call the grouper def to split the list into groups of 3
list_of_groups = list(grouper(4, assignmentlist))
#Print length to ensure proper splitting into groups of 3
print(list_of_groups)

#loop through pairs
for pair in list_of_groups:
    largerPair = 0
    #find larger range for pair
    largerPair=determineLargerRange(pair)
    print("The larger pair is: " + str(largerPair))

    #find if there is full overlap
    thereIsOverlap = determineOverlap(pair, largerPair)
    if thereIsOverlap == True:
        overlappingSections += 1

print("There are: " + str(overlappingSections))
