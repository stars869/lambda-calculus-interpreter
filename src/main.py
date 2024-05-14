from parse_file import file_parser
from parse_expr import expr_parser
from serialize import serialize_expr
from normalize import normalize

if __name__ == "__main__":
    file = open("./test/test.lambda", "r")
    bindings = list(map(
        lambda p: (p[0], expr_parser.parse(p[1])), 
        file_parser.parse(file.read())
    ))
    env = {}
    
    for (name, expr) in bindings:
        assert(name not in env)

        norm_expr = normalize(expr, env)

        print(f"{name} = {serialize_expr(expr)}")
        print(f"{name} = {serialize_expr(norm_expr)}")
        print()

        env[name] = norm_expr