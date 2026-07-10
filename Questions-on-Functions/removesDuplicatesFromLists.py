#Remove duplicates from a list
lst=[1,1,2,3,3,4,5]
unique=[]

for i in lst:
    if i not in unique:
        unique.append(i)
    
print(unique)