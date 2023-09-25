import random
import csv

random.seed(2023)

loci_list = list(range(0, 5162))  
selected_numbers = random.sample(loci_list, 2000)

set1 = selected_numbers[:1000]  
set2 = selected_numbers[1000:]  


with open('charset.csv', 'r') as charsets:
    reader = csv.reader(charsets)
    # Skip the header
    next(reader)
    names, starts, ends = [], [], []
    for row in reader:
        names.append(row[3])
        starts.append(row[4])
        ends.append(row[5])


with open('loci1.txt', 'w') as loci:
    for i in set1:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')


with open('loci2.txt', 'w') as loci:
    for i in set2:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')
        