import json
def insertionSort(lis,last):
    compare = 0
    if last == 0:
        return lis
	
    for i in range(1,last+1):
        j = i-1
        current = lis[i]
        while j >= 0 and current < lis[j]:
            compare += 1
            lis[j+1] = lis[j]
            j -= 1
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