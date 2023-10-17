from reversing import *
from pwn import xor

import time
bufa = b'\x00'*1
bufb = b'\x00'*1
N = 10000
def func1():
    for i in range(N):
        xorb(bufa,bufb)
def func2():
    for i in range(N):
        xor(bufa,bufb)
x = time.time()
func1()
x1 = time.time()
print("rev: ", x1-x)
func2()
x2 = time.time()
print("pwn: ", x2-x1)
