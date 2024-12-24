from lexer import Lexer
from parser import Parser


source_code = """
    (claim id ((-> A) A))
    (define id (lam x x))
    """

tokens = Lexer(source_code).tokenize()
parser = Parser(tokens)

while (statment := parser.parse()):
    print(statment)