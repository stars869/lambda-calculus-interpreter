from parse_file import file_parser
from parse_expr import expr_parser
from serialize import serialize_expr
from normalize import normalize

if __name__ == "__main__":
    file = open("./test/test.lambda", "r")
    bindings = file_parser.parse(file.read())
    env = {}
    
    for (name, expr_str) in bindings:
        assert(name not in env)

        expr = expr_parser.parse(expr_str)
        norm_expr = normalize(expr, env)

        print(f"{name} = {serialize_expr(expr)}")
        print(f"{name} = {serialize_expr(norm_expr)}")
        print()

        env[name] = norm_expr