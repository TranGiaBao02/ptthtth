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
string = str1 + " " + str2
print(string)

# Substring
string = 'Hello world'
print (string[0:4])
print (string[:4])
print (string[-3:])
print (string[6:-3])

# String lenght

text = 'Hello world'
count = len(text)
print(count)



# Search & replace
string = 'Hello world'
newstr = string.replace('Hello','Bye')
print ("replace: " + newstr)

# Search substring
string = 'Hello world'
print (string.find('world'))

print (string.find('Bye'))


#
string = 'Hello world'
print (string.split(' '))

#
str_1 = '//Hello world//'
new_str_1 = str_1.strip("/")
print("strip: " + new_str_1)

new_str_2 = str_1.lstrip("/")
print("lstrip: " + new_str_2)

new_str_3 = str_1.rstrip("/")
print("rstrip: " + new_str_3)

# isnumeric, lower, upper
string = 'Hello world'
print(string.isnumeric())
print(string.lower())
print(string.upper())

# List
numbers = [1, 2, 3, 4, 5]
names = ['Marry', 'Peter']

print (numbers[0])
print (numbers[-3])
print (names[1])

# Kiểm tra theo index
index = 20
if index < len(names):
    print(names[index])
else:
    print("Index:" + str(index) + " > độ dài chuỗi: " + str(len(names)))



#
try:
    names[index]
except IndexError:
    print("Lỗi")

#
mylist = ['a','b','c']
print ('a' in mylist)

print ('b' not in mylist)

#Trích xuất chuỗi con
numbers = ['a','b','c','d']
print (numbers[:2])
print (numbers[2:])
#Xóa phần tử của mảng
numbers = [1, 2, 3, 4, 5]
del numbers[0]
print (numbers)
#Xóa một khoảng phần tử trong mảng
numbers = [1, 2, 3, 4, 5, 6, 7]
del numbers[2:4]
print (numbers)
#Nối 2 mảng
a = [1, 2]
b = [1, 3]
print (a + b)
#Thêm phần tử vào mảng
numbers = [1, 2, 3]
numbers.append(4)
print (numbers)
#Lấy phần tử cuối mảng
numbers = [1, 2, 3]
mynumber = numbers.pop()
print (mynumber)
print (numbers)
#Tìm một giá trị trong mảng
aList = [123,'xyz','zara','abc']
print ("Index for xyz : ", aList.index('xyz'))
print ("Index for zara : ", aList.index('zara'))
#Đảo ngược giá trị trong mảng
numbers = [1, 2, 3, 4]
numbers.reverse()
print (numbers)
#Sắp xếp giá trị các phần tử
#aList = [123,'xyz','zara','abc','xyz']
#aList.sort()
#print ("List : ", aList)
#Tuple
mytuple = ('x','y','z')
print (mytuple)
#Dictionary
point = {'x': 3, 'y': 6, 'z': 9}
print(point['x'])
#Thêm một phần tử
user = {'name': 'Jone','age': 30}
user['country'] = 'Vietnam'
print (user)
#Một số hàm và phương thức thông dụng
#dict.clear(): Xóa toàn bộ dữ liệu bên trong đối tượng
#dict.copy(): Trả về một bản copy của đối tượng
#dict.formkeys(seq[, value]):
#dict.has_key(key): Kiểm tra một key có tồn tại trong đối tượng hay không
#dict.value(): Trả về một List chứa các value

#Phân chia module
#Các loại module
#1. Viết bằng python: phần mở rộng (.py)
#2. Các thư viên liên động: mở rồng (.dll .pyd .so .sl),...
#3. C-module liên kết với trình phiên dịch

#Đường dẫn để tìm load module
#mport math
#math.__file__

#import random
#random.__file__
#Cách khai báo và sử dụng module
import mymath
num1 = 1
num2 = 2
print("Tong cua 2 so la: " + str(mymath.cong(num1,num2)))
#Class
class animal():
    name = ''
    age = 0
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age
    def show(self):
        print ('My name is ', self.name)
    def run(self):
        print ('Animal is running...')
    def go(self):
        print ('Animal is going...')
class dog(animal):
    def run(self):
        print ('Dog is running...')
myanimal = animal()
myanimal.show()
myanimal.run()
myanimal.go()
mydog = dog('Lucy')
mydog.show()
mydog.run()
mydog.go()

#Tập tin(File)
