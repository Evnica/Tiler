import numpy as np

a = np.array([1,2,3], ndmin=2)
print(a)
print(a.shape)

d = np.zeros(shape=(10, 5, 3))
# print(d.ndim)

my_data = np.genfromtxt('testNumpyArrayRead.tsv', delimiter='  ', skip_header=1, dtype='int')
# print(my_data)

b = np.arange(30)
b = b.reshape(5, 6)

c = np.arange(30)
c = c.reshape(5, 6)

print(b + c)
print(b - c)
print(b * c)

print(b.sum())
print(b)

print(b.sum(axis=0))  # m axis, columns
print(b.sum(axis=1))  # n axis, rows

b = b + np.ones(shape=(5, 6), dtype='int')
print(b)
print(b.argmax())  # index of the max element
print(b.min())
print(b.argmin())



