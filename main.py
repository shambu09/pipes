class Pipe:
    def __init__(self, funcs):
        self.funcs = funcs
        self.wrap()

    def wrap(self):
        for i in range(len(self.funcs)):
            if self.funcs[i].__defaults__ == None or self.funcs[i].__defaults__.count("__no_wrap__") == 0:
                self.funcs[i] = self.__wrap(self.funcs[i])
    
    def __wrap(self, func):
        def wrapper(seq):
            for i in range(len(seq)):
                seq[i] = func(seq[i])
            return seq
        return wrapper

    def __call__(self, seq):
        for func in self.funcs:
            seq = func(seq)
        return seq