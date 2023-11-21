import csv  
 
                
with open('validate.txt', 'r') as file:
    lines = file.readlines()

part_list = []
for i in range(len(lines)):
    part_list.append(str(i+1) + '_' + lines[i].split()[0] + '.nex')   
    
model_list = ['GTR+FU+I+R6', 'l1','l2','l5','l10']
    
# =============================================================================
# with open('mf_results_dec.csv','w+',newline='') as csvf:
#     csv_write = csv.writer(csvf)
#     csv_write.writerow(['partition', 'q1', 'l1','l2','l5','l10'])   
#     
#     
# for part_name in part_list:
#     file_name = 'mf_dec/' + part_name + '.iqtree'
#     order_dict = {}
#     current_order = 1
#     with open(file_name, 'r') as file:
#         for line in file:
#             for model in model_list:
#                 if model in line and model not in order_dict:
#                     order_dict[model] = current_order
#                     current_order += 1
#     
#     result_row = [part_name] +  [order_dict[model] for model in model_list]
#     
#     with open('mf_results_dec.csv','a+',newline='') as csvf:
#         csv_write = csv.writer(csvf)
#         csv_write.writerow(result_row)
# =============================================================================



with open('mf_results_inc.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['partition', 'q1', 'l1','l2','l5','l10'])   
    
        
        
for part_name in part_list:
    file_name = 'mf_inc/' + part_name + '.iqtree'
    order_dict = {}
    current_order = 1
    with open(file_name, 'r') as file:
        for line in file:
            for model in model_list:
                if model in line and model not in order_dict:
                    order_dict[model] = current_order
                    current_order += 1
    
    result_row = [part_name] +  [order_dict[model] for model in model_list]
    
    with open('mf_results_inc.csv','a+',newline='') as csvf:
        csv_write = csv.writer(csvf)
        csv_write.writerow(result_row)

    