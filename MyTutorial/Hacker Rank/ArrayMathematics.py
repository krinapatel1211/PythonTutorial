import numpy
import math
n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    A = list(input().split())
for i in range(n):
    B = list(input().split())

A = numpy.array(A, int)
B = numpy.array(B, int)
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
