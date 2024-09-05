'''
 int bir degeri parametre olarak alan ve asagidaki kalibi ekrana basab disp_shape isimli fonksiyonu yaziniz:
 fonksiynonun parametrik yapisi soyle olmalidir :
     def disp_shape(n)
            pass

'''


# 1---------------ODEV 1 --------------------------------------------------------
def disp_shape(n):
    for i in range(n):
        print(' ' * i, end='')
        for k in range(i + 1, n + 1):
            print(k, end=' ')
        print()

    for i in range(n - 2, -1, -1):
        print(' ' * i, end='')
        for k in range(i + 1, n + 1):
            print(k, end=' ')
        print()


# disp_shape(6)

# --------------------------------------------------------------------ODEV 2------------------------------------------------------------------------------#

# Asagidaki deseni cikartan crown isimli fonksionu yaziniz.Fonksiyonun parametrik yapisi soyle olmalilidir:

'''
     * en asagi satirda bosluk yoktur
     * sayilar 1'den n'e kadar artip eksiltilmelidir.
     * girilen sayi yuksleme ve alcalmada yinelenmektedir.
     * kalvyeden bir deger girerek fonksiyonu o dgerle cagiirp deseni ekranna bastiriniz.
     * en asagi satirin yukariisnda 2'ser bolsuk daha yukariisnda 4'er bosluk biicminde bir desen vardir.En tepedeki bosluk " n*2-2 " tanedir.

'''


def crown(n):
    space_count = n
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(f'{k}', end='')
        print(end=' ' * (space_count * 2 - 2))
        space_count -= 1
        for k in range(i, 1, -1):
            print(k, end='')

        for k in range(1, i + 1):
            print(f'{k}', end='')
        print(end=' ' * ((space_count + 1) * 2 - 2))
        for k in range(i, 0, -1):
            print(k, end='')
        print()


# crown(6)


# --------------------------------------------------------------------ODEV 3------------------------------------------------------------------------------#

# fonksiyon bool bir deger geri dondurmeliidir..

# sonra dongu icersinde kalvyeden sayi okuyarak bu sayiyla fonksiyonu cagiriinz.
# geri donus degerine bakarak sayinin armstrong olup olmadigni kontrol edniz.
# 0 girildigninde donguden cikiniz...

import math


def is_armstrong(a):
    # result = '\n'.join(['adana', 'adıyaman', 'afyon'])
    total = 0
    for c in str(a):
        total += int(c) ** 3
    return total == a


'''while True:
    a = int(input('bir sayi giriniz: '))
    if a == 0:
        break
    print('Armstrong' if is_armstrong(a) else 'Armstrong degil')'''


# --------------------------------------------------------------------SORU 4 ------------------------------------------------------------------------------#

# klavydeden bir sayi isteyiniz.Sonra yazi icerisindeki sozcukleri aralarina tek bosluk karakteri koyarak yan yana tersten yazdiriniz.
# bugun hava cok souguk ---------- soguk bugun hava cok

def reversed_text(text):
    result = text.split(' ')
    revers_list = result[::-1]
    k = ' '.join(revers_list)
    print(k)


# val = input(' bir text giriniz : ')
# reversed_text(val)


# --------------------------------------------------------------------SORU 5 ---------------------------------------------------------------------------------#
# INT DEGERLERDEN OLUSAN DOLASILABILIR BIR NESNEYI PARAMETRE OLARAK ALAN VE O LISTEDI SAYILARIN BASAMAKLARINDAN DEMET ELDE EDEREK BIR DEMET DIZISINE DONEN DIGITATE ISIMLI FONKSIOYNU YAZINIZ...

def digitate(vals):
    vals_list = []

    for i in vals:
        inner_list = []
        k = ''.join(str(i))
        l = tuple(k)
        for j in range(len(l)):
            convert_int = int(l[j])
            inner_list.append(convert_int)
        convert_tuple = tuple(inner_list)
        vals_list.append(convert_tuple)
    return vals_list


vals = [23, 4, 765, 34589, 42, 4857576, 0]
result = digitate(vals)


# print(result)

def digitate1(vals):
    result = []
    for x in vals:
        digits = []
        for c in str(x):
            digits.append(int(c))
        result.append(tuple(digits))

    return result


# vals = [23, 4576, 34, 2]
# print(digitate1(vals))


def digitate2(vals):
    result = []
    for x in vals:
        result.append(tuple(map(int, str(x))))
    return result


# vals = [23, 4576, 34, 2]
# print(digitate2(vals))


a = [1, 2, 3, 4, 5]


def square(x):
    return x * x


iterable = map(square, a)  # map bize bir dolasim nesnesi verir

x = list(iterable)
# print(x)

# --------------------------------------------------------------------SORU 6 ---------------------------------------------------------------------------------#

'''sentence = input(' bir yazi giriniz : ')
sen_lsit = sentence.split()
new_list = []
for word in sen_lsit:
    if word not in new_list:
        new_list.append(word)
print(new_list)'''


# --------------------------------------------------------------------SORU 7 ---------------------------------------------------------------------------------#

# int bir degeri parametre olarak alip kalibi ekrana basan print_shape fonksionunu yaziniz.
# Fonksiyonun paarmetrik yapisi :
def print_shapee(n):
    space_count = 0
    for i in range(n, 0, -1):
        print(' ')
        for j in range(i):
            print('*', end='')
        space_count += 1
        print(end=' ' * (space_count * 2 - 2))
        for j in range(i):
            print('*', end='')

    for i in range(1, n + 1):
        print(' ')
        for k in range(i):
            print('*', end='')
        space_count -= 1
        print(end=' ' * (space_count * 2))

        for k in range(i):
            print('*', end='')


# print_shapee(5)

def print_shape(n):
    for i in range(n):
        print('*' * (n - i) + ' ' * (i * 2) + '*' * (n - i))
    for i in range(1, n + 1):
        print('*' * i + ' ' * ((n * 2) - (i * 2)) + '*' * i)


# print_shape(5)


def print_shape_sir(n):
    for i in range(n):
        print('*' * (n - i) + ' ' * (i * 2) + '*' * (n - i))
    for i in range(n - 1, -1, -1):
        print('*' * (n - i) + ' ' * (i * 2) + '*' * (n - i))


# print_shape_sir(5)

# --------------------------------------------------------------------SORU 8 ---------------------------------------------------------------------------------#

# bir karakteri parametre olarak alip (karakter kucuk ya da buyuk harf olabilir) asagidaki kalibi ekrana yazdiran
# disp_char_pattern isimli fonksiyonu yaziniz:

def disp_char_pattern(ch):
    ch_upper = ch.upper()
    difference = ord(ch_upper) - ord('A')

    for i in range(ord('A'), ord(ch_upper)):
        # print(' '* difference + chr(i) + ' '*(ord(ch_upper)-i) + chr(i) )
        if i == ord('A'):
            print(' ' * (ord(ch_upper) - i + 1) + chr(i) + ' ' * (difference - (ord(ch_upper) - i)) * 2)
        print(' ' * (ord(ch_upper) - i) + chr(i + 1) + ' ' * (difference - (ord(ch_upper) - i)) * 2 + ' ' + chr(i + 1))

    for i in range(ord(ch_upper) - 1, ord('A') - 1, -1):
        if i == ord('A'):
            print(' ' * (ord(ch_upper) - i + 1) + chr(i) + ' ' * (difference - (ord(ch_upper) - i)))
        else:
            print(' ' * (ord(ch_upper) - i + 1) + chr(i) + ' ' * (difference - (ord(ch_upper) - i + 1)) * 2 + ' ' + chr(
                i))


# disp_char_pattern('F')

# --------------------------------------------------------------------SORU 9  ---------------------------------------------------------------------------------#

# pi sayiisni geri donus degeri olarak veren fonksiyonlari asagida belirtildigi gibi yaziniz :

# a) Newton tarafindan onerilen asagidaki seriyi newton_pi isimli fonksion ile gerceklestiriniz :
# buradaki k n'nin alabilacegi son degeri belirtmektedir.Fonksiyon seri toplamina geri donmelidir.
# math modulundeki faktoriyel fonksiyonu da kullanilabilir.
################################################# a) ###############################################
import math


def newton_pi(k):
    total = 0
    for n in range(k + 1):
        total += ((pow(2, n + 1)) * (pow(math.factorial(n), 2)) / math.factorial(2 * n + 1))
    return total


'''while True:
    k = int(input('k : '))
    if k == 0:
        break
    pi = newton_pi(k)
    print(pi)'''


################################################# b) ###############################################

def somayaji_pi(n):
    base = 3

    for i in range(1, n + 1):
        if i % 2 == 0:
            base -= 4 / ((2 * i + 1) ** 3 - (2 * i + 1))
        else:
            base += 4 / ((2 * i + 1) ** 3 - (2 * i + 1))

    return base


while True:
    n = int(input('n : '))
    if n == 0:
        break
    pi = somayaji_pi(n)
    print(pi)



# --------------------------------------------------------------------SORU 10   ---------------------------------------------------------------------------------#

# Bir isim ve iki ayri sayidan olusan uclu demet listesini parametre olarak alip bu listeyi demetin birinci,
# ikinci ve ucuncu elemnalrina gore siraya dizen sort_tuple_list isimli fonksioynu yaziniz :
# Demetin ilk elemanlari esitse, ikinci elemanlarina, onlar da esitse ucuncu elemalarina bakilarak siraya dizme islemi uygulanacaktir.Ornegin :

def sort_tuple_list(a):
    a.sort()


a = [('Tom', 19, 80), ('json', 22, 90), ('johny', 17, 91), ('jony', 17, 93)]
sort_tuple_list(a)
#print(a)

