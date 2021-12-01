import csv

if __name__ == '__main__':
    with open('input.csv', 'r') as fd:
        reader = csv.reader(fd)
        previous_depth = None
        number_of_increases = 0
        for row in reader:
            current_depth = int(row[0])
            if previous_depth is not None and previous_depth < current_depth:
                number_of_increases += 1
            previous_depth = current_depth
        print(number_of_increases)