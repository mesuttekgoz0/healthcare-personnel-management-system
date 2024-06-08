import pandas as pd
import personel as per
import doktor as dr
import hemşire as hm
import hasta as has

personel=[
    per.Personel("p3244","Semih", "Öztürk", "Bakım", 6700),
    per.Personel("p5629","Safiye", "Marmara", "Temizlik", 5000)

]
doktor=[
    dr.Doktor("d47","Fırat", "Selen", "Sağlık", 17000, "Nöroloji", 7, "Kartal Eğitim Ve Araştırma Hastanesi"),
    dr.Doktor("d83","Yusuf", "Özdil", "Sağlık", 17500, "Jinekoloji", 3, "Yüksekova Devlet Hastanesi"),
    dr.Doktor("d66","Ayşe", "Keği", "Sağlık", 16000, "Üroloji", 8, "Bozyaka Eğitim Ve Araştırma Hastanesi")

]
hemsire=[
    hm.Hemsire("hm12","Derya", "Taş", "Sağlık", 9000, 12, "Pediatri", "Van Yüzüncü Yıl Hastanesi"),
    hm.Hemsire("hm22","Mustafa", "İşleyen", "Sağlık", 8500, 12, "Onkoloji", "Kartal Eğitim Ve Araştırma Hastanesi"),
    hm.Hemsire("hm2382","Selma", "Kutlu", "Sağlık", 8000, 12, "Yoğun Bakım", "Van Yüzüncü Yıl Hastanesi")
]
hasta=[
    has.Hasta(1232,"Sait", "Takoz",1987,"Grip","Normal")
]
hastane_çalışanları= doktor+ personel + hemsire
data={}
for person in hastane_çalışanları:
    data={
        "personel numarası":[person.get_personel_no],
        "İsim":[person.get_ad ],
        "Soyisim":[person.get_soyad ],
        "Departman":[person.get_departman],
        "Maaş":[person.get_maaş]   
    }
df=pd.DataFrame(data)
print(df)



        