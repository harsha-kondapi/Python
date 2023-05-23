import sys
from math import log

digit_map = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def convert(s):
    #print(s) # checking
    #x = -1
    try:
        number = ''
        for token in s:
            number += digit_map[token]
        x = int(number)
        #print(f"Conversion Succeeded! x = {x}")
        return x
    except (KeyError,TypeError) as e:
        #print("Conversion Failed!")
        #x = -1
        print(f"Conversion Failed : {e!r}", file = sys.stderr)
        return -1
        #raise
    '''except TypeError:
        print("Conversion Failed!")
        x = -1'''

def string_log(s):
    v = convert(s)
    return log(v)


#print("one".split())
print(convert("one three three seven".split()))
print(convert("ground two grillion".split()))
print(convert(521))

print(string_log("one three three seven".split()))
