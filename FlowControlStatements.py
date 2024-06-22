# #if else elif
# #looping
# #break
# #continue
# #pass

# #----if statement--------

# x=12
# if (x<10 and x==10):  #this will be always False
#     print("x is less than 10") 
# elif x==10:
#     print("x is equal to 10")
# elif x==11:
#     print("x is equal to 11")
# else:
#     print("x is greater than 10")

# x=4
# if(x==0):
#     print("I have value 0")
# elif(x==1 or x<5):
#     print("I have value lesser than 1")

# print(bool(0))
# print(bool(1))
# print(bool(-1))
# name="softlogic"
# if name.find('b')>0:
#     print("The String has 'o'")
# else:
#     print("The String do not have 'o'")

#Loopings
#for loop and While loop
#For loop-We should give start and end range
#While loop-Only starting point is enough ,it will go infinite times..

insName="softlogic"
# for data in insName:
#     print(data)
# print("---END----")

# for value in range(-5,-3):
#     print(value)
# print("END OF RANGE")

# #range-if we use the range,we will get the index of the value.If we dont need index,simply pass the string name(insName)
# for data in range(0,len(insName)):
#     #print(data)
#     print(data,insName[data])
# print("END")

stringLength=len(insName)
# num=0
# for data in range(stringLength):
#     print("first print",num)
#     num+=1
#     print("second print",num)
# print("END")

# for data in range(stringLength):
#     if (data%2==0):
#         print(data,insName[data])
# print("EOE")

# name="Softlogic"
# num=2
# for value in range(len(name)):
#    if value==num:
#       print(name[value])
#       num=num+3

name1="santhosh"
# print("length",len(name1))
output=""
# for value in name1:
#     output +=(value+"_")
# print(output)

# print(output[:-1])

for i in range(len(name1)):
    if (i==len(name1)-1):
        output+=name1[i]
    else:
        output+=name1[i]+"_"
print(output)



  
   
