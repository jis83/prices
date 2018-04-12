input = open('prices.html', 'r') #Input File with source code of the ML web page search results.
output = open('output.txt', 'w') 	#Output File with results
i = 0
cont = 1
avg = 0
acum = 0
price = 0

#For each line in file "input"
for line in input:
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
			price = s[18 : 18 + 7]
			print ("price:" + price)
			price = eval(price)
			acum = acum + price
			output.write(s + '\n') 
			e = e[ (i + len(s)) : len(e)]
			i = e.find('price__fraction')
			s = e[ i : i + 25]
		else:
			i = -1
	e = ''
	s = ''
	i = 0

#Get average price
if (cont != 0):
	avg = acum/cont
print ("Average price: " + str(avg))
output.write('Average price: ' + str(avg))
