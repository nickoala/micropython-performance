import show
import math

@show.time
def math_pow(a, p):
    s = 0
    for i in a:
        s += math.pow(i, p)
    return s

@show.time
def func_pow(a, p):
    s = 0
    for i in a:
        s += pow(i, p)
    return s

@show.time
def builtin_pow(a, p):
    s = 0
    for i in a:
        s += i ** p
    return s

@show.time
def simply_2times(a):
    s = 0
    for i in a:
        s += i * i
    return s

@show.time
def simply_3times(a):
    s = 0
    for i in a:
        s += i * i * i
    return s

a = list(range(0, 50))
fa = [i+0.1 for i in a]

s = 0

print('=== math.pow()')
s = math_pow(a, 2)
print(s)

print('=== pow()')
s = func_pow(a, 2)
print(s)

print('=== x**2')
s = builtin_pow(a, 2)
print(s)

print('=== x * x')
s = simply_2times(a)
print(s)

print('+++++ Float +++++')

print('=== math.pow()')
s = math_pow(fa, 2)
print(s)

print('=== pow()')
s = func_pow(fa, 2)
print(s)

print('=== x**2')
s = builtin_pow(fa, 2)
print(s)

print('=== x * x')
s = simply_2times(fa)
print(s)

print('+++++ Cube Float +++++')

print('=== math.pow()')
s = math_pow(fa, 3)
print(s)

print('=== pow()')
s = func_pow(fa, 3)
print(s)

print('=== x**3')
s = builtin_pow(fa, 3)
print(s)

print('=== x * x * x')
s = simply_3times(fa)
print(s)
