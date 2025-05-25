from ctypes import c_uint32
import sys

def hash(value, seed):
    result = seed
    for char in value:
        result = c_uint32((ord(char) ^ result) * 0x1000193).value
    return result

seed = int(sys.argv[2],16)
names = open("names", "r").readlines()
for name in names:
    if hash(name.strip(), seed) == int(sys.argv[1],16):
        print(name)
        break

