import capstone
import os

base = 0x400000
inst_start_addr = 0x401adf - base
inst_end_addr = 0x808c9c - base

with open("./try_me", "rb") as file:
    data = file.read()[inst_start_addr:inst_end_addr]

#print(data)
engine = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)

instructions = []
for inst_data in engine.disasm(data, 0):
    inst = f"{inst_data.mnemonic} {inst_data.op_str}"
    inst = inst.strip()
    if inst_data.mnemonic == 'endbr64':
        print(inst_data.address)
    instructions.append(inst)
 
block = bytearray(b'\x17X\xB4\xBD\x94\xEB\v\x81')
block.reverse()
encoded = block

block = bytearray(b'\x11\xAAb\xCB\xD0c\xB5P')
block.reverse()
encoded += block

block = bytearray(b'\xD9\x19_\x0F\x8E\xE9\x87w')
block.reverse()
encoded += block

block = bytearray(b'\x01\x99\xE9\x91\xE4\xF0\xC2\')
block.reverse()
encoded += block

print(encoded)
instructions.reverse()
print(instructions[-1])
for test_inst in instructions:
    test_inst = test_inst.split()
    index = 0
    if (len(test_inst) > 4):
        try:
            if (test_inst[4] == '+'):
                index = test_inst[5][:-2]
                index = int(index, 16)
            else:
                index = 0
        except:
            print(test_inst)
            break
        mnemonic = test_inst[0]
        value = test_inst[-1]
        value = int(value, 16)
        try:
            if (mnemonic == 'add'):
                encoded[index] = (encoded[index] - value) & 0xff
            if (mnemonic == 'sub'):
                encoded[index] = (encoded[index] + value) & 0xff
            if (mnemonic == 'xor'):
                encoded[index] ^= value & 0xff
        except:
            print(test_inst)
            print(encoded[index], value)
            break
print(encoded)

