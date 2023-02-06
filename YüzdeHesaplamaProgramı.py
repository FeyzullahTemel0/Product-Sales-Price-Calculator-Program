
# Ürünlerin Trendyol Satışı İçin Gerekli Durumların Hesaplanmasını Sağlayan Python Programı

urun_fiyatı = float(input("Ürün Fiyatını Girin: "));
urun_toptan_fiyati = float(input("Ürünün Toptan Fiyatını Giriniz: "));

urunu_satmak_mantikli_mi = False;
yuzde = float(20/100);
komisyon_fiyati = float(urun_fiyatı * yuzde);
komisyonlu_satilmasigereken_fiyat = float(komisyon_fiyati + urun_fiyatı);
kar = float((urun_fiyatı + komisyon_fiyati) - urun_toptan_fiyati)-komisyon_fiyati;

print("\nBu Üründe Alınacak Komisyon: {k} ".format(k = komisyon_fiyati));
print("\nKomisyonu Eklenerek Satılması Gereken fiyatı: {a}".format(a=komisyonlu_satilmasigereken_fiyat));
print("\nÜründen Elde Edilen Kar: {x} ".format(x = kar));

#Ürün satmak mantıklı mı kontrolü
if(kar>urun_toptan_fiyati):
    urunu_satmak_mantikli_mi = True;
    if(urunu_satmak_mantikli_mi == True):
        print("Bu ürünü satmak mantıklıdır. Çünkü Kar'ı toptan fiyatından fazladır.");
    else:
        print("Bu ürünü satmak mantıklı değildir. Çünkü kar'ı toptan fiyatından azdır.");
    if(urun_toptan_fiyati==kar):
        print("Üründen elde edilen kar ile toptan fiyatı birbirine eşittir. Satmak mantıklı değildir.");
else:
    urunu_satmak_mantikli_mi= False;

if(urunu_satmak_mantikli_mi==False):
    i=0;
    while i<100000:
        continue;


urun_fiyatı = float(input("Ürün Fiyatını Girin: "));

urun_toptan_fiyati = float(input("Ürünün Toptan Fiyatını Giriniz: "));

urunu_satmak_mantikli_mi = False;
yuzde = float(20/100);
komisyon_fiyati = float(urun_fiyatı * yuzde);
komisyonlu_satilmasigereken_fiyat = float(komisyon_fiyati + urun_fiyatı);
kar = float((urun_fiyatı + komisyon_fiyati) - urun_toptan_fiyati)-komisyon_fiyati;

print("\nBu Üründe Alınacak Komisyon: {k} ".format(k = komisyon_fiyati));
print("\nKomisyonu Eklenerek Satılması Gereken fiyatı: {a}".format(a=komisyonlu_satilmasigereken_fiyat));
print("\nÜründen Elde Edilen Kar: {x} ".format(x = kar));

#Ürün satmak mantıklı mı kontrolü
if(kar>urun_toptan_fiyati):
    urunu_satmak_mantikli_mi = True;
    if(urunu_satmak_mantikli_mi == True):
        print("Bu ürünü satmak mantıklıdır. Çünkü Kar'ı toptan fiyatından fazladır.\n\n");
    else:
        print("Bu ürünü satmak mantıklı değildir. Çünkü kar'ı toptan fiyatından azdır.\n\n");
else:
    urunu_satmak_mantikli_mi= False;
