from ete3 import Tree

true_treefile = r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal\trees\AA_REV.treefile'
true_treestr = open(true_treefile,'r').read()

true_tree = Tree(true_treestr,format = 1)
true_tree.unroot()
with open(r'C:\Users\u7151703\Desktop\research\RFmixture\data\mammal\trees\aa_t90_unrooted.treefile', 'w+') as result:
    result.write(true_tree.write(format = 9) + '\n')    
