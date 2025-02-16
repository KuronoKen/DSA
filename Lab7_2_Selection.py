import json
def selectionsort(lis,last):
    current = 0
    compare = 0
    while current <= last:
        smallest = current
        for i in range(current+1,last+1):
            compare += 1
            if lis[i] < lis[smallest]:
                smallest = i
        lis[current],lis[smallest] = lis[smallest],lis[current]
        current += 1
        if current <= last:
            print(lis)
    print(f'Comparison times: {compare}')
def main():
    lis = json.loads(input())
    last = int(input())
    selectionsort(lis,last)
main()