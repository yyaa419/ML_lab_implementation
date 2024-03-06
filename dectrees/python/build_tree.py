import monkdata as m
import dtree as d

#divide monk1 into two subsets according to condition that whether a5=1
subset1=d.select(m.monk1,m.attributes[4],1)
subset2=list(set(m.monk1).difference(subset1))


#compute the information gains for the nodes on the next level
print(d.averageGain(subset1,m.attributes[0]))
print(d.averageGain(subset1,m.attributes[1]))
print(d.averageGain(subset1,m.attributes[2]))
print(d.averageGain(subset1,m.attributes[3]))
print(d.averageGain(subset1,m.attributes[4]))
print(d.averageGain(subset1,m.attributes[5]))

print(d.averageGain(subset2,m.attributes[0]))
print(d.averageGain(subset2,m.attributes[1]))
print(d.averageGain(subset2,m.attributes[2]))
print(d.averageGain(subset2,m.attributes[3]))
print(d.averageGain(subset2,m.attributes[4]))
print(d.averageGain(subset2,m.attributes[5]))

print(d.mostCommon(subset1))
print(d.mostCommon(subset2))

tree1=d.buildTree(m.monk1,m.attributes)
print("E_train for Monk1",1-d.check(tree1,m.monk1))
print("E_test for Monk1",1-d.check(tree1,m.monk1test))

tree2=d.buildTree(m.monk2,m.attributes)
print("E_train for Monk2",1-d.check(tree2,m.monk2))
print("E_test for Monk2",1-d.check(tree2,m.monk2test))

tree3=d.buildTree(m.monk3,m.attributes)
print("E_train for Monk3",1-d.check(tree3,m.monk3))
print("E_test for Monk3",1-d.check(tree3,m.monk3test))