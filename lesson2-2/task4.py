
def calc_expression(a,b,c):
    result = int((a or not b) and (c or not a))
    print a,b,c,"|",result

def view_results():
    print "(a or not b) and (c or not a)"
    print "abc|r"
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
               calc_expression(x,y,z)

def main():
   view_results()

if __name__ == '__main__':
    main()
