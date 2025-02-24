def percent (marks):
    p = ((marks[0]+marks[1]+marks[3]+marks[4])/400)*100
    return p

marks2 = [45, 77,93,61]
percentage2 =(marks2)

print(percentage,percentage2)





def greet(name="stranger"):
    print("good day,"+name)
  
def mysum(no1 , no2):
    return no1 +no2
greet("sneha")
greet()  
s = mysum(6,32)
print(s)



n = 1
product = 1
for i in range(n):
    product = product * (i+1)
print(product)


def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product *(i+1)
    return product
def factorial_recursive(n):
    if n == 1 or n ==0:
        return 1
    return n*factorial_recursive(n-1)

f = factorial_iter(n)
f = factorial_recursive(5)
print(f)







def max(no1,no2,no3):
    if(no1>no2):
        if(no1>no3):
            return no1
        else:
            return no3
    else:
        if(no2>no3):
            return no2
        else:
            return no3     

m = max  (3,6,88) 
print("the value of max is "+str(m))





def far(cel):
    return  (Cel * (9/5)) + 32

c = 45
f = far(c)
print("farenhite temperature is" +str(f))




def cm(inch):
    return 2.54 *(inch)

i = 45
c = cm(i)
print("inches is cm is" +str(c))



print("hello", end="")
print("how", end="")
print("are", end="")
print("you?", end="")



n = 6
for i in range(n):
    print("*"*(n-i))




def remove_and_split(string,word):
        newstr = string.replace(word,"")
        return newstr.split()
this ="    sneha is very good    "
remove_and_split(this,"very")
print(n)
# print(this.strip())