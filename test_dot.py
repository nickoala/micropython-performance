import show

@show.time
def accum(a, b):
    s = 0
    for i in range(0, min(len(a), len(b))):
        s += a[i] * b[i]
    return s

@show.time
def sum_comprehend_index(a, b):
    return sum([a[i] * b[i] for i in range(0, min(len(a), len(b)))])

@show.time
def sum_map_index(a, b):
    return sum(map(lambda i: a[i] * b[i], range(0, min(len(a), len(b)))))

@show.time
def sum_comprehend_zip(a, b):
    return sum([x*y for x,y in zip(a,b)])

@show.time
def sum_map_zip(a, b):
    return sum(map(lambda z: z[0]*z[1], zip(a,b)))

a = list(range(0, 100))
b = list(range(-50, 50))

fa = [x + 0.1 for x in a]
fb = [x - 0.1 for x in b]

s = 0

print('=== Accumulate')
s = accum(a, b)
print(s)

print('=== Sum Comprehend Index')
s = sum_comprehend_index(a, b)
print(s)

print('=== Sum Map Index')
s = sum_map_index(a, b)
print(s)

print('=== Sum Comprehend Zip')
s = sum_comprehend_zip(a, b)
print(s)

print('=== Sum Map Zip')
s = sum_map_zip(a, b)
print(s)

print('+++++ Floating point +++++')

print('=== Sum Map Zip')
s = sum_map_zip(fa, fb)
print(s)

print('=== Sum Comprehend Zip')
s = sum_comprehend_zip(fa, fb)
print(s)

print('=== Sum Map Index')
s = sum_map_index(fa, fb)
print(s)

print('=== Sum Comprehend Index')
s = sum_comprehend_index(fa, fb)
print(s)

print('=== Accumulate')
s = accum(fa, fb)
print(s)
