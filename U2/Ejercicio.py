from random import randrange
lista = [0 for i in range(0,100)]

def RandomNumbers(inputList,inicio,fin):
    i = 0
    inputList = list(inputList)
    repetido = False
    while i < len(inputList):
        n = randrange(inicio,fin)
        for k in range(len(inputList)):
            if n not in inputList:
                repetido = False              
            else:
                repetido = True
                break
        if repetido == False:
            inputList[i] = n
            i = i+1
        else:
            continue
    return inputList

def BubbleSort(inputList):
    swapped = True 
    while swapped:
        swapped = False
        for i in range(len(inputList) - 1):
            if inputList[i] > inputList[i + 1]:
                swapped = True 
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
    return inputList

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

def quicksort(listNoSort, primero ,ultimo):
    pivote = listNoSort[(primero+ultimo)//2]
    i = primero
    j = ultimo
    while i<=j:
        while listNoSort[i] < pivote: i += 1 
        while listNoSort[j] > pivote: j -= 1
        if i <= j:
            listNoSort[i],listNoSort[j] = listNoSort[j],listNoSort[i]
            i += 1
            j -= 1
    if (primero<j):
        quicksort(listNoSort, primero, j)
    if (i < ultimo):
        quicksort(listNoSort,i, ultimo)
    return listNoSort

def Print10x10(lista):
    for i in range(0,10):
        print("\n")
        for j in range(0,10):
            print(lista[j+(i*10)],sep=" ",end=", ")


RandList = RandomNumbers(lista,101,500)
print("\n\nRandom List:",end="")
Print10x10(RandList)

MetodoSorteo = int(input("\nMetodo de Sorteo:\n1. BubbleSort\n2. Quicksort\n"))

if MetodoSorteo == 1:
    ListBubble = BubbleSort(RandList)
    print("\n\nBubbleSort List:",end="")
    Print10x10(ListBubble)
elif MetodoSorteo == 2:
    QuickSort = quicksort(RandList,0,int(len(RandList))-1)
    print ("\n\nQuicksorted List:", end="")
    Print10x10(QuickSort)
else:
    print("Metodo invalido")
    exit()

if MetodoSorteo == 1:
    Num = int(input("\n\nNumero a buscar:\n"))
    indexFound, timesTried = binarysearch(ListBubble,Num)

if MetodoSorteo == 2:
    Num = int(input("\n\nNumero a buscar:\n"))
    indexFound, timesTried = binarysearch(QuickSort,Num)

print ("\n\n\nBinarySearch\nPosition:", indexFound)
print ("Times searched:", timesTried)