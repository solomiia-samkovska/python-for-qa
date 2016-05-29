import re


def read_file(file):
    with open(file,'r') as f:
        file_str = f.read()
        return file_str


def count_sentences(str):
    pattern = re.compile('\.\W')
    number = len(pattern.findall(str))
    return number


def main():
    text = read_file('alice_in_wonderland.txt')
    sentences = count_sentences(text)
    print sentences

if __name__ == '__main__':
    print 'Number of sentences:'
    main()

