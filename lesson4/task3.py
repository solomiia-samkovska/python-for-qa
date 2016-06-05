
import xml.etree.ElementTree as etree

def main():
    habra_xml = etree.parse('habraharb_all.xml')
    root = habra_xml.getroot()
    print(root)

    items = root.findall('.//item')
    print len(items)
    for item in items:
        title = item.find('.//title')
        author = item.find('.//author')

        categories = item.findall('.//category')
        category_text = [category.text.strip() for category in categories]

        print(u'Стаття: ' + title.text.strip())
        print(u'Автор: ' + author.text.strip())
        print(u"Категорії: " + u", ".join(category_text))


if __name__ == '__main__':
    main()

