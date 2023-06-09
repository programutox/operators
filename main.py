def _operator(op_name, n):
    if not isinstance(n, int):
        raise TypeError(f"Expected int, found {type(n)}")
    return op_name, n


plus       = lambda n : _operator("plus", n)
minus      = lambda n : _operator("minus", n)
times      = lambda n : _operator("times", n)
divided_by = lambda n : _operator("divided_by", n)


def _number(n, op_components):
    if op_components is None:
        return n
    
    op_name, m = op_components
    if op_name == "plus":
        return n + m
    elif op_name == "minus":
        return n - m
    elif op_name == "times":
        return n * m
    elif op_name == "divided":
        if m == 0:
            raise ZeroDivisionError
        return n / m 
    
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
    print("1 + 1 =", one(plus(one())))

