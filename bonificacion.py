# Calculador de bonificacion de ventas

MV = int(raw_input("Monto venta: "))

if MV >= 0 and MV <1000:
	TB = (0*MV)/100
	print "Tu bonificacion es: ", TB
elif MV >= 1000 and MV < 5000:
	TB = (3*MV)/100
	print "Tu bonificacion es: ", TB