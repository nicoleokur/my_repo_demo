print("Hello World.") 

# single line comment

'''
multiple
line
comment
'''

# x = 100
# y = 11
# z =10 
#highlight the data and do control forward slash (/) to comment out temporarily

x = 100
y = 10.1 
x = "hello"
print(x) #no declarations so data types can change

# Math Operators
x = 100
y = 10

z = x/y
print(z)
z = int(z) #convert to int
print(z)

# OR use floor division
x = 100
y = 3

z = x//y
print(z)

min_val = min(10, 1)
print(min_val)
raised = pow(2, 4) #this is 2 to the 4th
raised = 2**4 #either method works
print(raised)

if x < 0:
    print("negative")
else:
    print("positive")

if x < 0 and y < 0:
    print("negative")

if x <0 or y < 0:
    print("one negative")

if x<0:
    print("negative")
elif y<0:
    print("negative")
else:
    print("positive")

counter = 0
while counter < 10:
    print(counter)
    counter+=1 # counter++ does not exist in python

print()
a_list = [1, 2, 3, 4, 5]
for i in range(5): # range(start, end, incrament) - starts at 0, does not include 5, inc. by 1
    print(i, a_list[i])
print()

for i in range(1, len(a_list)):
    print(i, a_list[i])
print()

for i in range(len(a_list)-1, -1, -1): #start at last element, go up to not including -1
    print(i, a_list[i])
print()

for i,val in enumerate(a_list):
    print(i,val)
print()

for value in a_list:
    print(value) # to not print new line, value, end ="  "
print()

#exercise 1
for i in range(1, 21, 1):
    if i % 3 == 0:
        print(i)
print() 

#exercise 2
counter = 1
sum = 0
while counter <= 50:
    if counter % 2 == 0:
        sum += counter
    counter += 1
print(sum)
print()

# exercise 3 (correct)
numbers = [5, 8, 2, 15, 10, 3, 7]
for num in numbers:
    if num > 5:
        print(num, end = "  ")
print()

#challenge
lst = [1, 2, 3, 4, 5]
lst2 = []
lst2.append(lst[0])
for i in range(1, len(lst)):
    lst2.append(lst2[i-1]+lst[i])
print(lst2)

#functions
def hello_world():
    print("Hello World.")
hello_world()

def hello(name = "Jack"):
    print("hello", name) # "hello"+name removes space between
hello("Bob")
hello()

# exercise 4
def swap(lst):
    tmp = lst[0]
    lst[0] = lst[len(lst)-1]
    lst[len(lst)-1] = tmp
# can be done as 
# lst[0] = lst[-1] 
# lst[-1] = tmp

lst = [0, 3, 8, 4, 5]
swap(lst)
print(lst)

full_name = "Nicole Okur"
first = full_name[0]
print(first)
last = full_name[-1]
print(last)

#slicing strings
first_name = full_name[:6]
print(first_name)
last_name = full_name[-4:]
print(last_name)

print("hello world")