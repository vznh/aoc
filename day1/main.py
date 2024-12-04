from typing import List, Tuple, Optional

# sort l, r list
# distance between nth smallest number, then add up all
# return total distance as int

# prerequisite to extract data
def pull_data_from_file() -> Tuple[List[int], List[int]]:
  l, r = [], []
  with open('in.txt', 'r') as file:
    for line in file:
      n1, n2 = line.split()
      l.append(int(n1))
      r.append(int(n2))

  return l, r

# .start day1/main.py
# .start sol
def dist(l: List[int], r: List[int]) -> Tuple[Optional[int], Optional[int]]:
  l, r = sorted(l), sorted(r)
  sol = sum(map(lambda a, b: abs(a - b), l, r))
  sim = sum(map(lambda a: a * r.count(a), l))
  return sol, sim

# .end sol

# run test cases using python3 aoc/main.py
if __name__ == "__main__":

  # error: file is not correctly defined
  l, r = pull_data_from_file()
  assert len(l) > 0
  assert len(r) > 0

  sol, sim = dist(l, r)
  print(f"Part 1: {sol}\nPart 2: {sim}")
# .end day1/main.py
