# def get_names():
#     my_file = open("names.txt", "a")
#     current_name = input("enter your name: ")
#     my_file.write(current_name + "\n")
#     my_file.close()
#
#
# def read_names():
#     try:
#         my_file = open("names.txt", "r+")
#         for name in my_file.readlines():
#             # my_file.write("bla")
#             print(f"hello my best friend {name}", end='')
#         my_file.truncate(0)
#         my_file.close
#     except BaseException as e:
#         print("idiot, you cant write here")
#
#
# for i in range(3):
#     get_names()
# read_names()


def save_names():
    my_file = open ("names.txt", "a")
    current_name = input ("enter your name:")
    my_file.write((current_name + "\n"))
    my_file.close()


def show_name():
    with open ("names.txt", "r") as my_file:
        for name in my_file.readlines():
            print("current name is: " + name, end='')


for i in range(3):
    save_names()
show_name()


