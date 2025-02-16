class ArrayStack():
    def __init__(self):
        self.size = 0
        self.data = list()
        pass
    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.data.pop()
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
    def is_empty(self):
        empty = True
        if self.data:
            empty = False
        return empty
    def get_stack_top(self):
        pointer = None
        for i in self.data:
            pointer = i
        if not pointer:
            print("Underflow: Cannot get stack top from an empty list")
        return pointer
            
    def get_size(self):
        return self.size
    def print_stack(self):
        print(self.data)
    
def is_parenthese_matching(text:str):
    stack = ArrayStack()
    unmatched = ArrayStack()
    for i in text:
        if i == "(":
            stack.push(i)
        elif i == ")":
            x = stack.pop()
            if not x:
                unmatched.push(i)
    returning = stack.is_empty() and unmatched.is_empty()
    return returning

def main():
    text = input()
    matching = is_parenthese_matching(text)
    if matching:
        print(f'Parentheses in {text} are matched')
    else:
        print(f'Parentheses in {text} are unmatched')
    print(matching)

main()