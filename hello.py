def hello(name):
    print(f"Hello {name}")
   
def year_of_birth(name,age):
    year=2024-age
    print(f"Hello {name},your born in {year}") 
def my_country(country="Uganda"):
    print(f"Hello akirachix from {country}")     
def greet(*name1):
    for name in name1:
        print(f"Hello{name1}")
def create_sentence(**words):
    print(words)
    sentence=" "
    for word in words.values():
        sentence+=word
        sentence+=" "
    return sentence
def sum_and_greet(*args,**kwargs):
    total=0
    for x in args:
        total+=x 
    f=kwargs["First_name"]
    l=kwargs["Last_name"]
    greeting=f"Hello{f}{l},total of your numbers is{total}"
    return greeting 
                  