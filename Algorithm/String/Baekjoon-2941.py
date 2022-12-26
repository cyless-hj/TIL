word = input()

alpabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpabet_list:
    word = word.replace(i, '*')

print(len(word))