import random
import csv
import os

random.seed(2023)

loci_list = list(range(0, 5162))  
selected_numbers = random.sample(loci_list, 2000)

validate_list = list(set(loci_list) - set(selected_numbers))


with open('charset.csv', 'r') as charsets:
    reader = csv.reader(charsets)
    # Skip the header
    next(reader)
    names, starts, ends = [], [], []
    for row in reader:
        names.append(row[3])
        starts.append(row[4])
        ends.append(row[5])

with open('validate.txt', 'w') as loci:
    for i in validate_list:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')
        
os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l validate.txt -u nexus')

for i in validate_list:
    old_name = 'alignment_' + names[i] + '-out.nex'
    new_name =  names[i] + '.nex'
    os.rename(old_name, new_name)