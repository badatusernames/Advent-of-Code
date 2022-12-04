import itertools as itertools

#splits mylist into groups of size 3 for comparison
def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

#splits arrays into lists of characters
def arrayToCharacterList(array):
    result = []
    for element in array:
        result.append(element)

    return result

#compares groups of three for common values
def threeArrayIntersection(arr1,arr2,arr3):

    #parse array to character list
    array1 = arrayToCharacterList(arr1)
    array2 = arrayToCharacterList(arr2)
    array3 = arrayToCharacterList(arr3)

    #Assigning arrays to sets to element duplicate values
    set1 = set(array1)
    set2 = set(array2)
    set3 = set(array3)

    #Calculate common value from the sets
    commonElement = set1.intersection(set2,set3)

    print("The common element is: " + str(commonElement))
    return commonElement

badge = []
totalPriority = 0
backpacksProcessed = 0

#Read the file and output the result into a list with no newlines
with open('input.txt','r') as f:
    mylist = f.read().splitlines()
    print(mylist)
    print('\n')
    print('\n')

    #Call the grouper def to split the list into groups of 3
    list_of_groups = list(grouper(3, mylist))
    #Print length to ensure proper splitting into groups of 3
    print(len(list_of_groups))

for group in list_of_groups:
    #looks at each group of three and returns the common character
    badge = threeArrayIntersection(group[0],group[1],group[2])
    print(badge)

    #Converts match into Unicode number then offsets to problem priority value
    for item in badge:
        value=ord(item)
        if value >= 97:
            value -= 96
        else:
            value -= 38
        #Adds value to priority total
        totalPriority = totalPriority + value

    #Clears the matchedItems list for the next iteration
    badge = []

print("The total Priority of the items is: " + str(totalPriority))
