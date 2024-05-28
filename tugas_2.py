# rekrusif palindrom
def palindrom(huruf,awal=0,akhir=0):
    if akhir==0:
        akhir=len(huruf)-1
    if huruf[awal] != huruf[akhir]:
        return ("bukan palindrom")
    if awal >= akhir:
        return ("palindrom")
    else:
        return palindrom(huruf,awal+1,akhir-1)

print(palindrom("kak"))