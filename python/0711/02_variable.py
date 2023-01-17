import keyword

a = 5
a = 5 + 1
print(a)

x = y = 1000
print(x, y)
c, d = 10, 20
print(c, d)

x, y = 10, 20
tmp = x
x = y
y = tmp
print(x, y)

x, y = 10, 20
y, x = x, y
print(x, y)

print(keyword.kwlist)
