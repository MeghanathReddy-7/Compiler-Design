class Compiler: 
    def __init__(self): 
        self.temp_count = 0 
        self.ls = [] 
    def generate_temp(self): 
        temp_name = f"t{self.temp_count}" 
        print(temp_name) 
        self.temp_count += 1 
        return temp_name 
    def compile_expression(self, expression): 
        tokens = expression.split() 
        result=tokens[0] 
        for i in range(1, len(tokens), 2): 
            flag = 0 
            if len(tokens[i+1])==2: 
                flag = 1 
                temp1 = self.generate_temp() 
                print(f"{temp1} = {tokens[i+1]}") 
                self.ls.append(f"{temp1} = {tokens[i+1]}") 
            op = tokens[i]  
            operand = tokens[i+1] 
            temp = self.generate_temp() 
            if flag == 1: 
                operand = temp1 
            print(f"{temp} = {result} {op} {operand}") 
            self.ls.append(f"{temp} = {result} {op} {operand}") 
            result = temp 
        return result 
    def compile_assignment(self, assignment): 
        var, expr = assignment.split(' = ') 
        result = self.compile_expression(expr) 
        print(f"{var} = {result}") 
        self.ls.append(f"{var} = {result}") 
    def compile(self, code): 
        statements = code.split(';') 
        for statement in statements: 
            if '=' in statement: 
                self.compile_assignment(statement.strip()) 
            elif statement.strip(): 
                self.compile_expression(statement.strip()) 
    def convertToAsm(self): 
        print(self.ls) 
        for i in self.ls: 
            var,expr = i.split(' = ') 
            print(f"MOV {var} {self.evalExpr(expr)}") 
    def evalExpr(self,expr): 
        if len(expr)==2: 
            return expr 
        tokens = expr.split() 
        if tokens[1]=='+': 
            print(f"ADD {tokens[0]} {tokens[2]}") 
            return tokens[0] 
        if tokens[1]=='*': 
            print(f"MUL {tokens[0]} {tokens[2]}") 
            return tokens[0] 
        return expr 
compiler = Compiler() 
code = """ 
a = b * c + f * -e ; 
"""  
compiler.compile(code) 
# print(set(compiler.ls)) 
compiler.convertToAsm()