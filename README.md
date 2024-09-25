# Learning_Python_DSA
This  repository includes all python files i made to learn python and DSA with Python

# Variables

A word that can be used to store a value and can be called again and again
a word that is bined to some value


Best practice for a variables
- snake_case- user_iq instead of useriq
- Start with lowercase or underscore- abc, _abc 
- letter numbers and underscroes no spaces
- Case sensitive- "iq" is not the same as "IQ"
- Don't overwrite keywords- you can't use preused keyword for  example print =5 cannot work
- make variable easily understandable and descriptive- age, 
- constants usualy meant for other programmers to never change it,- typed in capitals - PI=3.14


# Datatype
Type of Datatypes
1. int - Numerical types
2. float- Decimal types, Takes more space than int
3. string- alphabets symbols and numbers
4. boolean
5. list
6. tuple
7. dictionary
8. set
9. complex

## int and float
- int- integer conatins just numbers
- float = these conatin number with a decimal value for example 3.5 note 3.0 is also a float and not an int  

## Str
- A string is a collection of characters stored withing quoatations 'a' or "a" it can conatin any character number symbol
- multiline sting can be made with ''' a ''' for example 
````
long_string = '''This 
is a 
very 
long 
string
''' 
````
- you can add ' to string by using a \ for example <br  >
````
weather = 'it\'s kind of \"sunny\"'
````


 - you can add "\t" to add tab spacing to your string <br>
 ````
print('\tthis has a tab here')
````

- you can add "\n" to add new line to sting <br>
````
print('this has \n a new line here')
````

-  Formatted strings
````
name = "Derp"
age= 55
````
````

print("hey "+ name+" you are "+ str(age)+' years old')
````

 > instead use
 ````

print(f'hey {name}.You are {age} years old')
````

