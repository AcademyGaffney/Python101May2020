a = "dog"
b = "doggonit"
c = "Dog"
d = "goddess"

print(a in b)
print(a in d)
print(a[-1:len(a)*-1 -1:-1] in d)
print(a[0] == b[0])
print(a.lower() == c.lower())

e = 5

print(a + str(e) + c)

