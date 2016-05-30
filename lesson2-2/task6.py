
def dict_creation(n = 100):
    dict = {i:i*i for i in range(1,n) if (i % 2 == 0)}
    return dict

def main():
    print(dict_creation(10))

if __name__ == '__main__':
    main()

