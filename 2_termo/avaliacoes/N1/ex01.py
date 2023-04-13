def repet(stri):
    sai = " "
    st = list(stri)
    for i in range(len(stri)):
        if stri.count(st[i]) >= 2:
            sai += st[i] + " "
    print(sai)

stri = input().upper()
repet(stri)