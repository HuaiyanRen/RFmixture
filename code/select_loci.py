import random
import csv
import os

random.seed(2023)

loci_list = list(range(0, 1308))  
set1 = random.sample(loci_list, 1000)

set_l5 = random.sample(set1, 500)

set_l2 = random.sample(set_l5, 200)

set_l1 = random.sample(set_l2, 100)


with open('charset.csv', 'r') as charsets:
    reader = csv.reader(charsets)
    # Skip the header
    next(reader)
    names, starts, ends = [], [], []
    for row in reader:
        names.append(row[3])
        starts.append(row[4])
        ends.append(row[5])


with open('l10_1.txt', 'w') as loci:
    for i in set1:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l10_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l10.nex')
os.rename('partitions.txt', 'l10_par.txt')
os.system('rm *out.nex')


with open('l5_1.txt', 'w') as loci:
    for i in set_l5:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l5_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l5.nex')
os.rename('partitions.txt', 'l5_par.txt')
os.system('rm *out.nex')


with open('l2_1.txt', 'w') as loci:
    for i in set_l2:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l2_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l2.nex')
os.rename('partitions.txt', 'l2_par.txt')
os.system('rm *out.nex')


with open('l1_1.txt', 'w') as loci:
    for i in set_l1:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l1_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l1.nex')
os.rename('partitions.txt', 'l1_par.txt')
os.system('rm *out.nex')

