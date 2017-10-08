# Python - 3.4.3

class Interpreter:
    def __init__(self, program):
        self.SetProgram(program)
        
        # 將指令與對應的函數做關聯
        self.__methods = {
            'mov': self.__mov,
            'inc': self.__inc,
            'dec': self.__dec,
            'jnz': self.__jnz
        }
    
    def __mov(self, params):
        regName, value = params
        if value.isalpha():
            value = self.__registers[value]
        else:
            value = int(value)
            
        self.__registers[regName] = value
        self.__insPtr += 1
    
    def __inc(self, params):
        regName = params[0]
        
        self.__registers[regName] += 1
        self.__insPtr += 1
    
    def __dec(self, params):
        regName = params[0]
        
        self.__registers[regName] -= 1
        self.__insPtr += 1
        
    def __jnz(self, params):
        value, offset = params
        if value.isalpha():
            value = self.__registers[value]
        else:
            value = int(value)
        
        if value != 0:
            self.__insPtr += int(offset)
        else:
            self.__insPtr += 1
    
    # 將所有指令碼拆解成 指令 與 參數
    def SetProgram(self, program):
        self.__instructions = []
        for code in program:
            cmd, *params = code.split(' ')
            self.__instructions.append((cmd, params))
    
    def Run(self):
        self.__insPtr = 0       # 指令指標
        self.__registers = {}   # 暫存器
        
        # 執行到所有指令都執行過為止
        while self.__insPtr < len(self.__instructions):
            cmd, params = self.__instructions[self.__insPtr]
            self.__methods[cmd](params)
        
        return self.__registers

def simple_assembler(program):
    return Interpreter(program).Run()