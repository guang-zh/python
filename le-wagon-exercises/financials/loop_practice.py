# -*- coding: utf-8 -*-
"""

@author: Guang
"""

# Loops for and while

for i in range(0, 4):
    print(i)
    

for letter in "python":
    print(letter)
    

words = ['cat', 'bear','python','java']
for word in words:
    print(word, len(word))
    

import math
i=0
while i<10:
    print(f'{i}! is {math.factorial(i)}')
    i+=1