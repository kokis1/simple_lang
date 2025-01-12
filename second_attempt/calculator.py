from scanner import *
from syntax import *

class cal_parser():
    def __init__(self, token_array):
        self.stack = []
        self.position = 0
        self.token_array = token_array
        self.current_token = token_array[self.position]
    
    def advance(self):
        if self.position < len(self.token_array) - 1:
            self.position += 1
            self.current_token = self.token_array[self.position]
        else:
            self.current_token = self.token_array[-1]
    
    def main(self):
        while self.current_token.type != EOF:
            if self.current_token.type == INTEGER:
                self.stack.append(self.current_token.value)
            elif self.current_token.type in (PLUS, MINUS, TIMES, DIVIDE):
                rhs = self.stack.pop()
                lhs = self.stack.pop()
                if self.current_token.type == PLUS:
                    self.stack.append(lhs + rhs)
                elif self.current_token.type == MINUS:
                    self.stack.append(lhs - rhs)
                elif self.current_token.type == TIMES:
                    self.stack.append(lhs * rhs)
                elif self.current_token.type == DIVIDE:
                    self.stack.append(lhs / rhs)
            elif self.current_token.type == S_COLON:
                print(self.stack.pop())
            self.advance()