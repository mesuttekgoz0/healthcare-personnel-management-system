class Personel():
    def __init__(self, personel_no, ad, soyad, departman, maaş):
        self.__ad=ad
        self.__soyad=soyad
        self.__departman=departman
        self.__maaş=maaş
        self.__personel_no=personel_no

    def get_personel_no(self):
        return self.__personel_no

    def get_ad(self):
        return self.__ad
    
    def get_soyad(self):
        return self.__soyad
    
    def get_departman(self):
        return self.__departman
    
    def get_maaş(self):
        return self.__maaş
    def set_maaş(self, yeni_maas):
        self.__maaş=yeni_maas
    
    def __str__(self):
        return f"{self.__personel_noS} {self.__ad}  {self.__soyad}  {self.__departman}  {self.__maaş}"
    
    
    