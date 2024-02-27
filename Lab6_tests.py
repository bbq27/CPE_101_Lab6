from data import *
from Lab6 import *
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_smallest_book_index1(self):
        book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = Book(['Ocean Vuong'], 'On Earth We\'re Briefly Gorgeous')
        book3 = Book(['Harper Lee'], 'To Kill a Mockingbird')
        book4 = Book(['George Orwell'], 'Animal Farm')
        book_list = [book1,book2,book3,book4]
        self.assertEqual(3,smallest_book_index(book_list,0))

    def test_smallest_book_index2(self):
        book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = Book(['Ocean Vuong'], 'On Earth We\'re Briefly Gorgeous')
        book3 = Book(['Harper Lee'], 'To Kill a Mockingbird')
        book4 = Book(['George Orwell'], 'Animal Farm')
        book_list = [book2,book4,book1,book1,book3]
        self.assertEqual(1,smallest_book_index(book_list,0))

    def test_selection_sort_books2(self):
        book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = Book(['Ocean Vuong'], 'On Earth We\'re Briefly Gorgeous')
        book3 = Book(['Harper Lee'], 'To Kill a Mockingbird')
        book4 = Book(['George Orwell'], 'Animal Farm')
        book_list = [book1,book2,book3,book4]
        self.assertEqual([book4,book1,book2,book3],selection_sort_books(book_list))

    def test_selection_sort_books2(self):
        book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = Book(['Ocean Vuong'], 'On Earth We\'re Briefly Gorgeous')
        book3 = Book(['Harper Lee'], 'To Kill a Mockingbird')
        book4 = Book(['George Orwell'], 'Animal Farm')
        book5 = Book(['Suzanne Collins'], 'Catching Fire')
        book6 = Book(['Quentin Tarantino'], 'Once Upon A Time')
        book_list = [book1,book2,book3,book4,book5,book6]
        self.assertEqual([book4,book5,book1,book2,book6,book3],selection_sort_books(book_list))
    # Part 2
    def test_swap_case1(self):
        self.assertEqual('HelLo',swap_case('hELlO'))

    def test_swap_case2(self):
        self.assertEqual('heYy ThEre!',swap_case('HEyY tHeRE!'))

    def test_swap_case3(self):
        self.assertEqual('H0w ARe you?',swap_case('h0W arE YOU?'))

    def test_swap_case4(self):
        self.assertEqual('',swap_case(''))

    # Part 3
    def test_str_translate1(self):
        self.assertEqual('xbcdcbx', str_translate('abcdcba', 'a', 'x'))

    def test_str_translate2(self):
        old = 'i am having a great day!'
        self.assertEqual('i pm hpving p grept dpy!', str_translate(old, 'a', 'p'))

    def test_str_translate3(self):
        old = 'hello karina how are you?'
        self.assertEqual('hello_karina_how_are_you?',str_translate(old, ' ', '_'))

    def test_str_translate4(self):
        old = 'he has a heavenly smile'
        self.assertEqual('Not a valid input',str_translate(old, 'e', '_'))

    # Part 4
    def test_histogram1(self):
        dictionary = {'hello':3,'there':2,'world':2}
        self.assertEqual(dictionary, histogram('hello there hello world hello there world'))

    def test_histogram2(self):
        dictionary = {'karina':1,'how':2,'could':2,'you':1,'berf':1,'she':1}
        self.assertEqual(dictionary, histogram('karina how could you berf how could she'))



if __name__ == '__main__':
    unittest.main()
