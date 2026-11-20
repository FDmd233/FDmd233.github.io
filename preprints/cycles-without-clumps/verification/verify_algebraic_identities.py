"""Exact identities in characteristic two used in the manuscript.

Polynomials in F_2[s] are stored as bitsets.  In the quadratic algebra
F_2[s,w]/(w^2+w+s^5+1), elements are pairs (constant, w-coefficient).
This verifies exact algebraic identities, not the field-intersection
or no-clump theorems, which are proved in the manuscript.
"""

def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def powpoly(x, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n >>= 1
    return out


def deriv(p):
    out = 0
    i = 1
    while (1 << i) <= p:
        if i & 1 and (p >> i) & 1:
            out ^= 1 << (i-1)
        i += 1
    return out


S = 2  # polynomial variable s
D = powpoly(S, 5) ^ 1


def mult_pair(a, b):
    a0, a1 = a
    b0, b1 = b
    both = mul(a1, b1)
    return (mul(a0, b0) ^ mul(both, D),
            mul(a0, b1) ^ mul(a1, b0) ^ both)


def powpair(x, n):
    r = (1, 0)
    while n:
        if n & 1:
            r = mult_pair(r, x)
        x = mult_pair(x, x)
        n >>= 1
    return r


W = (0, 1)
W6 = powpair(W, 6)
Ws10 = (0, powpoly(S, 10))
left = (W6[0] ^ Ws10[0], W6[1] ^ Ws10[1])
right = (D ^ powpoly(D, 2) ^ powpoly(D, 3), 0)
assert left == right
print('E=x^6+x is rational in s: exact polynomial identity verified')

A = powpoly(S, 16) ^ S
E = powpoly(S, 6) ^ S
assert deriv(A) == 1 and deriv(E) == 1
assert (A ^ E) == powpoly(powpoly(S, 8) ^ powpoly(S, 3), 2)
assert ((A.bit_count() % 2) == 0 and (E.bit_count() % 2) == 0)
print('A and E derivatives, square identity and x=0,1 test verified')

B = powpoly(S, 16) ^ S
rho = powpoly(S, 2)
assert B ^ powpoly(rho, 8) == S
assert deriv(D) == powpoly(S, 4)
print('s=B+(s^2)^8 and differential relation verified')

assert 25 - 10 + 1 == 16
assert (5*4//2)**2 == 100
print('K5,5 cycle rank and 4-cycle count verified')
