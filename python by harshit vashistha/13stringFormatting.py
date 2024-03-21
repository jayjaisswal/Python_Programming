name = "Jay Kumar"
age = 20
#method 1
print("hello " + name + " Your age is :" + str(age+2))

# method 2
print("hello {} your age is :{}".format(name,age+2))  #-->python 3

#method 3
print(f"hello {name} your age is :{age+2}")

#output
# hello Jay Kumar Your age is :22
# hello Jay Kumar your age is :22
# hello Jay Kumar your age is :22
