# Busqueda binaria (dividir por la mitad)
list1 = [-3,0,1,5,7,9]

def binarysearch (sortedList,valueToSearch):
    lowerLimit = 0
    upperLimit = len(sortedList)
    i = int((lowerLimit + upperLimit)//2)
    n = 1
    while lowerLimit <= upperLimit and valueToSearch <= sortedList[-1] and valueToSearch >= sortedList[0]: # Num no puede ser mayor al ultimo numero de lista ni menor al primer numero de lista
        if sortedList[i] == valueToSearch:
            return i,n
        elif sortedList[i] >= valueToSearch: # Lado izquierdo
            upperLimit = i - 1
        elif sortedList[i] <= valueToSearch: # Lado derecho
            lowerLimit = i + 1
        i = int((lowerLimit + upperLimit)//2)
        n = n + 1
    return -1,n

valueToSearch = int(input('INgrese el valor a buscar: '))

indexFound, timesTried = binarysearch(list1,valueToSearch)

print ("Position:", indexFound)
print ("Times searched:", timesTried)

