class Node: # Hasta que no tenga nombre, es una plantilla
    def __init__(self, data): #__Init__ genera el dato por primera vez
        self.data = data # Propiedad de clase = variable
        self.next = None
    
    def getData(self): # Regresar el dato
        return self.data
    
    def setData(self, data): # cambiar el dato
        self.data = data # Cuando pones self, es la propiedad del objeto, no la variable    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass


nodo_1 = Node("Tony Stark")
print (nodo_1.data)# Nodo_1 es direccion
print (nodo_1.getData()) # Metodos son cubitos, las propiedades estan entre corchetes [O]
print(nodo_1.next)

nodo_1.setData("Iron Man")
print(nodo_1.getData())

nodo_2 = Node("Jose")

nodo_1.next = nodo_2 # Pasa direccion para que pueda acceder a cualquier atributo
"""print (nodo_1.next)
print (nodo_2.next)"""

nodo_3 = Node("Tony Stark")

nodo_2.next = nodo_3
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(nodo_1.data)
print (nodo_1.next.data)
print (nodo_1.next.next.data)
"""print (nodo_2.next)
print(nodo_3.next)
"""