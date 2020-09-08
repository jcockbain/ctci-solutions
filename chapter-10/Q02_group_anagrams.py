def group_anagrams(word_list):
    anagrams = {}
    for w in word_list:
        sorted_word = "".join(sorted(w))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(w)
        else:
            anagrams[sorted_word] = [w]

    res = []
    for sorted_word in anagrams:
        for word in anagrams[sorted_word]:
            res.append(word)

    return res
