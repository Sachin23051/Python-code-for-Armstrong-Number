n= int(input("Enter the number : "))
order = len(str(n))
copy_n=n
sum=0
while(n>0):
    digit=n%10
    sum+=digit**order
    n=n//10
if (sum==copy_n):
    print("Number is Armstrong ")
else:
    print("Number is  not Armstrong ")