def metnikucult(metin):
    metin=metin.lower()
    return metin
def harfleribol(metin):
     harfler = [harf for harf in metin if harf.isalpha()]
     toplamharf=len(harfler)
     return harfler,toplamharf
def harfhesapla(harfler):
    harfler_sayilari = {}
    for harf in harfler:
        if harf in harfler_sayilari:
            harfler_sayilari[harf] += 1
        else:
            harfler_sayilari[harf] = 1
    return harfler_sayilari
def oranhesapla(harfler_sayilari,toplam_harf_sayisi):
     for harf, sayi in harfler_sayilari.items():
        oran = (sayi / toplam_harf_sayisi) * 100
        print("{} harfi {} kez geçiyor ve oranı %{:.2f}".format(harf,sayi,oran))
print("Mustafa Hilmi Oruç")
print("ogr no : 211213070")
print("python kolaylıktır")

