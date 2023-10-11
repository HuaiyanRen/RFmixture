from multiprocessing import Pool
from functools import partial
import os
import pandas as pd
import argparse
 
                
with open('validate.txt', 'r') as file:
    lines = file.readlines()

part_list = []
for i in range(len(lines)):
    part_list.append(str(i+1) + '_' + lines[i].split()[0] + '.nex')    
    

def control(train_name, model_type, classes, rhas, start, end, pool_num):
    model_name = train_name + '_' + model_type + str(classes)
    if not os.path.isdir(model_name):
        os.makedirs(model_name)

    model_df = pd.read_excel(model_name + '.xlsx')
    AC = model_df['AC'].tolist()
    AG = model_df['AG'].tolist()
    AT = model_df['AT'].tolist()
    CG = model_df['CG'].tolist()
    CT = model_df['CT'].tolist()
    FA = model_df['FA'].tolist()
    FC = model_df['FC'].tolist()
    FG = model_df['FG'].tolist()
    FT = model_df['FT'].tolist()
    assert len(AC) == int(classes)
    
    model_str ='MIX\"{'
    for i in range(int(classes)):
        if i == 0:
            model_str = model_str + 'GTR{'+str(AC[i])+'/'+str(AG[i]) +'/'+str(AT[i])+'/'+str(CG[i])+'/'+str(CT[i])+'}+F{'+str(FA[i])+'/'+str(FC[i])+'/'+str(FG[i])+'/'+str(FT[i])+'}'
        else:
            model_str = model_str + ',GTR{'+str(AC[i])+'/'+str(AG[i]) +'/'+str(AT[i])+'/'+str(CG[i])+'/'+str(CT[i])+'}+F{'+str(FA[i])+'/'+str(FC[i])+'/'+str(FG[i])+'/'+str(FT[i])+'}'
    model_str = model_str + '}+' + rhas + '\"' 
    
    para_list = []
    for j in range(int(start) - 1, int(end)):
        para_list.append((part_list[j], model_str, model_name))
    
    partial_running = partial(running_iqtree)
    with Pool(int(pool_num)) as p:
        p.map(partial_running, para_list)

def running_iqtree(paras):
    file_name, model_str, model_name = paras
    cmd = 'iqtree2 -s ' + file_name + ' -m ' + model_str + ' -pre ' + model_name + '/' + file_name + ' -nt 1'
    os.system(cmd)  
    
# running
parser = argparse.ArgumentParser(description='')
parser.add_argument('--train_name', '-n', help='',
                    required=True)
parser.add_argument('--model_type', '-t', help='q r f',
                    required=True)
parser.add_argument('--classes', '-c', help='',
                    required=True)
parser.add_argument('--rhas', '-r', help='', type=str,
                    required=True)
parser.add_argument('--start', '-o1', help='', 
                    required=True)
parser.add_argument('--end', '-o2', help='', 
                    required=True)
parser.add_argument('--pool_num', '-p', help='', 
                    required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        control(args.train_name, args.model_type, args.classes, args.rhas, args.start, args.end, args.pool_num)
    except Exception as e:
        print(e)
