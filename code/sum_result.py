import os
import csv   

                
with open('validate.txt', 'r') as file:
    lines = file.readlines()

part_list = []
for i in range(len(lines)):
    part_list.append(str(i+1) + '_' + lines[i].split()[0] + '.nex')
    

with open('results.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['partition', 'length', 'classes', 'lnl', 'bic', 'time', 'time_mix', 'time_q10'])


for part_name in part_list:
    if os.path.exists('mix_bic/' + part_name + '.iqtree'):
        if os.path.exists('q10/' + part_name + '.iqtree'):
            with open('mix_bic/' + part_name + '.iqtree') as iqtree_file:
                for line in iqtree_file.readlines():
                    if 'Input data:' in line:
                        length = float(line.split()[5])
                    if 'Best-fit model according to BIC:' in line:
                        classes = int(line.count(','))+1
                    if 'Log-likelihood of the tree:' in line:
                        lnl_mix = float(line.split()[4])
                    if 'Bayesian information criterion (BIC) score' in line:
                        bic_mix = float(line.split()[-1])
                    if 'Total CPU time used:' in line:
                        time_mix = float(line.split()[4])
                            
            with open('q10/' + part_name + '.iqtree') as iqtree_file:
                for line in iqtree_file.readlines():
                    if 'Log-likelihood of the tree:' in line:
                        lnl_q10 = float(line.split()[4])
                    if 'Bayesian information criterion (BIC) score' in line:
                        bic_q10 = float(line.split()[-1])
                    if 'Total CPU time used:' in line:
                        time_q10 = float(line.split()[4])
                            
            if lnl_mix > lnl_q10:
                lnl = 'MixtureFinder'
            else:
                lnl = 'Q10'
                    
            if bic_mix < bic_q10:
                bic = 'MixtureFinder'
            else:
                bic = 'Q10'
                
            if time_mix < time_q10:
                time = 'MixtureFinder'
            else:
                time = 'Q10'
                    
            result_row = [part_name, length, classes, lnl, bic, time, time_mix, time_q10]    
            
            with open('results.csv','a+',newline='') as csvf:
                csv_write = csv.writer(csvf)
                csv_write.writerow(result_row)

