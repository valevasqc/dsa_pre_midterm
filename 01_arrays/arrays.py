'''
List ('array') elements in memory.
'''


arr = [1, 2, 3, 4, 5]

for i in range(5):
    print(f'Element {arr[i]} is in address: {id(arr[i])}')
