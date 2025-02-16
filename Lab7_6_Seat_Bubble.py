import json
def bubble(lis,last):
    compare = 0
    for i in range(last+1):
        swapped = False
        for j in range(last,i,-1):
            compare += 1
            cond = lis[j][0] < lis[j-1][0] or (lis[j][0] == lis[j-1][0] and int(lis[j][1:]) < int(lis[j-1][1:]))
            if cond:
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