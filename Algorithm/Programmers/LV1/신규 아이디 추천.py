import string

def solution(new_id):
    answer = ''
    new = new_id.lower()

    allow_list = list(string.ascii_lowercase)
    allow_list.append('-')
    allow_list.append('_')
    allow_list.append('.')
    for i in range(10):
        allow_list.append(str(i))

    for s in new:
        if s not in allow_list:
            new = new.replace(s, '')

    while True:
        b = len(new)
        new = new.replace('..', '.')
        if b == len(new):
            break

    if new[0] == '.':
        if len(new) == 1:
            new = ''
        else:
            new = new[1:]
    if new[-1:] == '.':
        if len(new) == 1:
            new = ''
        else:
            new = new[:-1]

    if new == '':
        new = 'a'

    if len(new) >= 16:
        new = new[:15]
        if new[-1:] == '.':
            new = new[:-1]

    if len(new) <= 2:
        new += new[-1] * (3 - len(new))
    answer = new
    return answer