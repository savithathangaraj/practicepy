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
n=int(input())
for i in range(n):
	k=int(input())
	lst.append(k)
for i in range(n):
	for j in range(1,i):
		if(i%j==0):
			print('NO')
		else:
			print("Yes")
