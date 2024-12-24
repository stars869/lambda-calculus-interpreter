from typing import List, Union

from lexer import TokenType, Token 


type Expr = Union[Variable, Abstraction, Application]

class Variable:
    def __init__(self, token : Token):
        assert(token.type == TokenType.SYMBOL)
        self.name = token.value

    def __repr__(self):
        return self.name

class Abstraction:
    def __init__(self, param : Variable, body : Expr):
        self.param = param
        self.body = body

    def __repr__(self):
        return f"(λ{self.param}.{self.body})"

class Application:
    def __init__(self, func : Expr, arg : Expr):
        self.func = func
        self.arg = arg

    def __repr__(self):
        return f"({self.func} {self.arg})"
    
class Claim:
    def __init__(self, var : Variable, expr : Expr):
        self.var = var
        self.expr = expr 

    def __repr__(self):
        return f"{self.var} : {self.expr}"


class Define:
    def __init__(self, var : Variable, expr : Expr):
        self.var = var
        self.expr = expr 

    def __repr__(self):
        return f"{self.var} = {self.expr}"
    

