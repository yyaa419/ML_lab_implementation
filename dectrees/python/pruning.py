import dtree as d
import monkdata as m
import random
import drawtree_qt5 as q

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

monk1_train, monk1_validation=partition(m.monk1,0.2)
tree=d.buildTree(monk1_train,m.attributes)
#for all the prunched trees
while True:
    flag=True
    alternatives=d.allPruned(tree)
    for tree_prunched in alternatives:
        error_origin=1-d.check(tree,monk1_validation)
        error_prunched=1-d.check(tree_prunched,monk1_validation)
        if(error_prunched>=error_origin):
            flag=False
            break
        else:
            tree=tree_prunched
    if(flag==False):
        #which means the tree stops prunching and has found the best decision model
        print(1-d.check(tree,m.monk1test))
        break

q.drawTree(tree)