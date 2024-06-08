import pandas as pd
from personel import Personel
from doktor import Doktor
from hemşire import Hemsire
from hasta import Hasta

personel=[
    Personel("p3244","Semih", "Öztürk", "Bakım", 6700),
    Personel("p5629","Safiye", "Marmara", "Temizlik", 5000)

]
doktor=[
    Doktor("d47","Fırat", "Selen", "Sağlık", 17000, "Nöroloji", 7, "Kartal Eğitim Ve Araştırma Hastanesi"),
    Doktor("d83","Yusuf", "Özdil", "Sağlık", 17500, "Jinekoloji", 3, "Yüksekova Devlet Hastanesi"),
    Doktor("d66","Ayşe", "Keği", "Sağlık", 16000, "Üroloji", 8, "Bozyaka Eğitim Ve Araştırma Hastanesi")

]
hemsire=[
    Hemsire("hm12","Derya", "Taş", "Sağlık", 9000, 12, "Pediatri", "Van Yüzüncü Yıl Hastanesi"),
    Hemsire("hm22","Mustafa", "İşleyen", "Sağlık", 8500, 12, "Onkoloji", "Kartal Eğitim Ve Araştırma Hastanesi"),
    Hemsire("hm2382","Selma", "Kutlu", "Sağlık", 8000, 12, "Yoğun Bakım", "Van Yüzüncü Yıl Hastanesi")
]
hasta=[
    Hasta(1232,"Sait", "Takoz",1987,"Grip","Normal")
]
tüm_hastane= doktor+ personel + hemsire+hasta

df=pd.DataFrame(columns=["personel numarası","Ad","Soyad","Departman","Maaş","uzmanlık","deneyim yılı","çalışma saati",
                         "sertifika","hastane","Doğum yılı","Hasta no","Hastalık","Tedavi"])

for kisi in tüm_hastane:
    if isinstance(kisi, Personel):
        df=df.append({
           "personel numarası":kisi.get_personel_no,
           "Ad":kisi.get_ad,
           "Soyad":kisi.get_soyad,
           "Departman":kisi.get_departman,
           "Maaş": kisi.get_maaş,
           "uzmanlık":"",
           "deneyim yılı":"",
           "çalışma saati":"",
           "sertifika":"",
           "hastane":"",
           "Doğum yılı":"",
           "Hasta no":"",
           "Hastalık":"",
           "Tedavi":""
        }, ignore_index=True)
    elif isinstance(kisi,Doktor):
        df=df.append({
           "personel numarası":kisi.get_personel_no,
           "Ad":kisi.get_ad,
           "Soyad":kisi.get_soyad,
           "Departman":kisi.get_departman,
           "Maaş": kisi.get_maaş,
           "uzmanlık":kisi.get_uzmanlik,
           "deneyim yılı":kisi.get_deneyim_yili,
           "çalışma saati":"",
           "sertifika":"",
           "hastane":kisi.get_hastane,
           "Doğum yılı":"",
           "Hasta no":"",
           "Hastalık":"",
           "Tedavi":""
        }, ignore_index=True)
    elif isinstance(kisi,Hemsire):
        df=df.append({
           "personel numarası":kisi.get_personel_no,
           "Ad":kisi.get_ad,
           "Soyad":kisi.get_soyad,
           "Departman":kisi.get_departman,
           "Maaş": kisi.get_maaş,
           "uzmanlık":"",
           "deneyim yılı":"",
           "çalışma saati":kisi.get_calisma_saati,
           "sertifika":kisi.get_calisma_saati,
           "hastane":kisi.get_hastane,
           "Doğum yılı":"",
           "Hasta no":"",
           "Hastalık":"",
           "Tedavi":""
        }, ignore_index=True)
    elif isinstance(kisi,Hasta):
        df=df.append({
           "personel numarası":"",
           "Ad":kisi.get_ad,
           "Soyad":kisi.get_soyad,
           "Departman":"",
           "Maaş": "",
           "uzmanlık":"",
           "deneyim yılı":"",
           "çalışma saati":"",
           "sertifika":"",
           "hastane":"",
           "Doğum yılı":kisi.get_dogum_yili,
           "Hasta no":kisi.get_hasta_no,
           "Hastalık":kisi.get_hastalik,
           "Tedavi":kisi.get_tedavi
        }, ignore_index=True)
print(df)







        