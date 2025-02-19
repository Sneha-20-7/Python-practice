#dictionary&sets
mydict = {
    "fast": "in a quick Manner",
    "sneha": "a quick learner",
    "marks": [1,2,3],
    "anotherdict": {'sneha': 'player'},
    1: 2,
}

print(mydict['fast'])
mydict['marks'] = [45,78]
print(mydict['marks'])
print(mydict['sneha'])
print(mydict['anotherdict']['sneha'])


print(mydict.key())
print(type(mydict.key()))
print(list(mydict.key()))
print(mydict.values())
print(mydict.items())
print(mydict)
updatedict = {
    "anki": "friend",
    "sneha": "now learning Python",
}
mydict.update(updatedict)
print(mydict)

print(mydict.get("sneha"))
print(mydict["sneha2"])# shows error as  sneha2 is not present in the dictionary
print(mydict.get("sneha2"))
print(mydict["sneha"])


#sets
a = {1,3,4,5,6,6}
print(type(a))
print(a)
#it will create an empty dict not an empty set
a = {}
print(type())


#empty set
b = set()
print(type(b))
b.add(4)
b.add(5)
b.add((1,3,4,5,))
b.add({1,3,4,5,})#not allowed
b.add([1,3,4,5,])#not allowed
print(b)

print(len(b))
b.remove(5)
b.remove(15)#throw error cause 15 is not present 
print(b)

print(b.pop())
print(b)
print(b.clear())
print(b)




#practice set
myDict ={
    "pankha": "fan",
    "dabba": "box",
    "vastu" :"item",
}
print("options are", myDict.keys())
a = input("enter the hindi word\n")
print("the meaning of your word is :", myDict.get(a))



num1 = int(input("enter num 1"))

num2 = int(input("enter num 2"))

num3 = int(input("enter num 3"))

num4 = int(input("enter num 4"))

num5 = int(input("enter num 5"))

num6 = int(input("enter num 6"))

num7 = int(input("enter num 7"))

s = {num1, num2 , num3, num4 , num5 , num6 , num8}






s = {18, "18", 18.0}
print(s)




s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s)


s = {}
type(s) #dict




favl = {}
a = input("enter your fav lang ankita\n")
d = input("enter your fav lang deba\n")
b = input("enter your fav lang bips\n")
t = input("enter your fav lang taishi\n")
favlang['ankita'] = a
favlang['debo'] = d
favlang['bips'] = b
favlang['taishi'] = t

print(favlang)

s ={7,7,8,8,4,"sneha" ,[1,4]}


