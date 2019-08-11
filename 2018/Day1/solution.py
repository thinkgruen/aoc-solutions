def main():
  with open('example.txt', 'r') as f:
    instructions = f.read().splitlines()
  print(part_one(instructions))
  print(part_two(instructions))


def part_one(instructions):
  current_frequency = 0
  for instruction in instructions:
    current_frequency += int(instruction)

  return current_frequency

def part_two(instructions):
  frequencies = set()
  current_frequency = 0
  found = False 

  while(not found):
    for instruction in instructions:
      if(current_frequency in frequencies):
        found = True
        break
      else:
        frequencies.add(current_frequency)
        current_frequency += int(instruction)

  return current_frequency

if __name__ == '__main__':
  main()
