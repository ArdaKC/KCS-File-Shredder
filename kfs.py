#  Copyright <2021> <KCS>

#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import string
import os
from random import *
print("KCS File Shredder Open Source 2021.1.2.0-^ Supported GNU/Linux")
dosya = input("Konum giriniz:")
silinsinmi = input("Parçaladiktan sonra dosyanin silinmesi için 1 yazin:")
print("0 Varsayilan parçalama değeridir. Varsayilan değer = 900")
kackere = input("Kaç kere parçalansin:")
kacaralik = input("Minimum kod oluşturma araliği belirleyin. Örnek = 4:")
kacaralik3 = input("Maksimum kod oluşturma araliği belirleyin. Örnek = 15:")
if kackere == "0":
    kackere = "900"
kackere2 = int(kackere)

if kacaralik == "0, 0" or kacaralik == "0":
    kacaralik = "4"
kacaralik2 = int(kacaralik)

if kacaralik3 == "0, 0" or kacaralik3 == "0":
    kacaralik3 = "15"
kacaralik4 = int(kacaralik3)

def shredd():
    print("Başliyor...")
x=0
while x < kackere2:
 x += 1
 sifre1 = string.ascii_letters + string.punctuation  + string.digits
 sifre2 =  "".join(choice(sifre1) for x in range(randint
 (kacaralik2, kacaralik4)))
 f = open(dosya,"r+")
 f.write(sifre2);
 f.close()
 print("Parçalama işlemi kaç kez yapildi: ", x, "Yazılan kod: ", sifre2)
print(dosya + " Parçalama işlemi tamamlandi!")

if silinsinmi == "1":
 os.unlink(dosya)
