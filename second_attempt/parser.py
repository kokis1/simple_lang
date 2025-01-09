########################
## this is where      ##
## all the different  ##
## types of value go  ##
########################
IF = "IF"
ELSE = "ELSE"
WHILE = "WHILE"
INT = "INT"
INTEGER = "INTEGER"
BOOL = "BOOL"
BOOL_LITERAL = "BOOL_LITERAL"
STRING = "STRING"
STR_LITERAL = "STR_LITERAL"
RETURN = "RETURN"
IDENTIFIER = "IDENTIFIER"
FN = "FN"
COLON = "COLON"
S_COLON = "S_COLON"
L_BRACKET = "L_BRACKET"
R_BRACKET = "R_BRACKET"
L_PAREN = "L_PAREN"
R_PAREN = "R_PAREN"
AND = "AND"
OR = "OR"
NOT = "NOT"
PLUS = "PLUS"
MINUS = "MINUS"
TIMES = "TIMES"
DIVIDE = "DIVIDE"
LESS = "LESS"
GREATER = "GREATER"
EQUAL = "EQUAL"
QUOTATION = "QUOTATION"
EOF = "EOF"


class variable_class:
    def __init__(self, type, identifier, value):
        self.type = type
        self.identifier = identifier
        self.value = value


class tok():
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line
    def __str__(self):
        return "TOKEN({type}, {value}) in line {line}".format(type=self.type, value=self.value, line=self.line)
    
    def __repr__(self):
        return self.__str__()

class parser:
    def __init__(self, token_array):
        self.token_array = token_array
        
        
        self.current_token = token_array[0]
        # the stack where things will be popped from
        self.stack = []
        
        # the heap where variables will be left in
        self.heap = []
        
        # what index in the array of tokens the head is looking at
        self.position = 0
        
        # the program counter is a second stack that holds different positions to move the head to
        self.program_counter = []
    
    def advance(self):
        if self.position < len(self.token_array) - 1:
            self.position += 1
            self.current_token = self.token_array[self.position]
        else:
            self.current_token = None
    
    def get_variable(self, identifier):
        for variable in self.heap:
            if variable.identifier == identifier:
                return variable
        else:
            raise Exception("{var} has not been declared in this scope".format(identifier))
    def int_expression(self):
        pass
    
    def int_declaration(self):
        self.advance()
        if self.current_token.type == IDENTIFIER:
            variable = variable_class(INT, self.current_token.value, 0)
        else:
            raise Exception("expected an identifier after int")
        self.advance()
        if self.current_token.type == S_COLON:
            self.heap.append(variable)
            return
        elif self.current_token.type in (IDENTIFIER, INTEGER):
            self.int_expression()
        else:
            raise Exception("unexpected type after identifier")
        self.advance()
        if self.current_token.type != S_COLON:
            raise Exception("excpected semi-colon after declaration")
        value = self.stack.pop()
        variable.value = value
        self.heap.append(variable)
        
    
    def declaration(self):
        if self.current_token.type == INT:
            self.int_declaration()
        elif self.current_token.type == BOOL:
            self.bool_declaration()
        elif self.current_token.type == STRING:
            self.string_declaration()
        elif self.current_token.type == FN:
            self.function_declaration()
    
    def statement(self):
        if self.current_token.type in (INT, BOOL, STRING, FN):
            self.declaration()
    
    def parse(self):
        while self.current_token.type != EOF:
            self.statement()
            self.advance()
    
    def main(self):
        self.parse()