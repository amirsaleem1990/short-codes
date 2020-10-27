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
