import os
import random

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

folder_path = os.getcwd()
tree_path = os.path.join(folder_path,'mix_bic')
output_file = 'trees.txt'



treefile_list = []
n = 0
for file in os.listdir(tree_path):
    if file.endswith('.treefile'):
        file_order = int(file.split('_')[0])
        if file_order in list1:
            treefile_list.append(file)
            n = n + 1
            print(file)
print(n)
#treefile_list = [file for file in os.listdir(folder_path) if file.endswith('.treefile')]

with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        treefile_path = os.path.join(tree_path, treefile)
        with open(treefile_path, 'r') as current_file:
            output_file.write(current_file.read())