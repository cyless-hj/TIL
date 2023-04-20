def solution(n, words):
    answer = []
    word_set = set()
    say = ''
    for idx, word in enumerate(words):
        if say == '':
            word_set.add(word)
            say += word
        else:
            if say[-1] == word[0] and word not in word_set:
                word_set.add(word)
                say = word
            else:
                return [idx % n + 1, idx // n + 1]

    return [0, 0]