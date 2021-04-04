#count the even and oddd numbers in the list
lst=[]
k=0
l=0
m=0
n=int(input())
for i in range(n):
	k=int(input())
	lst.append(k)
for i in range(n):
	if(lst[i]%2==0):
		l=l+1
	else:
		m=m+1
print(l,'\n',m)
#to find whether the given no in the list is prime or not
lst=[]
l=0
n=int(input())
for i in range(n):
	k=int(input())
	lst.append(k)
for i in range(n):
	for j in range(2,lst[i]):
		if(lst[i]%j==0):
		    l=l+1
		    print('NO')
		    break
	if(l==0):
		print("Yes")
	l=0

#selection sort
lst=[]
n=int(input())
l=1
for i in range(n):
	k=int(input())
	lst.append(k)
for j in range(n):
    min=lst[j]
    for i in range(j+1,n):
        if(lst[i]<lst[j]):
	        lst[j],lst[i]=lst[i],lst[j]
l+=1
for i in range(n):
	print(lst[i],end=" ")

#print largest and smallest in the list
lst=[]
n=int(input())
for i in range(n):
	k=int(input())
	lst.append(k)
max=lst[0]
min=lst[0]
for i in range(n):
    if(max<lst[i]):
        max=lst[i]
    if(min>lst[i]):
        min=lst[i]
	
print(max,'\n',min)
#finding the second largest value
lst=[]
temp=0
n=int(input())
for i in range(n):
    k=int(input())
    lst.append(k)
min=lst[0]
for i in range(n):
    if(min<lst[i]):
        temp=min
        min=lst[i]
		
print(temp)