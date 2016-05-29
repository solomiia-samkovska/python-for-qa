
def count_elements_while(arr):
    len_arr = len(arr)
    sum13 = 0
    i = 0
    while i < len_arr and arr[i] != 13:
        if type(arr[i]) is int:
            sum13 = sum13 + arr[i]
        i = i+1
    return sum13

def count_elements_for(arr):
    sum13 = 0
    for el in arr:
        if type(el) is not int:
            continue
        elif el == 13:
            break
        sum13 = sum13 + el
    return sum13

def main():
    print(count_elements_for([1, 1, 3, 'd']))
    print(count_elements_while([1, 1, 3, 13,2]))

if __name__ == '__main__':
    main()

