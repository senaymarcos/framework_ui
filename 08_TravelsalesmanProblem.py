'''
a) Gezgin saticinin bulundugu A sehri ve diger sehirler asagidaki grafta gosterilmektedir:

b) Bir sehirden hangi sehirlere gidebildigi ve bunlarin yol uzakliklari bir sozluk nesnesinde bulundurulmalidir.Sozluk nesnesi soyle olabilir.

c) Burada her permustasyon icin yol yoktur.Arada dogrudan yol olmayan permutasyonlarin fark edilerek atlanmasi gerekir.

# yonsuz graf ise herhengi bir ok bulundurmuyor demektir.
'''
import itertools
import math
import sys

d = {'A': {'B': 5, 'C': 7, 'D': 10},
     'B': {'A': 5, 'D': 4, 'E': 17, 'G': 20},
     'C': {'A': 7, 'D': 6, 'F': 9},
     'D': {'A': 10, 'B': 4, 'C': 6, 'E': 3, 'F': 12},
     'E': {'B': 17, 'D': 3, 'F': 14, 'G': 6},
     'F': {'C': 9, 'D': 12, 'E': 14, 'G': 10},
     'G': {'B': 20, 'E': 6, 'F': 10}}

'''def find_distance(d):
    destination = 0
    for i in d:
        flag = 0
        start_point = i
        for k in d[start_point]:
            destinatioin_point = k
            if d[start_point][destinatioin_point] is None:
                continue
            else:
                destination += d[start_point][destinatioin_point]
                flag += 1
                if flag == 2:
                    break
        return destination


d_list = ['B', 'C', 'D', 'E', 'F', 'G']
total_path = itertools.permutations(d_list)
perm_count = math.factorial(len(d_list))
count = 0
for path in total_path:
    full_path = ('A',) + path + ('A',)
    path_s = find_distance(full_path)
    print(full_path)
    count += 1
    if count == perm_count / 2:
        break'''


def get_length(tour):
    tlen = 0
    for i in range(len(tour) - 1):
        ddict = d.get(tour[i])
        nlen = ddict.get(tour[i + 1])
        if nlen is None:
            return None
        tlen += nlen

    return tlen  # min tour : ('A', 'B', 'D', 'E', 'G', 'F', 'C', 'A'), min length : 44


cities = ['B', 'C', 'D', 'E', 'F', 'G']

min_len = sys.float_info.max
min_tour = []

for t in itertools.permutations(cities, len(cities)):
    tour = ('A',) + t + ('A',)
    if (tlen := get_length(tour)) is None:
        continue
    if tlen < min_len:
        min_len = tlen
        min_tour = tour
print(f'min tour : {min_tour}, min length : {min_len}')
