listNoSort = [-5,2,3,6,1,9,14]

def quicksort(a, primero ,ultimo):
    pivote = a[(primero+ultimo)//2]
    i = primero
    j = ultimo
    while i<=j:
        while a[i] < pivote: i += 1 
        while a[j] > pivote: j -= 1
        if i <= j:
            a[i],a[j] = a[j],a[i]
            i += 1
            j -= 1
    if (primero<j):
        quicksort(a, primero, j)
    if (i < ultimo):
        quicksort(a,i, ultimo)
    return a

listNoSort = quicksort(listNoSort,0,int(len(listNoSort)-1))
print (listNoSort)
