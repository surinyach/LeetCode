def solution(s):
    i = 1
    while i < len(s):
        c = s[i]
        if ord(c) >= ord("A") and ord(c) <= ord("Z"):
            s = s[0:i] + " " + s[i:len(s)]
            i += 1
        i += 1
    return s