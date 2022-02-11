def count_chars(s, chars):
    X = []
    for e in chars:X.append(0)
    for e in s:
        for i in range(len(chars)):
            if e == chars[i]:X[i] += 1
    return X
# exec(input().strip())