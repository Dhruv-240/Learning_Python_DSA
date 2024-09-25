'''
Type of Datatypes
1. int - Numerical types
2. float- Decimal types, Takes more space than int
3. string- alphabets symbols and numbers
4. boolean
5 list
6. tuple
7. dictionary
8 set
9 complex
'''
# int and float

print(2+4)
print((type(2)))
print(type(2+4)) # gives int
print(type(2/4))  # gives float
print(type(20+1.1)) # coverts to float
print(type(1.9+1.1)) # although 3 is int gives float as 3.0

# String- a string is a collection of characters stored withing quoatations 'a' or "a" it can conatin any character number symbol

a ='a'
print(a)

b = "5"
print(type(a))

long_string = '''This
is a 
very 
long
string
''' # multiple lines of stings usefuul for exaple paragraphs

print(long_string)

# strings can be added together
first_name = 'Dhruv'
last_name = 'Bhateja'
full_name = first_name+ ' '+last_name
print(full_name)

str_num =100
print(type(str(str_num))) # covert int to string

# - you can add ' to string by using a \ for example 

weather = 'it\'s kind of \"sunny\"'
print(weather)
  #you can add "\t" to add tab spacing to your string
print('\tthis has a tab here')

 # you can add "\n" to add new line to sting
print('this has \n a new line here')

# - formatted strings
name = "Derp"
age= 55

print("hey "+ name+" you are "+ str(age)+' years old')
# instead use
print( f'hey {name}.You are {age} years old')

