# Problem 1

# --- introduction ---

# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Arithmetic Operators
if __name__ == '__main__':
    x = int(input())
    y = int(input())

    print (x + y)
    print (x - y)
    print (x * y)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print (a//b)
print (a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print (i**2)

# Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print (i, end="")

# Write a function
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4== 0:
        leap = True
    else:
        leap = False

    return leap

# Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n >= 20:
    print("Not Weird")

# --- basic data types ---

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

result = [[i, j, k]
           for i in range(x+1)
           for j in range(y+1)
           for k in range(z+1)
           if i + j + k != n]

print(result)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))


max_score = max(arr)
new_arr = [x for x in arr if x != max_score]
runner_up = max(new_arr)
print(runner_up)

# Nested Lists
if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = [score for name, score in records]
    second_lowest = sorted(set(scores))[1]
    names = [name for name, score in records if score == second_lowest]

    for n in sorted(names):
        print(n)

# Lists
if __name__ == '__main__':
    N = int(input())        # numero di comandi
    arr = []                # lista iniziale vuota

    for _ in range(N):
        command = input().split()     # leggo il comando, diviso in parole
        operation = command[0]        # es: 'insert', 'append', 'print', ecc.

        # controllo il tipo di operazione
        if operation == 'insert':
            i = int(command[1])
            e = int(command[2])
            arr.insert(i, e)

        elif operation == 'print':
            print(arr)

        elif operation == 'remove':
            e = int(command[1])
            arr.remove(e)

        elif operation == 'append':
            e = int(command[1])
            arr.append(e)

        elif operation == 'sort':
            arr.sort()

        elif operation == 'pop':
            arr.pop()

        elif operation == 'reverse':
            arr.reverse()

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    mean =sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{mean:.2f}")

# --- strings ---

# sWAP cASE
def swap_case(s):
    return s.swapcase()

# String Split and Join


def split_and_join(line):
   new_line = line.split()
   result = '-'.join(new_line)
   return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

# Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

# Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+(len(sub_string))] == sub_string:
            count += 1
    return count

# String Validators
if __name__ == '__main__':
    s = input()

    print(any((c.isalnum()) for c in s))
    print(any((c.isalpha()) for c in s))
    print(any((c.isdigit()) for c in s))
    print(any((c.islower()) for c in s))
    print(any((c.isupper()) for c in s))

# Text Alignment
# Enter your code here. Read input from STDIN. Print output to STDOUT

thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

for i in range(thickness + 1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

for i in range((thickness + 1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness + 1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Text Wrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)

# Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())
for i in range (N // 2):
    print(('.|.' * (2*i+1)).center(M, '-'))

print(('WELCOME').center(M, '-'))

for i in reversed(range (N // 2)):
    print(('.|.' * (2*i+1)).center(M, '-'))

# String Formatting
def print_formatted(number):
    width = len(bin(number) [2:])
    for i in range(1, number + 1):
        print(str(i).rjust(width),
        oct(i)[2:].rjust(width),
        hex(i)[2:].upper().rjust(width),
        bin(i)[2:].rjust(width))

# Alphabet Rangoli
import string

def print_rangoli(n: int) -> None:
    alpha = string.ascii_lowercase
    width = 4 * n - 3
    lines = []

    for i in range(n):
        left = [alpha[n - 1 - k] for k in range(i + 1)]
        row  = '-'.join(left + left[-2::-1])
        lines.append(row.center(width, '-'))

    for line in lines:
        print(line)
    for line in lines[-2::-1]:
        print(line)

# Capitalize!


# Complete the solve function below.
def solve(s):
    res_chars = []

    for i in range(len(s)):
        if i == 0 or s[i-1] == ' ':
            res_chars.append(s[i].upper())
        else:
            res_chars.append(s[i])
    return ''.join(res_chars)

# The Minion Game
def minion_game(string):
    vowels = set('AEIOU')
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

# Merge the Tools!
def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        substring = string[i:i+k]
        seen = set()
        result = ''
        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result += ch
        print(result)

# --- sets ---

# Introduction to Sets
def average(array):
    heights = set(array)
    return sum(heights) / len(heights)

# Symmetric Difference
if __name__ == "__main__":
    M = int(input().strip())
    M_2 = set(map(int, input(). split()))
    N = int(input().strip())
    N_2 = set(map(int, input().split()))

S = M_2.symmetric_difference(N_2)
for num in sorted(S):
    print(num)

# Set .add()
if __name__ == "__main__":
    N = int(input())
    Countries = set()
    for _ in range(N):
        Country = input().strip()
        Countries.add(Country)
    print(len(Countries))

# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().strip().split()

    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))

# Set .union() Operation
if __name__ == "__main__":
    n = int(input())
    eng = set(map(int, input().split()))
    b = int(input())
    fra = set(map(int, input().split(),))

s = eng.union(fra)
print(len(s))

# Set .intersection() Operation
if __name__ == "__main__":
    n = int(input())
    eng = set(map(int, input().split()))
    b = int(input())
    fra = set(map(int, input().split()))

s = eng.intersection(fra)
print(len(s))

# Set .difference() Operation
if __name__ == "__main__":
    n = int(input())
    eng = set(map(int, input().split()))
    b = int(input())
    fra = set(map(int, input().split()))

s = eng.difference(fra)
print(len(s))

# Set .symmetric_difference() Operation
if __name__ == "__main__":
    n = int(input())
    eng = set(map(int, input().split()))
    b = int(input())
    fra = set(map(int, input().split()))

    s = eng.symmetric_difference(fra)
    print(len(s))

# Set Mutations
if __name__ == "__main__":
    n = int(input())
    A = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        command = input().split()[0]
        other = set(map(int, input().split()))

        if command == 'intersection_update':
            A.intersection_update(other)
        elif command == 'update':
            A.update(other)
        elif command == 'symmetric_difference_update':
            A.symmetric_difference_update(other)
        elif command == 'difference_update':
            A.difference_update(other)

print(sum(A))

# The Captain's Room
if __name__ == "__main__":
    k = int(input())
    r = list(map(int, input().split()))

    un = set(r)
    cap = (k * sum(un) - sum(r)) // (k - 1)
    print (cap)

# Check Subset
if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        _ = int(input().strip())
        A = set(map(int, input().split()))
        _ = int(input().strip())
        B = set(map(int, input().split()))
        print(A.issubset(B))

# Check Strict Superset
if __name__ == "__main__":
    A = set(map(int, input().split()))
    n = int(input())

    result = True


    for _ in range(n):
        B = set(map(int, input().split()))
        if not (A.issuperset(B)):
            result = False
            break
    print(result)

# No Idea!
if __name__ == "__main__":
    n, m = map(int, input().split())
    N = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    hap = 0
    for x in N:
        hap += (x in A) - (x in B)

    print(hap)

# --- collections ---

# collections.Counter()
if __name__ == "__main__":
    from collections import Counter

    X = int(input())  # numbers of shoes
    S = list(map(int, input().split()))
    Y = int(input())  # number of customers

    Money = 0

    counter = Counter(S)

    for i in range(Y):
        size, price = map(int, input().split())
        if counter[size]> 0:
            counter[size] -= 1
            Money += price
    print(Money)

# DefaultDict Tutorial
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    d = defaultdict(list)


    for i in range(1, n + 1):
        word = input().strip()
        d[word].append(i)

    for _ in range(m):
        query = input().strip()
        if query in d:
            print(*d[query])
        else:
            print(-1)

# Collections.namedtuple()
from collections import namedtuple
if __name__ == "__main__":

    N = int(input())
    Cname = input().split()
    Student = namedtuple('S', Cname)

    Total = 0

    for _ in range(N):
        data = input().split()
        stud = Student(*data)
        Total += int(stud.MARKS)

    print("{:.2f}".format(Total/N))

# Collections.OrderedDict()
from collections import OrderedDict

if __name__ == "__main__":
    N = int(input())
    d = OrderedDict()

    for _ in range(N):
        line = input().split()
        item_name = " ".join(line[:-1])
        price = int(line[-1])

        d[item_name] = d.get(item_name, 0) + price

for x,y in d.items():
    print(x,y)

# Collections.deque()
from collections import deque
if __name__ == "__main__":
    N = int(input())
    d = deque()

    for _ in range(N):
        command = input().split()
        x = command[0]
        if len(command)> 1:
            value = command[1]

        if x == "append":
            d.append(int(value))
        elif x == "pop":
            d.pop()
        elif x == "popleft":
            d.popleft()
        elif x == "appendleft":
            d.appendleft(int(value))
    print(*d)

# Word Order
from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    d = OrderedDict()

    for _ in range(n):
        word = input().strip()
        d[word] = d.get(word, 0) + 1

    print(len(d))
    print(*d.values())

# Piling Up!
from collections import deque

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        blocks = deque(map(int, input().split()))

        last = float('inf')
        possible = True

        while blocks:
            if blocks[0] >= blocks[-1]:
                pick = blocks.popleft()
            else:
                pick = blocks.pop()

            if pick > last:
                possible = False
                break
            last = pick

        print("Yes" if possible else "No")

# Company Logo
#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter

if __name__ == "__main__":
    s = input().strip()
    counts = Counter(s)

    # ordina per frequenza decrescente e poi alfabetico crescente
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for ch, freq in sorted_items[:3]:
        print(ch, freq)

# --- date and time ---

# Calendar Module
if __name__ == "__main__":
    month, day, year = map(int, input().split())

    import calendar
    day_index = calendar.weekday(year, month, day)

    days = ["MONDAY" ,"TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    print(days[day_index])

# Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

def time_delta(t1, t2):

    time1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((time1 - time2).total_seconds())))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# --- exceptions ---

# Exceptions
n = int(input().strip())
for _ in range(n):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except Exception as e:
        print(f"Error Code: {e}")

# --- built-ins ---

# Zipped!
n, x = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(x)]

for student_scores in zip(*subjects):
    print(sum(student_scores) / x)

# Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda x: x[k])

    for row in arr:
        print(*row)

# ginortS
s = input()

lower = sorted([c for c in s if c.islower()])
upper = sorted([c for c in s if c.isupper()])
odd = sorted([c for c in s if c.isdigit() and int(c) % 2 == 1])
even = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])

print(''.join(lower + upper + odd + even))

# --- functionals ---

# Map and Lambda Function
cube = lambda x: x ** 3

def fibonacci(n):
    seq = [0,1]
    for i in range(2, n):
        seq.append(seq[-1]+seq[-2])
    return seq[:n]

# --- regex ---

# Detect Floating Point Number
import re

pattern = r'^[+-]?\d*\.\d+$'

T = int(input())

for _ in range(T):
    string = input()
    if re.match(pattern, string):
        print(True)
    else:
        print(False)

# Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

# Group(), Groups() & Groupdict()
import re

s = input().strip()
m = re.search(r'([A-Za-z0-9])\1+', s)
print(m.group(1) if m else -1)

# Re.findall() & Re.finditer()
import re

s = input()

pattern = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])'

matches = re.findall(pattern, s, re.I)

if matches:
    print(*matches, sep='\n')
else:
    print(-1)

# Re.start() & Re.end()
import re

S = input()
k = input()

pattern = re.compile(r'(?={})'.format(re.escape(k)))
matches = list(pattern.finditer(S))

if matches:
    for m in matches:
        start = m.start()
        end = start + len(k) - 1
        print((start, end))
else:
    print((-1, -1))

# Regex Substitution
import re

n = int(input())
for _ in range(n):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)

# Validating Roman Numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

# Validating phone numbers
import re

n = int(input())
pat = re.compile(r'^[789]\d{9}$')

for _ in range(n):
    print('YES' if pat.match(input().strip()) else 'NO')

# Validating and Parsing Email Addresses
import re
from email.utils import parseaddr

n = int(input())
pat = re.compile(r'^[A-Za-z][\w\.-]*@[A-Za-z]+\.[A-Za-z]{1,3}$')

for _ in range(n):
    s = input().strip()
    name, addr = parseaddr(s)
    if name and addr and pat.fullmatch(addr):
        print(s)

# Hex Color Code
import re

n = int(input())
for _ in range(n):
    line = input()
    matches = re.findall(r'(?<=[: ,(])#[0-9A-Fa-f]{3,6}', line)
    for m in matches:
        print(m)

# HTML Parser - Part 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for a, v in attrs:
            print("->", a, ">", v)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for a, v in attrs:
            print("->", a, ">", v)

if __name__ == "__main__":
    n = int(input())
    html = "\n".join(input() for _ in range(n))
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

# HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

if __name__ == "__main__":
    n = int(input())
    html = "\n".join(input() for _ in range(n))
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a, v in attrs:
            print("->", a, ">", v)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for a, v in attrs:
            print("->", a, ">", v)

if __name__ == "__main__":
    n = int(input())
    html = "\n".join(input() for _ in range(n))
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

# Validating UID
import re
pat = re.compile(r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}$')

for _ in range(int(input())):
    s = input().strip()
    print("Valid" if pat.match(s) else "Invalid")

# Validating Credit Card Numbers
import re

fmt = re.compile(r'^[456]\d{3}(?:-?\d{4}){3}$')  # formato valido con/o senza trattini
rep4 = re.compile(r'(.)\1\1\1')                  # 4 ripetizioni consecutive

for _ in range(int(input())):
    s = input().strip()
    if not fmt.match(s):
        print("Invalid")
        continue
    digits = s.replace('-', '')
    print("Valid" if not rep4.search(digits) else "Invalid")

# Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"

# Matrix Script
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = ''.join(matrix[i][j] for j in range(m) for i in range(n))
decoded = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded)
print(decoded)

# --- xml ---

# XML 1 - Find the Score


def get_attr_number(node):
    count = (len(node.attrib))
    for child in node:
        count += get_attr_number(child)
    return count

# XML2 - Find the Maximum Depth


maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)

# --- closures and decorators ---

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f(['+91 ' + n[-10:-5] + ' ' + n[-5:] for n in l])
    return fun

# Decorators 2 - Name Directory


def person_lister(f):
    def inner(people):
        return [f(p) for p in sorted(people, key=lambda x: int(x[2]))]
    return inner

# --- numpy ---

# Arrays


def arrays(arr):
    return numpy.array(arr, float)[::-1]

# Shape and Reshape
import numpy

n = numpy.array(input().split(), int)

print(numpy.reshape(n, (3,3)))

# Transpose and Flatten
import numpy

n,m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
a = numpy.array(rows, int)

print(numpy.transpose(a))
print(a.flatten())

# Concatenate
import numpy

n, m, p = map(int, input().split())

NP = [list(map(int, input().split())) for _ in range(n)]
MP = [list(map(int, input().split())) for _ in range(m)]
np_array = numpy.array(NP)
mp_array = numpy.array(MP)
print(numpy.concatenate((np_array, mp_array), axis=0))

# Zeros and Ones
import numpy



N = tuple(map(int,(input().split())))
print(numpy.zeros(N, dtype = int))
print(numpy.ones(N, dtype = int))

# Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')

N,M = map(int,input().split())


print(numpy.eye(N, M, k = 0))

# Array Mathematics
import numpy

N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(N)], int)
B = numpy.array([list(map(int, input().split())) for _ in range(N)], int)

print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(numpy.floor_divide(A, B))
print(numpy.mod(A, B))
print(numpy.power(A, B))

# Floor, Ceil and Rint
import numpy

numpy.set_printoptions(legacy='1.13')

A = numpy.array(list(map(float, input().split())))

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

# Sum and Prod
import numpy

N, M = tuple(map(int, input().split()))

array = numpy.array([list(map(int, input().split())) for _ in range(N)])

sumarray = numpy.sum(array, axis=0)
print(numpy.prod(sumarray))

# Min and Max
import numpy

N, M = tuple(map(int, input().split()))

arr = numpy.min([list(map(int, input().split())) for _ in range(N)], axis = 1)
print(numpy.max(arr))

# Mean, Var, and Std
import numpy

N, M = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(N)])

print(numpy.mean(arr, axis=1))      # media per riga
print(numpy.var(arr, axis=0))       # varianza per colonna
print(round(numpy.std(arr), 11))    # deviazione standard totale, arrotondata a 11 decimali

# Dot and Cross
import numpy

N = int(input())
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(N)])

print(numpy.dot(A, B))

# Inner and Outer
import numpy

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print(numpy.inner(A, B))
print(numpy.outer(A, B))

# Polynomials
import numpy

coeff = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(coeff, x))

# Linear Algebra
import numpy

N = int(input())
A = numpy.array([list(map(float, input().split())) for _ in range(N)])

print(round(numpy.linalg.det(A), 2))


# Problem 2

# Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    max_h = -1
    cnt = 0
    for h in candles:
        if h > max_h:
            max_h = h
            cnt = 1
        elif h == max_h:
            cnt += 1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"

    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    recipients = 5
    total = 0
    for _ in range(n):
        likes = recipients // 2
        total += likes
        recipients = likes * 3
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    total = sum(map(int, n)) * k

    def helper(x):
        if x < 10:
            return x
        return helper(sum(map(int, str(x))))

    return helper(total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    key = arr[-1]
    i = n - 2


    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1


    arr[i + 1] = key
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(*arr)



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
