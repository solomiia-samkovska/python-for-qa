
str_test = 'Hi one, hi two, hi three. Hi!'

low_str = str_test.lower()
n = low_str.count('hi')
new_str = low_str.replace('hi', 'bye')

print(n)
print(new_str)