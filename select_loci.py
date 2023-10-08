import random
import csv
import os

random.seed(2023)

loci_list = list(range(0, 5162))  
selected_numbers = random.sample(loci_list, 2000)

set1 = selected_numbers[:1000]  
set2 = selected_numbers[1000:]  

set_l5_1 = random.sample(set1, 500)
set_l5_2 = random.sample(set2, 500)

set_l2_1 = random.sample(set_l5_1, 200)
set_l2_2 = random.sample(set_l5_2, 200)

taxa_list = list(range(0, 90))

set_t50_1 = random.sample(taxa_list, 40)
set_t50_2 = random.sample(taxa_list, 40)

set_t25_1 = random.sample(list(set(taxa_list) - set(set_t50_1)), 25)
set_t25_2 = random.sample(list(set(taxa_list) - set(set_t50_2)), 25)

set_l1_1 = random.sample(set_l2_1, 100)
set_l1_2 = random.sample(set_l2_2, 100)


with open('charset.csv', 'r') as charsets:
    reader = csv.reader(charsets)
    # Skip the header
    next(reader)
    names, starts, ends = [], [], []
    for row in reader:
        names.append(row[3])
        starts.append(row[4])
        ends.append(row[5])

with open('taxa_list.csv', 'r') as charsets:
    reader = csv.reader(charsets)
    taxa_name = []
    for row in reader:
        taxa_name.append(row[0])

with open('alignment.nex', 'r') as aln:
    lines = [line for line in aln]

set_t50_1_list = []
for i in set_t50_1:
    set_t50_1_list.append(taxa_name[i])

set_t50_2_list = []
for i in set_t50_2:
    set_t50_2_list.append(taxa_name[i])

set_t25_1_list = []
for i in set_t25_1:
    set_t25_1_list.append(taxa_name[i])

set_t25_2_list = []
for i in set_t25_2:
    set_t25_2_list.append(taxa_name[i])

with open('alignment_t50_1.nex', 'w') as aln:
    for line in lines:
        if not any(s in line for s in set_t50_1_list):
               aln.write(line)

with open('alignment_t50_2.nex', 'w') as aln:
    for line in lines:
        if not any(s in line for s in set_t50_2_list):
                aln.write(line)

with open('alignment_t25_1.nex', 'w') as aln:
    for line in lines:
        if not any(s in line for s in set_t25_1_list) and not any(s in line for s in set_t50_1_list):
                aln.write(line)

with open('alignment_t25_2.nex', 'w') as aln:
    for line in lines:
        if not any(s in line for s in set_t25_2_list) and not any(s in line for s in set_t50_2_list):
                aln.write(line)

with open('l10_1.txt', 'w') as loci:
    for i in set1:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l10_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l10t90_1.nex')
os.rename('partitions.txt', 'l10t90_1_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t50_1.nex -l l10_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l10t50_1.nex')
os.rename('partitions.txt', 'l10t50_1_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t25_1.nex -l l10_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l10t25_1.nex')
os.rename('partitions.txt', 'l10t25_1_par.txt')
os.system('rm *out.nex')


with open('l10_2.txt', 'w') as loci:
    for i in set2:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')
  
os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l10_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l10t90_2.nex')
os.rename('partitions.txt', 'l10t90_2_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t50_2.nex -l l10_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l10t50_2.nex')
os.rename('partitions.txt', 'l10t50_2_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t25_2.nex -l l10_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l10t25_2.nex')
os.rename('partitions.txt', 'l10t25_2_par.txt')
os.system('rm *out.nex')

with open('l5_1.txt', 'w') as loci:
    for i in set_l5_1:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l5_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l5t90_1.nex')
os.rename('partitions.txt', 'l5t90_1_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t50_1.nex -l l5_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l5t50_1.nex')
os.rename('partitions.txt', 'l5t50_1_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t25_1.nex -l l5_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l5t25_1.nex')
os.rename('partitions.txt', 'l5t25_1_par.txt')
os.system('rm *out.nex')

with open('l5_2.txt', 'w') as loci:
    for i in set_l5_2:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')
  
os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l5_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l5t90_2.nex')
os.rename('partitions.txt', 'l5t90_2_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t50_2.nex -l l5_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l5t50_2.nex')
os.rename('partitions.txt', 'l5t50_2_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t25_2.nex -l l5_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l5t25_2.nex')
os.rename('partitions.txt', 'l5t25_2_par.txt')
os.system('rm *out.nex')

with open('l2_1.txt', 'w') as loci:
    for i in set_l2_1:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l2_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l2t90_1.nex')
os.rename('partitions.txt', 'l2t90_1_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t50_1.nex -l l2_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l2t50_1.nex')
os.rename('partitions.txt', 'l2t50_1_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t25_1.nex -l l2_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l2t25_1.nex')
os.rename('partitions.txt', 'l2t25_1_par.txt')
os.system('rm *out.nex')

with open('l2_2.txt', 'w') as loci:
    for i in set_l2_2:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')
  
os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l2_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l2t90_2.nex')
os.rename('partitions.txt', 'l2t90_2_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t50_2.nex -l l2_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l2t50_2.nex')
os.rename('partitions.txt', 'l2t50_2_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t25_2.nex -l l2_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l2t25_2.nex')
os.rename('partitions.txt', 'l2t25_2_par.txt')
os.system('rm *out.nex')


with open('l1_1.txt', 'w') as loci:
    for i in set_l1_1:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l1_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l1t90_1.nex')
os.rename('partitions.txt', 'l1t90_1_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t50_1.nex -l l1_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l1t50_1.nex')
os.rename('partitions.txt', 'l1t50_1_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t25_1.nex -l l1_1.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l1t25_1.nex')
os.rename('partitions.txt', 'l1t25_1_par.txt')
os.system('rm *out.nex')

with open('l1_2.txt', 'w') as loci:
    for i in set_l1_2:
        loci.write(names[i] + ' = ' + starts[i] + '-' + ends[i] + '\n')
  
os.system('python3 AMAS.py split -f nexus -d dna -i alignment.nex -l l1_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l1t90_2.nex')
os.rename('partitions.txt', 'l1t90_2_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t50_2.nex -l l1_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l1t50_2.nex')
os.rename('partitions.txt', 'l1t50_2_par.txt')
os.system('rm *out.nex')

os.system('python3 AMAS.py split -f nexus -d dna -i alignment_t25_2.nex -l l1_2.txt -u nexus')
os.system('python3 AMAS.py concat -f nexus -d dna -i *out.nex')
os.rename('concatenated.out', 'l1t25_2.nex')
os.rename('partitions.txt', 'l1t25_2_par.txt')
os.system('rm *out.nex')



  