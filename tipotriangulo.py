L1 = raw_input("Ingresar Primer lado: ")
L2 = raw_input("Ingresar Segundo lado: ")
L3 = raw_input("Ingresar Tercer lado: ")

if (L1 != L2) and (L2 != L3):
	print "Escaleno"
elif (L1 == L2) and (L2 == L3):
	print "Equilatero"
else:
	print "Isosceles"

