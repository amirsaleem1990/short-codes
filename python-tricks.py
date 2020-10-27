#Print The File Path Of Imported Modules.
>>> import os 
>>> import socket 
  
>>> print(os) 
# <module 'os' from '/usr/lib/python3.5/os.py'>

>>> print(socket) 
# <module 'socket' from '/usr/lib/python3.5/socket.py'>

# --------------------
# Chaining Of Comparison Operators.
>>> n = 10
>>> 1 < n < 20
# True

>>> 1 > n <= 9
# False

# ---------------------
# Underscore(_) separator for Large Number
# '_' can be used as a separator for expressing a large number
>>> ten_billion = 10_000_000_000
>>> print(f'{ten_billion:,}')
# 10,000,000,000

#.......................
enumerate(grades, starting_number)
#======================
# Unpacking
# unpacking values inside of tuples
>>> cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' )

# extract ace, 2, 3 only
>>> ace, two, three, *_ = cards
>>> print(ace, two, three)
# A 2 3

# extract ace, [numbers], J, Q, K
>>> ace, *numbers, J, Q, K = cards
>>> print(ace, numbers, J, Q, K)
# A ['2', '3', '4', '5', '6', '7', '8', '9', '10'] J Q K


# ---------------------------
# Convert two lists into a dictionary
itemDictionary = dict(zip(lst_1, lst_2))

#-----------------------------------
# Naming slices (slice(start, end, step))
>>> a = [0, 1, 2, 3, 4, 5]
>>> LASTTHREE = slice(-3, None)
>>> LASTTHREE
# slice(-3, None, None)
>>> a[LASTTHREE]
# [3, 4, 5]

#--------------------------------
# Zipping and unzipping lists and iterables
>>> a = [1, 2, 3]
>>> b = ['a', 'b', 'c']
>>> z = zip(a, b)
>>> z
# [(1, 'a'), (2, 'b'), (3, 'c')]
>>> zip(*z)
# [(1, 2, 3), ('a', 'b', 'c')]
#--------------------------------
# Inverting a dictionary using zip

>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> m.items()
# [('a', 1), ('c', 3), ('b', 2), ('d', 4)]
>>> zip(m.values(), m.keys())
# [(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
>>> mi = dict(zip(m.values(), m.keys()))
>>> mi
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
#--------------------------------
# multiple lists to one big list
>>> a = [[1, 2], [3, 4], [5, 6], ['amir', 4]]
>>> sum(a,[])
# [1, 2, 3, 4, 5, 6, 'amir', 4]

>>> list(itertools.chain.from_iterable(a))
# [1, 2, 3, 4, 5, 6, 'amir', 4]

>>> [x for l in a for x in l]
# [1, 2, 3, 4, 5, 6, 'amir', 4]
#--------------------------------
# Sets and set operations
>>> A = {1, 2, 3, 3}
>>> A
# set([1, 2, 3])
>>> B = {3, 4, 5, 6, 7}
>>> B
# set([3, 4, 5, 6, 7])
>>> A | B
set([1, 2, 3, 4, 5, 6, 7])
>>> A & B
set([3])
>>> A - B
set([1, 2])
>>> B - A
set([4, 5, 6, 7])
>>> A ^ B
set([1, 2, 4, 5, 6, 7])
>>> (A ^ B) == ((A - B) | (B - A))
#--------------------------------
# Grouping rows by a given key (itertools.groupby)
>>> from operator import itemgetter
>>> import itertools
>>> date = [line.strip().split(',') for line in open('contactlenses.csv', 'r')]
>>> data = data[1:]
>>> def print_data(rows):
		print '\n'.join('\t'.join('{: <16}'.format(s) for s in row) for row in rows)

>>> print_data(data)
young               myope                   no                      reduced                 none
young               myope                   no                      normal                  soft
young               myope                   yes                     reduced                 none
young               myope                   yes                     normal                  hard
young               hypermetrope            no                      reduced                 none
young               hypermetrope            no                      normal                  soft
young               hypermetrope            yes                     reduced                 none
young               hypermetrope            yes                     normal                  hard
pre-presbyopic      myope                   no                      reduced                 none
pre-presbyopic      myope                   no                      normal                  soft
pre-presbyopic      myope                   yes                     reduced                 none
pre-presbyopic      myope                   yes                     normal                  hard
pre-presbyopic      hypermetrope            no                      reduced                 none
pre-presbyopic      hypermetrope            no                      normal                  soft
pre-presbyopic      hypermetrope            yes                     reduced                 none
pre-presbyopic      hypermetrope            yes                     normal                  none
presbyopic          myope                   no                      reduced                 none
presbyopic          myope                   no                      normal                  none
presbyopic          myope                   yes                     reduced                 none
presbyopic          myope                   yes                     normal                  hard
presbyopic          hypermetrope            no                      reduced                 none
presbyopic          hypermetrope            no                      normal                  soft
presbyopic          hypermetrope            yes                     reduced                 none
presbyopic          hypermetrope            yes                     normal                  none
#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

#--------------------------------

