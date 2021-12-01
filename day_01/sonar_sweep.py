import csv

if __name__ == '__main__':
    with open('input.csv', 'r') as fd:
        reader = csv.reader(fd)
        previous_depth = None
        number_of_increases = 0
        list_of_depths = []
        for row in reader:
            current_depth = int(row[0])
            list_of_depths.append(current_depth)
            if previous_depth is not None and previous_depth < current_depth:
                number_of_increases += 1
            previous_depth = current_depth
        print('The depth has increased ' + str(number_of_increases) + ' number of times!')
        sliding_a_index = 0
        sliding_b_index = 1
        sliding_c_index = 2
        previous_window_sum = None
        number_of_window_increases = 0
        for current_index in range(len(list_of_depths)):
            sliding_a_index = current_index
            sliding_b_index = current_index + 1
            sliding_c_index = current_index + 2
            try:
                current_window_sum = list_of_depths[sliding_a_index] + list_of_depths[sliding_b_index] + list_of_depths[
                    sliding_c_index]
                if previous_window_sum is not None and previous_window_sum < current_window_sum:
                    number_of_window_increases += 1
                previous_window_sum = current_window_sum
            except:
                print('No complete window possible! Abort.')
                break
        print(number_of_window_increases)
