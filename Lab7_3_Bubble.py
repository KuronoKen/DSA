import json
def bubble(lis,last):
    compare = 0
    for i in range(last+1):
        swapped = False
        for j in range(last,i,-1):
            compare += 1
            if lis[j] < lis[j-1]:
                swapped = True
                lis[j],lis[j-1] = lis[j-1],lis[j]
        print(lis)
        if not swapped:
            break
    print(f'Comparison times: {compare}')
def main():
    lis = json.loads(input())
    last = int(input())
    bubble(lis,last)
main()