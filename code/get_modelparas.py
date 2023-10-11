import csv 

with open(r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal\qresult.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['weight', 'AC', 'AG',  'AT', 'CG', 'CT', 'GT', 'FA', 'FC', 'FG', 'FT'])


iqtree_file = r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal\l2t90_1_q10.iqtree'

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


with open(r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal\qresult.csv','a+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    for i in range(0,10):
        csv_write.writerow([weight[i], AC[i], AG[i], AT[i], CG[i], CT[i], GT[i], FA[i], FC[i], FG[i], FT[i]])


