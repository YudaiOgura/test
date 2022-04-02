a = []
for i in range(5):
    c = list(input())
    for j in range(5):
        a.append(c[j])

count = 0
for i in range(5):
    b = a[i:25+i:5]
    if len(set(b)) == 1 and b[0] != '.':
        print(b[0])
        break
    else:
        count = count + 1

if count == 5:
    print('D')
