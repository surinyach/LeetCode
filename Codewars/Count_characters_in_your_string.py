def count(s):
    if not s:
        return {}
    
    res = {}
    for c in s:
        if not c in res:
            res[c] = 1
        else:
            res[c] += 1
            
    return res