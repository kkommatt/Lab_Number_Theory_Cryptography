from RSA import rsa
from RhoPollard import rho
from chinese_theorem import chinese_theorem
from ell_gamal import ell_gamal
from euler_mobius import euler_mobius
from legandre_jacobi import legandre_jacobi
from log import logarithm_disc
from solovei import solovei
from sqrt_ch import sqrt_ch

print("Euler. Mobius")
euler_mobius()

print("Chinese Theorem")
chinese_theorem()

print("Legandre. Jacobi")
legandre_jacobi()

print("Rho-pollard")
rho()

print("Logarithm")
logarithm_disc()

print("Sqrt")
sqrt_ch()

print("Solovei")
solovei()

print("RSA")
rsa()

print("Ell Gamall")
ell_gamal()