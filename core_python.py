# create a dict with juct 2 lists,
dict(zip('amir kamran ajmal noman'.split(), [28, 22, 40, 27]))
# {'ajmal': 40, 'amir': 28, 'kamran': 22, 'noman': 27}

-------------------------------------------------------------------------
# if and else in list comprehension 

lst = 'amir hamza uqba ayesha danish'.split()
# ['amir', 'hamza', 'uqba', 'danish']

[i if i[0] == 'a' else 'hahaha' for i in lst]
# ['amir', 'hahaha', 'hahaha', 'hahaha']

-------------------------------------------------------------------------
# if and else and assign to one line

a = 10
b =2 
print(a) if b else 0
# 10
-------------------------------------------------------------------------
a = range(5)
b = range(6,11)
list(zip(a,b))
# [(0, 6), (1, 7), (2, 8), (3, 9), (4, 10)]
----
list(zip([1,2], ['a', 'b', 'c']))
# [(1, 'a'), (2, 'b')]
-------------------------------------------------------------------------
a = list(range(11))
a[::2]
# [0, 2, 4, 6, 8, 10]
-------------------------------------------------------------------------
list(range(10, 0, -1))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
-------------------------------------------------------------------------
ORDERED DICTNORY
import collections
m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
print(', '.join(m.keys()))
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
-------------------------------------------------------------------------
PAIRS OF TUPLES TO DICT
dict((('a', 'b'), (1, 2)))
# {'a': 'b', 1: 2}
--------------------------------------------------------------------------
MAP FUNCTION
def multiply_by_two(num):
    return num * 2

a = list(range(5, 39))
print(list(map(multiply_by_two, a)))
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76]
--------------------------------------------------------------------------
# function calling itself:
def isPalindrome(s):
   if len(s) <= 1:
       return True
   else:
       if s[0] != s[len(s)-1]:
           return False
       else:
           return isPalindrome(s[1:len(s)-1])
print(isPalindrome("poop"))
----------------------------------------------------------------------------
# smallest palindrome function 
def isPalindrome(s):
    return s == s[::-1]
print(isPalindrome('poop'))

def is_palindrome(word):
    return word == ''.join(reversed(word))
print(is_palindrome('poop'))

def palindrome_checker(word):
    return True if len(word) < 2 else (word[0] == word[-1]) and palindrome_checker(word[1:-1])
----------------------------------------------------------------------------
from time import localtime
activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }
time_now = localtime()
hour = time_now.tm_hour
for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print('Unknown, AFK or sleeping!')
----------------------------------------------------------------------------
# ALL POSSIBLE 4 CHARACTER PASSWORD WITH 2 NUM AND 2 ALPHA
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids
----------------------------------------------------------------------------
vals = ['aa','bb','cc','dd','ee']
d = dict(enumerate(vals))
d
# {0: 'aa', 1: 'bb', 2: 'cc', 3: 'dd', 4: 'ee'}
----------------------------------------------------------------------------
# defrence between two sets
a = 'abcdefgh'
b = 'acdefh'
set(a) - set(b)
# {'b', 'g'}
----------------------------------------------------------------------------
# sort dictionary by values
key = list('amirsaleem')
value = [9,3,1,4,3,2,8,3,2,1]
d= dict(zip(key,value))
d 
# {'a': 2, 'e': 2, 'i': 1, 'l': 8, 'm': 1, 'r': 4, 's': 3}

sorted(d.items(), key=lambda w: w[1], reverse=True)
[('l', 8), ('r', 4), ('s', 3), ('a', 2), ('e', 2), ('m', 1), ('i', 1)]
----------------------------------------------------------------------------
# create variables in loop (run time)
for x in range(0, 10):
    globals()['string%s' % x] = 'Hello'
# this code will create a 10 variables [string1, string2... string9] each variable contain <'Hello'>
----------------------------------------------------------------------------
# tuple to multiple lists
a,b = zip(*[(1, 2), (3, 4), (5, 6)])
a
# (1, 3, 5)
b
# (2, 4, 6)
The only difference is that you get tuples instead of lists. You can convert them to lists using
list(map(list, zip(*[(1, 2), (3, 4), (5, 6)])))
# [[1, 3, 5], [2, 4, 6]]

# another example:
# <names2> is a list of tuples, each tuple contain 2 values
a, b = zip(*names2)
len(a), len(b)
# (874, 874)
a[0], b[0]
# ('aamir talal khan', 'Aamir Khan')
df['orignal_name'] = list(a)
df['wikipedia_name'] = list(b)
df.shape
# (874, 2)
df.to_csv('name_deffrence.csv')
----------------------------------------------------------------------------
# fix split size
# list me kitni values chahyeh?
n = 'saleem amir hamza uqba'

n.split(' ', 1)
#['saleem', 'amir hamza uqba']

n.split(' ', 2)
#['saleem', 'amir', 'hamza uqba']

n.split(' ', 3)
#['saleem', 'amir', 'hamza', 'uqba']

n.split(' ', 4)
#['saleem', 'amir', 'hamza', 'uqba']
----------------------------------------------------------------------------
# all digits in text to 0, 4 -> 0, 45 -> 00, 4555 -> 0000 and 4.55 -> 0.00
import re
for i in renge(len(text)):
  text[i] = re.sub('\d', '0', text[i])
----------------------------------------------------------------------------
# rendomely split data
a = list('amirsaleem')
a1, a2 = train_test_split(a)
a1  
# ['l', 'a', 'i', 'a', 'e', 'r', 'm']
a2 
# ['m', 's', 'e']
----------------------------------------------------------------------------
# match the end of a word
[w for w in text.split() if re.search('ed$', w)]
# same as:
[w for w in text.split() if w[-2:] == 'ed']
------------------------------------------------------
# current directory
!pwd
 ------------------------------------------------------
 # list of all files names located in your working directory
 contents = !ls
 ------------------------------------------------------
 !pwd # check your working directory
 %cd .. # go back one folder
 %mkdir from_shell # creat new folder <from_shell>
 %cd from_shell/ # go to <from_shell> folder
 !pwd # now you are in <from_shell> folder
 ------------------------------------------------------
 # agar ye pehly sy ON ho ga to mkdir wagera sy pehly <%> ya <!> lagany ki zaroorat nahi h
 %automagic
 ------------------------------------------------------
# sorted by last value
names = ['Amir saleem', 'Ayesha Haji', 'muhammd muaz', 'Hamza khalid', 'Zahid mughal', 'Muhammad imran']
sorted(names, key=lambda name:name.split()[-1])
# ['Ayesha Haji',
# 'Muhammad imran',
# 'Hamza khalid',
# 'muhammd muaz',
# 'Zahid mughal',
# 'Amir saleem'] 
----------------------------------------------------------------------------
# get only last value
names = ['Amir saleem', 'Ayesha Haji', 'muhammd muaz', 'Hamza khalid', 'Zahid mughal', 'Muhammad imran']
lmbda = lambda name: name.split()[-1]
[lmbda(i) for i in names]
# ['saleem', 'Haji', 'muaz', 'khalid', 'mughal', 'imran']
----------------------------------------------------------------------------
# multiply function
def h(*lens_multiply):
    i =iter(lens)
    v = next(i)
    for l in i:
        v *= l
    return v
h(4,5,9,4)
# 720

# another aproach
def h(a, *aa):
    v = a
    for i in aa:
        v *= i
    return v
h(3,5,7,9)
# 945
----------------------------------------------------------------------------
# dict comprehension
{i:'*'*i for i in range(20) if i % 2 == 1}
----------------------------------------------------------------------------
order dictnory by keys:
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
----------------------------------------------------------------------------
order dictnory by values:
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
----------------------------------------------------------------------------
# all possible combinations (ignoring order, so <a,b> == <b,a>)
from itertools import combinations
input = ['a', 'b', 'c', 'd']
output = sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])
----------------------------------------------------------------------------
age = 27.5
print(f"i im {age} years old")
----------------------------------------------------------------------------
most frequent value in list ............... x = [1,2,4,5,3,2,1,4,5,2, 1, 2]; max(set(x), key = x.count) 
----------------------------------------------------------------------------
create variable name and assing it a value within a loop:
a = ["love", "for", "data"]
for k in range(len(a)):
    exec('var_{} = "{}"'.format(k, a[k]))

print(var_0)
print(var_1)
print(var_2)
----------------------------------------------------------------------------
import string
string.ascii_letters
# return list of ALPHBETS
----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------
# .4e7 == 4000000.0


# Converting Epoch time into the datetime
from datetime import datetime
datetime.fromtimestamp(1562674474)


# find python library place in your computer
pip3 show pandas


# usually we install python packegs using <pip>, As an alternative to using pip, you can download a package directly from the site (make certain that is downloaded to the proper directory), unpack it (see Chapter 9 on how to unpack software), and then run the following:
python setup.py install
# This will install any unpacked packages that haven’t yet been installed.


-----------------------------------------------------
# ignore warnings
import warnings
warnings.filterwarnings('ignore')
-----------------------------------------------------
# all files and folder (like <tree> in bash>) ..................... import os, list(os.walk("."))
--------------------------------------------
# print in difrent colors
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))
--------------------------------------------

# isinstance multiple OR conditions ................ isinstance(a, (int, str))
# replace multiple items ............... 'amirsaleem'.translate(str.maketrans({'a': 'A', 'e': 'E'}))
---------------------
from tqdm import tqdm_notebook
for param in tqdm_notebook(range(1000000)):
    pass
--------------------
----------------------------
# multiple replaces in one string
s = 'one two one two one'

print(s.translate(str.maketrans({'o': 'O', 't': 'T'})))
# One TwO One TwO One
---------------------------

# remove multiple chracters from string:
characters_to_remove = ['a', "b"]
translationtable = str.maketrans({i:'' for i in characters_to_remove})
"amirbhai".translate(translationtable)
# get file last modification time ............. os.path.getmtime("proceced_IDs.csv")
# get only characters from string .............. import re; word1 = " ".join(re.findall("[a-zA-Z]+", st))

# check if a variable exists ................. if 'myVar' in locals(): print("<myVar> is in your variables")
# Convert seconds to hh:mm:ss in Python ................... import time; time.strftime('%H:%M:%S', time.gmtime(12345))
# load local html in BeautifulSoup : s = BeautifulSoup(open("Resume_2.html", "r"), "lxml")

# beautifulsoup get all hrefs in given link ............ for i in soup.find_all('a', href=True): print(i['href'])
# latters ................. string.ascii_letters

# list comprehention with for,if and else .............. [f(x) if condition else g(x) for x in sequence]

# list of lists to one big list ......... list(more_itertools.flatten(lst))
# Finishing_time = datetime.datetime.now() + datetime.timedelta(minutes=approx_remaining_minutes)
# approx_remaining_minutes %= 60

# print list each element in saperate line ......... a=list("amirsaleem");  print(*a, sep="\n")

# map ............. s='1 3 3 7 2 5 1 2 4 6' ; list(map(int, s.split())) ............ [1, 3, 3, 7, 2, 5, 1, 2, 4, 6]
# two aritmatic operations in short ......... 'm' if 10>f<5 else 'amir'
# sort dictionary by length ............. sorted(dic, key=len, reverse=True)

#----------------------
# convert minutes to hours,minutes and seconds
>>> import datetime
>>> str(datetime.timedelta(seconds=666))
'0:11:06'
#-----------END
# print fixed width / spaces ........... "{:<15}".format(string) ........... "{:>15}".format(string) .......... "{0:<15}".format(string)

# get value using id / memory id / ram id ................. import ctypes; ctypes.cast(id_, ctypes.py_object).value

# for building combinations ................. import itertools; friends = ['Team 1', 'Team 2', 'Team 3', 'Team 4']; list(itertools.combinations(friends, r=2)) # [('Team 1', 'Team 2'),      ('Team 1', 'Team 3'),  ('Team 1', 'Team 4'),  ('Team 2', 'Team 3'),  ('Team 2', 'Team 4'),  ('Team 3', 'Team 4')] ............. this will result : [('Team 1', 'Team 2'), ('Team 1', 'Team 3'),('Team 1', 'Team 4'),('Team 2', 'Team 3'),('Team 2', 'Team 4'), ('Team 3', 'Team 4')]

# count (as pd.Series.value_counts()) : from collections import Counter; Counter(['a','b','c','d','b','c','d','b']) ............ which restul: Counter({'b': 3, 'c': 2, 'd': 2, 'a': 1})

# convert two lists into dictionary ............. dictionary = dict(zip(lst_1, lst_2))

# get absuloute max ............... max([3,2,-8,1],key=abs)
# sorted by func .............. sorted([3,2,-8,1,key=abs)
# Finding the index of the min/max item in an iterable............  min(enumerate(a),key=lambda x: x[1])[0]
# Multiple predicates short-cut. ............... n=10;  1 < n < 20 # True

# Try-catch-else construct
try:
  foo() 
except Exception: 
  print("Exception occured")
else:
  print("Exception didnt occur")
finally:
  print("Always gets here")

# there is while-else as for-else

# A generator comprehension is the lazy version of a list comprehension........ m = (x ** 2 for x in range(5)); m # <generator object <genexpr> at 0x108efe408> ; next(m) # 0

# List comprehension with the current and previous value................ [y - x for x,y in zip(a,a[1:])]

# a, *b, c = [1, 2, 3, 4, 5]

def test(x, y, z):
  print(x, y, z)  
res = test(*[10, 20, 30]) 
# 10 20 30
res = test(**{'x': 1, 'y': 2, 'z': 3} )
# 10 20 30  

# Flatten iterables................. list(itertools.chain.from_iterable(nested_list))

# Creating cartesian products from iterables.
for p in itertools.product([1, 2, 3], [4, 5]):
   print(''.join(str(x) for x in p))
# (1, 4)
# (1, 5)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)

# Creating permutation from iterable.
for p in itertools.permutations([1, 2, 3, 4]):
     print(''.join(str(x) for x in p))
# 123
# 132
# 213
# 231
# 312
# 321

# Use A Dictionary To Store A Switch
>>> func_dict = {'sum': lambda x, y: x + y, 'subtract': lambda x, y: x - y}
>>> func_dict['sum'](9,3) # 12
>>> func_dict['subtract'](9,3) #6





# Failure to define a dictionary
webstersDict = {(1, 2.0): 'tuples can be keys',
                1: 'ints can be keys',
                'run': 'strings can be keys', 
                ['sock', 1, 2.0]: 'lists can NOT be keys'}



# remove value from dictionay............. del dict['key']

# in dictionay we can access value by <[]> or <.get> methog. agar <[]> use karen gy or galat gey dalen gy to keyerror aay ga, or agar <.get> method use karty hwy galat key pass karen gy to None return ho jay ga. You can also specify a default value to return if the key doesn’t exist. (eg:dictionay.get('chicken', 0))

#-----------------------------------
create variable from string
>>> %whos
Interactive namespace is empty.

>>> student = ["lloyd", "alice", "tyler"] 
>>> for i in student: 
        exec(i+"={}")

>>> %whos                                                                                                          
Variable   Type    Data/Info
----------------------------
alice      dict    n=0
i          str     tyler
lloyd      dict    n=0
student    list    n=3
tyler      dict    n=0

#----------------------------------
# Reimport a module in python while interactive .............. import importlib; importlib.reload(nameOfYourModule)

#Thousand coma (for more readability for big numbers ......... f'{value:,}'

time.time() ............ get epoch time

# set(parsing_error) & set(corrupt_error) ............. intersection between two sets


# replace one or more spaces/new line/sub string with one ............. import re; re.sub(' +', ' ', 'The     quick brown    fox') # this is an example of spaces
# get all code for given librery ........... import inspect, datetime; print(inspect.getsource(datetime))

# convert byte to str .......... _str = b"abcde".decode("utf-8")

# print line being executed when running a Python script ............. python3 -m trace -t my_script.py my_peram_1 my_peram_2 ............... https://tereshenkov.wordpress.com/2018/10/26/how-to-print-line-being-executed-when-running-a-python-script/

# get file size ................ os.path.getsize("/path/to/file")

# sclice list with multiple indexes ...............  from operator import itemgetter, a = [-2, 1, 5, 3, 8, 5, 6, b = [1, 2, 5, print(itemgetter(*b)(a) # (1, 5, 5)

# split on multiple characters at once ............. import re, re.split(', |_|-|!|\+', "GeeksforGeeks, is_an-awesome ! app + too") # ['GeeksforGeeks', ' is', 'an', 'awesome', ' app', 'too']

# print dictinory nicely| prety ................. import json, print (json.dumps(my_dict, indent=2, default=str)) .............. pip install print_dict, from print_dict import pd, pd(your_dictionary_name) ............ import pprint, pp = pprint.PrettyPrinter(depth=4), pp.pprint(mydict) ................ pout.vs(my_dict) [or you can return the formatted string output of your object: v = pout.s(data)]
