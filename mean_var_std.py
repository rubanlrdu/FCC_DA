import numpy as np
def calculate(d):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  result={}
  Mean1=d.mean(axis=0)
  Mean2=d.mean(axis=1)
  Mean=np.mean(d)
  Mlist=[Mean1,Mean2,Mean]
  result['mean']=Mlist
  Var1=d.var(axis=0)
  Var2=d.var(axis=1)
  Var=d.var()
  Vlist=[Var1,Var1,Var]
  result['Variance']=Vlist
  SD1=d.std(axis=0)
  SD2=d.std(axis=1)
  SD=np.std(d)
  SDList=[SD1,SD2,SD]
  Max1=d.max(axis=0)
  Max2=d.max(axis=1)
  Max=c.max()
  MList=[Max1,Max2,Max]
  result['Max']=MList
  Min1=d.min(axis=0)
  Min2=d.min(axis=1)
  Min=c.min()
  MinList=[Min1,Min2,Min]
  result["Min"]=MinList
  Sum1=d.sum(axis=0)
  Sum2=d.sum(axis=1)
  Sum=d.sum()
  result["Sum"]=[Sum1,Sum2,Sum]
  return result
a=[]
for i in range(9):
  temp=int(input("enter value " + str(i+1) + ": "))
  a.append(temp)
b=np.array(a)
c=b.reshape(3,3)
print(calculate(c))
