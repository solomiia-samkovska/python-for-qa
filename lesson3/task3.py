from datetime import datetime

def str_to_date(str):
    formats = ['%d %b %Y', '%d %B %Y', '%d.%m.%Y', '%m/%d/%y']
    for frm in formats:
        try:
            date_object = datetime.strptime(str, frm)
            return date_object
        except ValueError:
            print("Date {} doesn't support {} format".format(str, frm))

def main():
    print(str_to_date('03/2491'))

if __name__ == '__main__':
    main()

