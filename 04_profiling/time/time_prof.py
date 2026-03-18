'''
Perfilamiento de tiempo simple.
'''

import time


def func_test(x):
    
    n = x * 100000

    for _ in range(n):
        pass


# Experimento
deltas = []

for _ in range(1000):

    start_time = time.time()
    func_test(8)
    end_time = time.time()
    delta_time = end_time - start_time
    deltas.append(delta_time)

avg_time = sum(deltas)/1000
    
print(f'La función tomó: {round(avg_time, 4)}s en ejecutarse.')
