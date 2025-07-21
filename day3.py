#print a start pattern like:
#if n=3
#  *
# ***
#*****
a=int(input("enter the num "))
k=a-1
for i in range(1,a+1,1):
    b=(2*i)-1
    for j in range(0,k,1):
       print(" ",end="")
    for m in range(0,b,1):  
       print("*",end ="") 
    k=k-1
    print("")
 
    
