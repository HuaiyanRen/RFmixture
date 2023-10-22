import csv  
 
                
with open('validate.txt', 'r') as file:
    lines = file.readlines()

part_list = []
for i in range(len(lines)):
    part_list.append(str(i+1) + '_' + lines[i].split()[0] + '.nex')   
    
model_list = ['GTR+FU+R8', 'l1t90_1','l1t90_2','l2t90_1','l2t90_2','l5t90_1','l10t90_1','l10t90_2']
    
with open('mf_results.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['partition', 'q1', 'l1t90_1','l1t90_2','l2t90_1','l2t90_2','l5t90_1','l10t90_1','l10t90_2'])   
    
    
for part_name in part_list:
    file_name = 'mf_dec/' + part_name + '.iqtree'
    order_dict = {}
    current_order = 1
    with open(file_name, 'r') as file:
        for line in file:
            for model in model_list:
                if model in line and model not in order_dict:
                    order_dict[model] = current_order
                    current_order += 1
    
    result_row = [part_name] +  [order_dict[model] for model in model_list]
    
    with open('mf_results.csv','a+',newline='') as csvf:
        csv_write = csv.writer(csvf)
        csv_write.writerow(result_row)

    