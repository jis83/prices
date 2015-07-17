entrada = open('precios.html', 'r') #Archivo con datos de entrada que quiero buscar (es el codigo fuente de la pagina web).
salida = open('salida.txt', 'w') 	#Archivo de salida que se generara con la lista de datos encontrados
i = 0
cont = 1
prom = 0
acum = 0
precio = 0
for line in entrada:
	e = line

	i = e.find('ch-price')
	s = e[i : i + 25]
	
	while (i != -1):
		if (len(s) != 0):
			print ("s: " + s)
			cont = cont+1
			precio = s[12 : 12 + 7]
			print ("precio: " + precio)
			precio = eval(precio)
			acum = acum + precio
			salida.write(s + '\n') 
			e = e[ (i + len(s)) : len(e)]
			i = e.find('ch-price')
			s = e[ i : i + 25]
		else:
			i = -1
	e = ''
	s = ''
	i = 0

#Calculo precio promedio
if (cont != 0):
	prom = acum/cont
print ("Precio promedio: " + str(prom))
salida.write('Precio promedio: ' + str(prom))
