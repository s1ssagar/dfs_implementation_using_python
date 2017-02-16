from stack import Stack

result = Stack()

def depth_first_search(dictionary, vertex):
    if vertex not in result.show_stack():
        result.push(vertex)
    if dictionary == {}:
        return
    if vertex in dictionary.keys():
        if dictionary[vertex] == []:
            dictionary.pop(vertex)
            depth_first_search(dictionary, result.get_item())
        else:
            for repeated in dictionary[vertex]:
                if repeated in result.show_stack():
                    dictionary[vertex].remove(repeated)
            min_val = min(dictionary[vertex])
            # REMOVE MIN VAL IF IT'S VISITED
            dictionary[vertex].remove(min_val)
            depth_first_search(dictionary, min_val)
    else:
        depth_first_search(dictionary, result.show_stack()[result.show_stack().index(vertex)-1])

    

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
    depth_first_search(dic, "S")
    print result.show_stack()
    

def main():
    read_file()

if __name__ == "__main__":
    main()