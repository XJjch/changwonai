O = 'Abcdefg'

# break 사용하면 'd' 에서 끝남
for X in O:
    if X in ('d'):
        break
    print(X)
print('끝')

# continue 사용하면 'b' 건너뛰고 다 돌고 끝남
for Y in O:
    if Y in ('b'):
        continue
    print(Y)
print("끝")