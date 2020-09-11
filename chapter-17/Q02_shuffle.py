import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    for index_we_are_choosing_for in range(0, len(the_list) - 1):

        random_choice_index = get_random(
            index_we_are_choosing_for, last_index_in_the_list
        )

        # Place our random choice in the spot by swapping
        if random_choice_index != index_we_are_choosing_for:
            the_list[index_we_are_choosing_for], the_list[random_choice_index] = (
                the_list[random_choice_index],
                the_list[index_we_are_choosing_for],
            )


a = [1, 2, 3, 4, 5]
shuffle(a)
print(a)
