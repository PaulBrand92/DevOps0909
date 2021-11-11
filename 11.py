import io

my_file = open("read_my_contents.txt", "r")
contents = my_file.readlines()
#print(contents)
for line in contents:
    print(line, end='')
my_file.close()

my_file = open("names.txt", "w")
for i in range(3):
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")
my_file.close()

try:
    my_file =open("names.txt", "r")
    for name in my_file.readlines():
        # my_file.write("bla")
        print(f"hello {name}", end='')
except io.UnsupportedOperation as e:
    print("idiot, you cant write here")


