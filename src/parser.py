from typing import List, Optional, Tuple, Union
from lexer import TokenType, Token 
from expr import Variable, Abstraction, Application, Expr, Claim, Define

class Parser:
    def __init__(self, tokens : List[Token]):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def advance(self):
        if self.position < len(self.tokens):
            self.position += 1

    def parse(self):
        token = self.peek()
        if token is None:
            return None 
        
        if token.type == TokenType.LPAREN: 
            self.advance() 
            token = self.peek()
            
            if token.type == TokenType.CLAIM:
                statment = self._parse_claim()
            elif token.type == TokenType.DEFINE:
                statment = self._parse_define()
            elif token.type == TokenType.LAMBDA:
                statment = self._parse_abstraction()
            elif token.type == TokenType.SYMBOL:
                statment = self._parse_application()
            elif token.type == TokenType.LPAREN:
                statment = self._parse_application()    
            else:
                return ValueError("Unexpected token")

            if self.peek() and self.peek().type == TokenType.RPAREN:
                self.advance() 
            else:
                raise ValueError("Unmatched parenthesis")
            
            return statment 
    
        elif token.type == TokenType.SYMBOL: 
            self.advance()
            return Variable(token)
        
        else:
            raise ValueError(f"Unexpected token: {token}")

    def _parse_claim(self):
        token = self.peek()
        assert(token.type == TokenType.CLAIM)
        self.advance()

        token = self.peek()
        assert(token.type == TokenType.SYMBOL)
        var = Variable(token)
        self.advance()

        expr = self.parse()
        assert(type(expr) is Variable or type(expr) is Abstraction or type(expr) is Application)

        return Claim(var, expr)

    def _parse_define(self):
        token = self.peek()
        assert(token.type == TokenType.DEFINE)
        self.advance()

        token = self.peek()
        assert(token.type == TokenType.SYMBOL)
        var = Variable(token)
        self.advance()

        expr = self.parse()
        assert(type(expr) is Variable or type(expr) is Abstraction or type(expr) is Application)

        return Define(var, expr)

    def _parse_abstraction(self):
        token = self.peek()
        assert(token.type == TokenType.LAMBDA)
        self.advance()

        token = self.peek()
        assert(token.type == TokenType.SYMBOL)
        var = Variable(token)
        self.advance()

        expr = self.parse()
        assert(type(expr) is Variable or type(expr) is Abstraction or type(expr) is Application)

        return Abstraction(var, expr)

    def _parse_application(self):
        token = self.peek()
        if token.type is TokenType.SYMBOL:
            expr1 = Variable(token)
            self.advance()
        elif token.type is TokenType.LPAREN:
            expr1 = self.parse()
        
        assert(type(expr1) is Variable or type(expr1) is Abstraction or type(expr1) is Application)

        token = self.peek()
        if token.type is TokenType.SYMBOL:
            expr2 = Variable(token)
            self.advance()
        elif token.type is TokenType.LPAREN:
            expr2 = self.parse()

        assert(type(expr2) is Variable or type(expr2) is Abstraction or type(expr2) is Application)

        return Application(expr1, expr2)


if __name__ == "__main__":
    source = '(claim square ((-> Nat) ((-> Nat) Nat))) (define square (lam x ((* x) x))) "Hello, World!" 42 -15'
    
    from lexer import Lexer
    tokens = Lexer(source).tokenize()

    parser = Parser(tokens)
    
    try:
        ast = parser.parse()
        print("AST:", ast)
        ast = parser.parse()
        print("AST:", ast)
        ast = parser.parse()
        print("AST:", ast)
        ast = parser.parse()
        print("AST:", ast)
        ast = parser.parse()
        print("AST:", ast)
        ast = parser.parse()
        print("AST:", ast)
        ast = parser.parse()
        print("AST:", ast)
        ast = parser.parse()
        print("AST:", ast)
        
    except ValueError as e:
        print("Error:", e)