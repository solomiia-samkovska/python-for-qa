import json

def read_file(file):
    with open(file,'r') as f:
        file_str = f.read()
        return file_str

def update_owner(jsn):
    for item in jsn:
        item['Owner'] = 'qa5'
    return jsn

def write_to_file(file, str):
    with open(file, 'w') as f:
        f.write(str)


def main():
    str_json = read_file('bugs.json')
    parsed_json = json.loads(str_json)
    print(parsed_json)
    updated_json = update_owner(parsed_json)
    print(updated_json)
    new_json = json.dumps(updated_json)
    print(new_json)
    write_to_file('new_bugs.json',new_json)

if __name__ == '__main__':
    main()

