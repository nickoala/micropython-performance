import show

"""
Test different methods to map a function element-wise to a list.
"""

@show.time
def map_by_map(src, f):
    return list(map(f, src))

@show.time
def map_by_comprehension(src, f):
    return [f(x) for x in src]

@show.time
def map_by_iteration(src, dest, f):
    for i in range(0, len(src)):
        dest[i] = f(src[i])
    return dest

src = list(range(0, 1000))

print('=== Map by map')
result = map_by_map(src, lambda x: x * 0.1)
print(result)

print('=== Map by comprehension')
result = map_by_comprehension(src, lambda x: x * 0.1)
print(result)

dest = [0] * len(src)

print('=== Map by iteration')
result = map_by_iteration(src, dest, lambda x: x * 0.1)
print(result)
