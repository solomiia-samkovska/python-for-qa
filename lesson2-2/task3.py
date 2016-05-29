
def del_duplicates(list):
    list_res = []
    for el1 in list:
        count = 0
        for el2 in list:
            if el1 == el2:
                count += 1
        if count == 1:
            list_res.append(el1)
    return list_res

def main():
    list = [1,2,3,4,4,6,2]
    new_list = del_duplicates(list)
    print(new_list)

if __name__ == '__main__':
    main()
