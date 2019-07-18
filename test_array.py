import show
from array import array

r = range(-50, 50)

print('=== Integer List')
x = show.memory(lambda: list(r))()

print('=== Integer Array')
ax = show.memory(lambda: array('i', x))()

print('=== Float List')
fx = show.memory(lambda: [float(i) for i in x])()

print('=== Float array')
fax = show.memory(lambda: array('f', fx))()

print('=== Double array')
dax = show.memory(lambda: array('d', fx))()

@show.time
def read100times(a):
    for i in range(0, 100):
        a[i]

print('+++++ Read 100 times +++++')

print('=== Integer List')
read100times(x)

print('=== Integer Array')
read100times(ax)

print('=== Float List')
read100times(fx)

print('=== Float array')
read100times(fax)

print('=== Double array')
read100times(dax)

#start = gc.mem_alloc()
#x = list()
#end = gc.mem_alloc()
#print('Bytes used:', end - start)

#start = gc.mem_alloc()
#y = array('i', x)
#end = gc.mem_alloc()
#print('Bytes used:', end - start)

#start = gc.mem_alloc()
#xf = [float(i) for i in x]
#end = gc.mem_alloc()
#print('Bytes used:', end - start)

#start = gc.mem_alloc()
#z = array('d', xf)
#end = gc.mem_alloc()
#print('Bytes used:', end - start)

#timeit(read100times)(x)
#timeit(read100times)(y)
#timeit(read100times)(xf)
#timeit(read100times)(z)
