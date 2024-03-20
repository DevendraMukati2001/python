# creating calculator for calculating lcm and hcf

x = int(input("Enter first no.\n"))
y = int(input("Enter second no.\n"))


def lcm_finder(x, y):
    set1 = {*()}
    set2 = {*()}
    for i in range(1, x * y):
        a = x * i
        b = y * i
        set1.add(a)
        set2.add(b)

    z = set1.intersection(set2)
    c = (list(z))
    c.sort()
    print(c[0])
    pass


lcm_finder(x, y)


def hcf_finder(x, y):
    if x < y:
        n = x
    else:
        n = y
    while n >= 1:
        if x % n == 0 and y % n == 0:
            return n
        else:
            n = n - 1


print(hcf_finder(x, y))
