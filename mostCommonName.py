def mostCommonName(L):
    dictionary1 = {}
    max = 0
    s = set()
    for element in L:
        count = dictionary1.get(element, 0) + 1
        dictionary1[element] = count
    if dictionary1[element] > max:
        max = count
    if dictionary1[element] == max:
        s.add(element)
    return s


j = "scott"
def hi(j):
    print(j)

print(hi(j))
