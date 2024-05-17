def check_case(sentence):
    # ln= sentence.split('')
    a=0
    b=0
    for i in sentence:
        if i.isupper():
            a +=1
        
        else:
            b+=1
    

    print('UPPERCASE:',a)  
    print('LOWERCASE:',b)  

check_case('Hello brenda')

def numbers(nums):
    a=[]
    for i in nums:
        a.append(i**i)


    print(a) 
numbers([8,5,7,2])      