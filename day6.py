a = 45
if(a>3) :
    print("the value of a is greater than 3")
elif(a>7):
    print("the value of a is greater than 7")
elif(a>17):
    print("the value of a is greater than 17")
else :
    print("the value is not greater than 3 or 7")


    #multiple if statement
if(a>3) :
    print("the value of a is greater than 3")
elif(a>7):
    print("the value of a is greater than 7")
elif(a>17):
    print("the value of a is greater than 17")
else :
    print("the value is not greater than 3 or 7")


age =int(input("enter your age"))
if age>18:
    print("yes")
else:
    print("no")


age = int(input("enter your age"))
if(age>34 and age<56):
    print("you can work with us")

age = int(input("enter your age"))
if(age>34 or age<56):
    print("you can work with us")

a = 4
if(a == 7):
        print("yes")
elif(a>56):
        print("no and yes")





#practice set
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
num3 = int(input("enter number 3: "))
num4 = int(input("enter number 4: "))

if(num1>num4) :
    f1 = num1
else :
    f1 = num4
if(num2>num3) :
    f2 = num2
else :
    f2 = num3
if(f1>f4) :
    print(str(f1) + "is greatest")
if(f1>f2) :
    print(str(f2) + "is greatest")


sub1 = int(input("enter marks of sub 1"))
sub2 = int(input("enter marks of sub 2"))
sub3 = int(input("enter marks of sub 3"))

if(sub1<33 or sub2<33 or sub<33):
    print("you are fail in one sub")
elif((sub1+sub2+sub3)/3 <40):
    print("you are fail")
else:
    print("congratulations!, you are passed")



text = input("enter the text ")
spam = False

if("make a lot of money " in text):
    spam  = True
elif("bye now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("this text is spam")
else:
    print("this text is not spam")






username = int(input("enter your user name"))
a = len(name)
if(a>=10):
    print("True")
else:
    print("false")



names = ["sneha","ankita", "debo","bips","tanny","taishi"]
name =input("enter your name")

if name in names:
    print("your name is present in the list")
else:
    print("your name is not present in the list")



marks =int(input("enter your number"))

if marks>=90:
    grade = "ex"
elif marks>=80:
    grade = "a"
elif marks>=70:
    grade = "b"
elif marks>=60:
    grade = "c"
elif marks>=50:
    grade = "d"
else:
    grade = "f"

print("ypur grade is" + grade)





post=input("Enter the post\n")
post=post.upper()
if "SNEHA" in post:
    print("yes the post is talking about sneha")
else:
    print("The post is not talking about sneha")