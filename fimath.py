# noinspection SpellCheckingInspection
class Fi:

    # Constructor takes a base10 value
    def __init__(self, value, n_bits=32, n_fbits=0, signed=False, *args, **kwargs):
        # TODO: add override kwarg to prevent sign coersion
        # TODO: args and kwargs definition/unpacking

        # Validate inputs
        # Make sure n_bits is >= n_fbits
        if n_bits < n_fbits:
            raise ValueError("Fractional bits cannot exceed total number of bits")

        # make sure signed is a boolean
        if not isinstance(signed, bool):
            raise TypeError("Argument 'signed' must by of type 'bool'.")

        # if value is a string, try and interpret it as dec, bin, hex, or oct if possible
        #

        # make sure value can be represented with n_bits and n_fbits
        # if the value is not signed, but is negative, try and make it a signed value
        conv_signed = False
        if not signed:
            if value < 0:
                conv_signed = True
                signed = True
                # raise ValueError("Unsigned value cannot be negative")
            elif value >= 2**(n_bits - n_fbits):
                raise ValueError(f"Value is too large to be represented with {n_bits} integer bits "
                                 f"and {n_fbits} fractional bits")

        if signed and ((-(2**(n_bits - n_fbits - 1))) > value or value >= 2**(n_bits - n_fbits - 1)):
            if conv_signed:
                print("Failed to convert value to signed")

            raise ValueError(f"Value is outside of range for {n_bits - 1} integer bits "
                             f"and {n_fbits} fractional bits")

        self.value = value
        self.n_bits = n_bits
        self.n_fbits = n_fbits
        self.signed = signed

        for arg in args:
            print(arg)

        for key in kwargs.keys():
            print(f"{key} : {kwargs[key]}")

    def bin(self, binary_point_on=True, grouping=0):
        # TODO: Input validation

        if not isinstance(binary_point_on, bool):
            raise TypeError("Argument 'binary_point_on' must be of type 'bool'")

        if not isinstance(grouping, int):
            raise TypeError("Argument 'grouping' must be of type 'int'")

        if grouping < 0:
            raise ValueError("Grouping cannot be negative")

        # Return the floating point binary representation of self.value
        temp = self.value
        output = "0b"
        for i in range(self.n_bits):
            if binary_point_on and i == (self.n_bits - self.n_fbits):
                output += "."
            elif grouping > 0 and len(output) != 2:
                if (self.n_bits - self.n_fbits - i) % grouping == 0:
                    output += " "

            exp = self.n_bits - self.n_fbits - i - 1
            if temp >= 2**exp:
                output += "1"
                temp -= 2**exp
            else:
                output += "0"

        return output

    # TODO: Define builtin functions using Python Data Model (CH 3)

    def __add__(self, x):
        return self.value + x

    def __sub__(self, x):
        return self.value - x

    def __mul__(self, x):
        return self.value * x

    def __truediv__(self, x):
        return self.value / x

    def __floordiv__(self, x):
        return self.value // x

    def __index__(self):
        return self.value
