from parsec import (spaces, string, regex, generate, many, many1)

lexeme = lambda p: p << regex(r' *')

symbol = lexeme(regex(r'[_a-zA-Z][_a-zA-Z0-9]*'))
assign = lexeme(string('='))
expr_body = regex(r'[^\n]*')

empty_line = regex(r'\s*\n')
comment_line = regex(r'--.*\n')

@generate
def line():
    s = yield symbol 
    yield assign
    e = yield expr_body
    yield regex(r'\n')
    return (s, e)

@generate 
def file():
    yield many(empty_line)
    yield many(comment_line)
    ls = yield many(line << many(empty_line ^ comment_line)) 
    return ls 

file_parser = file

if __name__ == "__main__":
    f = open("./test/test.lambda", "r")
    text = f.read()
    print(file_parser.parse(text))