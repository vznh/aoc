import re
from operator import not_
# .start day3/main.py

def pull_data_from_file() -> str:
  s = ""
  with open('in.txt', 'r') as file:
    for line in file:
      s += line.strip()

  return s

def product(s: str) -> int:
  # regex pattern that signals for keyword
  # digit that could be more than one place in left and right and ending parentheses
  pattern = r'mul\((\d+),(\d+)\)'
  matches = re.findall(pattern, s)

  return sum(int(x) * int(y) for x, y in matches)
'''
  *note
  This function is fundamentally different than Part 2, but if I were to change it to align with part 2,
    - remove doing flag
    while idx < len(s):
      if s.startswith('mul(', idx) and doing:
        match = re.match(pattern, s[idx:])
        if match:
          x, y = map(int, match.groups())
          total += x * y
          idx += match.end()
        else:
          idx += 3 # move past "mul"
  ...or just doing the same thing.
'''

def detect_and_produce(s: str) -> int:
  pattern = r'mul\((\d+),(\d+)\)'
  doing = True
  total = 0

  idx = 0
  while idx < len(s):
    if s.startswith('mul(', idx) and doing:
      match = re.match(pattern, s[idx:])
      if match:
        x, y = map(int, match.groups())
        total += x * y
        idx += match.end()
      else:
        idx += 3 # move past "mul"
    elif s.startswith("do()", idx):
      doing = True
      idx += 4 # move past "do()"
    elif s.startswith("don't()", idx):
      doing = False
      idx += 7 # move past "don't()"
    else: idx += 1

  return total

if __name__ == "__main__":
  s = pull_data_from_file()
  print(detect_and_produce(s))

# .end day3/main.py
