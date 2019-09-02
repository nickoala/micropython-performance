import show

"""
Test different methods to create a list.
"""

@show.time
def create_by_append(n):
    a = []
    for i in range(0, n):
        a.append(0)
    return a

@show.time
def create_by_comprehension(n):
    return [0 for i in range(0, n)]

@show.time
def create_by_multiply(n):
    return [0] * n

@show.time
def create_init_by_comprehension(n):
    return [i for i in range(0, n)]

@show.time
def create_init_by_multiply(n):
    a = [0] * n
    for i in range(0, n):
        a[i] = i
    return a

print('=== Create by Multiply')
a = create_by_multiply(200)
print(a)

print('=== Create by Comprehension')
a = create_by_comprehension(200)
print(a)

print('=== Create by Append')
a = create_by_append(200)
print(a)

print('=== Create Init by Comprehension')
a = create_init_by_comprehension(200)
print(a)

print('=== Create Init by Multiply')
a = create_init_by_multiply(200)
print(a)
