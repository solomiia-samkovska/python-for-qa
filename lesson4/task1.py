from lxml import html


def main():
    dom = html.parse('http://deshevshe.net.ua/multifunctiondevice/')

    price = dom.find('//*[@id="viewGaleryBl"]/div[1]/div/div[2]/div[1]')
    print(price.text)

if __name__ == '__main__':
    main()

