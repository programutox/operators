def _operator(op_name, n):
    if not isinstance(n, int):
        raise TypeError(f"Expected int, found {type(n)}")
    return op_name, n


plus       = lambda n : _operator("plus", n)
minus      = lambda n : _operator("minus", n)
times      = lambda n : _operator("times", n)
divided_by = lambda n : _operator("divided_by", n)
power      = lambda n : _operator("power", n)
modulo     = lambda n : _operator("modulo", n)

def _number(n, op_components):
    if op_components is None:
        return n
    
    op_name, m = op_components
    match op_name:
        case "plus":
            return n + m
        case "minus":
            return n - m
        case "times":
            return n * m
        case "divided":
            return n / m
        case "power":
            return n ** m
        case "modulo":
            return n % m
        case _:
            raise ValueError(f'Expected op_name to be "plus", "minus", "times" or "divided", found "{op_name}"')


zero  = lambda op=None : _number(0, op)
one   = lambda op=None : _number(1, op)
two   = lambda op=None : _number(2, op)
three = lambda op=None : _number(3, op)
four  = lambda op=None : _number(4, op)
five  = lambda op=None : _number(5, op)
six   = lambda op=None : _number(6, op)
seven = lambda op=None : _number(7, op)
eight = lambda op=None : _number(8, op)
nine  = lambda op=None : _number(9, op)


if __name__ == '__main__':
    print("3 % 2 =", three(modulo(two())))

