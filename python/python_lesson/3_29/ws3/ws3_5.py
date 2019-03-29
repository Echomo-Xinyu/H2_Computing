handler = open("R&J_WORD_FREQS.txt", 'r')
word_list = {}
word_list['a'] = 0

def checkNotPresent(str1):
    if word_list==None:
        return True
    for a in word_list.keys():
        if a==str1:
            return False
    return True

mf_count = 0
for line in handler:
    data = line.strip().split(" ")
    for i in range(len(data)):
        rdata = data[i].lower()
        if rdata.isalpha() and checkNotPresent(rdata):
            word_list[rdata] = 1
        elif rdata.isalpha():
            word_list[rdata] += 1
            mf_count = max(mf_count, word_list[rdata])

print(mf_count)
        
            