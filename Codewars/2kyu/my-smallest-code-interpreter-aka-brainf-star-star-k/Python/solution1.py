# Python - 2.7.6

class memory:
    MIN_VALUE = 0
    MAX_VALUE = 255
    
    def __init__(self):
        self.reset()

    def set(self, value):
        self.__data[self.__index] = value
        
    def get(self):
        return self.__data[self.__index]
    
    def reset(self):
        self.__data = [self.MIN_VALUE]
        self.__index = 0

    def next(self):
        self.__index += 1
        if self.__index == len(self.__data):
            self.__data.append(self.MIN_VALUE)

    def prev(self):
        self.__index -= 1

    def inc(self):
        if self.get() == self.MAX_VALUE:
            self.set(self.MIN_VALUE)
        else:
            self.set(self.get() + 1)

    def dec(self):
        if self.get() == self.MIN_VALUE:
            self.set(self.MAX_VALUE)
        else:
            self.set(self.get() - 1)

class instructions:
    def __init__(self):
        self.__index = 0

    def setCode(self, code):
        self.__code = code
        self.__index = 0

    def finish(self):
        return self.__index == len(self.__code)
    
    def current(self):
        return self.__code[self.__index]

    def next(self):
        self.__index += 1

    def prev(self):
        self.__index -= 1
        
    def back(self):
        cnt = 0
        while self.__index >= 0:
            ins = self.current()
            if ins == brainfuck.INSTRUCTION_RIGHT:
                cnt += 1
            elif ins == brainfuck.INSTRUCTION_LEFT:
                cnt -= 1
            self.prev()
                
            if cnt == 0:
                self.next()
                break

    def forward(self):
        cnt = 0
        while not self.finish():
            ins = self.current()
            if ins == brainfuck.INSTRUCTION_RIGHT:
                cnt -= 1
            elif ins == brainfuck.INSTRUCTION_LEFT:
                cnt += 1
            self.next()
            
            if cnt == 0:
                break
        
class brainfuck:
    INSTRUCTION_INCPTR = '>'
    INSTRUCTION_DECPTR = '<'
    INSTRUCTION_INC    = '+'
    INSTRUCTION_DEC    = '-'
    INSTRUCTION_INPUT  = ','
    INSTRUCTION_OUTPUT = '.'
    INSTRUCTION_LEFT   = '['
    INSTRUCTION_RIGHT  = ']'
    
    def __init__(self):
        self.__data = memory()
        self.__instructions = instructions()
        self.__input = ''
        self.__output = ''
        self.__operatorInstrucions = [self.INSTRUCTION_INCPTR,
                                      self.INSTRUCTION_DECPTR,
                                      self.INSTRUCTION_INC,
                                      self.INSTRUCTION_DEC,
                                      self.INSTRUCTION_INPUT,
                                      self.INSTRUCTION_OUTPUT]

    def __operator(self, instruction, input = ''):
        if instruction == self.INSTRUCTION_INCPTR:
            self.__data.next()
        elif instruction == self.INSTRUCTION_DECPTR:
            self.__data.prev()
        elif instruction == self.INSTRUCTION_INC:
            self.__data.inc()
        elif instruction == self.INSTRUCTION_DEC:
            self.__data.dec()
        elif instruction == self.INSTRUCTION_OUTPUT:
            self.__output += chr(self.__data.get())
        elif instruction == self.INSTRUCTION_INPUT:
            self.__data.set(ord(input))
        self.__instructions.next()
                
    def execute(self, code, input):
        self.__instructions.setCode(code)
        self.__output = ''
        self.__data.reset()

        input = list(input)
        while not self.__instructions.finish():
            instruction = self.__instructions.current()

            if instruction in self.__operatorInstrucions:
                if instruction == self.INSTRUCTION_INPUT:
                    self.__operator(instruction, input.pop(0))
                else:
                    self.__operator(instruction)
            elif instruction == self.INSTRUCTION_LEFT:
                d = self.__data.get()
                if d == 0:
                    self.__instructions.forward()
                else:
                    self.__instructions.next()
            elif instruction == self.INSTRUCTION_RIGHT:
                d = self.__data.get()
                if d > 0:
                    self.__instructions.back()
                else:
                    self.__instructions.next()
            else:
                break
            
        return self.__output

def brain_luck(code, input):
    b = brainfuck()
    return b.execute(code, input)