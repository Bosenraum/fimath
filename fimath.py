# noinspection SpellCheckingInspection
class Fi:

    def __init__(self, value, n_bits=32, n_fbits=16, signed=0, *args, **kwargs):
        self.value = value
        self.n_bits = n_bits
        self.n_fbits = n_fbits
        self.signed = signed

        for arg in args:
            print(arg)

        for key in kwargs.keys():
            print(f"[{key}] : {kwargs[key]}")

    # TODO: Implement builtin functions
