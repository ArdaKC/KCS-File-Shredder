#  Copyright <2021> <KCS>

#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import os
from random import randint
print("KCS File Shredder Open Source 2021.1.2.3-^ Supported GNU/Linux")

dil = int(input("Which language? / Hangi dil? \n 1-Türkçe\n 2-English:"))

if(dil==1):
    dosya = input("Konum giriniz:")
    silinsinmi = input("Parçaladiktan sonra dosyanin silinmesi için 1 yazin:")
    print("0 Varsayilan parçalama değeridir. Varsayilan değer = 900")
    kackere = input("Kaç kere parçalansin:")
    kacaralik = input("Olusturulacak rastgele verinin uzunlugunu yazin. Örnek = 4:")
    if kackere == "0":
        kackere = "900"
    kackere2 = int(kackere)
    if kacaralik == "0" or kacaralik == "":
        kacaralik = int(346)
    x=0
    while x < kackere2:
        x += 1
        sifre2 = ""
        for qwe in range(int(kacaralik)):
            karakterler1 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
            sifre2 += karakterler1[randint(0, len(karakterler1) - 1)]
        pass
        f = open(dosya,"r+")
        f.write(sifre2)
        f.close()
        print("Parçalama işlemi kaç kez yapildi: ", x, "Yazılan kod: ", sifre2)
    print(dosya + " Parçalama işlemi tamamlandi!")

    if silinsinmi == "1":
        os.unlink(dosya)

    pass
        #Türkçe
if(dil==2):
    dosya = input("Specify the location:")
    silinsinmi = input("Write 1 to delete file after shredding:")
    print("0 is the default shredding value. Default is 900")
    kackere = input("How many times do you want to shred file:")
    kacaralik = input("Write the width of random code to be generated. Example = 4:")
    if kackere == "0":
        kackere = "900"
    kackere2 = int(kackere)

    if kacaralik == "0" or kacaralik == "":
        kacaralik = int(346)
    x=0
    while x < kackere2:
        x += 1
        sifre1 = ""
        for qwew in range(int(kacaralik)):
            karakterler2 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
            sifre1 += karakterler2[randint(0, len(karakterler2) - 1)]
        pass
        f = open(dosya,"r+")
        f.write(sifre1)
        f.close()
        print("How many times file shredded: ", x, "Written code: ", sifre1)
    print(dosya + " Has been terminated!")

    if silinsinmi == "1":
        os.unlink(dosya)

    pass
#English
