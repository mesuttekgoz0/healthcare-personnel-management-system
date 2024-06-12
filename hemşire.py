import personel
class Hemsire(personel.Personel):
    def __init__(self, personel_no,ad, soyad, departman, maaş, caalisma_saati, sertifika, hastane):
        super().__init__(personel_no,ad, soyad, departman, maaş)
        self.__calisma_saati=caalisma_saati
        self.__sertifika=sertifika
        self.__hastane=hastane
    def get_calisma_saati(self):
        return self.__calisma_saati
    def set_calışma_saati(self,yeni):
        self.__calisma_saati=yeni
    
    def get_sertifika(self):
        return self.__sertifika
    def set_sertifika(self,yeni):
        self.__sertifika=yeni
    
    def get_hastane(self):
        return self.__hastane
    def set_hastane(self, yeni_hastane):
        self.__hastane=yeni_hastane
    
    def maas_arttir(self):
        kat=1.05
        yeni_maas=self.__maaş*kat
        self.set_maaş(yeni_maas)
        return self.__maaş
    
    def __str__(self):
        return f"{super().__str__()} {self.__calisma_saati} {self.__sertifika} {self.__hastane}"