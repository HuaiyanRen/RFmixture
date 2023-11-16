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
    if method == 'MF' or method == 'MFP':
        if not os.path.isdir('mf_dec'):
            os.makedirs('mf_dec')
        if not os.path.isdir('mf_inc'):
            os.makedirs('mf_inc')
    elif method == 'one':
        if not os.path.isdir('one'):
            os.makedirs('one')
    elif method == 'mix_lrt':
        if not os.path.isdir('mix_lrt'):
            os.makedirs('mix_lrt')  
    elif method == 'mix_bic':
        if not os.path.isdir('mix_bic'):
            os.makedirs('mix_bic') 
    elif method == 'q10':
        if not os.path.isdir('q10'):
            os.makedirs('q10')
    
    para_list = []
    for j in range(int(start) - 1, int(end)):
        para_list.append((part_list[j],method, decrease))
    
    partial_running = partial(running_modelfinder)
    with Pool(int(pool_num)) as p:
        p.map(partial_running, para_list)

def running_modelfinder(paras):
    file_name, method, decrease = paras
    if method == 'MF' or method == 'MFP':
        if decrease:
            cmd = 'iqtree2 -s ' + file_name + ' -m ' + method + ' -mset best_q1,l5_q10,l2_q10,l1_q10 -mrate E -mdef modelfile.nex -pre mf_dec/' + file_name + ' -nt 1 -redo'
        else:
            cmd = 'iqtree2 -s ' + file_name + ' -m ' + method + ' -mset best_q1,l1_q10,l2_q10,l5_q10 -mrate E -mdef modelfile.nex -pre mf_inc/' + file_name + ' -nt 1 -redo'
    elif method == 'one':
        cmd = 'iqtree2 -s ' + file_name + ' -m GTR -mrate E,I,G,I+G,R,I+R -pre one/' + file_name + ' -nt 1 -redo'
    elif method == 'mix_lrt':
        cmd = 'iqtree2 -s ' + file_name + ' -m "ESTMIXNUM" -mset GTR -mrate E,I,G,I+G,R,I+R -opt_qmix_criteria 1 -opt-rhas-once -pre mix_lrt/' + file_name + ' -nt 1'
    elif method == 'mix_bic':
        cmd = 'iqtree2 -s ' + file_name + ' -m "ESTMIXNUM" -mset GTR -mrate E,I,G,I+G,R,I+R -opt_qmix_criteria 2 -opt-rhas-once -pre mix_bic/' + file_name + ' -nt 1'
    elif method == 'q10':
        cmd = 'iqtree2 -s ' + file_name + ' -m MIX"{GTR{13.5788/9.12648/5.87384/3.91449/54.535}+F{0.0532163/0.567914/0.124632/0.254238},GTR{0.000900126/0.0001/0.00713744/0.000247094/0.00891884}+F{0.622545/0.322908/0.0457865/0.00876112},GTR{2.24618/40.6955/0.408369/9.93118/0.153179}+F{0.299587/0.112554/0.104247/0.483612},GTR{0.171885/0.951409/0.248211/0.773395/1.78843}+F{0.247786/0.397173/0.228577/0.126464},GTR{3.13412/5.05262/1.89122/1.34808/3.36969}+F{0.127164/0.173037/0.560579/0.13922},GTR{0.116097/1.86907/0.149692/1.13247/0.421683}+F{0.443453/0.2219/0.0558192/0.278827},GTR{1.78396/7.4584/1.12893/0.913365/3.60818}+F{0.243643/0.371645/0.177325/0.207387},GTR{0.98099/0.0376085/1.29205/1.13175/100.0}+F{0.291487/0.132811/0.235039/0.340662},GTR{0.397348/5.54019/0.6541/0.446946/20.7838}+F{0.294635/0.127321/0.490188/0.0878567},GTR{1.90897/2.74895/0.708922/2.16591/9.70559}+F{0.292202/0.103357/0.276422/0.328019}}+R7{0.2796,0.04126,0.1727,0.246,0.1407,0.6401,0.1681,1.124,0.1643,2.021,0.06118,3.853,0.01335,7.43}" -pre q10/' + file_name + ' -nt 1 -redo'
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
