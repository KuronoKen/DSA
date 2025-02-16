import json

class Student:
    def __init__(self,id,name,gpa):
        self.std_id = id
        self.name = name
        self.gpa = gpa
        pass
    
    def print_details(self):
        print(f'ID: {self.std_id}')
        print(f'Name: {self.name}')
        print(f'GPA: {self.gpa:.2f}')



def binary_search(data:list,name):
    begin = 0
    end = len(data)-1
    mid = -1
    found : Student = None
    compare = 0
    while end != mid or begin != mid:
        compare += 1
        mid = (begin+end)//2
        if name == data[mid].name:
            found = data[mid]
            break
        elif name > data[mid].name:
            begin = mid + 1
        elif name < data[mid].name:
            end = mid - 1
        if begin < 0 or end > len(data) or begin > end:
            break
        
    if found:
        print(f'Found {found.name} at index {mid}')
        found.print_details()
    else:
        print(f'{name} does not exists.')
    print(f'Comparisons times: {compare}')


def main():
    inplist = json.loads(input())
    outlist = []
    for i in inplist:
        std = Student(i["id"],i["name"],i["gpa"])
        outlist.append(std)
    binary_search(outlist,input())

main()