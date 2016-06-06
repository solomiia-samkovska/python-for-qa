# -*- coding: utf-8 -*-
from lxml import html


def main():
    dom = html.parse('http://deshevshe.net.ua/laptop-asus/asus_x540lj_x540lj_xx002d_chocolate_blac')

    price = dom.find('//*[@itemprop="price"]')
    print(u"Price: " + price.text)

    exist = dom.find('//*[@class="wareAvail"]')
    if exist.text_content() == u'Нет в наличии':
        print("The product is out of stock")

if __name__ == '__main__':
    main()

