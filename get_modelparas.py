import csv 
import numpy as np
import os

with open(r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal\qresult.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['weight', 'AC', 'AG',  'AT', 'CG', 'CT', 'GT', 'FA', 'FC', 'FG', 'FT'])


iqtree_file = r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal\l10t90_1_q10.iqtree'

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
        for i in range(0,10):
            if str(i) + '  GTR' in line:
                weight.append(float(line.split()[-2]))
                gtr_all = line.split()[-1]
                gtr_list = gtr_all.split(',')
                true_q[i][0] = float(gtr_list[0].split('{')[1])
                true_q[i][1] = float(gtr_list[1])
                true_q[i][2] = float(gtr_list[2])
                true_q[i][3] = float(gtr_list[3])
                true_q[i][4] = float(gtr_list[4].split('}')[0])
                true_f[i][0] = float(gtr_list[4].split('{')[1])
                true_f[i][1] = float(gtr_list[5])
                true_f[i][2] = float(gtr_list[6])
                true_f[i][3] = float(gtr_list[7].split('}')[0])