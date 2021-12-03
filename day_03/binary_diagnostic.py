import csv

if __name__ == '__main__':
    with open('input.csv', 'r') as fd:
        reader = csv.reader(fd)
        input_list = []
        for row in reader:
            char_list_of_row = [char for char in row[0]]
            input_list.append(char_list_of_row)

        gamma_rate = ''
        epsilon_rate = ''
        for column_index in range(len(input_list[0])):
            one_bit_count = 0
            zero_bit_count = 0
            for row_index in range(len(input_list)):
                current_bit = input_list[row_index][column_index]
                if current_bit == '0':
                    zero_bit_count += 1
                else:
                    one_bit_count += 1
            if zero_bit_count > one_bit_count:
                epsilon_rate += '0'
                gamma_rate += '1'
            elif zero_bit_count < one_bit_count:
                epsilon_rate += '1'
                gamma_rate += '0'

    print(int(epsilon_rate, 2) * int(gamma_rate, 2))
