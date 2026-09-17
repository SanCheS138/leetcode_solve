class Solution:
    def fractionAddition(self, expression: str) -> str:
        ints = list(map(int, re.findall(r'[+-]?[0-9]+', expression)))
        A, B = 0, 1
        
        # Iterate over numerators and denominators in pairs
        for a, b in zip(ints[::2], ints[1::2]):
            A = A * b + a * B
            B *= b
            
        # Simplify using greatest common divisor
        g = math.gcd(A, B)
        A //= g
        B //= g
        
        return f"{A}/{B}"
        