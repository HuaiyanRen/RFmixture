import os
from ete3 import Tree
import csv   

                
data_name = 'l10t90_1'
classes = 10
file_name = data_name + '_q' + str(classes) 

with open('validate.txt', 'r') as file:
    lines = file.readlines()

part_list = []
for i in range(len(lines)):
    part_list.append(str(i+1) + '_' + lines[i].split()[0] + '.nex')
    

with open(file_name + '_results.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['data','partition', 'bic', 'nrf', 'tree_length'])
    
count = 0    
for part_name in part_list:
    if os.path.exists(file_name + '/' + part_name + '.iqtree'):
        count += 1
                    
        part_treefile = file_name + '/' + part_name + '.treefile'
        part_treestr = open(part_treefile,'r').read()
        part_tree = Tree(part_treestr)
        nodes = set(part_tree.get_leaf_names())
        
        true_treefile = 'aa_t90_unrooted.treefile'
        true_treestr = open(true_treefile,'r').read()
        true_tree = Tree(true_treestr)        
        true_tree.prune(nodes)
        sub_true_treefile =  file_name + '/' + part_name + '_true.treefile'
        with open(sub_true_treefile, 'w') as result:
            result.write(true_tree.write() + '\n')
        
        if not os.path.exists(file_name + '/' + part_name + '_rf.rfdist'):
            rf_cmd = 'iqtree2 -rf ' + part_treefile + ' ' + sub_true_treefile + ' -pre ' + file_name + '/' + part_name + '_rf'
            os.system(rf_cmd)
        
        with open(file_name + '/' + part_name + '.iqtree') as iqtree_file:
            for line in iqtree_file.readlines():
                if 'Input data:' in line:
                    ntaxa = float(line.split()[2])
                if 'Bayesian information criterion (BIC) score' in line:
                    bic = float(line.split()[-1])
                if 'Total tree length (sum of branch lengths)' in line:
                    tree_length = float(line.split()[-1])
        
        with open(file_name + '/' + part_name + '_rf.rfdist') as rf_file:
            for line in rf_file.readlines():
                if 'Tree0' in line:
                    rf = float(line.split()[-1])
                    
        nrf = rf/(2*ntaxa-6)

        result_row = [data_name, part_name, bic, nrf, tree_length]
        
        with open(file_name + '_results.csv','a+',newline='') as csvf:
            csv_write = csv.writer(csvf)
            csv_write.writerow(result_row)

print(str(count) + ' results are recorded')
