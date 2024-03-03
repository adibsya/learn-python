from sympy import symbols, diff, integrate

x = symbols('x')
# input fungsi di sini
f = x**3 + 4*x + 2

# Menghitung turunan pertama
turunan_f = diff(f, x)
print("Turunan pertama dari f adalah: ", turunan_f)

# Menghitung integral tak tentu
integral_f = integrate(f, x)
print("Integral tak tentu dari f adalah: ", integral_f)

# Menghitung integral tentu dari 0 sampai 1
integralTentu_f = integrate(f, (x, 0, 1))
print("Integral tentu dari f dari 0 sampai 1 adalah: ", integralTentu_f)
