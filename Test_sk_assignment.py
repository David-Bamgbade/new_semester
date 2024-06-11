import numbers

import unittest

from sk_task_assignment.assignment import generate_random_numbers, custom_len_function, collection_number, \
    sum_of_even_index, sum_of_odd_index, multiplication_of_every_third_index, average_of_all_elements_in_the_list, \
    largest_of_the_elements_in_the_list, smallest_of_the_elements_in_the_list, list_of_strings, letter, \
    duplicate_elements_in_the_list, sequential_list, remove_duplicate_in_list


class MyTestCase(unittest.TestCase):
    def test_that_10_numbers_are_generated_in_list(self):

     self.assertEqual(generate_random_numbers(),[37, 3, 28, 31, 37, 1, 14, 30, 32, 18])

    def test_that_custom_len_function_counts_number_in_list(self):

        self.assertEqual(custom_len_function(generate_random_numbers()), 10)

    def test_that_result_is_sum_of_even_index(self):
        self.assertEqual(sum_of_even_index(collection_number), 20)

    def test_that_result_is_sum_of_odd_index(self):
        self.assertEqual(sum_of_odd_index(collection_number), 18)


    def test_that_result_is_multiplication_of_third_index(self):
        self.assertEqual(multiplication_of_every_third_index(collection_number), 28)

    def test_that_result_is_the_average_of_all_elements_in_the_list(self):
        self.assertEqual(average_of_all_elements_in_the_list(collection_number), 4.5)

    def test_that_result_is_the_largest_element_in_the_list(self):
        self.assertEqual(largest_of_the_elements_in_the_list(collection_number), 37)

    def test_that_result_is_the_smallest_element_in_the_list(self):
        self.assertEqual(smallest_of_the_elements_in_the_list(collection_number), 1)

    def test_that_result_will_return_string_if_first_and_last_character_are_the_same_and_if_string_character_is_more_than_two(self):
        self.assertEqual(list_of_strings(letter), "David")

    def test_that_elements_in_list_are_duplicated(self):
        self.assertEqual(duplicate_elements_in_the_list(sequential_list),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] )


    def test_that_duplicated_elements_are_removed(self,):
        self.assertEqual(remove_duplicate_in_list(new_list), {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15})











if __name__ == '__main__':
    unittest.main()
