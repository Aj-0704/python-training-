#1.Write a python program to create and print a dictionary which stores your information. 
d={'Name': 'Agam', 'Age': 20, 'Gender':'Male'}
print(d)

#2.Write a python program to access the items of a dictionary by referring to its key 
d={'Name': 'Agam', 'Age': 20 , 'Gender':'Male'}
print(d['Name'])
print(d['Age'])
print(d['Gender'])

#3.Write a python program to get a list of the values from a dictionary. 
for item in d:
    print(item,d[item], sep=' , ')

#4.Write a python program to change the value of a specific item by referring to its key name. 
d1 = {'Name': "Agam jain", 'Age': 20, 'Gender': "male"} 
d1 ['Name'] = "Agam jain"
print(d1) 

#.5.Write a python program to print all key names in the dictionary, one by one.
d1 = {'Name': "agam jain", 'Age': 20, 'Gender': "male"} 
for key in d1: print(key)

#6.Write a python program to create a dictionary that contains three dictionaries. (nested) 
d1 = {   100: {101: 'agam', 102: 'ananya', 103: 'kanishk'},   200: {201: 'ruchika', 202: 'yogesh', 203: 'savi'}, 
  300: {301: 'aman', 302: 'abhishek', 303: 'manu'} } 
print(d1[100],d1[200],d1[300],sep='\n') 

#7.. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries. 
d1 = {'Name': "agam", 'Age': 20, 'Gender': "Male"} 
d2 = {'Name': "ananya", 'Age': 21, 'Gender': "female"} 
d3 = {'Name': "abhishek", 'Age': 19, 'Gender': "Male"} 
d4 = { 1:{'Name': "manu", 'Age': 19, 'Gender': "Male"}, 
       2:{'Name': "ananya", 'Age': 21, 'Gender': "female"}, 
       3:{'Name': "abhishek", 'Age': 19, 'Gender': "Male"} } 
print(d1,d2,d3,d4,sep='\n') 

#8.. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value. 
L1 = [100, 101, 102, 103] 
L2 = ['agam', 'ananya', 'abhishek', 'manu']
d1 = {} 
x = 0 
while x < len(L1):    
    d1[L1[x]] = L2[x]   
    x += 1 
for item in d1: 
   print(item, d1[item], sep=' = ')

#9.Write a python program to merge two python dictionaries into one dictionary. 
d1 = {100: 'agam', 101: 'ananya'} 
d2 = {102: 'abhishek', 103: 'manu'} 
d1.update(d2) 
print(d1) 

#10.Write a python program to get the key of lowest value from the dictionary. 
sample_dict = { 'C': 92, 'Java': 66, 'Python': 85 } 
sample_dict = {'C': 92,'Java': 66,'Python': 85} 
print(min(sample_dict.values())) 


