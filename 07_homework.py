# -------------------------------------------------------------------SORU 1----------------------------------------------------------
# BIR YAZIDAKI SESLI HARFLERI VEREN KUME ICLEMINI TEK BIR IFADE BICIMINDE YAZINIZ.
# ORNEGIN YAZI 'BUGUN HAVA COK GUZEL OLSUN'
# buradan elde edilecek kume 'u, 'ü', 'a', 'o','e' stringlerini bulundurmalidir.

'''count = 0
while True:
    text = input(' bir yazi giriniz : ')
    letter_list = ['a', 'e', 'i', 'ö', 'ü', 'o', 'u']
    result = {i for i in text if i in letter_list}
    print(result)
    count += 1
    if count == 3:
        break
'''
# -------------------------------------------------------------------SORU 2-------------------------------------------------------------
# bir liste iclemi ile bir liste icerisindeki sayilardan olusan bir demet listesi olusturunuz.
# Demetin ilk elemani sayinin kendisinden ikinci elemai ise 'tek' ya da 'cift' yazilardan olusmalidir.


# a = [1, 2, 3, 4, 5]
b = ['tek', 'cift']
# result = [(i, 'cift' if i % 2 == 0 else 'tek') for i in a]
# print(result)

# -------------------------------------------------------------------SORU 3 -------------------------------------------------------------

# liste iclemi kullanarak esit uzunluklu sutunlardan olusan matrisel bir listeyi tek bir ifade ile transpoze ediniz.
# ornegin :  a = [[1,2,3], [4,5,6],[7,8,9]]
# iclemden elde edilen liste soyle olmalidir : [1,4,7],[2,5,8],[3,6,9]

'''a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for i in range(len(a)):
    cols = []
    for x in a:
        cols.append(x[i])
    result.append(cols)
# print(result)

result_2 = [[x[i] for x in a] for i in range(len(a))]
# print(result_2)'''

# -------------------------------------------------------------------SORU 4 ------------------------------------------------------------------

# Yukardaki soruyu sutun uzunluklari esit olmayan matrisler icin liste iclemlerini kullanarak tek bir ifade ile cozunuz.
# ornegin matris soyle olsun :

'''a = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 11], [10]]

max_col = 0
for i in range(len(a)):
    if len(a[i]) > max_col:
        max_col = len(a[i])
print(max_col)

result = []
for i in range(max_col):
    column = []
    for x in a:
        if len(x) > i:
            column.append(x[i])
    result.append(column)

# print(result)

result1 = [[x[i] for x in a if len(x) > i] for i in range(max([len(row) for row in a]))]
# print(result1)
'''
# -------------------------------------------------------------------SORU 5 ------------------------------------------------------------------

# bir listenin tum n'li (n listenin uzunlugundan buyuk olamaz) orneklerinin ortalamalarinin ortalamasini liste iclemlerini kullanarak tek bir ifade biicminde olusturunuz.
# Merkezi limit teoremine gore bu ortalmamanin ana kutle ortalmasina esit olmasi gerekmektedir.
# ornegin :
# a = [1,2,3,4,5]

# burada bu listenin ikili orneklerinin ortalamalarinin ortalamamlari hesaplanancak olsun.
# budurumda siz listenin tum ikili alt kumelerini bulup, bunlarin ortalamamlarini hesaplayip onun ortalamasini bulmalisiniz.

# ipucu : listenin n'li alt kumleri icin itertools.combinations fonksiyonunu kullaniniz.Ortalama almak icin statics.mean fonksiyonunu kullannabilirisninz.

import statistics
import itertools

a = [1, 2, 3, 4, 5]
combination_list = list(itertools.combinations(a, 2))
mean_toplam = 0
for i in combination_list:
    mean_value = statistics.mean(i)
    mean_toplam += mean_value

# print(mean_toplam / len(combination_list))


SAMPLE_SIZE = 2
result_mean = statistics.mean([statistics.mean(i) for i in list(itertools.combinations(a, SAMPLE_SIZE))])

# -------------------------------------------------------------------SORU 6 ------------------------------------------------------------------

# s isimli bir degiskende bir yazi bulunuyor olsun.Yazinin sozcuklerinin bosluk karakterleri ile ayrilmis oldugu varsayilsin.
# oyle bir liste iclemi iceren ifade yaziniz ki bunun sonucunda yazidaki sozcuklerde sesli harfler yok edilsin.Ornegin :

# ornegin s = 'bugun hava cok guzel' yazacaginiz iclem iceren ifadeden elde edilecek yazi soyle olmalidir: bgn hv ck gzl

# yani girdi yazisindaki sozcuklerin arasinda birden fazla bosluk karakteri bulunabilir ancak elde edilecek yazida sozcukler arasinda tek bosluk olmali.

s = input('bir yazi giriniz : ')

text = ''
for i in s.split(' '):
    s_new = []
    for x in i:
        if x in 'aeioüuö':
            continue
        s_new.append(x)
    result = ''.join(s_new)
    text += result + ' '
#print(text)

result_3 = ' '.join([''.join([c for c in w if c not in 'aeouüöi']) for w in s.split()])
print(result_3)
