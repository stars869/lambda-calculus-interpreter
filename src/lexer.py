from enum import Enum, auto

class TokenType(Enum):
    LPAREN = auto()
    RPAREN = auto()
    CLAIM = auto()
    DEFINE = auto()
    LAMBDA = auto()
    SYMBOL = auto() 
    EOF = auto() 

class Token:
    def __init__(self, token_type : TokenType, value : str):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0

    def peek(self):
        if self.position < len(self.source_code):
            return self.source_code[self.position]
        return None  

    def advance(self):
        if self.position < len(self.source_code):
            self.position += 1

    def tokenize(self):
        tokens = []
        while (current := self.peek()) is not None:
            if current.isspace():
                self.advance() 
            elif current == '(':
                tokens.append(Token(TokenType.LPAREN, '('))
                self.advance()
            elif current == ')':
                tokens.append(Token(TokenType.RPAREN, ')'))
                self.advance()
            else:
                tokens.append(self._consume_symbol())
        return tokens

    def _consume_symbol(self):
        start = self.position
        while self.peek() and not self.peek().isspace() and self.peek() not in '()':
            self.advance()
        value = self.source_code[start:self.position]
        
        if value == "claim":
            return Token(TokenType.CLAIM, value)
        elif value == "define":
            return Token(TokenType.DEFINE, value) 
        elif value == "lam":
            return Token(TokenType.LAMBDA, value)   
        else:
            return Token(TokenType.SYMBOL, value)
    

if __name__ == "__main__":
    source = "(claim square (-> Nat (-> Nat Nat))) (define square (lam x (* x x))) 'Hello, World!' 42 -15"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)

    