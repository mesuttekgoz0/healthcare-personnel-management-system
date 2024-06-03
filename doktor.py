import personel
class Doktor(personel.Personel):
    def __init__(self, ad, soyad, departman, maaş, uzmanlik, deneyim_yili, hastane):
        super().__init__(ad, soyad, departman, maaş)
        self.__uzmanlik=uzmanlik
        self.__deneyim_yili=deneyim_yili
        self.__hastane=hastane

    def get_uzmanlik(self):
        return self.__uzmanlik
    def set_uzmanlik(self, yeni_uzmanlik):
        self.__uzmanlik=yeni_uzmanlik
    
    def get_deneyim_yili(self):
        return self.__deneyim_yili
    def set_deneyim_yili(self, yeni_deneyim):
        self.__deneyim_yili=yeni_deneyim
    
    def get_hastane(self):
        return self.__hastane
    def set_hastane(self, yeni_hastane):
        self.__hastane=yeni_hastane

    
    def maas_arttir(self):
        kat=1.1
        yeni_maas=self.__maaş*kat
        self.set_maaş(yeni_maas)
        return self.__maaş
    
    def __str__(self):
        return f"{super().__str__()} {self.__deneyim_yili} {self.__hastane} {self.__maaş}"
        
        