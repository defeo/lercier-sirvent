# -*- coding: utf-8 -*-

# Apply `isogeny.patch` first

from sage.schemes.elliptic_curves import ell_isogeny_char_zero as c0
from sage.schemes.elliptic_curves import ell_isogeny_finite_field as ff

# Any odd integer will work
m = 7

# The curves
#      y² + xy = A(x)
#      y² + xy = m⁶A(x/m²) + (m²-1)/4 x²
#
# are isomorphic and there is a normalized isogeny of degree m²
# between them, namely the usual multiplication-by-m map.
#
# Notice that, if m is odd, m²-1 is divisible by 4.
E = EllipticCurve([1, 0,           0, 0, 1   ])
F = EllipticCurve([1, (m**2-1)//4, 0, 0, m**6])

K = Qp(2, prec=20)
T = ff._diff_solve_char2(E.change_ring(K), F.change_ring(K), m**2)
D = ff._frac_reconst(T)

assert(D == E.change_ring(GF(2)).division_polynomial(m).monic()**2)
