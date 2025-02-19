#list
a = [1, 2, 3, 5,34, 6]
print(a)
a[0] = 90
print(a)

c = [45, "sneha", false, 8.9]

#list slicing
friends = ["sneha", "debo", "ankita"]
print(friends[0:1])
print(friends[-3:])

l1 = [1, 5, 6,9,32,5]
print(l1)
l1.sort()
print(l1)
l1.append(45)
print(l1)
l1.insert(2,544)
print(l1)
l1.pop(2)
print(l1)
l1.remove(21)
print(l1)


#tuple
t = (1, 2,4,6)
t1 = ()
t1 = (1) # wrong way to dec tuple with single element
t1 = (1,)#tuple with sigle element
print(t1)
print(t[0])
#a tuple is an immutable data type in python
t[0] = 34

t = (1, 2,1,3,2,1,2,3,4,1,5,1,5,1,11,3,4,6)
print(t.count(1))
print(t.index(5))




#practice set 4
f1 = input("enter fruit number 1 ")
f2 = input("enter fruit number 2 ")
f3 = input("enter fruit number 3 ")
f4 = input("enter fruit number 4 ")
f5 = input("enter fruit number 5 ")
f6 = input("enter fruit number 6 ")
f7 = input("enter fruit number 7 ")
myfruitlist = [f1, f2 , f3, f4, f5 , f6, f7]
print(myfruitlist)




f1 = int(input("enter marks for student no 1 "))
f2 = int(input("enter marks for student no 2 "))
f3 = int(input("enter marks for student no 3 "))
f4 = int(input("enter marks for student no 4 "))
f5 = int(input("enter marks for student no 5 "))
f6 = int(input("enter marks for student no 6 "))

mylist = [m1, m2,m3, m4, m5,m6]
mylist.sort()
print(mylist)



a = (2, 4,5,7,8)
a[0] = 45



a= [2,3,4,78,]
print(a[0] + a[1] + a[2] + a[3])
print(sum(a))


a = [5,0,8,0,9,7,0,7,8,5,0,7,0,0]
print(a.count(0))


