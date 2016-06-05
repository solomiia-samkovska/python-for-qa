from lxml import etree

def main():
    course_xml = etree.parse('course.xml')
    xslt = etree.parse('course_transform.xml')

    transform = etree.XSLT(xslt)
    result = transform(course_xml)

    print(etree.tostring(result, pretty_print=True))

if __name__ == '__main__':
    main()
