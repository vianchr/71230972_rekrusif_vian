# Buatlah fungsi rekursif untuk menghitung jumlah deret ganjil dari 1 + 3 + 7 + . . .+ n!
def faktorialganjil(n,awal=1):
    if n%2==0:
        return ("n bukan bilangan ganjil")
    if n==1:
        return 1
    else:
        return n+faktorialganjil(n-2,awal)

print(faktorialganjil(5))
print(faktorialganjil(7))
print(faktorialganjil(12))
