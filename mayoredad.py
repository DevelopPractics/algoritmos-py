AN = int(raw_input("En que ano Naciste: "))
AA = int(raw_input("Ano Actual: "))
Edad = AA - AN

if Edad > 17:
	print ""
	print "Debes solicitar tu Cedula de Ciudadania!"
else:
	print ""
	print "Todavia eres un nino!!"	
