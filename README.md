# Performance Study of Various Programming Techniques on MicroPython

Say, I want to find the dot product of two vectors `a` and `b`. Which of the
following implementations is faster?

```python
def dot_product_by_accumulate(a, b):
    s = 0
    for i in range(0, len(a)):
        s += a[i] * b[i]
    return s

def dot_product_by_zip(a, b):
    return sum([x*y for x,y in zip(a,b)])
```

The first uses an imperative style; the second uses a functional style. Which is
faster on a given MicroPython platform?

This type of questions may not be of much concern on a high level, but it can
make a big difference in heavy-lifting parts of some algorithms. When it is done
repeatedly for each pixel on a 480x360 image, small differences add up.

Faced with this uncertainty, I set out to test the speed of various programming
techniques. Experiments are run on [OpenMV](https://openmv.io), a Pyboard with a
STM32H743VI ARM Cortex M7 processor at 480 MHz.

## Lessons learned

1. Imperatively accumulating a sum is faster than `sum([... zip(...)])`

2. `[func(x) for x in list]` is faster than `map(func, list)`

3. `[0] * length` to create a list is the fastest

4. `a ** b` is faster than `pow(a, b)`

5. Accessing an element in an `array` is slower than accessing an element in a
   list. However, an `array` with float elements uses far less memory than a
   corresponding list.

These knowledge informs my programming style in these projects:

- [micropython-vec](https://gitlab.com/nickoala/micropython-vec) -
  Vector Operations on MicroPython

- [micropython-mtx](https://gitlab.com/nickoala/micropython-mtx) -
  Fast Matrix Multiplication and Linear Solver on MicroPython

- [OpenRV](https://github.com/nickoala/openrv) -
  Robot Vision routines for OpenMV
