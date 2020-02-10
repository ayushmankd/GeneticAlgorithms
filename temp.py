s1 = [8, 4, 7, 3, 6, 2, 5, 1, 9, 0]
s2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c1 = 3
c2 = 8
swapped = s1, s2
map_ = s1[c1:c2], s2[c1:c2]
def _repeated(element, collection):
    c = 0
    for e in collection:
        if e == element:
            c += 1
    return c > 1
for i in range(n):
    if not c1 < i < c2:
        for j in range(2):
            while _repeated(swapped[j][i], swapped[j]):
                map_index = map_[j].index(swapped[j][i])
                swapped[j][i] = map_[1 - j][map_index]