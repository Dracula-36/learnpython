#!/usr/bin/python3
#Filename:picking.py
import pickle
shoplistfile='shoplist.dt'
shoplist=['apple','mango','carrot']
f=open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close()
del shoplist
f=open(shoplistfile,'rb')
storedlist=pickle.load(f)
print(storedlist)
