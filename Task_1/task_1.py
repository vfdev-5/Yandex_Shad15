__author__ = 'vfdev'


def nextElements(a):
    return 0.25 * a**2 * (a - 3.0)

a = -0.5
for i in range(1, 100):
    print a
    a = nextElements(a)
