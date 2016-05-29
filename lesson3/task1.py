def comprehension_generate():
    new_list = [i for i in range(1,10000) if ((i % 2 == 0) & (i % 3 == 0))]
    return new_list

def filter_generate():
    new_list = filter(lambda i: i % 2 == 0 and i % 3 == 0, range(1,10000))
    return new_list

def main():
    print 'Generate list using list comprehension approach:'
    print comprehension_generate()
    print 'Generate list using filter function:'
    print filter_generate()

if __name__ == '__main__':
    main()
