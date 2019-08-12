import re

def main():
  with open('example.txt', 'r') as f:
      instructions = get_instructions(f.read().splitlines())

  fabric = [[0 for j in range(1000)] for i in range(1000)]
  for index, instruction in instructions.items():
    fabric = make_claim(index, instruction, fabric)

  print(part_one(fabric))
  print(part_two(instructions, fabric))

def part_one(fabric):
  return sum([i.count('#') for i in fabric]) 

def part_two(instructions, fabric):
  for index, instruction in instructions.items():
    index = check_claim(index, instruction, fabric)
    if index !=  'Some claims overlap':
      break
  return index

def get_instructions(lines):
  instructions = {}
  for line in lines:
    index = re.search('.*(?= @)', line).group(0)
    coordinates = re.search('(?<=@ ).*(?=:)', line).group(0)
    x_y = coordinates.split(',', 2)
    sizes = re.search('(?<=: ).*', line).group(0)
    steps_x_y = sizes.split('x', 2)
    instructions[index] = {
      'start_coordinates': [int(x_y[0]), int(x_y[1])],
      'steps': [int(steps_x_y[0]), int(steps_x_y[1])]}
  return instructions

def make_claim(index, instruction, fabric):
  x, y = instruction.get('start_coordinates')
  steps_x, steps_y = instruction.get('steps')
  for i in range(x, x + steps_x):
    for j in range(y, y + steps_y):
      if fabric[i][j] == 0:
        fabric[i][j] = index
      else:
        fabric[i][j] = '#'
  return fabric

def check_claim(index, instruction, fabric):
  x, y = instruction.get('start_coordinates')
  steps_x, steps_y = instruction.get('steps')
  has_no_overlap = True
  for i in range(x, x + steps_x):
    for j in range(y, y + steps_y):
      if fabric[i][j] == '#':
        has_no_overlap = False
        break
  if has_no_overlap:
    return index
  else:
    return 'Some claims overlap'

if __name__ == '__main__':
  main()