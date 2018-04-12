entrada = open('precios.html', 'r') #Archivo con datos de entrada que quiero buscar (es el codigo fuente de la pagina web).
salida = open('salida.txt', 'w') 	#Archivo de salida que se generara con la lista de datos encontrados
i = 0
cont = 1
prom = 0
acum = 0
precio = 0

#For each line in file "entrada"
for line in entrada:
	#Put the line in variable "e"
	e = line
	
	#Find a substr that contain 'price__fraction' and get the index in the line (i=initial position of the substr in the line)
	i = e.find('price__fraction')
	
	#Put substr 'index + 25 follows chars' in the "s" variable
	s = e[i : i + 25]
	
	while (i != -1):
		if (len(s) != 0):
			print ("s:" + s)
			cont = cont+1
			#Get the price of the substr in 's'
			precio = s[18 : 18 + 7]
			print ("precio:" + precio)
			precio = eval(precio)
			acum = acum + precio
			salida.write(s + '\n') 
			e = e[ (i + len(s)) : len(e)]
			i = e.find('price__fraction')
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
