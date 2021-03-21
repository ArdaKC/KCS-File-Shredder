import string
import os
from random import *
print("KCS File Shredder Open Source 2021.1.0.0-^ Supported GNU/Linux")
dosya = input("Konum giriniz:")
silinsinmi = input("Parçaladiktan sonra dosyanin silinmesi için 1 yazin:")
print("0 Varsayilan parçalama değeridir. Varsayilan değer = 900")
kackere = input("Kaç kere parçalansin:")
if kackere == "0":
    kackere = "900"
kackere2 = int(kackere)
def shredd():
    print("Başliyor...")
x=0
while x < kackere2:
 x += 1
 sifre1 = string.ascii_letters + string.punctuation  + string.digits
 sifre2 =  "".join(choice(sifre1) for x in range(randint
 (4, 15)))
 f = open(dosya,"r+")
 f.write(sifre2);
 f.close()
 print("Parçalama işlemi kaç kez yapildi: ", x, "Yazılan kod: ", sifre2)
print(dosya + " Parçalama işlemi tamamlandi!")

if silinsinmi == "1":
 os.unlink(dosya)
