def jum_digit(bil,bagi=10):
    if bil//bagi < 1:
        return bil
    else:
        belakang=bil%bagi
        bil=bil//bagi
        return belakang+jum_digit(bil,bagi)

print(jum_digit(231234))
print(jum_digit(123))
print(jum_digit(234))