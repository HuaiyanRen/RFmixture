import random
import csv
import os
import re
import shutil

random.seed(2023)

# combine 3162 genes to 3 sequences
validate_list = list(range(0, 3162))
random.shuffle(validate_list)

list1 = random.sample(validate_list, 1054)
for element in list1:
    validate_list.remove(element)

list2 = random.sample(validate_list, 1054)
for element in list2:
    validate_list.remove(element)

list3 = validate_list 


with open('charset.csv', 'r') as charsets:
    reader = csv.reader(charsets)
    # Skip the header
    next(reader)
    names, starts, ends = [], [], []
    for row in reader:
        names.append(row[3])
        starts.append(row[4])
        ends.append(row[5])


source_directory = os.getcwd()

if not os.path.exists('list1'):
    os.makedirs('list1')
if not os.path.exists('list2'):
    os.makedirs('list2')    
if not os.path.exists('list3'):
    os.makedirs('list3')    
    

for order_num in list1:
    file_name = f"{order_num}_"
    for file in os.listdir(source_directory):
        if file.startswith(file_name):
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join('list1', file)
            shutil.copy2(source_path, destination_path)

os.system('python3 AMAS.py concat -f nexus -d dna -i list1/*')
os.rename('concatenated.out', 'vali1.nex')
os.rename('partitions.txt', 'vali1_par.txt')    
os.system('rm -rf list1')

for order_num in list2:
    file_name = f"{order_num}_"
    for file in os.listdir(source_directory):
        if file.startswith(file_name):
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join('list2', file)
            shutil.copy2(source_path, destination_path)

os.system('python3 AMAS.py concat -f nexus -d dna -i list2/*')
os.rename('concatenated.out', 'vali2.nex')
os.rename('partitions.txt', 'vali2_par.txt')    
os.system('rm -rf list2')

for order_num in list3:
    file_name = f"{order_num}_"
    for file in os.listdir(source_directory):
        if file.startswith(file_name):
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join('list3', file)
            shutil.copy2(source_path, destination_path)

os.system('python3 AMAS.py concat -f nexus -d dna -i list3/*')
os.rename('concatenated.out', 'vali3.nex')
os.rename('partitions.txt', 'vali3_par.txt')    
os.system('rm -rf list3')

