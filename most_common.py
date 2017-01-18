from collections import Counter
b = Counter(raw_input()).most_common(3)
for j,k in b:
    print"%s %s" %(j,k)