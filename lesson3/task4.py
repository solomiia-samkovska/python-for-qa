import csv

def read_file():
    array_csv = []
    with open('Python for QA - bugs list - Sheet1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            array_csv.append(row)
        return array_csv

def remove_low(data):
    result = [item for item in data if item['Priority'] != 'low']
    return result

def decrease_priority(data):
    priorities = ['low', 'medium', 'high', 'critical']
    for item in data:
        current_index = priorities.index(item['Priority'])
        item['Priority'] = priorities[current_index - 1]
    return data

def save_to_file(data):
    with open('new_bugs_list.csv', 'w') as csvfile:
        header = ['#', 'Description', 'Environment', 'Priority', 'Owner', 'Created At']
        writer = csv.DictWriter(csvfile, fieldnames=header)

        writer.writeheader()
        for item in data:
            writer.writerow(item)

def main():
    bug_list = read_file()
    print bug_list
    bug_list_filtered = remove_low(bug_list)
    print bug_list_filtered
    bug_list_dec_priority = decrease_priority(bug_list_filtered)
    print bug_list_dec_priority
    save_to_file(bug_list_dec_priority)


if __name__ == '__main__':
    main()

