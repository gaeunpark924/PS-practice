def search_pattern(strl, length, a):
    pattern = ""
    for i in range(length):
        cnt = 0
        for j in range(a-1):
            if strl[j][i] == strl[j+1][i]:
                cnt += 1
                continue
            elif strl[j][i] != strl[j+1][i]:
                pattern += '?'
                break
        if cnt == a-1:
            pattern += strl[0][i]
    return pattern

a = int(input())
strl = []
for i in range(a):
    strl.append(input())
print(search_pattern(strl, len(strl[0]), a))
