#Clay Kynor
#10/4/17
#divisor - shows all the divisors of a number

num = int(input("Enter a number "))
for i in range(1,num,1):
    if num%i==0:
        print(i)

