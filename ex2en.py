#Check if the entered number is even.
#Check if a number is odd, divisible by three and five at the same time, but not divisible by 10.
#Enter a number, display all its divisors.
#Enter a number, output its digits and their multipliers.
n = int(input())

#whether the entered number is even
if (n%2):
     print("Odd")
else:
     print("Even")

#is the number odd,
#is divisible by three and five at the same time,
#but so as not to divide by 10
if (not(n%2) and not(n%3) and not(n%5) and (n%10)):
     print("Yes")
else:
     print("No")

#output all its divisors
print("Fractors:")

for i in range(1,n//2+1):
     if (not(n%i)):
         print(i)

print(n)

# output its digits and their multipliers
print("Degrees:")
i = 0

while (n//10):
     d = n%10
     print(d,"*10^",i, end = " + ")
     i += 1
     n //= 10
d = n%10
print(d,"*10^",i)