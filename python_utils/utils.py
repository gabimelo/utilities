import functools


def compose(*functions):
    """
        Warning: this composition is done in the opposite way of many implementations.
        Functions will be executed from first to last.
        That is, if you call compose(inc_by_one, mult_by_two)(3)
        your result will be mult_by_two(inc_by_one(3)) = 2*(3+1) = 8
    """
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)
