#!/usr/bin/env python
# coding: utf-8

# In[6]:


fruitstuple=("Banana","Mango","Apple","Orange","Grapes")
print("Original Tuple:")
print(fruitstuple)

#Modify each to have 'first alphabet for fruit name'#
flist=[]
FRUIT_CONV_STR="{} for {}"
for fruit in fruitstuple:
    flist.append(FRUIT_CONV_STR.format(fruit[0],fruit))
fruitstuple=tuple(flist)
print("\nModify with first alphabet: ") 
print(fruitstuple)

#Display alphabetically. on separate line
flist.sort()
fruitstuple=tuple(flist)
cnt=0
print("\nDisplay alphabetically on separate line:")
for x in fruitstuple:
    print(x)

#String variable called 'all_fruits' with all fruit names
fruitstuple=("Banana","Mango","Apple","Orange","Grapes")
all_fruits="--".join(fruitstuple)
print(all_fruits)


# In[7]:


#Nested for
fruits_tuple=("Banana","Mango")
for fruit in fruits_tuple:
    for element in fruit:
        print(element)


# In[3]:





# In[ ]:




