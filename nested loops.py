#activity 1
string = input("please enter your own word:")
char = input("please enter your own character")
i = 0
count = 0
while(i < len(string)):
    
    if(string[i]== char):
        count = count + 1
    i = i+1
    
print("the total number of times", char,"has occured =",count)

#activity 2
lower = int(input("enter a lower range:"))
upper = int(input("enter a upper range:"))

print ("prime numbers between",lower,"and",upper,"are:")
for num in range(lower, upper +1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)
                
#activity 3
num = int(input("enter the number:"))
t = num
numlen = 0
while t > 0:
    numlen = numlen + 1
    t = int(t/10)
    
if numlen >= 4:
    numlen = int(numlen/2)
    chk = 0
    while num > 0:
        rem = num%10
        if chk == numlen:
            midOne = rem
        elif chk == (numlen-1):
            midTow = rem
        num = int(num/10)
        chk = chk+1
    prod = midOne*midTow
    print("\n product of mid digits("+str(midOne)+ "*"+str (midTow)+")=",prod)
    
else:
    print("\n it's not a 4 or more than 4-digit number")