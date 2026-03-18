'''
Object Oriented Programming recap in Python.
'''


class Car: 
    def __init__(self, name):
        self.name = name
        self.kms = 0

    def __repr__(self):
        info = f'Nombre: {self.name} | KMs: {self.kms}'
        return info

    def vroom(self, kms_added):
        self.kms += kms_added


daily = Car('Porsche 911')
classic = Car('Mercedes 190D')
print(daily)
daily.vroom(100)
print(daily)
print(classic)
