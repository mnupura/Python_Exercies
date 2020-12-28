#!/usr/bin/env python
# coding: utf-8

# In[4]:


#years_list
years_list = [1984,1985,1986,1987,1988]
print('Years list:{} '.format(years_list))
print('Third birthday:{}'.format(years_list[3]))
print('Oldest year:{}'.format(years_list[-1]))


# In[12]:


#'things' list
things=['mozerella','cindrella','salmonella']
print('Things list:'.format(things))
things[1]=things[1].capitalize()
print('Name is capitalized: '+things[1])
things[0]=things[0].upper()
print('Cheezy element is in all uppercase: '+things[0])
things.pop()
things.append('Noble Prize')
print('Disease removed, new element added:{}'.format(things))


# In[53]:


#'surprise' list
surprise=['Grucho','Chico','Harpo']
print('Surprise list:{}'.format(surprise))
surprise[2]=surprise[2].lower()  #lower case the last element
print('Last element in lowercase: '+surprise[2])

surprise[2]=surprise[2][::-1]  #Reverse the string
print('Reversed string: '+surprise[2])
surprise.reverse()  #Reverse the list
surprise[0]=surprise[0].capitalize()  #Capitalize the lower case element
print('List reversed:{}'.format(surprise))


# In[56]:


#English to French (e2f) dictionary
e2f={
    "dog":"chien",
    "cat":"chat",
    "walrus":"morse"
}
print('English to French dictionary:{}'.format(e2f))
print('Walrus in French: '+e2f["walrus"])

f2e={}
#Method 1
#for animal in e2f:
#    f2e.update({e2f[animal]:animal})
#Method 2
#for an_key,an_value in e2f.items():
#    f2e[an_value]=an_key

#Method 3
for an_key,an_value in e2f.items():
    f2e.update({an_value:an_key})
    
print('French to English dictionary:{}'.format(f2e))
print('English equivalent of \'chien\':'+f2e['chien'])

print('English values from e2f keys: {}'.format(e2f.keys()))


# In[50]:


#Multilevel dictionary 'life'
life={
    'animals':{
        'cats':['Henri','Grumpy','Lucy'],
        'octopi':{},
        'emus':{}
        },
    'plants':{},
    'others':{}
    }
print('Life multilevel dictionary:{}'.format(life))
print('Toplevel:{}'.format(life.keys()))
print('Keys for life[\'animals\']: {}'.format(life['animals'].keys()))
print('Values for life[\'animals\'][\'cats\']:{}'.format(life['animals']['cats']))


# In[ ]:




