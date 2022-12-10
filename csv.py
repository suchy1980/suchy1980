path = 'C:\\Users\\vdi-student\\Desktop\\rozliczenie.csv'
mode = 'r'
with open(path,mode) as plik:
    content = plik.readlines()

for i in range (len(content)):
    content[i] = content[i].split(',')
print(content)
print(range (len(content)))
linia = 0
kolumna = 1
total=0
for i in range(1,len(content)):
    total = total + int(content[i][1])
average = total / (len(content)-1)
print(round(average,2))

total1=0
for i in range(1,len(content)):
    if content[i][3] == 'k' and content[i][4] == 't\n'
        total1 += 1
print(total1)