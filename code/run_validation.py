from multiprocessing import Pool
from functools import partial
import os
import argparse
 
                
with open('validate.txt', 'r') as file:
    lines = file.readlines()

part_list = []
for i in range(len(lines)):
    part_list.append(str(i+1) + '_' + lines[i].split()[0] + '.nex')    
    

def control(start, end, pool_num):
    if not os.path.isdir('mf'):
        os.makedirs('mf')
    
    para_list = []
    for j in range(int(start) - 1, int(end)):
        para_list.append(part_list[j])
    
    partial_running = partial(running_iqtree)
    with Pool(int(pool_num)) as p:
        p.map(partial_running, para_list)

def running_iqtree(paras):
    file_name = paras
    cmd = 'iqtree2 -s ' + file_name + ' -m MFP -mset l1t90_1_q10,l1t90_2_q10,l2t90_1_q10,l2t90_2_q10,l5t90_1_q10,l10t90_1_q10,l10t90_2_q10,best_q1 -mrate E -mdef modelfile.nex -pre mf/' + file_name + ' -nt 1'
    os.system(cmd)  
    
# running
parser = argparse.ArgumentParser(description='')
parser.add_argument('--start', '-o1', help='', 
                    required=True)
parser.add_argument('--end', '-o2', help='', 
                    required=True)
parser.add_argument('--pool_num', '-p', help='', 
                    required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        control(args.start, args.end, args.pool_num)
    except Exception as e:
        print(e)
