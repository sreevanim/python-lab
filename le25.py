from collections import Counter
a=list()
b=list()
n=int(input("Enter size of first list:"))
for i in range(n):
    c=input("enter strings:")
    a.append(c)
print("the first list is:",a)
n1=int(input("enter size of 2nd list:"))
for i in range(n1):
    c=input("enter strings:")
    b.append(c)
print("The 2nd list is:",b)
a[-1:]=b
print("the resultant list is :",a)
