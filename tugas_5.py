def kombinasi(a,b):
    if a < b:
        return "a harus lebih besar dari b"
    if b == 0:
        return 1
    if b == 1:
        return a
    if a == b:
        return 1
    else:
        return kombinasi(a - 1, b) + kombinasi(a - 1, b - 1)

print(kombinasi(7,3))
        
        
        
        
        