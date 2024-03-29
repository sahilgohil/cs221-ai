def edit_distance(s,t):
    cache = {}
    def recurse(m ,n):
        if (m,n) in cache:
            return cache[(m,n)]
        elif m == 0:
            result = n
        elif n == 0:
            result = m
        elif s[m-1] == t[n-1]:
            result = recurse(m-1,n-1)
        else:
            substitutionCost = 1 + recurse(m-1,n-1)
            insertionCost = 1 + recurse(m,n-1)
            deletionCost = 1 + recurse(m-1,n)
            result = min(substitutionCost, insertionCost, deletionCost)
            cache[(m,n)] = result
        return result
    return recurse(len(s),len(t))
print(edit_distance("a cat"*10,"the cats"*10))