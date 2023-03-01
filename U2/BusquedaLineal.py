# Return index of a number from a not sorted list and a sorted list

listNoSort = [-5,2,3,6,1,9,14]
listSorted = [-3,0,5,7,9,10,14]

# NOTSORTED
def SearchNotSort(notSortedList , valueToFind):
    for i in range (0,len(notSortedList)):
        if notSortedList[i] == valueToFind:
            return i+1
        else:
            pass
    return -1

# SORTED
def SearchSort(sortedList , valueToFind):
    for i in range (0,len(sortedList)):
        if sortedList[i] > valueToFind:
            break
        elif sortedList[i] == valueToFind:
            return i+1
        else:
            pass
    return -1

valueToSearch = int(input("Value to search (Not Sorted): "))
indexInList = SearchNotSort(listNoSort, valueToSearch)
print ("The number is in position:", indexInList, end="\n\n")

valueToSearch = int(input("Value to search (Sorted): "))
indexInList = SearchSort(listSorted, valueToSearch)
print ("The number is in position:", indexInList, end="\n\n")
