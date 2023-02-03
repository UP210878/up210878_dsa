# 3 Edificios, 15 pisos, 20 cuartos cada uno
# True si esta ocupado, cuandos ocupantes tiene en el piso 15 del tercer edificio

cuartos = [[[False for r in range(20)] for f in range(15)] for b in range(3)]
print ("Building, floor, rooms",)
print (cuartos.shape[2][14])


