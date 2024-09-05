# ------------------------------------------------------------- SORU 1-------------------------------------------------------------
# parametresi ile aldigiyazidaki karakterlerden artan sirada tamsayi olusturup bunu bir liste biciminde donduren
# increasing_numbers isimli fonksiyonu yaziniz.
import numpy


def increasing_number(s):
    vals = []
    prev_val = int(s[0])
    vals.append(prev_val)
    beg_index = 1

    for i in range(1, len(s)):
        val = int(s[beg_index: i + 1])
        if val > prev_val:
            vals.append(val)
            prev_val = val
            beg_index = i + 1
    return vals


# print(increasing_number('09745456'))


# ------------------------------------------------------------- SORU 2-------------------------------------------------------------------
# Bir listedeki yan yana n tane sayinin toplaminn en buyuygue ve o dizilimn baslangic indeksine bir demet olarak geri donen
# consecutive_total isimli bir fonksiyonu yaziniz :

def consecutive_total(a, n):
    prev_val = a[0]
    total_list = []
    total_sum = 0

    if n > len(a):
        return None, None

    for i in range(0, len(a)):
        vals = a[i: i + n]
        for k in range(n):
            if n > len(vals):
                break
            else:
                val = vals[k]
                total_sum += val
                prev_val = val
        total_list.append(total_sum)
        total_sum = 0

    return max(total_list), total_list.index(max(total_list)) + 1


a = [8, 3, 6, 4, 7]

# n = int(input('ardisillik miktarini giriniz : '))
# print(consecutive_total(a, n))
# birinci parametresi liste,ikincisi ardisillik miktarini belirtir.

# ------------------------------------------------------------- SORU 3-------------------------------------------------------------------

# Klavyeden sayi giriniz.Asagidaki deseni cikarttiniz.

# size = int(input('bir  size  giriniz : '))
size = 3


def display_size(size):
    for i in range(size):
        index = size - 1
        direction = -1

        print('-' * (size - i - 1) * 2, end='')
        for k in range(2 * i + 1):
            if k != 0:
                print('-', end='')
            print(chr(ord('a') + index), end='')
            if k == i:
                direction = 1
            index += direction
        print('-' * (size - i - 1) * 2)


# ------------------------------------------------------------- SORU 4 -----------------------------------------------------------------------------

# Hayali bir makinenin kartezyen koordinat sisteminde (0,0) konumunda oldugunu varsayalim.Bu makineye su komutlar gonderilmektedir :


def move_machine(s):
    text = s.split(' ; ')
    x = 0
    y = 0
    for move in text:
        direction = move.split()
        val = int(direction[1])
        if 'up' in direction:
            y += val
        elif 'down' in direction:
            y -= val
        elif 'left' in direction:
            x -= val
        elif 'right' in direction:
            x += val

    print(x, y)


s = ' up 4 ; down 2 ; down 3 ; left 4 ; up 2 '
# move_machine(s)


# ------------------------------------------------------------- SORU 5 -----------------------------------------------------------------------------

# bir anakutle icersinden cekilen rastgele orneklere iliskin ortalamalarin dagilimi normal olma egilimimddir.
# buna istatistikte merkezi limit teoremi denilmektedir.
# ornekler ne kadar buyuk olursa ve ornek sayisi ne kadar fazla olursa ornek ortalamalri normal dagilima o kadar yaklasir.
# ana kutle dailimi ne olursa olsun boyledir.

# - 0 ile 10.000 arasindaki sayilar anakutleyi temsil etsin.
# - ornek buyuklugu 3 olarak belirleyiniz.
# anakutleden rastgele 3'luk rastegele ornek cekerek ortalamalarini hesaplayiniz.
# bu islemi random.sample fonksiyonuyla yapanbilirisniz.ornegin 5000 kez

# 20 elemanli bir liste acarak sifirlayiniz.
import random
import statistics

FREQUENCE = 500
mean_list = []
freq_list = [0] * 20
# print(freq_list)
for _ in range(5000):
    column = random.sample(range(10_000), 3)
    mean_cal = statistics.mean(column)
    index = round(mean_cal / FREQUENCE) - 1
    freq_list[index] += 1

for i in freq_list:
    pass
    # print('X' * round(i / 30))

# ------------------------------------------------------------- SORU 6 -----------------------------------------------------------------------------
import random
import statistics
import matplotlib.pyplot as plt

FREQUENCE = 500
mean_list = []
freq_list1 = [0] * 100

for _ in range(5000):
    column = random.sample(range(10_000), 10)
    mean_cal = statistics.mean(column)
    # print(mean_cal)
    index = round(mean_cal / FREQUENCE)
    freq_list1[index] += 1

# plt.hist(freq_list1, 100)
# plt.show()

# ------------------------------------------------------------- SORU 7 -----------------------------------------------------------------------------

# x degerlernini -10'dan 10'a kadar 0.1 aririmla bir liste bcicminde olustuurnuz.
# Gauss fonksiyonunu kullanarak bu degerleden y degerlerini elde edip bu degerleri bir listede toplayiniz.
# Matplotlib kutuphanesindeki plot fonksiyonuyla can egrisini asagidaki gibi cizdiriniz :

import matplotlib.pyplot as plt
import math


def gauss(x, mu, sigma):
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)


xs = [i * 0.1 for i in range(100, 101)]
ys = [gauss(x, 0, 1) for x in xs]

plt.plot(xs, ys)
plt.show()
