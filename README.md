# CTCI-solutions

[![codecov](https://codecov.io/gh/jcockbain/ctci-solutions/branch/master/graph/badge.svg)](https://codecov.io/gh/jcockbain/ctci-solutions)

Python solutions to algorithm questions in [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/).

"TODO" comments are left where more efficient solutions are suggested in the book, or follow-up questions not yet answered.

## Summary

Each solution, with its tests, should be self-contained inside the one file linked.

Test cases are added as I've understood the problems, and algorithms written to pass these tests.

PRs and issues are welcome where something is incorrect or could be done better!

## Running The Tests

I run the tests with pytest.

```shell
pytest # whole suite
pytest {path_to_test.py} # particular file
```

## Chapters

- [Chapter 1 - Arrays and Strings](chapter-01/)

  - [01_is_unique_string](chapter-01/Q01_is_unique_string.py)
  - [02_is_permutation](chapter-01/Q02_is_permutation.py)
  - [03_URLify](chapter-01/Q03_URLify.py)
  - [04_palindrome_permutation](chapter-01/Q04_palindrome_permutation.py)
  - [05_one_away](chapter-01/Q05_one_away.py)
  - [06_string_compression](chapter-01/Q06_string_compression.py)
  - [07_rotate_matrix](chapter-01/Q07_rotate_matrix.py)
  - [08_zero_matrix](chapter-01/Q08_zero_matrix.py)
  - [09_string_rotation](chapter-01/Q09_string_rotation.py)

- [Chapter 2 - Linked Lists](chapter-02/)

  - [01_remove_dups](chapter-02/Q01_remove_dups.py)
  - [02_return_kth_to_last](chapter-02/Q02_return_kth_to_last.py)
  - [03_delete_middle_node](chapter-02/Q03_delete_middle_node.py)
  - [04_partition](chapter-02/Q04_partition.py)
  - [05_sum_lists](chapter-02/Q05_sum_lists.py)
  - [06_palindrome](chapter-02/Q06_palindrome.py)
  - [07_intersection](chapter-02/Q07_intersection.py)
  - [08_loop_detection](chapter-02/Q08_loop_detection.py)

- [Chapter 3 - Stacks and Queues](chapter-03/)

  - [01_three_in_one](chapter-03/Q01_three_in_one.py)
  - [02_stack_min](chapter-03/Q02_stack_min.py)
  - [03_set_of_stacks](chapter-03/Q03_set_of_stacks.py)
  - [04_queue_via_stacks](chapter-03/Q04_queue_via_stacks.py)
  - [05_sort_stack](chapter-03/Q05_sort_stack.py)
  - [06_animal_shelter](chapter-03/Q06_animal_shelter.py)

- [Chapter 4 - Trees and Graphs](chapter-04/)

  - [01_route_between_two_nodes](chapter-04/Q01_route_between_nodes.py)
  - [02_minimal_tree](chapter-04/Q02_minimal_tree.py)
  - [03_list_of_depths](chapter-04/Q03_list_of_depths.py)
  - [04_check_balanced](chapter-04/Q04_check_balanced.py)
  - [05_validate_BST](chapter-04/Q05_validate_bst.py)
  - [06_successor](chapter-04/Q06_successor.py)
  - [07_valid_build_order](chapter-04/Q07_valid_build_order.py)
  - [08_common_ancestor](chapter-04/Q08_common_ancestor.py)
  - [09_bst_sequences](chapter-04/Q09_bst_sequences.py)
  - [10_check_subtree](chapter-04/Q10_check_subtree.py)
  - [11_random_node](chapter-04/Q11_random_node.py)
  - [12_path_with_sum](chapter-04/Q12_path_with_sum.py)

- [Chapter 5 - Bit Manipulation](chapter-05/)

  - [01_insertion](chapter_5/Q01_insertion.py)
  - [02_binary_to_string](chapter_5/Q02_binary_to_string.py)
  - [03_flip_bit_to_win](chapter-05/Q03_flip_bit_to_win.py)
  - [04_next_number](chapter-05/Q04_next_number.py)
  - [05_debugger](chapter-05/Q05_degugger.py)
  - [06_conversion](chapter-05/Q06_conversion.py)
  - [07_pairwise_swap](chapter-05/Q07_pairwise_swap.py)
  - [08_draw_line](chapter-05/Q08_draw_line.py)

- [Chapter 6 - Math and Logic Puzzles]

- [Chapter 7 - Object-Oriented Design](chapter-07/)

  - [01_deck_of_cards](chapter-07/Q01_deck_of_cards.py)

- [Chapter 8 - Recursion and Dynamic Programming](chapter-08/)

  - [01_triple_step](chapter-08/Q01_triple_step.py)
  - [02_robot_in_a_grid](chapter-08/Q02_robot_in_a_grid.py)
  - [03_magic_index](chapter-08/Q03_magic_index.py)
  - [04_power_set](chapter-08/Q04_power_set.py)
  - [05_recursive_multiply](chapter-08/Q05_recursive_multiply.py)
  - [06_towers_of_hanoi](chapter-08/Q06_towers_of_hanoi.py)
  - [07_permutations_without_dups](chapter-08/Q07_permutations_without_dups.py)
  - [08_permutations_with_dups](chapter-08/Q08_permutations_with_dups.py)
  - [09_parens](chapter-08/Q09_parens.py)
  - [10_paint_fill](chapter-08/Q10_paint_fill.py)
  - [11_coins](chapter-08/Q11_coins.py)
  - [12_n_queens](chapter-08/Q12_n_queens.py)
  - [13_stack_of_boxes](chapter-08/Q13_stack_of_boxes.py)
  - [14_boolean_evaluation](chapter-08/Q14_boolean_evaluation.py)

- [Chapter 9 - System Design and Scalibility]

- [Chapter 10 - Sorting and Search](chapter-10/)

  - [01_sorted_merge](chapter-10/Q01_sorted_merge.py)
  - [02_group_anagrams](chapter-10/Q02_group_anagrams.py)
  - [03_search_in_rotated_array](chapter-10/Q03_search_in_rotated_array.py)
  - [04_sorted_search_no_size](chapter-10/Q04_sorted_search_no_size.py)
  - [05_sparse_search](chapter-10/Q05_sparse_search.py)
  - [07_missing_int](chapter-10/Q07_missing_int.py)
  - [08_find_duplicates](chapter-10/Q08_find_duplicates.py)
  - [09_sorted_matrix_search](chapter-10/Q09_sorted_matrix_search.py)
  - [10_get_rank_from_stream](chapter-10/Q10_get_rank_from_stream.py)
  - [11_peaks_and_valleys](chapter-10/Q11_peaks_and_valleys.py)

- [Chapter 11 - Testing]

- [Chapter 12 - C and C++]

- [Chapter 13 - Java]

- [Chapter 14 - Databases]

- [Chapter 15 - Threads and Locks]

- [Chapter 16 - Moderate](chapter-16/)

  - [01_number_swapper](chapter-16/Q02_word_frequencies.py)
  - [02_word_frequencies](chapter-16/Q02_word_frequencies.py)
  - [03_intersection](chapter-16/Q03_intersection.py)
  - [04_tic_tac_toe_win](chapter-16/Q04_tic_tac_toe_win.py)
  - [05_factorial_zeroes](chapter-16/Q05_factorial_zeroes.py)
  - [06_smallest_difference](chapter-16/Q06_smallest_difference.py)
  - [07_number_max](chapter-16/Q07_number_max.py)
  - [08_english_int](chapter-16/Q08_english_int.py)
  - [09_operations](chapter-16/Q09_operations.py)
  - [10_living_people](chapter-16/Q10_living_op.py)
  - [11_diving_board](chapter-16/Q11_diving_board.py)
  - [12_xml_encoding](chapter-16/Q12_xml_encoding.py)
  - [13_bisect_squares](chapter-16/Q13_bisect_squares.py)
  - [14_best_line](chapter-16/Q14_best_line.py)
  - [15_master_mind](chapter-16/Q14_best_line.py)
  - [16_sub_sort](chapter-16/Q14_best_line.py)
  - [17_contiguous_sequence](chapter-16/Q17_contiguous_sequence.py)
  - [18_pattern_matching](chapter-16/Q18_pattern_matching.py)
  - [19_pond_size](chapter-16/Q19_pond_size.py)
  - [20_T9](chapter-16/Q20_T9.py)
  - [21_sum_swap](chapter-16/Q21_sum_swap.py)
  - [22_langstons_ant](chapter-16/Q22_langstons_ant.py)
  - [23_rand7_from_rand5](chapter-16/Q23_rand7_from_rand5.py)

- [Chapter 17 - Hard](chapter-17/)

  - [01_add_without_plus](chapter-17/Q01_add_without_plus.py)
  - [02_shuffle](chapter-17/Q02_shuffle.py)
  - [03_random_set](chapter-17/Q03_random_set.py)
  - [04_missing_number](chapter-17/Q04_missing_number.py)
  - [05_letters_and_numbers](chapter-17/Q05_letters_and_numbers.py)
  - [06_count_of_twos](chapter-17/Q06_count_of_twos.py)
  - [07_baby_names](chapter-17/Q07_baby_names.py)
  - [08_circus_tower](chapter-17/Q08_circus_tower.py)
  - [11_word_distance](chapter-17/Q11_word_distance.py)
  - [14_smallest_k](chapter-17/Q14_smallest_k.py)