
ba = "sneha's"
ka = "helicopter"
print(ba)
print(ba[0])
print(type(ba))
print(ba + ka)
print(ba[1:4])
#is same as ba[0.4]
print(ba[:4])
#is same as ba[1.5]
print(ba[1:])
#is sae is name [1:4]
c = ba[-4:-1]
print(c)
baa = "snehaisgood"
d = ba[0::2]
print(d)

story = "hi,im sneha, today is 18th of feb , im happy today, but now im felling sleepy, bye bye"
#string functions
print(len(story))
print(story.endswith("happy"))
print(story.count("c"))
print(story.capitalize())
print(story.find("upon"))
print(story.replace("sneha" , "Sneha"))

storyy = "sneha is good. \n he \t is very \\good"
print(story)


#chap 3 practice set
name = input("enter your name \n")
print("good evening, " +name)



letter = '''Dear<|NAME|>,
you are selectel!
Date: <|DATE|>
'''
Name = input("enter your Name\n")
Date = input("enter Date\n")
letter = letter.replace("<|NAME|>", Name)
letter = letter.replace("<|DATE|>", Date)
print(letter)



st = "This is a string with double spaces "
doubleSpaces = st.find(" ")
print(doubleSpaces)


st = "This is a string with double spaces "
st = st.replace(" "," ")
print(st)




letter = "Dear harry this python course is nice! thanks!"
print(letter)

formatted_letter = "Dear harry, \n\t this python course is nice! \n thanks!"
print(formatted_letter)


