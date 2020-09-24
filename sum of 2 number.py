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

# iterating 2 list in same time and returning as list
 c=0
    d=0
    for (i,j) in zip(a,b):
        if i>j:
            c+=1
        elif i<j:
            d+=1
        else:
            pass
    e=[c,d]
    # e[0]=c
    # e[1]=d

    return e

    # absolute sum of diagonals of a matrics
    def diagonalDifference(arr):
    # Write your code here
    sum1=0
    sum2=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i==j:
                sum1=sum1+arr[i][j]
                
                
    j=len(arr)
    
    for i in range(0,len(arr)):
        for j in range((len(arr)-1),-1,-1):
            if ((i+j)==(len(arr)-1)):
                sum2=sum2+arr[i][j]
                
                
    s=abs(sum1-sum2)
    return s
#printing number with 6 decimal digits
def plusMinus(arr):
    c=0
    d=0
    e=0
    for i in arr:
        if i>0:
            c+=1
        elif i<0:
            d+=1
        else:
            e+=1
    g=len(arr)
    
    print("{:.6f}".format(c/g))
    print("{:.6f}".format(d/g))
    print("{:.6f}".format(e/g))

