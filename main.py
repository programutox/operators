import operator as ope

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
    
    valid_ops = {
        "plus": ope.add,
        "minus": ope.sub,
        "times": ope.mul,
        "divided": ope.truediv,
        "power": ope.pow,
        "modulo": ope.mod,
    }

    
    op_name, m = op_components
    if op_name not in valid_ops:
        raise ValueError(f"{op_name} is not a valid operator")
    
    func = valid_ops[op_name]
    return func(n, m)
    


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

