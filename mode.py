num_list = [1, 2, 2, 2, 5, 2, 6, 7, 1, 4, 1, 9, 1]
count_dict = {num:0 for num in num_list}

for num in num_list:
	count_dict[num] += 1

numbers = count_dict.keys()
mode = numbers[0]
max_value = count_dict[mode]
mode_list = []
for n in numbers:
    cur_value = count_dict[n]
    if cur_value >= max_value:
        mode = n
        max_value = cur_value
        mode_list.append((mode, max_value))
print(mode_list)
