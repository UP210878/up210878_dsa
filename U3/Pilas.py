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
        self.head = newNode.next
        self.size += 1

    def pop(self):
        if self.size < 1:
            exit
        self.size -= 1

Stack1 = Stack()
dato1 = Node("Jesus")
dato2 = Node("Maria")
dato3 = Node("Jose")

(Stack.push(Stack1,dato1))
(Stack.push(Stack1,dato2))
print(Stack.getData(Stack1))
