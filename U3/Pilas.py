
class Node: # Hasta que no tenga nombre, es una plantilla
    def __init__(self, data): #__Init__ genera el dato por primera vez
        self.data = data # Propiedad de clase = variable
        self.next = None
    
    def getData(self): # Regresar el dato
        return self.data
    
class Stack: # clases se escriben con Mayuscula, metodos minuscula
    def __init__(self):
        self.head = None
        self.size = 0
        pass

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if self.size == 0 else False
        # return True if not self.head else False
    
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return
        popData = self.head
        self.head = self.head.next # Pila
        self.size -= 1
        return popData.data
        # self.next = self.head #Fila

    def peak(self):
        return self.head.data
    
    def showData(self):
        datos = ''
        id = self.head
        for i in range (0, self.size):
            datos += (id.data) + ' '
            id = id.next
        return datos
    
    def inverseData(self):
        dataStr = self.showData()
        dataList = dataStr.split()
        j = -1
        for i in range (0,len(dataList)//2):
            dataList[i],dataList[j] = dataList[j],dataList[i]
            j -= 1
        dataStr = ''
        for i in range (0,len(dataList)):
            dataStr += str(dataList[i]) + ' '
        return dataStr

        
Stack1 = Stack()

(Stack1.push("Jesus"))
(Stack1.push("Maria"))
(Stack1.push("Jose"))
(Stack1.push("Pavon"))
print(Stack1.getSize())
#print(Stack1.isEmpty())
print(Stack1.showData())
print(Stack1.inverseData())
#print(Stack1.peek())

print('=============================================')

print(Stack1.peak())

print("=============================================")

print(Stack1.getSize())
(Stack1.showData())

print("=============================================")

Stack2 = Stack()
Stack2.push("Hola")
print(Stack2.showData())
print("=============================================")
Stack2.pop()
Stack2.pop()
Stack2.pop()
Stack2.pop()
Stack2.pop()
