import pandas as pd
import numpy as np
import RegexFunction
from collections import Counter

RegexFunction.one()

df = pd.read_csv("C:/Users/Administrator/Desktop/Hose_Desc_Name3_Supplier Training Data.csv")
data = [{'ProDesc':'value','Manu':'Manu Value','Word':['1','2','3'],'Attributes':[{'Hose':'Value','Pos':'0'},{'Size':'1/2','Pos':'1'}]}]

a = []
b = []
c = []
d = []
e = [] #all companies

for index, row in df.iterrows():
    row2 = row['Product Description'].split()
    if row['Supplier'] == 'Eaton':
        for i in row2:
            a.append(i)
    elif row['Supplier'] == 'Manuli':
        for i in row2:
            b.append(i)
    elif row['Supplier'] == 'Taipan':
        for i in row2:
            c.append(i)
    elif row['Supplier'] == 'Powell':
        for i in row2:
            d.append(i)

################## Count Four Company ##################
aa = Counter(a)
bb = Counter(b)
cc = Counter(c)
dd = Counter(d)


#################### Output ######################
df3 = pd.DataFrame(np.array(aa), columns = list('a'))
df2 = pd.DataFrame(np.array(bb), columns = list('b'))
df2 = pd.DataFrame(np.array(cc), columns = list('c'))
df2 = pd.DataFrame(np.array(dd), columns = list('d'))


df2.to_csv('C:/Users/Administrator/Desktop/JsonOutput.csv', sep=',')


for index, row in df.iterrows():
    row2 = row['Product Description'].split()
    for i in row2:
        e.append(i)

ee = pd.value_counts(e)

ee.to_csv('C:/Users/Administrator/Desktop/CountWords.csv', sep=',')