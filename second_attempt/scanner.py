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


class tok():
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line
    def __str__(self):
        return "TOKEN({type}, {value})".format(type=self.type, value=self.value)
    
    def __repr__(self):
        return self.__str__()


class scanner:
    def __init__(self):
        self.position = 0
        self.line = 0
        self.current_char = 0
        self.token_array = []
        self.is_last_line = False
        
    def peek_next_char(self):
        new_position = self.position + 1
        return self.text[new_position]
    
    def advance(self):
        if self.position < len(self.text) - 1:
            self.position += 1
            self.current_char = self.text[self.position]
        else:
            self.current_char = None
            
    def skip_line(self):
        self.line += 1
        
    def get_number(self):
        result = ""
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == "-"):
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_word(self):
        result = ""
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        return result
    
    def get_string_literal(self):
        result = ""
        self.advance()
        while self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()
        return result
    
    def scan(self):
        '''my simple take on the tokeniser'''
        
        while True:
            if self.current_char == None:
                break
            elif self.current_char == " ":
                '''if the char is a space, we continue'''
                self.advance()
                continue
            elif self.current_char == '"':
                '''gets the value of any string literal between double quotes'''
                self.token_array.append(tok(QUOTATION, 0, self.line))
                str_literal = self.get_string_literal()
                self.token_array.append(tok(STR_LITERAL, str_literal, self.line))
                self.token_array.append(tok(QUOTATION, 0, self.line))
                continue
            elif self.current_char.isdigit():
                '''if the current char is a digit, we read until it isn't a digit'''
                integer = self.get_number()
                self.token_array.append(tok(INTEGER, integer, self.line))
                continue
            elif self.current_char.isalpha():
                '''this is for words'''
                word = self.get_word()
                if word in ("if", "else", "elif", "while", "int", "bool", "string", "return",
                            "fn", "and", "or","not"):
                    token = tok(word.upper(), 0, self.line)
                    self.token_array.append(token)
                    continue
                elif word in ("true", "false"):
                    token = tok(BOOL_LITERAL, word.upper(), self.line)
                    self.token_array.append(token)
                    continue
                else:
                    token = tok(IDENTIFIER, word, self.line)
                    self.token_array.append(token)
                    continue
            elif self.current_char == ":":
                self.token_array.append(tok(COLON, 0, self.line))
                
            elif self.token_array == ";":
                self.token_array.append(tok(S_COLON, 0, self.line))
                
            elif self.current_char == "+":
                self.token_array.append(tok(PLUS, 0, self.line))
                
            elif self.current_char == "-":
                if self.peek_next_char().isdigit():
                    number = self.get_number()
                    self.token_array.append(tok(INTEGER, number, self.line))
                else:
                    self.token_array.append(tok(MINUS, 0, self.line))
                    
            elif self.current_char == "(":
                self.token_array.append(tok(L_PAREN, 0, self.line))
                
            elif self.current_char == ")":
                self.token_array.append(tok(R_PAREN, 0, self.line))
                
            elif self.current_char == "{":
                self.token_array.append(tok(L_BRACKET, 0, self.line))
                
            elif self.current_char == "}":
                self.token_array.append(tok(R_BRACKET, 0, self.line))
            
            elif self.current_char == "=":
                self.token_array.append(tok(EQUAL, 0, self.line))
            self.advance()
        
        if self.is_last_line:
            self.token_array.append(tok(EOF, 0, self.line))
                
    
    
    def main(self, text):
        self.text = text
        self.current_char = self.text[self.position]
        self.scan()