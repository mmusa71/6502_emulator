class ALU:
    def __init__(self, registers):
        self.status = {} 
        


    def decode(self, instruction):
        self.current_instruction = instruction 
    
    def perform_operation(self, operation, registers, memory):
        pass 


class processor:
    def __init__(self):
        self.registers = {
                'A':0x00, 
                'X': 0xA0, 
                'Y':0x00, 
                'PC':0x00, 
                'SP': 0x00
                }
        self.status_reg = {}

    #next operation     
    def next():
        pass 




#Memory is a list of 8-bit values, indexed from 0 up to 65535 (2^16) 

memory = [0x0a, 0x00] + [0x00]*1023

def get_memory_content(address):
    return memory[address]

def set_memory(address, value):
    memory[address] = value 


