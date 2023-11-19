import random
import csv
import os
import re

random.seed(2023)


loci_list = list(range(0, 1308))  
set1 = random.sample(loci_list, 1000)

validate_list = list(set(loci_list) - set(set1))


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

def contains_required_letters(line):
    for letter in ['A', 'C', 'G', 'T']:
        if letter in line:
            return True
    return False

order = 1
for i in validate_list:
    old_name = 'alignment_' + names[i] + '-out.nex'
    new_name = str(order) + '_' + names[i] + '.nex'
    
    with open(old_name, 'r') as file:
        lines = file.readlines()
    
    filtered_lines = []
    remove = 0
    for idx, line in enumerate(lines, start=1):  
        if 7 <= idx < 45 and not contains_required_letters(line.split()[1]):
            remove += 1
            continue
        filtered_lines.append(line)
    
    filtered_lines[3] = re.sub(r'(NTAX=)\d+', r'NTAX=' + str(38 - remove), lines[3])
    
    with open(old_name, 'w') as file:
        file.writelines(filtered_lines)
    
    os.rename(old_name, new_name)
    order += 1
    
    
