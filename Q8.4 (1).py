# 1. Import entire module
import math
print("Using import math:")
print(math.sqrt(25))

# 2. Import specific members
from math import sqrt, pi
print("\nUsing from math import sqrt, pi:")
print(sqrt(36))
print(pi)

# 3. Import entire module with alias
import math as m
print("\nUsing import math as m:")
print(m.sqrt(49))

# 4. Import specific member with alias
from math import factorial as fact
print("\nUsing from math import factorial as fact:")
print(fact(5))

# 5. Import all members (not recommended)
from math import *
print("\nUsing from math import *:")
print(pow(2, 3))