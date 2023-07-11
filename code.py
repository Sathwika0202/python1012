# python1012

# sum of two numbers
a=int(input("value of a: "))
b=int(input("value of b: "))
sum=a+b
print("sum is: ", sum)

# python program to print name
name="sathwika"
print(name)

# python program to check the number is even or odd.
a=int(input("enter the value: "))
if (a%2==0);
   print("the number is even")
else;
   print("the given number is odd")

# python program to get a number and reverse the number    
a=int(input("enter a number: "))
b=0
c=1
while (a!=0);
   b=a%10
   c=c*10+b
   a//=10
print("reversed number is: ", c)

# python program to generate n odd numbers between 1 to n.
n=int(input("enter n value: "))
for i in range (0,n+1);
   if(i%2==1);
      print(i,end+" ")

# Write a python program to compute the value for the series
n=int(input("enter n value: "))
x=int(input("enter x value: "))
sum=0
i=0
while(i<=n);
   sum=sum+(x**i)
   i++
   print(sum)

#   Print characters from a string that are present at odd index number.
a="computerscience"
print(a)
for i in range(0,int(a),2);
   print(a[i],end=" ")
   
