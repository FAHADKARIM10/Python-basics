# strings in python are surrounded by either single code or double quote 
 
'hello word'    "hello world" #both are example of strings 

print('hello world')
print("hello world")

# more about strings 

a ='fahad karim'

print(len(a))   # this function will execute the total numbers of letter in the varibale a
 
print(a.upper()) #this will change the letter to upper case

# strings are immutable 

# you can create a new string but cannot change the existing string because strings are immutable    


# 1.assigning string to a variable

a = "hello world"
print(a)

# 2. assighning multiline string 

a ="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
print(a)

# we can use three double quotes to assign multiline string


f ='fahad karim'
print(f[1])

# we can use square bracket to acces the single element or more elements form a string 

descrip1 ='fahad karim is in love'
print('fahad'in descrip1)

# if the world fahad is present in the variable descrip1 then the python intreprer will execute 
# true if not it will execute false 

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")