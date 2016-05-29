def last_el(str):
        list_el = str.split(',')
        print(list_el[-1])

def main():
    str = '1,2,3,44,55,66,7aa'
    last_el(str)

if __name__ == '__main__':
    main()