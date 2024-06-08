import pandas as pd
from personel import Personel
from doktor import Doktor
from hemşire import Hemsire
from hasta import Hasta
import numpy as np

personel=[
    Personel("p3244","Semih", "Öztürk", "Bakım", 6700),
    Personel("p5629","Safiye", "Marmara", "Temizlik", 5000)

]
doktor=[
    Doktor("d47","Fırat", "Selen", "Sağlık", 17000, "Nöroloji", 7, "Kartal Eğitim Ve Araştırma Hastanesi"),
    Doktor("d83","Yusuf", "Özdil", "Sağlık", 17500, "Jinekoloji", 3, "Yüksekova Devlet Hastanesi"),
    Doktor("d66","Ayşe", "Keği", "Sağlık", 16000, "Nöroloji", 8, "Bozyaka Eğitim Ve Araştırma Hastanesi")

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


ana_data=[]
for kisi in tüm_hastane:
    if isinstance(kisi, Personel):
        if isinstance(kisi,Doktor):
            data={
           "ID":kisi.get_personel_no(),
           "Ad":kisi.get_ad(),
           "Soyad":kisi.get_soyad(),
           "Departman":kisi.get_departman(),
           "Maaş": kisi.get_maaş(),
           "uzmanlık":kisi.get_uzmanlik(),
           "deneyim yılı":kisi.get_deneyim_yili(),
           "çalışma saati":np.nan,
           "sertifika":np.nan,
           "hastane":kisi.get_hastane(),
           "Doğum yılı":np.nan,
           "Hasta no":np.nan,
           "Hastalık":np.nan,
           "Tedavi":np.nan
        }
        elif isinstance(kisi,Hemsire):
             data={
           "ID":kisi.get_personel_no(),
           "Ad":kisi.get_ad(),
           "Soyad":kisi.get_soyad(),
           "Departman":kisi.get_departman(),
           "Maaş": kisi.get_maaş(),
           "uzmanlık":np.nan,
           "deneyim yılı":np.nan,
           "çalışma saati":kisi.get_calisma_saati(),
           "sertifika":kisi.get_calisma_saati(),
           "hastane":kisi.get_hastane(),
           "Doğum yılı":np.nan,
           "Hasta no":np.nan,
           "Hastalık":np.nan,
           "Tedavi":np.nan
        }
        else:
            data={
               "ID":kisi.get_personel_no(),
               "Ad":kisi.get_ad(),
               "Soyad":kisi.get_soyad(),
               "Departman":kisi.get_departman(),
               "Maaş": kisi.get_maaş(),
               "uzmanlık":np.nan,
               "deneyim yılı":np.nan,
               "çalışma saati":np.nan,
               "sertifika":np.nan,
               "hastane":np.nan,
               "Doğum yılı":np.nan,
               "Hasta no":np.nan,
               "Hastalık":np.nan,
               "Tedavi":np.nan
            }
   
    elif isinstance(kisi,Hasta):
        data={
           "ID":"",
           "Ad":kisi.get_ad(),
           "Soyad":kisi.get_soyad(),
           "Departman":np.nan,
           "Maaş": np.nan,
           "uzmanlık":np.nan,
           "deneyim yılı":np.nan,
           "çalışma saati":np.nan,
           "sertifika":np.nan,
           "hastane":np.nan,
           "Doğum yılı":kisi.get_dogum_yili(),
           "Hasta no":kisi.get_hasta_no(),
           "Hastalık":kisi.get_hastalik(),
           "Tedavi":kisi.get_tedavi()
        }
    ana_data.append(data)

df=pd.DataFrame(ana_data)
print(df)
#boşlukları 0 ile doldurma
a=df.fillna(0)
print(a)

#uzmanlıklarına göre sayılarını bulma
print("\n uzmanlıklarına döre doktor sayıları")
b=df["uzmanlık"].value_counts().describe
print(b)

#deneyim yılına göre doktor sayısı bulma
sayac=0
for i in df["deneyim yılı"]:
    if i>5:
        sayac=sayac+1
print(f"deneyimi 5 yıldan fazla olan doktor sayısı {sayac}")








        