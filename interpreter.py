import csv

# list of types
INTEGER = "INTEGER"
ADD = "ADD"
MINUS = "MINUS"
UPSHIFT = "UPSHIFT"
DOWNSHIFT = "DOWNSHIFT"
S_COLON = "S_COLON"
WORD = "WORD"
INT = "INT"
WHILE = "WHILE"
IF = "IF"
ELSE = "ELSE"
ELIF = "ELIF"
RETURN = "RETURN"
BOOL = "BOOL"
TRUE = "TRUE"
FALSE = "FALSE"
EOF = "EOF"


class tok:
    '''basically a struct holding a type and a value for each token'''
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __str__(self):
        return "TOKEN({type}, {value})".format(type=self.type, value=self.value)
    
    def __repr__(self):
        return self.__str__()
    
class lexer:
    def __init__(self, text, syntax_filepath):
        self.position = 0
        self.current_char = text[self.position]
        self.text = text
        self.token_array = []
        self.keywords = dict()
        self.syntax_filepath = syntax_filepath
        
        
    def read_keywords(self):
        self.keywords = dict()
        with open(self.syntax_filepath, "r", newline="") as file:
            reader = csv.reader(file)
            for line in reader:
                self.keywords[str(line[1])] = str(line[0])
                
    
    def advance(self):
        '''advances the position of the current char in the text, and returns None if the end of the text has been reached'''
        if self.position < len(self.text) - 1:
            self.position += 1
            self.current_char = self.text[self.position]
        else: self.current_char =  None
    
    def tokeniser(self):
          while self.current_char is not None:  
            result = ""
            while self.current_char is not None and not (result in self.keywords):
                result += self.current_char
                self.advance()
                if self.current_char == None:
                    break
                if self.current_char == " ":
                    self.advance()
                    break
                if self.current_char in self.keywords:
                    break
            
            if result in self.keywords:
                token = tok(self.keywords[result], 0)
                self.token_array.append(token)
            
            elif result.isalnum():
                if result.isdigit():
                    token = tok("INTEGER", int(result))
                    self.token_array.append(token)
                else:
                    token = tok("WORD", result)
                    self.token_array.append(token)
            
            elif result == None:
                token = tok("None", 0)
                self.token_array.append(token)
            
            else:
                raise Exception("unrecognised character: {}".format(self.current_char))
            
    
    def main(self):
        self.read_keywords()
        self.tokeniser()

class parser:
    def __init__(self, token_array, keywords):
        self.token_array = token_array
        self.heap = dict()
        self.stack = []
        self.program_counter = []
        self.position = 0
        self.current_token = self.token_array[self.position]
        self.keywords = keywords
    
    def error(self, type, message):
        if self.current_token.type != type:
            raise Exception(message)
    
    def get_next_token(self):
        if self.position < len(self.token_array) - 1:
            self.position += 1
            self.current_token = self.token_array[self.position]
            return
        self.current_token = tok(EOF, 0)
    
    def eat(self, type, message):
        self.get_next_token()
        self.error(type, message)
    
    
    
    def expression(self):
        '''(INTEGER | VARIABLE) (S_COLON | (INTEGER | VARIABLE) OPERATOR S_COLON)
                    e.g x 56 +;
                    or 56;'''
        if self.current_token.type == INTEGER:
            self.stack.append(self.current_token.value)
        elif self.current_token.type == WORD:
            if self.current_token.value in self.heap:
                self.stack.append(self.heap[self.current_token.value])
            else:
                raise Exception("variable {} has not been declared".format(self.current_token.value))
        self.get_next_token()
        if self.current_token.type == S_COLON:
            return
        elif self.current_token.type == INTEGER:
            self.stack.append(self.current_token.value)
        elif self.current_token.type == WORD:
            if self.current_token.value in self.heap:
                self.stack.append(self.heap[self.current_token.value])
            else:
                raise Exception("variable {} has not been declared".format(self.current_token.value))
        self.get_next_token()
        operator = self.current_token
        if not(self.current_token.type in (ADD, MINUS)):
            raise Exception("an operator must follow an expression")
        self.get_next_token()
        if self.current_token.type != S_COLON:
            raise Exception("a semi colon must follow an expression")
        rhs = self.stack.pop()
        lhs = self.stack.pop()
        if operator.type == ADD:
            self.stack.append(lhs + rhs)
        elif operator.type == MINUS:
            self.stack.append(lhs - rhs)
        
        
    def declare_int(self):
        '''INT WORD ((EXPRESSION | S_COLON) | S_COLON)'''
        self.eat("WORD", "word must follow integer declaration")        
        self.stack.append(self.current_token.value)
        self.get_next_token()
        
        if self.current_token.type != S_COLON:
            self.expression()
            value = self.stack.pop()
            name = self.stack.pop()
            self.heap[name] = value
        else:
            name = self.stack.pop()
            self.heap[name] = 0
        
        
    
    def program(self):
        '''INT_DECLARE | BOOL | WHILE | IF | EXPRESSION'''
        while True:
            if self.current_token.type in (INTEGER, WORD):
                self.expression()
                print(self.stack)
                print(self.heap)
                
            elif self.current_token.type == INT:
                self.declare_int()
                print(self.heap)
                
            break
    
    def main(self):
        self.program()

class interpreter():
    def __init__(self):
        pass
    
    def get_input(self):
        self.text = input("calc> ")
    def main(self):
        self.get_input()
        self.lex = lexer(self.text, "syntax_and_keywords.csv")
        self.lex.main()
        self.token_array = self.lex.token_array
        self.parse = parser(self.token_array, self.lex.keywords)
        self.parse.main()

        while self.text != "quit":
            self.get_input()
            self.lex.text = self.text
            self.lex.main()
            self.parse.token_array = self.lex.token_array
            self.parse.main()
                        

                        
interp = interpreter()
interp.main()