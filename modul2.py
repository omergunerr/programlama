donenVarliklar=128000
duranVarliklar=183000
kisaVadeliYK=102000
uzunVadeliYK=150000
ozKaynak=59000
def aktif(donenVarliklar,duranVarliklar):
    global aktifToplam
    aktifToplam=donenVarliklar+duranVarliklar
    return aktifToplam
def pasif(kisaVadeliYK,uzunVadeliYK,ozKaynak):
    global pasifToplam
    pasifToplam=kisaVadeliYK+uzunVadeliYK+ozKaynak
    return pasifToplam
a=aktif(donenVarliklar,duranVarliklar)
p=pasif(kisaVadeliYK,uzunVadeliYK,ozKaynak)

