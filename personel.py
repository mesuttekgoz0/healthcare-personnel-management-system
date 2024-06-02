class Personel():
    def __init__(self, ad, soyad, departman, maaş):
        self.__ad=ad
        self.__soyad=soyad
        self.__departman=departman
        self.__maaş=maaş

    def get_ad(self):
        return self.__ad
    
    def get_soyad(self):
        return self.__soyad
    
    def get_departman(self):
        return self.__departman
    
    def get_maaş(self):
        return self.__maaş
    
    def __str__(self):
        return f"{self.__ad}  {self.__soyad}  {self.__departman}  {self.__maaş}"
    
    
    