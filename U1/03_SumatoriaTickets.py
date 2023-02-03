Dinero = int(input("Cuanto dinero estas dispuesto a pagar\n"))
precio_boletos = 1
N = 0
while Dinero >= precio_boletos:
    Dinero -= precio_boletos
    precio_boletos += 1
    N += 1
print ("Ajustaste ", N, " boletos")
print ("Te sobro $", Dinero,sep="")
print ("Necesitabas $", precio_boletos-Dinero, " Para otro boleto",sep="")