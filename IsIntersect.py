import json
def main():
    l1 = json.loads(input())
    l2 = json.loads(input())
    l3 = json.loads(input())
    for i in l1:
        cond1 = i in l2
        cond2 = i in l3
        if cond1 and cond2:
            print(True)
            return
    print(False)

main()
            

