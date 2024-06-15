# #StringHandling

# a="Dhara"
# b="Pranav"
# print("b value before->",b)
# b=a
# a="kumar"
# print("b value after->",b)


# a="suresh"
# b="ramesh"
# b=a
# a=b
# print("a value",a)
# print(b)

# a="suresh"
# b="ramesh"
# a,b=b,a
# print("a value:",a)
# print("b value:",b)

# #indexing-Getting the character in the given string based on the index number
# #postive Indexing -indexing with positive numbers
# #negative Indexing-indexing with negative numbers
name="Suresh"
# print(name)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
#Slicing 
# print(name[1:4])
# print(len(name))
# print(name[-1])
# print("new")
# print(name[-2])
# print(name[:-1])
# print(name[0:-1])


# name="Dhara"
# print(name)
# print(name[8:])
# print(name[-4:-8])
#Ranging-First we give beginning number or else we give final number
#name="Dharagai"
# print(name[:4])
# print(name[0:])
# print(name[:-1])
# print(name[-3:])
# print(name[-1])
# print("check")
#print(name[::5]) #doubt

#normal formatting
#Automatic formatting
#manual formatting
name="Dharagai"
age=33.5
email="Dhara@gmail.com"

formatted="My name is " +name+ "."+"My age is " +"33"+ "."+"My Email ID is " +email+"."
print(formatted)

#automatic formatting
formatter="My name is {} and my age is {}.Also my email ID is {}".format(name,age,email)
print(formatter)


formatter="My name is %s and age is %d.Also myemailID is %s"%(name,age,email)
print(formatter)
name1="Pranav"
formatter=f"My name is {name1} and my age is {age}.Also my email ID is {email}"
print(formatter)

#Manual formatting
formatter="My name is {1} and my age is {0}.Also my email ID is {2}".format(age,name,email)
print(formatter)

