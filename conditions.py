def print_numbers(n):
    numbers=range(n)
    for number in numbers:
        print(number)
def print_even_numbers(n):
    numbers=range(n)
    for number in numbers:
        if number%2==0:
            print(number)

def odd_or_even(n):
    numbers=range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number}is even")
        else:
            print(f"{number}is odd")    

def check_divisibilty(n):
    numbers=range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number}is divisible by 2")
        elif number%3==0:
            print(f"{number}is divisible by 3 ")
        elif number%5==0:
            print(f"{number}is divisible by 5 ")
        elif number%7==0:
            print(f"{number}is divisible by 7 ")
        else:
            print(f"{number}is not divisible by 2,3,5,7")  
def count_down(n):
    while n>0:
        print(n)
        n-=1
def count_down_to_five(n):
    while n>0:
        print(n)
        if n==5:
            break
        n-=1 
def divisible_by_seven(n):
    x=1
    while x<=n:
        x+=1
        if x%7!=0:
            continue
        print(x)
# Using if,else,elif create a function fizzbuzz
# Accepts a number n and generate a range of numbers 
#from 0 to n
        # for numbers divisible by 3 print fizz
        # by 5 print Buzz
        # else FizzBuzz

def fizz_divisible(n):
    numbers=range(n)
    for number in numbers:
        if number%3==0:
            print("Fizz")
        elif number%5==0:
            print("Buzz")
        else:
            print(number)
#using while if and contiunue function to [print all 
            # numbers from 0 to 50
def number_to_fifty():
    x=0
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)





    