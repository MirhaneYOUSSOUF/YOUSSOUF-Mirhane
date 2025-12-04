import csv
from matplotlib import pyplot as plt
from pylab import plot, figure, show
table=[]
with open('donnees_2008.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		#print(','.join(row))
		table.append(row)
#print(table)
#print(table[1][5])

for i in range(len(table)):
	if table[i][6]=='Auxerre':
		print('Auxerre',i)
		

donnees_2016=[]
with open('donnees_2016.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        #print(','.join(row))
        donnees_2016.append(row)
#print(donnees_2016)
#print(table[1][4])

for i in range(len(donnees_2016)):
	if donnees_2016[i][6]=='Auxerre':
		print('Auxerre', donnees_2016[i][9])
		
donnees_2021=[]
with open('donnees_2021.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        #print(','.join(row))
        donnees_2021.append(row)
#print(donnees_2021)		

for i in range(len(donnees_2021)):
	if donnees_2021[i][2]=='89024':
		print('890024', donnees_2021[i][5])
		

donnees_2023=[]
with open('donnees_2023.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
#        print(','.join(row))
        donnees_2023.append(row)
#print(donnees_2023)

for i in range(len(donnees_2023)):
	if donnees_2023[i][7]=='Auxerre':
		print('Auxerre', donnees_2023[i][10])
		

donnees=[2008,2016,2021,2023]

figure()
plot(donnees,[35575,39456,3554,35910])
show()
