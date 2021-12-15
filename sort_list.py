#without inbuilt function
list=[1,6,4,9,3,7]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)