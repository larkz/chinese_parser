# from main_class.classes import Class1
import re
import codecs
import numpy as np
import sys


ipath= u"./data/NCDC/上海/虹桥/9705大626661750dat.txt"
re.findall(u'[\u4e00-\u9fff]+', ipath)

for i in range(len(ipath)):
    if ipath[i] > u'\u4e00' and ipath[i] < u'\u9fff':
        print(ipath[i]
        )
def is_chinese(chn_str):
    chn_str[0] > u'\u4e00' and chn_str[0] < u'\u9fff'

ipath = "larkin"

def find_chinese_characters(chn_str):
    word_array = []
    for i in range(len(chn_str)):
        if chn_str[i] > u'\u4e00' and chn_str[i] < u'\u9fff':
            word_array.append((i, chn_str[i]))
    return word_array

i = 0
l = []
f = codecs.open('character_list.txt', encoding='utf-8')
for line in f:
    l.append(find_chinese_characters(line))
    i = i + 1
    print(i)

f.close

ranked_words = []
c = 0
for rank, tups in enumerate(l):
    print((rank, tups))
    for ind, tup in enumerate(tups):
        if tup[0] < 6 and tup[0] > 0:
                if tup[1] != "语":
                        ranked_words.append( (ind, tup[1]) )



# set the frequency slice
beg = int(sys.argv[1])
end = int(sys.argv[2])
print_char = int(sys.argv[3])
print(beg)
print(end)
r = ranked_words[beg:end]
r_subset = list(map(lambda x: x[1], r))

# keep running this

for i in range(0, print_char):
        print(np.random.choice(r_subset, 1)[0])




'''
while 1:
        print("ll")


key = 1
while key == 1:
        key = input("Press 1 to continue, any key to exit:")
        print(key)
        print(np.random.choice(r_subset, 1)[0])
'''





            
