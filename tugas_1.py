def cek_prima(a,b=2):
    if a <= 1:
        return ("bukan prima")
    elif b**2 > a:
        return ("prima")
    elif a % b == 0:
        return ("bukan prima")
    else:
        return cek_prima(a, b + 1)

print(cek_prima(97))
print(cek_prima(100))
print(cek_prima(101))
print(cek_prima(2))
print(cek_prima(3))