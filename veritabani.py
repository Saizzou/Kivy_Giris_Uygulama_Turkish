import datetime

class VeriTabani:
    def __init__(self,dosyaadi):
        self.dosyaadi = dosyaadi
        self.kullanicilar = None
        self.dosya = None
        self.yukle()

    def yukle(self):
        self.dosya = open(self.dosyaadi, "r")
        self.kullanicilar = {}

        for line in self.dosya:
            email, sifre, isim, tarih = line.strip().split(";")
            self.kullanicilar[email] = (sifre, isim, tarih)
            self.kullanicilar[isim] = (sifre, email, tarih)

        self.dosya.close()

    def get_kullanici(self, email):
        if email in self.kullanicilar:
            return self.kullanicilar[email]

        else:
            return -1

    def get_kullanici2(self, isim):
        if isim in self.kullanicilar:
            return self.kullanicilar[isim]
        else:
            return -1

    def add_kullanici(self,email,sifre,isim):
        if email.strip() not in self.kullanicilar:
            self.kullanicilar[email.strip()] = (sifre.strip(), isim.strip(), VeriTabani.get_date())
            self.kaydet()
            return 1

        else:
            print("Bu Email adressi zaten kullanılmaktadır!")
            return -1

    def onaylama(self,email,sifre):
        if self.get_kullanici(email) != -1:
            return self.kullanicilar[email][0] == sifre

        else:
            onaylama2()

    def onaylama2(self,isim,sifre):
        if self.get_kullanici2(isim) != -1:
            return self.kullanicilar[isim][0] == sifre

        else:
            return -1
    def kaydet(self):
        with open(self.dosyaadi, "w") as f:
            for kullanici in self.kullanicilar:
                f.write(kullanici + ";" + self.kullanicilar[kullanici][0] + ";" + self.kullanicilar[kullanici][1] + ";" + self.kullanicilar[kullanici][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
