# rekrusif palindrom
def palindrom(huruf,awal=0,akhir=0):
    if akhir==0:
        akhir=len(huruf)-1
    if huruf[awal] != huruf[akhir]:
        return (f"{huruf} bukan palindrom")
    if awal >= akhir:
        return (f"{huruf} palindrom")
    else:
        return palindrom(huruf,awal+1,akhir-1)

print(palindrom("kak"))
print(palindrom("khukhu"))
print(palindrom("popoopop"))