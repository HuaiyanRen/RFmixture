import pandas as pd
import os

data_list = ['l1t90_1','l1t90_2','l2t90_1','l2t90_2','l5t90_1','l10t90_1','l10t90_2']

classes = 10
path = r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal'
modelfile =  os.path.join(path, 'modelfile.nex')

with open(modelfile,'w+') as f:
    f.write('#nexus' + '\n' + 'begin models;' + '\n') 

for data_name in data_list:
    file_name = data_name + '_q' + str(classes) 
    full_file_name = os.path.join(path, file_name + '.xlsx')
    
    model_df = pd.read_excel(full_file_name)
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
    
    model_str ='MIX{'
    for i in range(int(classes)):
        if i == 0:
            model_str = model_str + 'GTR{'+str(AC[i])+'/'+str(AG[i]) +'/'+str(AT[i])+'/'+str(CG[i])+'/'+str(CT[i])+'}+F{'+str(FA[i])+'/'+str(FC[i])+'/'+str(FG[i])+'/'+str(FT[i])+'}'
        else:
            model_str = model_str + ',GTR{'+str(AC[i])+'/'+str(AG[i]) +'/'+str(AT[i])+'/'+str(CG[i])+'/'+str(CT[i])+'}+F{'+str(FA[i])+'/'+str(FC[i])+'/'+str(FG[i])+'/'+str(FT[i])+'}'
    model_str = model_str + '}+'
    
    with open(modelfile,'a+') as f:
        f.write('\tmodel ' + file_name + ' = ' + model_str + ';\n') 
        
with open(modelfile,'a+') as f:
    f.write('end;\n')
     