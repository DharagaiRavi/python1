# # #StringHandling

# # a="Dhara"
# # b="Pranav"
# # print("b value before->",b)
# # b=a
# # a="kumar"
# # print("b value after->",b)


# # a="suresh"
# # b="ramesh"
# # b=a
# # a=b
# # print("a value",a)
# # print(b)

# # a="suresh"
# # b="ramesh"
# # a,b=b,a
# # print("a value:",a)
# # print("b value:",b)

# # #indexing-Getting the character in the given string based on the index number
# # #postive Indexing -indexing with positive numbers
# # #negative Indexing-indexing with negative numbers
# name="Suresh"
# # print(name)
# # print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])
# # print(name[4])
# # print(name[5])
# #Slicing 
# # print(name[1:4])
# # print(len(name))
# # print(name[-1])
# # print("new")
# # print(name[-2])
# # print(name[:-1])
# # print(name[0:-1])


# # name="Dhara"
# # print(name)
# # print(name[8:])
# # print(name[-4:-8])
# #Ranging-First we give beginning number or else we give final number
# #name="Dharagai"
# # print(name[:4])
# # print(name[0:])
# # print(name[:-1])
# # print(name[-3:])
# # print(name[-1])
# # print("check")
# #print(name[::5]) #doubt

# #normal formatting
# #Automatic formatting
# #manual formatting
# name="Dharagai"
# age=33.5
# email="Dhara@gmail.com"

# formatted="My name is " +name+ "."+"My age is " +"33"+ "."+"My Email ID is " +email+"."
# print(formatted)

# #automatic formatting
# formatter="My name is {} and my age is {}.Also my email ID is {}".format(name,age,email)
# print(formatter)


# formatter="My name is %s and age is %d.Also myemailID is %s"%(name,age,email)
# print(formatter)
# name1="Pranav"
# formatter=f"My name is {name1} and my age is {age}.Also my email ID is {email}"
# print(formatter)

# #Manual formatting
# formatter="My name is {1} and my age is {0}.Also my email ID is {2}".format(age,name,email)
# print(formatter)

#------------String BuildIn Function-------
name="My institute is softlogic"
# new_name=name[1:]
# print(new_name)
# name_rep="S"
# print(name_rep+new_name)
# name=name_rep+new_name
# name="{}{}".format(name_rep,new_name)
# print("1st Format",name)
# name="%s%s"%(name_rep,new_name)
# print("2nd Format",name)
# name="{1}{0}".format(new_name,name_rep)
# print("3rd Format",name)
# name=f"{name_rep}{new_name}"
# print("4th Format",name)
#String Method
#1.Capitalize()
# print(name.capitalize())
# #2.Upper
# print(name.upper())
# #3.Lower
# print(name.lower())
# #4.Replace
# print(name.replace("My","Myy"))
# #5.Title-only sentence begging words will be in caps
# print(name.title())
# #6.CaseFold-Changes "Upper" to "Lower" case
# print(name.casefold())
# #7.Swapcase
# print(name.swapcase())
#8.Find
# yindex=name.find('b')
# print(yindex)
# #9.Index
# yindex1=name.index('b')
# print(yindex1)

#Find and index-will bring the index of the given character
#Difference between index and find is if the character is not available in the String,Find will not throw error,instead returns negative number -1
#Whereas index will throw an error
#9.Count
# counter=name.count("y")
# print(counter)
# counter1=name.count("b")
# print(counter1)
#10.Endswith
# endwithcheck=name.endswith('c')
# print(endwithcheck)
# #11.StartsWith
# startwithcheck=name.startswith('My')
# print(startwithcheck)
#12.Strip-remove spaces
# TestValue="  My Name  "
# fun=TestValue.strip()
# print(TestValue)
# #lstrip-Removing left space
# TestValue="  My Name  "
# fun=TestValue.lstrip()
# print(TestValue)
# print(fun[-1])
# #rstrip-Removing left space-1
# TestValue="  My Name  "
# fun=TestValue.rstrip()
# print(TestValue)
# print(fun[-1])
#Removing spaces inbetween the words
# name1="Hello World How Are you"
# name=name1.replace(" ","")
# print(name)
# #13.isalpha-check only alpha
# Testvalue="asd"
# check_data=Testvalue.isalpha()
# print(check_data)
# #14.isnumeric-check only numeric
# Testvalue="2321"
# check_data=Testvalue.isnumeric()
# print(check_data)
#15.isalnum-check for alphabets and numeric
# Testvalue="2321sds"
# check_data=Testvalue.isalnum()
# print(check_data)
# #16.partition-returns in tuple
Testvalue="Softloglic"
check_data=Testvalue.partition('l')
print(check_data)

# Testvalue="Softloglic"
# check_data=Testvalue.partition('d')
# print(check_data)


# Testvalue="Softloglic"
# check_data=Testvalue.partition('')
# print(check_data)
#17.split-returns the result in list
# Testvalue="Softloglic"
# check_data=Testvalue.split('l')
# print(check_data)

# Testvalue="Softloglic"
# check_data=Testvalue.split('d')
# print(check_data)

# Testvalue="Softloglic"
# check_data=Testvalue.split('')
# print(check_data)

name="my-institute-is-solftolgic"
name=name.replace("-","")[1:11]
first_half=name[:len(name)//2]
second_half=name[:len(name)//2:]
name=f"{first_half}_{second_half}"
print(name,len(name))



# name="my-institute-is-solftolgic"
# check_value=name.replace('-','')
# print("Check_name:",check_value)
# check_result=check_value[1:11]
# print(check_result)
# len_checkresult=len(check_result)/2
# print(len_checkresult)
# first_value=check_result[0:len(check_result)//2]
# print(first_value)
# second_value=check_result[len(check_result)//2:]
# print(second_value)
# #len_new_value=check_result.index(len_checkresult)
# #print(len_new_value)
# new_value="_"
# check_result1=check_result[0:5]
# print(check_result1)
# check_result2=check_result[5:10]
# print(check_result2)
# final_result=check_result1+new_value+check_result2
# print(final_result)
# print(len(final_result))


