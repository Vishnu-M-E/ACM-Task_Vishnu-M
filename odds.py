def oddSum(arr):
    odd = [x for x in arr if x % 2 != 0]
    
    return sum(odd)


lis = []
for i in range(101):
    e = input()
    if e == '':
        break
    else:
        lis.append(int(e))

print(oddSum(lis))
