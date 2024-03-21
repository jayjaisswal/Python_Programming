#String Addition
first_name = "Jay"
last_name = "Kumar"
full_name = first_name +" "+ last_name
print(full_name)

#We can't Add two datatype using + but we can using ','
#e.g., print(full_name + 3)-->error
#e.g., print(full_name , 3)--> No error

print(full_name + "3")
print(full_name,3)
print(full_name+str(3))
print(full_name*3)

#output
# Jay Kumar
# Jay Kumar3
# Jay Kumar 3
# Jay Kumar3
# Jay KumarJay KumarJay Kumar
