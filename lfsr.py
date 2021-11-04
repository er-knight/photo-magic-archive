import cython

@cython.cclass
class LFSR:

    WORD_SIZE = cython.declare(cython.uchar)
    seed_val  = cython.declare(cython.ulong)
    tap_code  = cython.declare(cython.uchar)

    def __init__(self, seed_val, tap_code):
        self.WORD_SIZE = cython.sizeof(cython.ulong) * 8
        self.seed_val  = seed_val
        self.tap_code  = tap_code % self.WORD_SIZE

    @cython.cfunc
    @cython.returns(cython.uchar) 
    def next_bit(self):
        mask = cython.declare(cython.ulong,
            ((self.seed_val >> self.tap_code) & 1) ^ ((self.seed_val >> (self.WORD_SIZE - 1)) & 1)
        )
        self.seed_val = (self.seed_val << 1) | mask
        return self.seed_val & 1

    @cython.ccall
    @cython.returns(cython.ulong)
    @cython.locals(k=cython.ulong)
    def next_bits(self, k):
        bit_sequence = cython.declare(cython.ulong, 0)
        
        i = cython.declare(cython.ulong, 0)
        for i in range(k):
            bit_sequence = (bit_sequence << 1) | self.next_bit()

        return bit_sequence
