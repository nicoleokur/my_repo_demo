name = input("Enter your name: ")
print("Hello", name)

try:
    num = int(input("Enter a number: "))
    print(num)
    num *= 2
    print(num)
except:
    print("You did not enter a number.")

with open("movies.txt") as file:
    for line in file:
        print(line.strip()) # .strip gets rid of new line character but still have one from the file

with open("heights.txt") as file:
    for line in file:
        # print(line.strip())
        info = line.strip().split()
        print(f"{info[0]} {info[1]} is {int(info[2])} inches tall")