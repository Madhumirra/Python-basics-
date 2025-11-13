a=[1,2,3,1,2]
b=(1,2,3,1,2)
print(a)
print(b)
#ouput
#[1, 2, 3, 1, 2]
#(1, 2, 3, 1, 2)

employee_ids = (1, 2, 3, 4, 5)
print("same type of objects:",employee_ids)
print(type(employee_ids))
#output
#same type of objects: (1, 2, 3, 4, 5)
#<class 'tuple'>

#Different elements in tuple
employee_details =  (1, "RGV", 1000.123,2+3j)
print("different type of objects:", employee_details)
#output
#different type of objects: (1, 'RGV', 1000.123, (2+3j))

#Parenthesis is optional for tuple
employee_ids = 1, 2, 3, 4, 5
print("same type of objects:",employee_ids)
print(type(employee_ids))
#output
#same type of objects: (1, 2, 3, 4, 5)
#<class 'tuple'>

#Example: Concatenation
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)
#output
#(10, 20, 30, 40, 50, 60)

#Example: Multiplication
t1=(10,20,30)
t2=t1*3
print(t2)
#output
#(10, 20, 30, 10, 20, 30, 10, 20, 30)

#Example: tuple packing
a=10
b=20
c=30
d=40
t=a, b, c, d
print(t)
#output
#(10, 20, 30, 40)

#Example: tuple unpacking
t=(10, 20, 30, 40)
a, b, c, d = t
print("a=",a , "b=" , b," c=", c ,"d=",d)
#output
#a= 10 b= 20  c= 30 d= 40

