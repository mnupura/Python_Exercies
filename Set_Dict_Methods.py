#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Dictionary methods
newdict={
    "Brand":"Nike",
    "Shoesize":5,
    "Colour":["black","blue","red"]
}
print('Length of dictionary: {}'.format(len(newdict)))
print('Type of dictionary: {}'.format(type(newdict)))

x=newdict.get("Shoesize")
print('Get funct:{}'.format(x))
y=newdict["Brand"]
print('Value by assignment: {}'.format(y))

key=newdict.keys()
print(key) #Returns the list of keys in that dictionary
newdict["Tshirtsize"]=40
print(key)

print(newdict.keys()) #Returns the keys
print(newdict.values()) #Returns the values
print(newdict.items()) #Returns the items

newdict.update({"Shoesize":7}) #Update item
print(newdict["Shoesize"])


# In[1]:


#Dictionaries small assignment
fruit_basket=['Mango','Apple','Banana','Kiwi','Mango','Banana','Orange','Guava','Guava']
fruit_dict={}

for fruit in fruit_basket:
    if fruit in fruit_dict:
        cnt=fruit_dict[fruit]
        fruit_dict.update({fruit:cnt+1})
    else:
        fruit_dict[fruit]=1

for fruit in fruit_dict: #Method 1
    print('There are {} {}'.format(fruit_dict[fruit],fruit))
    
for fruit,count in fruit_dict.items(): #Method 2
    print('There are {} {}'.format(count,fruit))

fruit_group={}
for fruit in fruit_dict:
    count=fruit_dict[fruit]
    if count in fruit_group:
        fruit_group[count].append(fruit)
    else:
        fruit_group[count]=[fruit]
for number in fruit_group:
    print('There are {} each of {}'.format(number,fruit_group[number]))


# In[32]:


#Set methods
new_list=[1,2,3,1,2,"A","B","A"]
new_set=set(new_list)
print(new_set)
new_set.add(1) #Does not allows to add duplicate item
print(new_set)

myset=["@","#"]
new_set.update(myset) #update current set. It can be updated by list,tuple or set
print(new_set)

set1={'T','E'}
set2=new_set.union(set1) #returns a new set with all items with both sets
print(set2)


# In[ ]:




