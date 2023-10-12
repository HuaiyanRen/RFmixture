import pandas as pd
import os

data_name = 'l2t90_1'
classes = 10
file_name = data_name + '_q' + str(classes) 
path = r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal'


iqtree_file = os.path.join(path, file_name + '.iqtree')

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
        for i in range(0,classes):
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


df = pd.DataFrame({
    'data': [data_name]*classes,
    'class': list(range(1,11)),
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

xlsx_file = os.path.join(path, file_name + '.xlsx')
df.to_excel(xlsx_file, index=False, engine='openpyxl')

