def bad_match_table(needle):
    m = len(needle)
    skip = []
    # 256 total characters in ASCII extended
    # 1 char = 1 Byte = 8 bits = 2^8 = 256 possible values
    for i in range(256): skip.append(m)
    for i in range(m - 1): skip[ord(needle[i])] = m - i - 1
    return skip


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # https://medium.com/@fsaldana/the-boyer-moore-horspool-algorithm-51b785afde67
    # Boyer Moore Horspool Algorithm
    skip_table = bad_match_table(needle)
    m = len(needle)
    n = len(haystack)
    
    if m > n: return -1

    i = m - 1
    while i < n: 
        skip = 0
        for j in range(m):
            if needle[m - 1 - j] != haystack[i - j]:
                print("diferente! " + needle[m - 1 - j] + " " + haystack[i - j] + " i = " + str(i) + " j = " + str(j))
                print(skip_table[ord(haystack[i - j])])
                if j != 0: skip = m
                else: skip = skip_table[ord(haystack[i - j])]
                break
            elif j == m - 1:
                return i - j

        i += skip
        print(i)

    return -1

haystack = "trusthardtoothbrushes"
needle = "tooth"
print(strStr(haystack, needle))