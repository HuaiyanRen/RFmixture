import pandas as pd
import os

data_list = ['l1t90_1','l1t90_2','l2t90_1','l2t90_2','l5t90_1','l5t90_2','l10t90_1','l10t90_2']

classes = 10
path = r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal'
modelfile =  os.path.join(path, 'modelfile.nex')

with open(modelfile,'w+') as f:
    f.write('#nexus' + '\n' + 'begin models;' + '\n') 

for data_name in data_list:
    file_name = data_name + '_q' + str(classes) 
    
    one_file_name = os.path.join(path, data_name + '_mf.iqtree')
    
    if_invar = False
    with open(one_file_name) as b:
        for line in b.readlines():
            if 'A-C:' in line:
                AC1 = float(line.split()[-1])
            if 'A-G:' in line:
                AG1 = float(line.split()[-1])
            if 'A-T:' in line:
                AT1 = float(line.split()[-1])
            if 'C-G:' in line:
                CG1 = float(line.split()[-1])
            if 'C-T:' in line:
                CT1 = float(line.split()[-1])
            if 'pi(A)' in line:
                FA1 = float(line.split()[-1])
            if 'pi(C)' in line:
                FC1 = float(line.split()[-1])
            if 'pi(G)' in line:
                FG1 = float(line.split()[-1])
            if 'pi(T)' in line:
                FT1 = float(line.split()[-1])
            if 'Proportion of invariable sites:' in line:
                if_invar = True
                invar = float(line.split()[-1])
            if 'Site proportion and rates:' in line:
                n_rate = line.count('(')
                rate_str = line.split('(')[1].split(')')[0]
                for i in range(2, n_rate+1):
                    rate_str = rate_str + ',' + line.split('(')[i].split(')')[0]
    
    model_str_1 = 'GTR{'+str(AC1)+'/'+str(AG1) +'/'+str(AT1)+'/'+str(CG1)+'/'+str(CT1)+'}+F{'+str(FA1)+'/'+str(FC1)+'/'+str(FG1)+'/'+str(FT1)+'}'
    if if_invar:
        model_str_1 = model_str_1 + '+I{' + str(invar) + '}+R' + str(n_rate) + '{' + rate_str + '};'
    else:
        model_str_1 = model_str_1 + '+R' + str(n_rate) + '{' + rate_str + '};'
    
    mix_file_name = os.path.join(path, file_name + '.xlsx')
    
    model_df = pd.read_excel(mix_file_name)
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
    
    model_str_mix ='MIX{'
    for i in range(int(classes)):
        if i == 0:
            model_str_mix = model_str_mix + 'GTR{'+str(AC[i])+'/'+str(AG[i]) +'/'+str(AT[i])+'/'+str(CG[i])+'/'+str(CT[i])+'}+F{'+str(FA[i])+'/'+str(FC[i])+'/'+str(FG[i])+'/'+str(FT[i])+'}'
        else:
            model_str_mix = model_str_mix + ',GTR{'+str(AC[i])+'/'+str(AG[i]) +'/'+str(AT[i])+'/'+str(CG[i])+'/'+str(CT[i])+'}+F{'+str(FA[i])+'/'+str(FC[i])+'/'+str(FG[i])+'/'+str(FT[i])+'}'
    if if_invar:
        model_str_mix = model_str_mix + '}+I{' + str(invar) + '}+R' + str(n_rate) + '{' + rate_str + '};'
    else:
        model_str_mix = model_str_mix + '}+R' + str(n_rate) + '{' + rate_str + '};'
    
    with open(modelfile,'a+') as f:
        if data_name == 'l10t90_1':
            f.write('\tmodel ' + data_name + '_mf = ' + model_str_1 + '\n') 
        f.write('\tmodel ' + file_name + ' = ' + model_str_mix + '\n') 
        
with open(modelfile,'a+') as f:
    f.write('end;\n')
     