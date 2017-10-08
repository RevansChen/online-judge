# Python - 3.4.3

class Interpreter:
    def __init__(self, program):
        self.SetProgram(program)
        
        # 將指令與對應的函數做關聯
        self.__methods = {
            'mov': self.__mov,
            'inc': self.__inc,
            'dec': self.__dec,
            'add': self.__add,
            'sub': self.__sub,
            'mul': self.__mul,
            'div': self.__div,
            'cmp': self.__cmp,
            'jmp': self.__jmp,
            'jne': self.__jne,
            'je': self.__je,
            'jge': self.__jge,
            'jg': self.__jg,
            'jle': self.__jle,
            'jl': self.__jl,
            'call': self.__call,
            'ret': self.__ret,
            'msg': self.__msg,
            'end': self.__end
        }
    
    def __mov(self, params):
        regName, value = params
        self.__registers[regName] = self.__getValue(value)
        self.__insPtr += 1
    
    def __inc(self, params):
        regName = params[0]
        self.__registers[regName] += 1
        self.__insPtr += 1
    
    def __dec(self, params):
        regName = params[0]
        self.__registers[regName] -= 1
        self.__insPtr += 1
    
    def __add(self, params):
        regName, value = params
        self.__registers[regName] += self.__getValue(value)
        self.__insPtr += 1
        
    def __sub(self, params):
        regName, value = params
        self.__registers[regName] -= self.__getValue(value)
        self.__insPtr += 1
    
    def __mul(self, params):
        regName, value = params
        self.__registers[regName] *= self.__getValue(value)
        self.__insPtr += 1
    
    def __div(self, params):
        regName, value = params
        self.__registers[regName] //= self.__getValue(value)
        self.__insPtr += 1
    
    def __cmp(self, params):
        x, y = params
        x = self.__getValue(x)
        y = self.__getValue(y)
        self.__isEqual = (x == y)
        self.__isGreater = (x > y)
        self.__isLess = (x < y)
        self.__insPtr += 1
    
    def __jumpWrap(self, labelName, condition):
        if condition:
            self.__insPtr = self.__labels[labelName]
        else:
            self.__insPtr += 1
    
    def __jmp(self, params):
        self.__jumpWrap(params[0], True)
    
    def __jne(self, params):
        self.__jumpWrap(params[0], not self.__isEqual)
    
    def __je(self, params):
        self.__jumpWrap(params[0], self.__isEqual)
    
    def __jge(self, params):
        self.__jumpWrap(params[0], not self.__isLess)
    
    def __jg(self, params):
        self.__jumpWrap(params[0], self.__isGreater)
    
    def __jle(self, params):
        self.__jumpWrap(params[0], not self.__isGreater)
    
    def __jl(self, params):
        self.__jumpWrap(params[0], self.__isLess)
    
    def __call(self, params):
        self.__stack.append(self.__insPtr)
        self.__jumpWrap(params[0], True)
    
    def __ret(self, params):
        ptr = self.__stack.pop()
        self.__insPtr = ptr + 1
        
    def __msg(self, params):
        for param in params:
            if param[0] == "'":
                self.__output += param[1:-1]
            else:
                self.__output += str(self.__getValue(param))
        self.__insPtr += 1
    
    def __end(self, params):
        self.__insPtr = len(self.__instructions)
        self.__isEnd = True
    
    def __getValue(self, x):
        if x.isalpha():
            return self.__registers[x]
        else:
            return int(x)
    
    # 將所有指令碼拆解成 指令 與 參數
    def SetProgram(self, program):
        self.__instructions = []
        self.__labels = {}
        
        ptr = 0
        for p in program.splitlines():
            p = p.strip()   # 去除頭尾的空白
            tmp = p.split(' ', 1)
            cmd = tmp[0]
            if len(tmp) > 1:
                p = tmp[1].strip()
            else:
                p = ''
                
            # 跳過空行, 或註解行
            if len(cmd) == 0 or cmd == ';':
                continue
            
            # 是標籤, 紀錄標籤位址
            if cmd[-1] == ':':
                self.__labels[cmd[:-1]] = ptr
                continue
                
            params = []
            while len(p):
                if p[0] == ';':
                    # 後面為註解, 不需要處理
                    break
                elif p[0] == ',':
                    # 吃掉分隔符號
                    p = p[1:]
                elif p[0] == "'":
                    # 字串常數
                    end = p.find("'", 1)
                    params.append(p[:end + 1])
                    p = p[end + 1:]
                else:
                    # 整數常數或暫存器名稱
                    i = 0
                    for c in p:
                        if c == ' ' or c == ';' or c == ',':
                            break
                        i += 1
                    params.append(p[:i])
                    p = p[i:]
                    
                p = p.strip()
            
            self.__instructions.append((cmd, params))
            ptr += 1
    
    def Run(self):
        self.__insPtr = 0           # 指令指標
        self.__registers = {}       # 暫存器
        self.__output = ''          # 輸出
        self.__stack = []           # 呼叫堆疊
        self.__isEqual = False      # je, jne
        self.__isGreater = False    # jg, jle
        self.__isLess = False       # jl, jge
        self.__isEnd = False        # 是否執行到 end
        
        # 執行到所有指令都執行過為止
        while self.__insPtr < len(self.__instructions):
            cmd, params = self.__instructions[self.__insPtr]
            self.__methods[cmd](params)
        
        # 沒有執行到end的結束程式都回傳-1
        return self.__output if self.__isEnd else -1

def assembler_interpreter(program):
    return Interpreter(program).Run()