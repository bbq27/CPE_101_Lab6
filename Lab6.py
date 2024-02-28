# Name: Berfredd Quezon
# Section: 11
from typing import Optional
from data import *

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# input: list of Book objects
# output: list of Book objects
# purpose: sort an inputted list of books in alphabetical order
# example:   book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
# #          book2 = Book(['Ocean Vuong'], 'On Earth We're Briefly Gorgeous')
# #          book3 = Book(['Harper Lee'], 'To Kill a Mockingbird')
# #          selection_sort_index([book1,book2,book3] -> [book1,book2,book3]
'''
1. check if the inputted book list is empty
    1.1 if it is, return an empty list
2. loop through each value in the book list
    2.1 create a variable mindex to store the index of the smallest alphabetical value in the book list
    2.2 create a variable tmp to store the book at the index mindex
    2.3 replace the book at the index mindex with the book at the current evaluated index
    2.4 replace the book at the current evaluated index to the book at the index mindex
3. return the sorted book list
'''
# implementation:

# input: list of Book objects and an integer
# output: integer
# purpose: return the index of a book where the first letter in the title appears first in the alphabet
# example: book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
#          book2 = Book(['Ocean Vuong'], 'On Earth We're Briefly Gorgeous')
#          book3 = Book(['Harper Lee'], 'To Kill a Mockingbird')
#          smallest_book_index([book1,book2,book3],0) -> 0
'''
1. check if the inputted index is greater than the length of the books list or if it is negative
    1.1 if it is, return None
2. set a variable mindex to the inputted integer value
3. loop through each value in the book list skipping the first item
    3.1 check if the title of the book is alphabetically less than the title of the next book
        3.1.1 if it is, set mindex to that book's index
4. return mindex
'''
def smallest_book_index(books:list[Book], start:int) -> Optional[int]:
    if start > len(books) or start < 0:
        return None
    mindex = start
    for idx in range(start+1, len(books)):
        if books[idx].title < books[mindex].title:
            mindex = idx
    return mindex

def selection_sort_books(book_list:list[Book]) -> list[Book]:
    if len(book_list) == 0:
        return []
    for idx in range(len(book_list)-1):
        mindex = smallest_book_index(book_list,idx)
        tmp = book_list[mindex]
        book_list[mindex] = book_list[idx]
        book_list[idx] = tmp
    return book_list

# Part 2
# input: string
# output: string
# purpose: swap the letter case of each character in a string and don't modify non-letter characters
# example: swap_case('HEyY tHeRE!') -> 'heYy ThEre!'
# implementation:
def swap_case(words:str) -> str:
    swapped = ''
    for letter in words:
        if letter.isupper():
            swapped += letter.lower()
        elif letter.islower():
            swapped += letter.upper()
        else:
            swapped += letter
    return swapped

# Part 3
# input: three strings
# output: string
# purpose: replace an inputted character with another inputted character in an inputted word
# example: str_translate('hello',l,x) -> 'hexxo'
'''
1. check if the inputted old or new strings are one character
    1.1 if they aren't return 'Not a valid input'
2. create an empty list chars to store each character in the inputted word
3. loop through each character in the world
    3.1 add the character to the chars list
4. loop through each character in chars
    4.1 check if the inputted string old is the same as that character
        4.1.1 if it is, replace that value with the inputted string new
5. create an empty string word to store the new word
6. loop through each character in chars
    6.1 add each character to the string word
7. return word
'''
# implementation:

def str_translate(word:str,old:str,new:str) -> str:
    if len(old) != 1 or len(new) != 1:
        return 'Not a valid input'
    chars = []
    for char in word:
        chars.append(char)
    for val in range(len(chars)):
        if old in chars[val]:
            chars[val] = new
    word = ''
    for letter in chars:
        word += letter
    return word

# Part 4
# input: string
# output: dictionary
# purpose: create a dictionary where each word from an inputted string is given a key associated with the number of
# times it appeared in the original string
# example: histogram('hi there hi hi') -> {hi:3,there:1}
# implementation:

def histogram(line:str) -> dict:
    dict = {}
    words = line.split()
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict
