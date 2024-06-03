import pandas as pd
import personel as per
import doktor as dr
import hemşire as hm
import hasta as has

personel=[
    per.Personel("Semih", "Öztürk", "Bakım", 6700),
    per.Personel("Safiye", "Marmara", "Temizlik", 5000)

]
doktor=[
    dr.Doktor("Fırat", "Selen", "Sağlık", 17000, "Nöroloji", 7, "Kartal Eğitim Ve Araştırma Hastanesi"),
    dr.Doktor("Yusuf", "Özdil", "Sağlık", 17500, "Jinekoloji", 3, "Yüksekova Devlet Hastanesi"),
    dr.Doktor("Ayşe", "Keği", "Sağlık", 16000, "Üroloji", 8, "Bozyaka Eğitim Ve Araştırma Hastanesi")

]
hemsire=[
    hm.Hemsire("Derya", "Taş", "Sağlık", 9000, 12, "Pediatri", "Van Yüzüncü Yıl Hastanesi"),
    hm.Hemsire("Mustafa", "İşleyen", "Sağlık", 8500, 12, "Onkoloji", "Kartal Eğitim Ve Araştırma Hastanesi"),
    hm.Hemsire("Selma", "Kutlu", "Sağlık", 8000, 12, "Yoğun Bakım", "Van Yüzüncü Yıl Hastanesi")
]
hastane_çalışanları= doktor + hemsire + personel
data={
    "İsim":[per.get_ad for per in hastane_çalışanları],
    "Soyisim":[per.get_soyad for per in hastane_çalışanları],
    "Departman":[per.get_departman for per in hastane_çalışanları],
    "Maaş":[per.get_maaş for per in hastane_çalışanları],
    

}
df=pd.DataFrame(data)
print(df)



        