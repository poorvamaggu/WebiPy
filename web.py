import ply.lex as lex

# Define the list of token names
tokens = (
    'IDENTIFIER',
    'INTEGER',
    'FLOAT',
    'STRING',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'ASYNC',
    'SECURE',
    'HTTP_REQUEST',
    'DATABASE',
    'XSS',
    'NEWLINE',
    'ASSIGN',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'FUNCTION',
    'CLASS',
    'RETURN',
    'TRUE',
    'FALSE',
    'AND',
    'OR',
    'NOT',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'EQUAL',
    'NOT_EQUAL',
    'DOT',
    'COMMA',
    'COLON',
    'SEMICOLON',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'AT_SYMBOL',
    'BACKTICK',
    'AMPERSAND',
    'PIPE',
    'CARET',
    'MODULO'
)

# Define regular expressions for some of the tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_NEWLINE = r'\n'

# Define a rule for IDENTIFIER
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Define a rule for INTEGER
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule for FLOAT
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Define a rule for STRING
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove double quotes
    return t

# Define keywords
reserved = {
    'async': 'ASYNC',
    'secure': 'SECURE',
    'http_request': 'HTTP_REQUEST',
    'database': 'DATABASE',
    'xss': 'XSS',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'class': 'CLASS',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
}

# ... (rules for the remaining tokens)

# A rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A rule to ignore whitespace and tabs
t_ignore = ' \t'

# A rule to handle comments (for illustration purposes, you can expand this)
def t_COMMENT(t):
    r'\#.*'
    pass

# A rule for handling errors
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Create a function to build the lexer
def build_lexer():
    lexer = lex.lex()
    return lexer

# Example input code
webipy_code = """
async def secure_example():
    if x > 0:
        return x
    else:
        return -x
    for i in range(10):
        print(i)
    function add(a, b):
        return a + b
    class MyClass:
        def __init__(self):
            self.value = 0
"""

# Create a function to tokenize the input code
def tokenize_code(lexer, code):
    lexer.input(code)
    tokens = []
    for token in lexer:
        tokens.append(token)
    return tokens

if __name__ == "__main__":
    # Build the lexer
    lexer = build_lexer()

    # Tokenize and print the output
    tokens = tokenize_code(lexer, webipy_code)
    for token in tokens:
        print(token)
