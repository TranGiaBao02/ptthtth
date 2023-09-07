print("Xin Chào")

a = 1
print(a)
a = 'Hello World'
print(a)
a = [1, 2, 3]
print(a)
a = [1.2,'Hello','W', 2]
print(a)

x = 2
1 < x < 3 # True
10 < x < 20 # False
3 > x <= 2 # True
2 == x < 4 # True

b = 2
if (b==1) :{
    print(b)
}
elif (b==2) :
    print("B không bằng 1")
else:
    print("a")


# For...in

for letter in 'Python':  # First Example
    print('Current Letter:', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # Second Example
    print('Current fruit:', fruit)
    print("Good bye!")

# While
count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1
print ("Good bye!")

# Function
def sum(a, b):
    return (a+b)

print(sum(27,8))

def plus(c, d=10):
    return (c+d)
print(plus(2))

# String
str1 = "Hello"
str2 = 'world'
print(str1[1])
print(str2[0])

paragraph = """This is line 1
This is line 2
This is line 3"""

# 
str = str1 + " " + str2
print(str)

# Substring
str = 'Hello world'
print (str[0:4])
print (str[:4])
print (str[-3:])
print (str[6:-3])

# String lenght

text = 'Hello world'
count = len(text)
print(count)



# Search & replace
str = 'Hello world'
newstr = str.replace('Hello','Bye')
print ("replace: " + newstr)

# Search substring
str = 'Hello world'
print (str.find('world'))

print (str.find('Bye'))


#
str = 'Hello world'
print (str.split(' '))

#
str_1 = '//Hello world//'
new_str_1 = str_1.strip("/")
print("strip: " + new_str_1)

new_str_2 = str_1.lstrip("/")
print("lstrip: " + new_str_2)

new_str_3 = str_1.rstrip("/")
print("rstrip: " + new_str_3)

# isnumeric, lower, upper
str = 'Hello world'
print(str.isnumeric())
print(str.lower())
print(str.upper())

# List
numbers = [1, 2, 3, 4, 5]
names = ['Marry', 'Peter']

print (numbers[0])
print (numbers[-3])
print (names[1])

#
index = 1
if index < len(names):
    names[index]
else:
    print("a")

#
try:
    names[index]
except IndexError:
    print("Lỗi")

#
mylist = ['a','b','c']
print ('a' in mylist)

print ('b' not in mylist)
