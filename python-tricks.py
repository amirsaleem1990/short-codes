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

