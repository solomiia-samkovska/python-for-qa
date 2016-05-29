def concatenate_str(str):
    str_res = str[:10] + str [-10:]
    return str_res

def main():
    str = '0123456789wwww0123456789'
    new_str = concatenate_str(str)
    print new_str

if __name__ == '__main__':
    main()