import csv
import sys



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


def main():
    try: sys.argv[1]
    
    except:
        while True:
            text = input("> ")
            if text == "quit":
                break
            else:
                lex = lexer(text, "syntax_and_keywords.csv")
                lex.main()
                print(lex.token_array)
    else:
        text = sys.argv[1]
        lex = lexer(text, "syntax_and_keywords.csv")
        lex.main()
        print(lex.token_array)
main() 