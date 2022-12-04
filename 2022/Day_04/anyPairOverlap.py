import itertools as itertools

#splits mylist into groups of size 3 for comparison
def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

#assign variables
pairlist = []
assignmentlist = []
thereIsOverlap = False
partialOverlappingSections = 0

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
    print(pair)

    #convert the pair to range and assess overlap
    for value in range(int(pair[0]), int(pair[1])+1):
        if value2 in range(int(pair[2]), int(pair[3])+1):
            partialOverlappingSections+=1
            break

print("There are # partial overlap: " + str(partialOverlappingSections))
