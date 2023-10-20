from multiprocessing import Pool
from functools import partial
import os
import argparse
 
                
with open('validate.txt', 'r') as file:
    lines = file.readlines()

part_list = []
for i in range(len(lines)):
    part_list.append(str(i+1) + '_' + lines[i].split()[0] + '.nex')    
    

def control(start, end, pool_num, method, decrease):
    if not os.path.isdir('mf'):
        os.makedirs('mf')
    
    para_list = []
    for j in range(int(start) - 1, int(end)):
        para_list.append((part_list[j],method, decrease))
    
    partial_running = partial(running_iqtree)
    with Pool(int(pool_num)) as p:
        p.map(partial_running, para_list)

def running_iqtree(paras):
    file_name, method, decrease = paras
    if decrease:
        cmd = 'iqtree2 -s ' + file_name + ' -m ' + method + ' -mset best_q1,l10t90_1_q10,l10t90_2_q10,l5t90_1_q10,l2t90_1_q10,l2t90_2_q10,l1t90_1_q10,l1t90_2_q10 -mrate E -mdef modelfile.nex -pre mf_dec/' + file_name + ' -nt 1 -redo'
    else:
        cmd = 'iqtree2 -s ' + file_name + ' -m ' + method + ' -mset best_q1,l1t90_1_q10,l1t90_2_q10,l2t90_1_q10,l2t90_2_q10,l5t90_1_q10,l10t90_1_q10,l10t90_2_q10 -mrate E -mdef modelfile.nex -pre mf_inc/' + file_name + ' -nt 1 -redo'
    os.system(cmd)  
    
# running
parser = argparse.ArgumentParser(description='')
parser.add_argument('--start', '-o1', help='', 
                    required=True)
parser.add_argument('--end', '-o2', help='', 
                    required=True)
parser.add_argument('--pool_num', '-p', help='', 
                    required=True)
parser.add_argument('--method', '-m', help='', 
                    required=True)
parser.add_argument('--decrease', '-d', help='', 
                    default = False)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        control(args.start, args.end, args.pool_num, args.method, args.decrease)
    except Exception as e:
        print(e)
