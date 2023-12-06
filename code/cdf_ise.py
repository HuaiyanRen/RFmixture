import csv 


def ise(file_name1, file_name2):
    file1 = file_name1 + '.iqtree'
    file2 = file_name2 + '.iqtree'
    
    with open(file1) as b:
        for line in b.readlines():
            if 'Mixture model of substitution:' in line:
                classes1 = line.count(',') + 1
                
    with open(file2) as b:
        for line in b.readlines():
            if 'Mixture model of substitution:' in line:
                classes2 = line.count(',') + 1
                
    r_list1 = []
    f_list1 = []
    w_list1 = []
    
    with open(file1) as b:
        for line in b.readlines():
            for i in range(0,classes1):              
                if str(i+1) + '  GTR' in line:
                    r = []
                    f = []
                    w_list1.append(float(line.split()[-2]))
                    gtr_all = line.split()[-1]
                    gtr_list = gtr_all.split(',')
                    r.append(float(gtr_list[0].split('{')[1]))
                    r.append(float(gtr_list[1]))
                    r.append(float(gtr_list[2]))
                    r.append(float(gtr_list[3]))
                    r.append(float(gtr_list[4].split('}')[0]))
                    r.append(1)
                    f.append(float(gtr_list[4].split('{')[1]))
                    f.append(float(gtr_list[5]))
                    f.append(float(gtr_list[6]))
                    f.append(float(gtr_list[7].split('}')[0]))
                    r_list1.append(r)
                    f_list1.append(f)
                    
    w_list1 = [n/sum(w_list1) for n in w_list1]
            
    for i in range(0, classes1):
        deno1 = sum(r_list1[i])
        r_list1[i] = [n/deno1 for n in r_list1[i]]
        
    r_list2 = []
    f_list2 = []
    w_list2 = []
    
    with open(file2) as b:
        for line in b.readlines():
            for i in range(0,classes2):              
                if str(i+1) + '  GTR' in line:
                    r = []
                    f = []
                    w_list2.append(float(line.split()[-2]))
                    gtr_all = line.split()[-1]
                    gtr_list = gtr_all.split(',')
                    r.append(float(gtr_list[0].split('{')[1]))
                    r.append(float(gtr_list[1]))
                    r.append(float(gtr_list[2]))
                    r.append(float(gtr_list[3]))
                    r.append(float(gtr_list[4].split('}')[0]))
                    r.append(1)
                    f.append(float(gtr_list[4].split('{')[1]))
                    f.append(float(gtr_list[5]))
                    f.append(float(gtr_list[6]))
                    f.append(float(gtr_list[7].split('}')[0]))
                    r_list2.append(r)
                    f_list2.append(f)
                    
    w_list2 = [n/sum(w_list2) for n in w_list2]
            
    for i in range(0, classes2):
        deno2 = sum(r_list2[i])
        r_list2[i] = [n/deno2 for n in r_list2[i]]    
        
        
    addendq_1 = 0
    addendq_2 = 0
    addendq_3 = 0
    addendf_1 = 0
    addendf_2 = 0
    addendf_3 = 0
    for c1 in range(classes1):
        for c2 in range(classes1):
                
            factorq = w_list1[c1]*w_list1[c2]
            for qi in range(6):
                factorq = factorq*(1-max([r_list1[c1][qi],r_list1[c2][qi]]))
            addendq_1 = addendq_1 + factorq
                
            factorf = w_list1[c1]*w_list1[c2]
            for fi in range(4):
                factorf = factorf*(1-max([f_list1[c1][fi],f_list1[c2][fi]]))
            addendf_1 = addendf_1 + factorf
               
    for c1 in range(classes1):
        for c2 in range(classes2):
            
            factorq = w_list1[c1]*w_list2[c2]
            for qi in range(6):
                factorq = factorq*(1-max([r_list1[c1][qi],r_list2[c2][qi]]))             
            addendq_2 = addendq_2 + factorq
        
            factorf = w_list1[c1]*w_list2[c2]
            for fi in range(4):                    
                factorf = factorf*(1-max([f_list1[c1][fi],f_list2[c2][fi]]))
            addendf_2 = addendf_2 + factorf
                
    for c1 in range(classes2):
        for c2 in range(classes2):
                
            factorq = w_list2[c1]*w_list2[c2]
            for qi in range(6):
                factorq = factorq*(1-max([r_list2[c1][qi],r_list2[c2][qi]]))
            addendq_3 = addendq_3 + factorq
        
            factorf = w_list2[c1]*w_list2[c2]
            for fi in range(4):
                factorf = factorf*(1-max([f_list2[c1][fi],f_list2[c2][fi]]))
            addendf_3 = addendf_3 + factorf
                 
    ise_q = addendq_1 - 2*addendq_2 + addendq_3
    ise_f = addendf_1 - 2*addendf_2 + addendf_3
            
    return ise_q, ise_f     


with open('ise.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['model1', 'model2',  'ise_r', 'ise_f'])
                       
        
file_list = ['l2t50_1_q5_1', 'l2t50_1_q5_2', 'l2t50_1_q5_3', 'l2t50_1_q5_4', 'l2t50_1_q5_5',
             'l2t50_1_q5_6', 'l2t50_1_q5_7', 'l2t50_1_q5_8', 'l2t50_1_q5_9', 'l2t50_1_q5_10', ]
for i in range(0, len(file_list)):
    for j in range(i, len(file_list)):
        file1 = file_list[i]  
        file2 = file_list[j]         
        ise_r, ise_f = ise(file1, file2)
        result_row = [file1, file2, ise_r, ise_f]
        
        with open('ise.csv','a+',newline='') as csvf:
            csv_write = csv.writer(csvf)
            csv_write.writerow(result_row)
        





























        
        
                    