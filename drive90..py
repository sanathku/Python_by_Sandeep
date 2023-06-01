'''1. Write a program to find the length of the string without using inbuilt function (len)'''
string = "Hello World"
str_length = 0
for char in string:
    str_length += 1

# -----------------------------------------------------------------------------------------------
'''2. Write a program to reverse the string without using inbuilt functions'''
string = "Hello World"
str_reverse = ''
for char in string:
    str_reverse = char + str_reverse

# -----------------------------------------------------------------------------------------------
'''3. Write a program to replace one string with another e.g., "Hello World" replaces "World" 
      with "Universe" '''
string = "Hello World"
replaced_str = string.replace("World", "Universe")

# -----------------------------------------------------------------------------------------------
'''4. How to convert a string to a list and vice-versa '''
string = "Hello World"
# str_list = string.split()
# new_string = " ".join(str_list)
str_list = list(string)
new_string = str(str_list)

# -----------------------------------------------------------------------------------------------
'''5. Convert the string "Hello welcome to Python" to a comma separated string '''
string = "Hello welcome to Python"
comma_sep_string = string.split()

# -----------------------------------------------------------------------------------------------
'''6. Write a program to print alternate characters in a string '''
string = "Hello World"
print('alternate characters in a string')
for i in range(0, len(string), 2):
    print(string[i])

# -----------------------------------------------------------------------------------------------
'''7. Write a program to print ASCII values of the character present in a string '''
string = "Hello World"
print('ASCII values of the character present in a string')
for char in string:
    print(ord(char))

# -----------------------------------------------------------------------------------------------
'''8. Write a function to convert upper_case to lower_case and vice-versa without using 
      inbuilt functions '''
# string = "Hello World"
upch = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74,
        'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84,
        'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90}

lowch = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105,
         'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114,
         's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

def lower_to_upper(string):
    upper = ''
    for char in string:
        if char in lowch:
            number = lowch[char] - 32
            for key, value in upch.items():
                if number == value:
                    upper += key
    return upper


def upper_to_lower(string):
    lower = ''
    for char in string:
        if char in upch:
            number = upch[char] + 32
            for key, value in lowch.items():
                if number == value:
                    lower += key
    return lower

# -----------------------------------------------------------------------------------------------
'''9. Write a program to swap two numbers without using 3rd variable '''
number_1 = 10
number_2 = 15
number_1, number_2 = number_2, number_1

# -----------------------------------------------------------------------------------------------
'''10. Write a program to merge two different lists '''
list1 = [1, 2, 3]
list2 = [4, 5, 6]
newlist = list1 + list2
# list1.extend(list2)

# -----------------------------------------------------------------------------------------------
'''11. Write a program to read a random line in a file (ex. 50, 65, 78th line) '''
import random

with open(r"sample.log", 'r') as file:
    content = file.readlines()
    line_no = random.randint(0, len(content) - 1)
    print(content[line_no])

# -----------------------------------------------------------------------------------------------
'''12. Write a program to read a random lines in a file (I want to read all lines from 10th to 
       15th line) '''
import random

with open(r"sample.log", 'r') as file:
    content = file.readlines()
    start = random.randint(0, len(content) - 1)
    end = random.randint(0, len(content) - 1)
    selected_content = content[min(start, end):max(start, end)]
    for line in selected_content:
        print(line)

# -----------------------------------------------------------------------------------------------
'''13. Write a program to last "N" lines of a file '''
n = 15
with open(r"sample.log", 'r') as file:
    for line in (file.readlines()[-n::]):
        print(-n, line)

# -----------------------------------------------------------------------------------------------
'''14. Write a program to check if the given string is a palindrome or not without using reversed 
       method '''
string = "Hello World"

# _____________________Method 1_____________________
def palindrome(string):
    if string == string[::-1]:
        return True
    return False

# _____________________Method 2_____________________
def palindrome(string):
    new_string = ''
    for char in string:
        new_string = char + new_string
    if string == new_string:
        return True
    return False

# -----------------------------------------------------------------------------------------------
'''15. Write a program to search for character in a given string and return the corresponding 
       index '''
string = "Hello World"
char= " "

def search(string, char):
    if string and char:
        if char in string:
            return string.index(char)
        return "char not found"
    return "string and char should have minimum 1 character"
    print(search(string, char))

# -----------------------------------------------------------------------------------------------
'''16. Write a program to get the below output 
sentence = "hello world welcome to python programming hi there"
out = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming']}'''

sentence = "hello world welcome to python programming hi there"

# _____________________Method 1_____________________
out = {}
words = sentence.split()
for word in words:
    if word[0] in out:
        out[word[0]] += [word]
    else:
        out[word[0]] = [word]

# _____________________Method 2_____________________
from collections import defaultdict
_out = defaultdict(list)
words = sentence.split()
for word in words:
    _out[word[0]] += [word]

# -----------------------------------------------------------------------------------------------
'''17. Write a program to replace all the characters with - if the character occurs more than 
       once in a string '''
my_string = "hellohai"      # o/p = "-e--o-ai"

# _____________________Method 1_____________________
_new_string = ''
for char in my_string:
    if my_string.count(char) > 1:
        _new_string += '-'
    else:
        _new_string += char

# _____________________Method 2_____________________
from collections import defaultdict
_out = defaultdict(int)
for char in my_string:
    _out[char] += 1
new_string = ''
for char in my_string:
    if _out[char] > 1:
        new_string += '-'
    else:
        new_string += char

# -----------------------------------------------------------------------------------------------
'''18. Write a decorator that returns only positive values of subtraction '''

def decorator(fname):
    def wrapper(*args, **kwargs):
        result = fname(*args, **kwargs)
        return result if result > 0.0 else None
    return wrapper

@decorator
def subtraction(a, b):
    return a - b

# -----------------------------------------------------------------------------------------------
'''19. How to get the count of the number of instances of a class that is being created '''

class Count:
    instance = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        Count.instance += 1

c1 = Count('first', 'last')

# -----------------------------------------------------------------------------------------------
'''20. Write a function which takes a list of strings and integers. If the item is a string it 
       should print as it is and if the item is integer of float it should reverse it '''

def decor(fname):
    def wrapper(*args, **kwargs):
        for item in args:
            if not isinstance(item, (str, float, int)):
                raise Exception("Only string and numbers are allowed as input")
        return fname(*args, **kwargs)
    return wrapper

@decor
def function(*args):
    res = []
    for value in args:
        if isinstance(value, str):
            res.append(value)
        elif isinstance(value, int):
            res.append(int(str(value)[::-1]))
        elif isinstance(value, float):
            res.append(float(str(value)[::-1]))
    return res

p = function(10, 20, 30, 11.123, 'har')                 # No Error
p1 = function(10, 20, 30, 11.123, 'har', [1,2,3])       # Error

# -----------------------------------------------------------------------------------------------
'''21. Write a class named Simple, and it should have iteration capability '''

class Simple:
    """Class to implement an iterator of powers of two"""

    def __init__(self, _max=0):
        self._max = _max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self._max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

numbers = Simple(10)  # create an object
i = iter(numbers)  # create an iterable from the object
print(next(i))  # using next to get the next iterator element

# Example-2
class InfIter:
    """Infinite iterator to return all odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

# -----------------------------------------------------------------------------------------------
'''22. Write a custom class which can access values of dictionaries using d['a'] and d.a '''

'''There are two primary classes of interest: DictionaryObject and MutableDictionaryObject. 
DictionaryObject is the base class, and it acts as an immutable dictionary. 
MutableDictionaryObject, as the name implies, provides the ability to mutate the object via 
__setattr__ (e.g. d.x = 500) and __setitem__ (e.g. d['x'] = 500).

The base DictionaryObject class is itself immutable, meaning that once the data is set during 
the call to DictionaryObject.__init__, no other keys may be added, nor may any existing keys 
have their values changed.  
One caveat to this is that if the values a DictionaryObject points to are themselves mutable, 
then the underlying object may change.

If your use-case requires a more liberal DictionaryObject with mutability, please use 
MutableDictionaryObject. It behaves the same, but you can add keys via __setattr__ or __setitem__ 
(e.g. d.x = 5 or d['x'] = 5).
'''

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getitem__(self, index):
        return self.__dict__[index]
        # return self.__dict__.get(index)

    # Point class is child class of object class
    # here __delattr__ is completely over-riding the __delattr__ method present in parent class

    def __delattr__(self, name):
        raise Exception("No you cannot delete an attribute")

p = Point(10, 20)

# -----------------------------------------------------------------------------------------------
'''23. Write a program to get the below output 
sentence = "Hi How are you" and o/p should be "iH woH era uoy" '''
sentence = "Hi How are you"
words = sentence.split()
reverse = [word[::-1] for word in words]
result = " ".join(reverse)

# -----------------------------------------------------------------------------------------------
'''24. Write a program to get the below output 
sentence = "Hi How are you" and o/p should be "uoy era woH iH" '''
sentence = "Hi How are you"
reverse = sentence[::-1]

# -----------------------------------------------------------------------------------------------
'''25. Write a lambda function to add two numbers (a, b) '''
add = lambda a, b: a + b
res = add(10, 15)

# -----------------------------------------------------------------------------------------------
'''26. What is the output of the following '''
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print([a, b])

# o/p
# [[1, 2, 3], [4, 5, 6]]
# [[1, 2, 3], [4, 5, 6]]

# -----------------------------------------------------------------------------------------------
'''27. How to remove duplicates from the list without using inbuilt functions '''
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]

# _____________________Method 1_____________________
remove_duplicates = {}
for item in items:
    remove_duplicates[item] = 1

unique_char = list(remove_duplicates.keys())

# _____________________Method 2_____________________
_remove_duplicates = {item: 1 for item in items}
_res = list(_remove_duplicates.keys())

# -----------------------------------------------------------------------------------------------
'''28. Find the longest word in the sentence '''
sentence = "Hello world. Welcome to Pythom"

# _____________________Method 1_____________________
words = [word for word in sentence.split()]
length = [len(word) for word in words]
longest_w = [word for word, num in zip(words, length) if num == max(length)]

# _____________________Method 2_____________________
longest_word = ''
for word in sentence.split():
    if len(word) > len(longest_word):
        longest_word = word

# -----------------------------------------------------------------------------------------------
'''29. Write a program to reverse the values in the dictionary if the values is of type string'''
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

# _____________________Method 1_____________________
reverse_list = [(key, value[::-1]) if isinstance(value, str) else (key, value) for key, value in d.items()]
reverse_dict = {key: value for key, value in reverse_list}

# _____________________Method 2_____________________
ED = {key: value for key, value in
      [(key, value[::-1]) if isinstance(value, str) else (key, value) for key, value in d.items()]}

# -----------------------------------------------------------------------------------------------
'''30. Write a program to get 1234 from the below tuple '''
t = ('1', '2', '3', '4')
tuple_add = ''
for num in t:
    tuple_add += num
print(tuple_add)

# -----------------------------------------------------------------------------------------------
'''31. How to get the elements that are in list b but not in list a '''
a = [1, 2, 3]
b = [1, 2, 3, 4]
res = [num for num in b if num not in a]

# -----------------------------------------------------------------------------------------------
'''32. A function takes variable number of positional arguments as input. How to check if the 
       arguments that are passed are more than 5 '''

def check_input_variable_gt5(*args):
    return True if len(args) > 5 else False

check_input_variable_gt5()

# -----------------------------------------------------------------------------------------------
'''33. Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file '''
''' -----------contents of log file----------- file_name: "log.txt"
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical 
'''

from collections import defaultdict
count = defaultdict(int)
with open(r"log.txt","w") as file:
    for line in file:
        if line.startswith('CRITICAL'):
            count['CRITICAL'] += 1
        elif line.startswith('INFO'):
            count['INFO'] += 1
        elif line.startswith('ERROR'):
            count['ERROR'] += 1
count = dict(count)
print(count)

# -----------------------------------------------------------------------------------------------
'''34. Write a function to reverse any iterable without using reverse function '''

# _____________________Method 1_____________________
def Reverse_While(*args):
    length = len(args)
    start = -1
    while start != -length - 1:
        print(args[start])
        start -= 1

# _____________________Method 2_____________________
def Reverse_For(*args):
    length = len(args)
    for ne in range(length - 1, -1, -1):
        print(args[ne])

# -----------------------------------------------------------------------------------------------
'''35. Write a function to print the below output '''
# func("TRACXN", 0)     # Should print RCN
# func("TRACXN", 1)     # Should print TAX

def func(string, number):
    if number == 0:
        number += 1
    else:
        number -= 1
    output = ''
    while number < len(string):
        output += string[number]
        number += 2
    print(output)

# -----------------------------------------------------------------------------------------------
'''36. Sum all the numbers in the below string '''
s = "Sony12India567Pvt2ltd"  # eg. 1+2+5+6+7+2
import re

# _____________________Method 1_____________________
numbers = re.findall(r"\d", s)
total = sum([int(num) for num in numbers])

# _____________________Method 2_____________________
_total = sum([int(num) for num in re.findall(r"\d", s)])

# -----------------------------------------------------------------------------------------------
'''37. Write a program to sum all the numbers in the below string '''
s = "Sony12India567Pvt2ltd"  # eg. 1+2+5+6+7+2
import re

# _____________________Method 1_____________________
numbers = re.findall(r"\d+", s)
total = sum([int(num) for num in numbers])

# _____________________Method 2_____________________
_total = sum([int(num) for num in re.findall(r"\d+", s)])

# -----------------------------------------------------------------------------------------------
'''38. Print all the numbers in the below list '''
a = ['abc', '123', 'hello', '23']

# _____________________Method 1_____________________
total = []
for item in a:
    if item[0] in '0123456789':
        total.append(int(item))

# _____________________Method 2_____________________
number = [int(item) for item in a if item[0] in '0123456789']

# -----------------------------------------------------------------------------------------------
'''39. Write a program to print the number of occurrences of characters in a string without 
       using inbuilt functions '''
s = 'helloworld'
from collections import defaultdict

occurrences = defaultdict(int)
for char in s:
    occurrences[char] += 1

# -----------------------------------------------------------------------------------------------
'''40. Write a program to print only the repeated characters and count of the same '''
s = 'helloworld'
repeated_char = {char: s.count(char) for char in s if s.count(char) > 1}

# -----------------------------------------------------------------------------------------------
'''41. Write a program to get altername of a string in list format '''
s = 'helloworld'
import re

alternate_characters = [char for i, char in enumerate(re.findall(r"\w", s)) if i % 2 == 0]

# -----------------------------------------------------------------------------------------------
'''42. Write a program to get squares of list of numbers using lambda function '''
a = [1, 2, 3, 4, 5]
squares = list(map(lambda num: num ** 2, a))

# -----------------------------------------------------------------------------------------------
'''43. Write a function that accepts two strings and returns True if the two strings are anagrams 
       of each other '''
string1 = 'martwal'
string2 = 'tramlaw'

# _____________________Method 1_____________________
def anagram(string1, string2):
    string1 = "".join(sorted(string1))
    string2 = "".join(sorted(string2))
    if string1 == string2:
        return True

# _____________________Method 2_____________________
from collections import defaultdict
def anagram_dict(string1, string2):
    dict1 = dict2 = defaultdict(int)
    for _ in string1:
        dict1[_] += 1
    for _ in string2:
        dict2[_] += 1
    if dict1 == dict2:
        return True

# -----------------------------------------------------------------------------------------------
'''44. Write a progeam to iterate through list and build a new list, only if the items of the 
       list has even number of characters '''
names1 = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

def iterate1(argumnet):
    new_arg = []
    for item in argumnet:
        if len(item) % 2 == 0:
            new_arg.append(item)
    return new_arg

iterate1(names1)

# -----------------------------------------------------------------------------------------------
'''45. Write a progeam to iterate through list and build a new dictionary, only if the items of 
       the list has even number of characters '''
names2 = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

from collections import defaultdict
def iterate2(argumnet):
    dict_arg = defaultdict(int)
    for item in argumnet:
        if len(item) % 2 == 0:
            dict_arg[item] += 1
    return dict(dict_arg)

iterate2(names2)

# -----------------------------------------------------------------------------------------------
'''46. Write a progeam which squares the numbers in a list using map object '''
a = [1, 2, 3, 4, 5]
squares = list(map(lambda num: num ** 2, a))

# -----------------------------------------------------------------------------------------------
'''47. Count the number of lines in a file without loading the file to the memory '''
line_no = 0
with open(r"log.txt", 'r') as file:
    for line in file:
        line_no += 1
print(line_no)

# -----------------------------------------------------------------------------------------------
'''48. Printing line and line no's in a file '''
with open(r"log.txt", 'r') as file:
    for line_no, line in enumerate(file):
        print(line_no, line)

# -----------------------------------------------------------------------------------------------
'''49. Write a program to print the sum of entire list and sum of only internal list '''
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

internal_list = [sum(list) for list in l]
entire_list = sum(internal_list)

# -----------------------------------------------------------------------------------------------
'''50. Write a program to reverse the below list '''
words = ['hi', 'hello', 'python']
words.reverse()

# -----------------------------------------------------------------------------------------------
'''51. Write a program to update the tuple '''
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)            # o/p = (1,2,3,4,100,200,300)

t3 = t1.__add__(t2)
# t3 = t1 + t2

# -----------------------------------------------------------------------------------------------
'''52. Write a program to replace the value present in nested dictionary '''
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace 'nose' with 'net'
d['b']['n'] = 'net'

# -----------------------------------------------------------------------------------------------
'''53. Write a program to count the number of white spaces present in a file '''
import re

white_spaces = 0
with open(r"log.txt", 'r') as file:
    for line in file:
        list_of_spaces = re.findall(r"\s", line)
        white_spaces += len(list_of_spaces)

# -----------------------------------------------------------------------------------------------
'''54. Grouping anagrams '''
l = ["listen", 'hello', 'eat', 'desserts', 'silent', 'peek', 'ate', 'keep', 'tea', 'stressed']

def anagram_dict(input_list):
    grouping_anagrams = {}
    for string in input_list:
        string1 = "".join(sorted(string))
        if string1 in grouping_anagrams:
            grouping_anagrams[string1] += [string]
        else:
            grouping_anagrams[string1] = [string]
    return list(grouping_anagrams.values())

# -----------------------------------------------------------------------------------------------
'''55. What is the difference beteen defaultdict and normal dictionary '''
# -----------------------------------------------------------------------------------------------
'''56. Explain property decorator in python'''
# -----------------------------------------------------------------------------------------------
'''57. What is Mutable and Immutable datatypes'''
# -----------------------------------------------------------------------------------------------
'''58. Explaing get() method in dictionaries'''
# -----------------------------------------------------------------------------------------------
'''59. Write a list comprehension to get a list of even numbers from 1-50'''
even_numbers = [num for num in range(1, 51) if num % 2 == 0]

# -----------------------------------------------------------------------------------------------
'''60. Find the longest non-repeated substring in the below string'''
s = "This is a Programming language and Programming is fun"

d = {}
for word in s.split():
    if word not in d:
        d[word] = len(word)
    else:
        d.pop(word)

longest_word = max(d.values())
for key in d:
    if d[key] == longest_word:
        print(key)

# -----------------------------------------------------------------------------------------------
'''61. Write a program to find the duplicate elements list without using inbuilt functions '''
names = ['apple', 'google', 'apple', 'yahoo', 'google']
d = {}
for name in names:
    if name in d:
        d[name] += 1
    else:
        d[name] = 1

for key in d:
    if d[key] > 1:
        print(key)

# -----------------------------------------------------------------------------------------------
'''62. Write a program to count the number of occurrences of each item in the list without using 
       any inbuilt functions '''
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
oc_count = {}
for name in names:
    if name in oc_count:
        oc_count[name] += 1
    else:
        oc_count[name] = 1

# -----------------------------------------------------------------------------------------------
'''63. Write a function to check if the number is prime or not '''

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# -----------------------------------------------------------------------------------------------
'''64. How to create a tuple of numbers form 0 to 10 using range function '''
create_tuple = (num for num in range(1, 11))  # generator object is created
c_tuple = tuple([num for num in range(1, 11)])  # correct answer

# -----------------------------------------------------------------------------------------------
'''65. Write a program to find the largest number in the list without using any inbuilt function '''
numbers = [10, 20, 30, 40, 50]
largest_num = 0
for num in numbers:
    if num > largest_num:
        largest_num = num
print(largest_num)

# -----------------------------------------------------------------------------------------------
'''66. Write a method that returns the last digit on an integer. 
       For example, the call of get_last_digit(3572) should return 2 '''

class Integer:
    def __init__(self, number):
        self.number = number

    def get_last_digit(self):
        last_digit = self.number % 10
        return last_digit

n = Integer(3572)
n.get_last_digit()

# -----------------------------------------------------------------------------------------------
'''67. Write a program to find most common words in a given list '''
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes',
         'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
         'look', 'into', 'my', 'eyes', "you're", 'under']

import collections

words_dict = collections.defaultdict(list)
for word in words:
    words_dict[words.count(word)] = list(set(words_dict[words.count(word)] + [word]))
most_common = words_dict[max(words_dict.keys())]

# -----------------------------------------------------------------------------------------------
'''68. Make a function named tail that takes a sequence (like a list, string, or tuple) and a 
       number n and returns the last n elements from the given sequence, as a list '''

def tail(sequence, n):
    return list(sequence[-n::])

sq1 = [1, 2, 3, 4, 5]
sq2 = (1, 2, 3, 4, 5)
sq3 = "12345"
number = 3

# -----------------------------------------------------------------------------------------------
'''69. Write a function named is_perfect_square that accepts a number and returns True if it's a 
       perfect square and False if it's not '''

def is_perfect_square(number):
    i = 0
    while True:
        if i * i > number:
            return False
        if i * i == number:
            return True
        i += 1

is_perfect_square(81)

# -----------------------------------------------------------------------------------------------
'''70. Write a program to get all the duplicate items and the number of times the item is 
       repeated in the list '''
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail',
         'gmail', 'gmail']
duplicates = {name: names.count(name) for name in names if names.count(name) > 1}

# -----------------------------------------------------------------------------------------------
'''71. Write a program to count the number of occurrences of each word in a file '''
#  using "log.txt" file from question no 33.

from collections import defaultdict

word_occurrences = defaultdict(int)
with open(r"log.txt", 'r') as file:
    for line in file:
        for word in line.split():
            word_occurrences[word] += 1
word_occurrences = dict(word_occurrences)

# -----------------------------------------------------------------------------------------------
'''72. Write a program to count the number of occurrences of each vowel in a file '''
#  using "log.txt" file from question no 33.

from collections import defaultdict

vowel_occurrences = defaultdict(int)
with open(r"log.txt", 'r') as file:
    for line in file:
        for char in sorted(line):
            if char in 'AEIOUaeiou':
                vowel_occurrences[char] += 1
vowel_occurrences = dict(vowel_occurrences)

# -----------------------------------------------------------------------------------------------
'''73. Write a program to print all the numeric values i a list '''
items = ['apple', 1.2, 'google', '12.6', 26, '100']
for item in items:
    if isinstance(item, (int, float)):
        print(item)

# -----------------------------------------------------------------------------------------------
'''74. Triangle Patterns 
*
* *
* * *
* * * *
* * * * * 
'''

def py_left1(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

def py_left2(n):
    if n == 0:
        return
    py_left2(n - 1)
    print("* " * n)

def py_left3(n):
    i = 1
    j = 0
    while i <= n:
        while j <= i - 1:
            print("* ", end="")
            j += 1
        print("\r")
        j = 0
        i += 1

'''
        *
      * *
    * * *
  * * * *
* * * * * 
'''

def py_right(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

def py_center(n):
    i = 0
    while i <= n:
        print(" " * (n - i) + "*" * i)
        i += 1

# -----------------------------------------------------------------------------------------------
'''75. Write a program to count the occurrence of a particular word in the file '''
#  using "log.txt" file from question no 33.

def count_custom_character(string):
    count_char = 0
    with open(r"log.txt", 'r') as file:
        for line in file:
            words = line.split()
            if string in words:
                count_char += words.count(string)
    return count_char

# -----------------------------------------------------------------------------------------------
'''76. Write a program to map a product to a company and build a dictionary with company and 
       list of products pair '''
all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 'iOS', 'Google Drive',
                'One Drive']

# # Pre-Defined products for different companies'
apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}

from collections import defaultdict
d = defaultdict(list)
for product in all_products:
    if product in apple_products:
        d['apple_products'] += [product]
    elif product in google_products:
        d['google_products'] += [product]
    elif product in msft_products:
        d['msft_products'] += [product]
d = dict(d)

# -----------------------------------------------------------------------------------------------
'''77. Write a program to rotate items of the list '''
names = ['apple', 'google', 'yahoo', 'gmail', 'facebook', 'amazon']
def rotate(args):
    args = args[1:] + args[:1]
    return args

for item in range(10):
    names = rotate(names)
    print(names)

# -----------------------------------------------------------------------------------------------
'''78. Write a program to rotate characters in a string '''
input = "HelloPython"
def rotate(string):
    args = [x for x in string]
    args = args[1:] + args[:1]
    return "".join(args)

for item in range(10):
    input = rotate(input)
    print(input)

# -----------------------------------------------------------------------------------------------
'''79. Write a program to count the number of white spaces in a given string '''

string = '''In case you have an else branch and you want to conditionally assign a value to a 
variable, the ternary operator is your friend. Say, you want to write the following 
if-then-else statement in a single line of code'''

import re
white_space = re.findall(r"\s", string)
print(len(white_space))

# -----------------------------------------------------------------------------------------------
'''80. Write a program to print only non-repeated characters in a string '''
string = "only non repeated characters"

non = [ x for x in string if string.count(x) == 1]

# -----------------------------------------------------------------------------------------------
'''81. What is the difference between a list and a tuple '''
# -----------------------------------------------------------------------------------------------
'''82. Write a program to print all the consonants in a given string '''
s = "helloworld"

def consonants(input):
    for char in input:
        if char not in 'AEIOUaeiou':
            print(char)

# -----------------------------------------------------------------------------------------------
'''83. Write a program to count the number of commented lines in a text file '''

def commented_lines():
    c = 0
    with open(r"file_name.exe", 'r') as f:
        for line in f:
            if line.startswith("#"):
                c += 1
    return c

# -----------------------------------------------------------------------------------------------
'''84. Write a program to check if the year is leap year or not '''

def leap_year(year):
    return True if year/4 == year//4 else False

# -----------------------------------------------------------------------------------------------
'''85. Linear Search '''

def search(collection, x):
    for i in range(len(collection)):
        if collection[i] == x:
            return i
    return -1

# -----------------------------------------------------------------------------------------------
'''86. Difference between xrange and range 

------- range() -------                     ------- xrange() -------
Returns a list of integers                  Returns a generator object
Execution speed is slower                   Execution speed is faster

Takes more memory as it keeps the           Takes less memory as it keeps only 
entire list of elements in memory           one element at a time in memory.

All arithmetic operations can be            Such operations cannot be performed on xrange() 
performed as it returns a list	

In python 3, xrange() is not supported      In python 2, xrange() is used to iterate in for loops
'''

# -----------------------------------------------------------------------------------------------
'''87. Write a program to count no of capital letters in a string '''
s = "Hi How are You WelCome to PytHon"

import re
capital_letters = len(re.findall(r"[A-Z]", s))

# -----------------------------------------------------------------------------------------------
'''88. Write a program to get the below output 

*
* *
* * *
* * * *
* * * * * 
'''
# -----------------------------------------------------------------------------------------------
'''89. Write a program to get the below output '''
a = [1,2,3,4,5,6,7,8,9]
# o/p = [1,2]
#       [3,4]
#       [5,6]
#       [7,8]
#       [9]

out = [ [a[x]] if x == len(a)-1 else [a[x], a[x+1]]  for x in range(0, len(a), 2)]
for item in out:
    print(item)

# -----------------------------------------------------------------------------------------------
'''90. Write a program to check if the elements in the second list is series of continuation of 
       the items in the first list '''
a = [10, 12, 14, 16, 18]
b = [20, 22, 24, 26, 28]

p = [0, 5, 10, 15]
q = [20, 25, 30, 35, 40]

x = [10, 20, 30, 40]
y = [50, 40, 60, 70]

def continuation(first, second):
    diff = first[1] - first[0]
    for i in range(2, len(first)):
        if first[i] - first[i-1] != diff:
            return False
    if second[0] - first[-1] != diff:
        return False
    for j in range(1, len(second)):
        if second[j] - second[j-1] != diff:
            return False
    return True

