#python file
a=3
b=8
sum=a+b

#subarrays of an array

list=[1,2,3,4]
j=0
count=0
for i in range(len(list)):
    if i<=j:
        
        print("Hello World{",list[i],"}")
        count+=1
    j+=1
    
for i in range(0,len(list),1):
    print("Hello World {",list[i],list[i+1],"}")
    count+=1
i=0
for i in range(0,len(list),1):
    print("hello world {",list[i],list[i+1],list[i+2],"}")
    count+=1
   