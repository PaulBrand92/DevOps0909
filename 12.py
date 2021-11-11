import requests
# my_variable = int(input("enter first number: "))
# my_other_var = int(input("enter second number: "))
# try:
#     result = my_variable / my_other_var
#     print(result)
# except BaseException as e:
#     print(e.args)
# try:
#     requests.get("httpps://github.com")
# except BaseException as e:
#     print("something is wrong, check this:" + str(e.args))
# print("hello")


def get_user_age():
    input_from_user = int(input("enter your age: "))
    if input_from_user < 0:
        raise ValueError("Age can not be negative")

try:
    get_user_age()
except ValueError as e:
    print(e.args)

age = print("conflict")
