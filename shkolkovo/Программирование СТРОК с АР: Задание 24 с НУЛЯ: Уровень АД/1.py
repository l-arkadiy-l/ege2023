f = open('1__1332q.txt')
abc = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
t = ''.join(list(f))
for i in abc:
    for j in abc:
        if i != j:
            t = t.replace(f'{i}{j}', f'{i} {j}')  # VVMMDDKKL -> #VV MM DD KK L
k = t.split()
c = 0  # counter
m = 0  # maximum
if len(k[0]) >= 2:
    c, m = 1, 1
for i in range(1, len(k)):
    if k[i - 1][0] != k[i][0] and len(k[i]) == 2:
        if (c == 1 and len(k[i - 1]) >= 2) or len(k[i - 1]) == 2:
            c += 1
    else:

        m = max(c, m)
        c = 1
print(m * 2) # solution
