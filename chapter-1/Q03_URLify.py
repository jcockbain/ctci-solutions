def urlify(string, length):
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == " ":
            string[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            string[new_index - 1] = string[i]
            new_index -= 1

    return string
