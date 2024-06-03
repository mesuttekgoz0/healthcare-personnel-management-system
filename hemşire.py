import personel
class Hemsire(personel.Personel):
    def __init__(self, ad, soyad, departman, maaş, caalisma_saati, sertifika, hastane):
        super().__init__(ad, soyad, departman, maaş)
        self.__calisma_saati=caalisma_saati
        self.__sertifika=sertifika
        self.__hastane=hastane
    def get_calisma_saati(self):
        return self.__calisma_saati
    
    def get_sertifika(self):
        return self.__sertifika
    
    def get_hastane(self):
        return self.__hastane
    
    def maas_arttir(self):
        kat=1.05
        yeni_maas=self.__maaş*kat
        self.set_maaş(yeni_maas)
        return self.__maaş
    
    def __str__(self):
        return f"{super().__str__()} {self.__calisma_saati} {self.__sertifika} {self.__hastane}"