# Strings

# Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are arrays
x="Hello, My name is Vrushti"
print(x[2])
print(len(x))

# Looping through a string
for i in x:
    print(i)

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Slicing of Strings
b = "Hello, World!"
print(b[2:5])       # llo
print(b[:5])        # Hello
print(b[5:])        # , World!
print(b[-5:-2])     # orl

# Modify Strings
b = "Hello, World!"
print(b.upper())   # upper() will return the string in uppercase.
print(b.lower())   # lower() will return the string in lowercase.
print(b.strip())    # strip() will remove the white spaces from the beginning and at the end
print(b.replace('H', 'J'))  # replace() will replace the old string with new one.
print(b.split(','))  # split() will split the string with ,

# String Concatenation
p = "Hello "
q = "World"
print(p + q)

# Format Strings (Placeholders and Modifiers)
age = 36
text = f"My name is John, I am {age}"
print(text)

name = "VV"
age = 21
msg= f"Name : {name}, Age: {age}"
print(msg)

#placeholder {}  Modifier :
msg= f"Name : {name}, Age: {age:.2f}" # add 2 decimals
print(msg)

# A placeholder can include a modifier to format the value &
# can contain variables, operations, functions, and modifiers to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type

# String Methods
# capitalize()
# count()
# endswith()
# find()
# format()
# index()
# isalpha()
# isalnum()
# isnumeric()
# upper()
# lower()