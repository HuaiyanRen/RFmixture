import pandas as pd
import os

classes = [5]
org = ['bfgs']
initi = [1,2]
dataset = [1,2]
rep = [1,2,3,4,5]

data_list = []
for c in classes:
    for o in org:
        for i in initi:
            for d in dataset:
                for r in rep:
                    data_list.append([c, o, i, d, r])

df = pd.DataFrame({
    'data': [],
    'class': [],
    'weight': [],
    'AC': [],
    'AG': [],  
    'AT': [], 
    'CG': [], 
    'CT': [], 
    'GT': [], 
    'FA': [], 
    'FC': [], 
    'FG': [], 
    'FT': []
})
path = r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal_rep'
xlsx_file = os.path.join(path, 'para.xlsx')


for iqfile in data_list:
    file_name = 'q'+str(iqfile[0]) + '_' + iqfile[1] + str(iqfile[2]) + '_d' + str(iqfile[3]) + '_rep' + str(iqfile[4])
    path = r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal_rep'
        
    iqtree_file = os.path.join(path, file_name + '.iqtree')
    if not os.path.exists(iqtree_file):
        continue
    
    weight = []
    AC = []
    AG = []
    AT = []
    CG = []
    CT = []
    GT = []
    FA = []
    FC = []
    FG = []
    FT = []
    
    with open(iqtree_file) as b:
        for line in b.readlines():
            for i in range(1,iqfile[0]+1):
                if str(i) + '  GTR' in line:
                    weight.append(float(line.split()[-2]))
                    gtr_all = line.split()[-1]
                    gtr_list = gtr_all.split(',')
                    AC.append(float(gtr_list[0].split('{')[1]))
                    AG.append(float(gtr_list[1]))
                    AT.append(float(gtr_list[2]))
                    CG.append(float(gtr_list[3]))
                    CT.append(float(gtr_list[4].split('}')[0]))
                    GT.append(1)
                    FA.append(float(gtr_list[4].split('{')[1]))
                    FC.append(float(gtr_list[5]))
                    FG.append(float(gtr_list[6]))
                    FT.append(float(gtr_list[7].split('}')[0]))
    
    
    df1 = pd.DataFrame({
        'data': [file_name]*iqfile[0],
        'class': list(range(1,iqfile[0]+1)),
        'weight': weight,
        'AC': AC,
        'AG': AG,  
        'AT': AT, 
        'CG': CG, 
        'CT': CT, 
        'GT': GT, 
        'FA': FA, 
        'FC': FC, 
        'FG': FG, 
        'FT': FT
    })
    
    df = pd.concat([df, df1], ignore_index=True)

df.to_excel(xlsx_file, index=False, engine='openpyxl')

