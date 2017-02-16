from stack import Stack

result = Stack()
glo_stack = Stack()

def depth_first_search(dictionary, vertex):
    result.push(vertex)
    glo_stack.push(vertex)
    pivot = glo_stack.get_item()
    while glo_stack.show_stack() != []:
        if pivot in dictionary.keys():
            if dictionary[pivot] != []:
                while dictionary[pivot] != []:
                    result.push(min(dictionary[pivot]))
                    glo_stack.push(min(dictionary[pivot]))
                    dictionary[pivot].remove(glo_stack.get_item())
                    pivot = glo_stack.get_item()
                    if pivot not in dictionary.keys():
                        dictionary[pivot] = []
            else:
                glo_stack.pop_value()
                pivot = glo_stack.get_item()
        else:
            glo_stack.pop_value()
            pivot = glo_stack.get_item()
                
def read_file():
    dic = {}
    with open('arcs.txt','r+') as ofs:
        str1 = ofs.readlines()
        for arc in str1:
            temp = arc.split("->")
            first_ele = temp[0].strip()
            second_ele = temp[-1].strip()
            if first_ele in dic:
                temp_list = dic[first_ele]
                temp_list.append(second_ele)
                dic[first_ele] = temp_list
            else:
                dic[first_ele] = [second_ele]
    print dic
    # Start point
    depth_first_search(dic, "S")
    print result.show_stack()
    

def main():
    read_file()

if __name__ == "__main__":
    main()