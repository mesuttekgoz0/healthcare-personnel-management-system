class Hasta():
    def __init__(self, hasta_no, ad, soyad, dogum_yili, hastalik, tedavi):
        self.__hasta_no=hasta_no
        self.__ad=ad
        self.__soyad=soyad
        self.__dogum_yili=dogum_yili
        self.__hastalik=hastalik
        self.__tedavi=tedavi
    
    def get_hasta_no(self):
        return self.__hasta_no
    
    def get_ad(self):
        return self.__ad
    
    def get_soyad(self):
        return self.__soyad
    
    def get_dogum_yili(self):
        return self.__dogum_yili
    
    def get_hastalik(self):
        return self.__hastalik
    
    def get_tedavi(self):
        return self.__tedavi
    
    def tedavi_suresi_hesapla(self):
        normal_süre=2
        if self.__tedavi=="İlaç Tedavisi":
            return normal_süre
        elif self.__tedavi=="Özel tedavi":
            return normal_süre+4
    
    
    def __str__(self):
        return f"{self.__hasta_no} {self.__ad} {self.__soyad} {self.__dogum_yili} {self.__hastalik} {self.__tedavi}  "
    
                                