import os
import csv   

                
with open('validate.txt', 'r') as file:
    lines = file.readlines()

part_list = []
for i in range(len(lines)):
    part_list.append(str(i+1) + '_' + lines[i].split()[0] + '.nex')
    

with open('weights.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['partition', 'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10'])
    
    
for part_name in part_list:
    if os.path.exists('q10/' + part_name + '.iqtree'):
        w_list = []
        with open('q10/' + part_name + '.iqtree') as iqtree_file:  
            for line in iqtree_file.readlines():
                for i in range(1,11):
                    if str(i) +'  GTR' in line:
                        w_list.append(float(line.split()[3]))
    
        result_row = [part_name] + w_list
        
        with open('weights.csv','a+',newline='') as csvf:
            csv_write = csv.writer(csvf)
            csv_write.writerow(result_row)

