# Buatlah fungsi rekursif untuk mengetahui jumlah digit dari suatu bilangan. Seperti
# misalnya tulisan: "234" maka jumlah digitnya adalah 2+3+4 = 9! 

def jum_digit(bil,bagi=10):
    if bil//bagi < 1:
        return bil
    else:
        belakang=bil%bagi
        bil=bil//bagi
        return belakang+jum_digit(bil,bagi)

print(jum_digit(231234))