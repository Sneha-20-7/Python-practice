f = open('sample.txt', 'r')
data = f.read()
data = f.readline()
print(data)
f.close()



f = open('another.txt', 'w')
f.write("I am writing")
f.close()


with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("me")
    print(a)