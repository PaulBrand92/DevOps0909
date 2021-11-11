a = "hello world"
b = 4
isMarried = False
d = ["aviel", 31, True]
e = ("moshe", 43, False)
f = {"name": "aviel", "age": 31, "isMarried": True, "hobbies": ["ski", "Guitar"],
     "work": {"position": "devops", "salary": "2M"}}
# print(a)
# print(b)
d[1] = 32
# e[2] = 44
# print(d[1])
# print(e[2])
# print(f["work"].values())
# print(f.keys())

g = "paul"
h = "brand"
i = g + " " + h
j = 4
k = g + str(j)
lm = f"{g} {h}"
lk = "%s %s" % (g, h)
lt = "paul\n\t \"brand\""
# print(i)
# print(k)
# print(lm)
# print(lk)
# print(lt)

if j == 4:
    print("j is 4")

if j != 4:
    print("j is 4")

first = 7
second = 44.3

print(first + second)
print(first * second)
print(second / first)

a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print(a, b, c)

my_name = "paul"
print(first * my_name)

z = """
bla bla
i am the best
"""
print(z)
