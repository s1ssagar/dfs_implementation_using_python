class Stack:
    def __init__(self):
        self.arr = [-1,]
    def push(self, value):
        self.arr.append(value)
    def pop_value(self):
        if self.arr[-1] == -1:
            return "Fuck off empty stack"
        else:
            return self.arr.pop()
    def get_item(self):
        if self.arr[-1] != -1:
            return self.arr[-1]
        else:
            print "Empty stack"
    def show_stack(self):
        return self.arr[1:]
    def clear_stack(self):
        self.arr = []