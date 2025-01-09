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


