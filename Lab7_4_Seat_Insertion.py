import json
def insertionSort(lis,last):
    compare = 0
    if last == 0:
        return lis
	
    for i in range(1,last+1):
        j = i-1
        current = lis[i]
        cond = current[0] < lis[j][0] or (current[0] == lis[j][0] and int(current[1:]) < int(lis[j][1:]))
        while j >= 0 and cond:
            compare += 1
            lis[j+1] = lis[j]
            j -= 1
            cond = current[0] < lis[j][0] or (current[0] == lis[j][0] and int(current[1:]) < int(lis[j][1:]))
        lis[j+1] = current
        if j >= 0:
            compare += 1
        print(lis)
    print(f'Comparison times: {compare}')


def main():
    lis = json.loads(input())
    last = int(input())
    insertionSort(lis,last)

main()