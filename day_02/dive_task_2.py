import csv

if __name__ == '__main__':
    with open('input.csv', 'r') as fd:
        reader = csv.reader(fd)
        horizontal_position = 0
        depth = 0
        aim = 0
        for row in reader:
            row_as_list = row[0].split(' ')
            instruction = row_as_list[0]
            instruction_number = int(row_as_list[1])
            if instruction == 'forward':
                horizontal_position += instruction_number
                depth = depth + (aim * instruction_number)
            elif instruction == 'down':
                aim += instruction_number
            elif instruction == 'up':
                aim -= instruction_number
        result = horizontal_position * depth
        print(result)
