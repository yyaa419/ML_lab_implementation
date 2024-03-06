import dtree as d
import monkdata as m

#used to calculate the information gain of dataset
print("information gain of monk1 a1",d.averageGain(m.monk1,m.attributes[0]))
print("information gain of monk1 a2",d.averageGain(m.monk1,m.attributes[1]))
print("information gain of monk1 a3",d.averageGain(m.monk1,m.attributes[2]))
print("information gain of monk1 a4",d.averageGain(m.monk1,m.attributes[3]))
print("information gain of monk1 a5",d.averageGain(m.monk1,m.attributes[4]))
print("information gain of monk1 a6",d.averageGain(m.monk1,m.attributes[5]))

print("information gain of monk2 a1",d.averageGain(m.monk2,m.attributes[0]))
print("information gain of monk2 a2",d.averageGain(m.monk2,m.attributes[1]))
print("information gain of monk2 a3",d.averageGain(m.monk2,m.attributes[2]))
print("information gain of monk2 a4",d.averageGain(m.monk2,m.attributes[3]))
print("information gain of monk2 a5",d.averageGain(m.monk2,m.attributes[4]))
print("information gain of monk2 a6",d.averageGain(m.monk2,m.attributes[5]))

print("information gain of monk3 a1",d.averageGain(m.monk3,m.attributes[0]))
print("information gain of monk3 a2",d.averageGain(m.monk3,m.attributes[1]))
print("information gain of monk3 a3",d.averageGain(m.monk3,m.attributes[2]))
print("information gain of monk3 a4",d.averageGain(m.monk3,m.attributes[3]))
print("information gain of monk3 a5",d.averageGain(m.monk3,m.attributes[4]))
print("information gain of monk3 a6",d.averageGain(m.monk3,m.attributes[5]))