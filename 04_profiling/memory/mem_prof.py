'''
Test decorador memory_profile.
'''


from memory_profiler import profile
import random


@profile
def func_test(x):
    
    n = x * 1000
    elements = []

    for _ in range(1, n + 1):
        val = random.randint(0, 100)
        vals = [val] * 10000
        elements += vals


func_test(8)
