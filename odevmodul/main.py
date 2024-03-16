import harfhesaplama
metin = input("Bir metin giriniz: ")
metin=harfhesaplama.metnikucult(metin)
metin,harfsayisi=harfhesaplama.harfleribol(metin)
metin=harfhesaplama.harfhesapla(metin)
harfhesaplama.oranhesapla(metin,harfsayisi)
