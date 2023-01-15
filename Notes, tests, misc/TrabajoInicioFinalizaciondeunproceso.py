# A que hora finaliza un proceso dado la hora de inicio, el minuto de inicio y los minutos de duracion
print ("--------Hora de finalizacion de un proceso--------")

horas = int (input("Dame la hora de inicio: "))
minutos = int (input("Dame el minuto de inicio: "))
duracion = int (input("Cuantos minutos duro el proceso: "))
dias = 0

# Duracion
horas += (minutos + duracion)//60
minutos = (minutos + duracion)%60
dias = (horas)//24
horas = horas%24

print("El proceso finaliza a las ",horas,":", str(minutos).zfill(2), "horas ")
print("Terminara en ", dias , "dias")
