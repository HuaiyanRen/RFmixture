from ete3 import Tree
import csv

with open(r'C:\Users\u7151703\Desktop\research\RFmixture\taxa_list.csv', 'r') as charsets:
    reader = csv.reader(charsets)
    t50_1 = []
    t50_2 = []
    t25_1 = []
    t25_2 = []
    for row in reader:
        t50_1.append(row[1])
        t50_2.append(row[2])
        t25_1.append(row[3])
        t25_2.append(row[4])

t50_1 = [s.strip() for s in t50_1 if s != '']
t50_2 = [s.strip() for s in t50_2 if s != '']
t25_1 = [s.strip() for s in t25_1 if s != '']
t25_2 = [s.strip() for s in t25_2 if s != '']

true_treefile = r'C:\Users\u7151703\Desktop\research\AA_REV.treefile'
true_treestr = open(true_treefile,'r').read()

true_tree = Tree(true_treestr,format = 1)
with open(r'C:\Users\u7151703\Desktop\research\aa_t90.treefile', 'w+') as result:
    result.write(true_tree.write(format = 9) + '\n')    
    
true_tree = Tree(true_treestr,format = 1)
true_tree.prune(set(t50_1))
with open(r'C:\Users\u7151703\Desktop\research\aa_t50_1.treefile', 'w+') as result:
    result.write(true_tree.write(format = 9) + '\n')    
    
true_tree = Tree(true_treestr,format = 1)
true_tree.prune(set(t50_2))
with open(r'C:\Users\u7151703\Desktop\research\aa_t50_2.treefile', 'w+') as result:
    result.write(true_tree.write(format = 9) + '\n')  
 
true_tree = Tree(true_treestr,format = 1)
true_tree.prune(set(t25_1))
with open(r'C:\Users\u7151703\Desktop\research\aa_t25_1.treefile', 'w+') as result:
    result.write(true_tree.write(format = 9) + '\n')      
    
true_tree = Tree(true_treestr,format = 1)
true_tree.prune(set(t25_2))
with open(r'C:\Users\u7151703\Desktop\research\aa_t25_2.treefile', 'w+') as result:
    result.write(true_tree.write(format = 9) + '\n')  
