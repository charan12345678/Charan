import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy 
import sklearn
import seaborn as sns 
import re 

print('Numpy: {}'.format(np.__version__))
print('SKLearn: {}'.format(sklearn.__version__))

dataset = pd.read_csv(r"C:\Users\charan\Desktop\NewScraping\quotetutorial\item.csv")
dataset['pname'] = dataset["product_name"]
dataset['pname']= dataset['pname'].astype(str)
dataset['xnew']=dataset['pname']
#print(dataset['pname'][15])
#xnew = re.findall(".[0-9].G......age", dataset['pname'][15])
for i in range(0,271):
    dataset['xnew'][i] = re.findall(".[0-9].G......age", dataset['pname'][i])
    i=i+1
#print(dataset['xnew'].head())

#print(dataset['xnew'].head())
dataset['battery'] = dataset["values"]
dataset['battery']= dataset['values'].astype(str)
dataset['bnew']=dataset['battery']
for j in range(0,271):
    dataset['bnew'][j] = re.findall("[0-9]{4}", dataset['battery'][j])
    j=j+1
#print(dataset['bnew'])
dataset['finalbattery'] = 0

#dataset[dataset['bnew'].map(lambda d: len(d)) > 0]
#dataset[~dataset.bnew.str.len().eq(0)]
#dataset['bnew'] = dataset['bnew'].astype(str)

'''thislist=[]
for k in range(0,271):
    thislist.append(k)
    print(thislist[k])'''



for k in range(0,14):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1

for k in range(15,53):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(57,60):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(62,82):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(84,90):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(92,95):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(97,100):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(101,110):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(111,121):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(122,134):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(138,162):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(165,173):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(178,195):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(197,202):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(206,210):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(211,219):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(225,237):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(238,243):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(244,250):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(256,259):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
for k in range(261,271):
    dataset['finalbattery'][k] = dataset['bnew'][k][-1]
    #print(dataset['finalbattery'][k])
    k=k+1
    
#print(dataset.head())
print(dataset.info())
dataset['cname'] = dataset['values']
dataset['cname']= dataset['cname'].astype(str)
dataset['camera']=0
#print(dataset['pname'][15])
#xnew = re.findall(".[0-9].G......age", dataset['pname'][15])
for i in range(0,271):
    dataset['camera'][i] = re.findall(".[0-9]MP", dataset['cname'][i])
    i=i+1
print(dataset['camera'])
print(dataset.info())
dataset['p_name'] = dataset['product_name'].astype(str)
for i in range(0,271):
    dataset['p_name'][i] = dataset['p_name'][i][0:10]
    i=i+1
dataset['product_name']= dataset['p_name']
dataset['Product_Dimensions'] = dataset['Product_Dimensions'].astype(str)
for i in range(0,271):
    dataset['Product_Dimensions'][i] = dataset['Product_Dimensions'][i][0:4]
    i=i+1
dataset['xnew'] = dataset['xnew'].astype(str)
for i in range(0,271):
    dataset['xnew'][i] = dataset['xnew'][i][0:5]
    i=i+1
for i in range(0,271):
    dataset['xnew'][i] = dataset['xnew'][i][-3:]
    i=i+1
    dataset['Storage']= 0
for i in range(0,271):
    dataset['Storage']= dataset['xnew']
    i=i+1
dataset.drop(['OS','Battery_Power_Rating','battery','bnew','cname','p_name','values','pname','xnew','product_name'],axis=1,inplace=True)
dataset['camera'] = dataset['camera'].astype(str)
for i in range(0,271):
    dataset['camera'][i] = dataset['camera'][i][0:4]
    i=i+1
for i in range(0,271):
    dataset['camera'][i] = dataset['camera'][i][-2:]
    i=i+1 
for i in range(0,271):
    dataset['RAM'][i] = dataset['RAM'][i][0:2]
    i=i+1
dataset['price']= dataset['price'].str.strip('₹')
dataset['Product_Dimensions']= dataset['Product_Dimensions'].str.strip('x')
dataset['price']= dataset['price'].str.replace(',','')
dataset['price']= dataset['price'].str.replace(' ','')

#dataset = dataset.dropna(how='any',axis=0)
dataset['camera'] = dataset['camera'].str.replace('[','')
dataset['camera'] = dataset['camera'].str.replace(']','0')
dataset['camera'] = dataset['camera'].str.replace(',','')
dataset['camera'] = dataset['camera'].astype(int)
dataset = dataset.dropna(how='any',axis=0)
dataset = dataset[['Product_Dimensions','RAM','camera','finalbattery','Storage','price']]
print(dataset)  
#dataset.to_csv("newitem1.csv")



