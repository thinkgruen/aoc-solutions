import itertools
from collections import defaultdict

def main():
  with open('example.txt', 'r') as f:
      instructions = f.read().splitlines()
  print(part_one(instructions))
  print(part_two(instructions))

def part_one(instructions):
  [x,y] = [0,0]
  for instruction in instructions:
    [x,y] = process_word(instruction, x, y)
  return x * y

def process_word(instruction, x, y):
  letter_count = defaultdict(int)
  for letter in instruction:
    letter_count[letter] += 1
  twos = False
  threes  = False
  for value in letter_count.values():
    if twos and threes:
      break
    elif value == 2:
      twos = True
    elif value == 3:
      threes = True
    
  return [x + twos, y + threes]

def part_two(instructions):
  for pair in itertools.combinations(instructions, 2):
    [common_word, suffices_criteria] = difference(pair[0], pair[1])
    if(suffices_criteria):
      return common_word

  return 'No common word found.'

def difference(word_a, word_b):
  difference = 0
  common_word = ""
  for i in range (0, len(word_a)):
    if word_a[i] != word_b[i]:
      difference += 1
      common_word = word_a[:i] + word_a[i+1:]
    if difference > 1:
      break

  return [common_word, difference == 1]

if __name__ == '__main__':
  main()