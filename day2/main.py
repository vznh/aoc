from typing import List
# .start day2/main

def pull_data_from_file() -> List[List[int]]:
  l = []
  with open('in.txt', 'r') as file:
    for line in file:
      numbers = list(map(int, line.split()))
      l.append(numbers)

  return l

def guide(material: List[int]) -> bool:
  inc, dec = True, True

  for i in range(len(material) - 1):
    difference = material[i+1] - material[i]

    if abs(difference) < 1 or abs(difference) > 3:
      return False

    if difference > 0: dec = False
    elif difference < 0: inc = False

    if not inc and not dec: return False

  return True

def deem(mat: List[List[int]]) -> int:
  return sum([guide(row) for row in mat])

def deem_with_dampener(mat: List[List[int]]) -> int:
  # iterate through a row
  # -> for ALL indexes within that row, remove them. if guide returns true for at least ONE of the outcomes, then it will work
  return sum([any([guide(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in mat])

if __name__ == "__main__":
  mat = pull_data_from_file()
  print(deem(mat))
  print(deem_with_dampener(mat))

# .end day2/main
