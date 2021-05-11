




def curry(f):
    def first(a):
        def second(b):
            return a+b+f
        return second
    return first


print(curry(10)(20)(30))