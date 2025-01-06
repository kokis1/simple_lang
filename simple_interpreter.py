'''this is a shell script to run within the command line'''

# list of types
INTEGER = "INTEGER"
PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
S_COLON = "S-_COLON"
WORD = "WORD"
INT = "int"
WHILE = "while"
IF = "if"
ELSE = "else"
ELIF = "ELIF"
RETURN = "return"
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
    
def integer(text, position):
    result = ""
    while position < len(text):
        current_char = text[position]
        if current_char.isdigit():
            result += current_char
            position += 1
        else:
            break
    return int(result), position - 1


def word(text, position):
    result = ""
    current_char = "a"
    while position < len(text):
        current_char = text[position]
        if current_char.isalpha():
            result += current_char
            position += 1
        else:
            break
    return result, position - 1

def check_for_keywords(word, keyword_list):
    if word in keyword_list:
        return True
    else: return False

def tokeniser(text):
    position = 0
    token_array = []
    current_char = text[position]
    while position < len(text):
        current_char = text[position]
        if current_char == " ":
            position += 1
            continue
        if current_char.isdigit():
            result, position = integer(text, position)
            token_array.append(tok(INTEGER, result))
            position += 1
            continue
        if current_char.isalpha():
            result, position = word(text, position)
            if check_for_keywords(result, ["int", "while", "if", "else", "elif", "return"]):
                token = tok(result.capitalize, 0)
            else:
                token = tok(WORD, result)
            token_array.append(token)
            position += 1
            continue
        if current_char == "+":
            token_array.append(tok(PLUS, 0))
            position += 1
            continue
        if current_char == "-":
            token_array.append(tok(MINUS,0))
            position += 1
            continue
        if current_char == "*":
            token_array.append(tok(MULTIPLY, 0))
            position += 1
            continue
        if current_char == "/":
            token_array.append(tok(DIVIDE, 0))
            position += 1
            continue
        if current_char == ";":
            token_array.append(tok(S_COLON, 0))
            position += 1
            continue
        raise Exception("trouble lexing the text")
    token_array.append(tok(EOF, 0))
    return token_array

def parser(token_array, position):
    current_token = token_array[position]
    
    values = []
    
    '''expression | declaration'''
    if current_token.type == INTEGER:
        values.append(current_token.value)
        position += 1
        current_token = token_array[position]
        if current_token.type == INTEGER:
            values.append(current_token.value)
            position += 1
            current_token = token_array[position]
            if current_token.type in (PLUS, MINUS, MULTIPLY, DIVIDE):
                operator = current_token
                position += 1
                current_token = token_array[position]
                if current_token.type != S_COLON:
                    raise Exception("a semi-colon must be at the end of an expression")
                else:
                    result = values.pop(0)
                    for value in values:
                        if operator.type == PLUS:
                            result += value
                        elif operator.type == MINUS:
                            result -= value
                        elif operator.type == MULTIPLY:
                            result *= value
                        elif operator.type == DIVIDE:
                            result /= value
                    print(result)
            else:
                raise Exception("an operator must follow a pair of integers")
        else:
            raise Exception("an integer must follow an integer in an expression")
    # returns if the parser has reached the end of the file
    elif current_token.type == EOF:
        return
    else:
        parser(token_array, position)
    

def main():
    while True:
        text = input("calc> ")
        if text == "quit":
            print("exiting the language")
            break
        else:
            position = 0
            token_array = tokeniser(text)
            parser(token_array, position)
main()