class one:

    static_var = 10

class two:

    def __init__(self):
        print(one.static_var)

obj = two()
