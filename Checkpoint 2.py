#!/usr/bin/env python
# coding: utf-8

# In[7]:


a=input("Entrez vôtre nom ") 
b=input("Entrez vôtre prénom ") 
print(a) 
print(b)
    


# In[1]:


#Write a program that will find all numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200 (both included). The numbers obtained should be printed in a list.

r1 = range(2000,3200)
 
list=[]
for i in r1:
   if i%7==0 and i%5!=0:
       list.append(i)
        
print(list)        

       
       


# In[2]:


#Algorithme Paire/Impaire
a=int(input("Donnez un numéro ") )
if a%2==0 :
   print (" Le nombre est paire ")
else :
   print (" Le nombre est impaire ")


# In[ ]:


#Algorithme factoriel avec for
a=int(input("donnez un numéro "))
if a==0 :
        print(" Le factoriel du nombre est : ",1)
else :
        x=1 
        for i in range(1,a+1) :
            x=x*i 
print(x)


# In[32]:


#Algorithme factoriel avec While
a=int(input("donnez un numéro "))
x=1 
while 1<=a :
        x=x*(a)
        a=a-1
print(x)


# In[129]:


#Programme supprimant la lettre se trouvant à une position k donnée par l'utilisateur
ch=input ("Donnez une phrase ou un mot : ")
n=input("Donnez la position de la lettre que vous voulez enlever : ")
n=int(n)
ch1=""
ch2=""
for i in range(0,n):
    ch1=ch1+ ch[i]
for i in range(n+1,len(ch)):
    ch1=ch1+ ch[i]

print("Le nouveau mot est: " , ch1)
      


# In[130]:


n=input("Donnez la position de la lettre que vous voulez enlever : ")
a=len(ch)
for i in range(n):
    Newch=Newch+ch[i]


print(Newch)
        


# In[37]:



MyDict={}
n=int(input("donnez un nombre ")) 
for i in range(1,n+1) :
    MyDict[i]= i*i  #adding new element (new key and new value)
MyDict


# In[55]:


#Programme permettant de calculer d'articles Soldés
a=int(input("Donnez un nombre "))

if a>500 :
    a=a-(0.5)*a 
    print("Le nouveau prix est",a)
elif a>200 and a<500
    a=a-(0.3)*a
    print("Le nouveau prix est",a)
else  :
    a=a-(0.1)*a
    print("Le nouveau prix est",a)


# In[74]:


import numpy as np 
List=[]
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(0,3) :
    for j in range(0,3):
        List.append(a[i,j])
print(List)

        


# In[99]:


#Programme permettant d'entrée un vecteur , le transformer en Matrice puis en liste 

import array as arr
import numpy as np 

a = arr.array('i', [])
k = int(input("Entrée la taille de vôtre vecteur: "))

for i in range(0, k):
    num = int(input("Entrez l'élément %d du vecteur :" %(i + 1))) # Demander les valeurs du vecteur à l'utilisateur
    a.append(num)
    
m, n = input("Donnez la taille de vôtre Matrice mxn").split() #Taille de la matrice
m=int(m)
n=int(n)

A=np.reshape(a,(m,n))
l = A.tolist()
print(l)
    


# In[101]:


#Transformation d'une matrice en liste
a=np.array([[1,2,3,4],[5,6,7,8]])
l = a.tolist()
print(l)


# In[133]:



import math 
Q=[]
D=input("Donnez les valeurs de D ").split(",")
a=len(D)

for i in range(0,a):
    Q.append(round(math.sqrt(10*int(D[i])/3)))
    
print(Q)




# In[135]:


#NumPy program to compute the covariance matrix of two given arrays.
import numpy as np
a=np.array([[0,1,2]])
b=np.array([[2,1,0]])
np.cov(a,b)


# In[ ]:




