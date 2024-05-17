def add(x,y):
    result=x+y
    return result
def subtract(a,b):
    subt=a-b
    return subt
def divide(d,e):
    dev=d/e
    return dev
def multiply(f,g):
    mult=f*g
    return mult
def remainder(h,i):
    rem=h%i
    return rem
def power_0f(j):
    power=j**3
    return power
def integral(num):
    my_dict={ }
    for number in range(1,num+1):
       my_dict[number]=number*number
    return my_dict
    

print(integral(9))

def sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total 
def multiply_many(*nums):
    mult=1
    for num in nums:
        mult*=num
    return mult       