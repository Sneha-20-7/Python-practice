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