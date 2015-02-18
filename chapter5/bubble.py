def bubble_sort(a_list):
	for pass_num in range(len(a_list) - 1, 0, -1):
		for i in range(pass_num):
			if a_list[i] > a_list[i + 1]:
				temp = a_list[i]
				a_list[i] = a_list[i + 1]
				a_list[i + 1] = temp


if __name__ == '__main__':
	a_list = [61, 42, 13, 75, 71, 21, 94, 53, 19]
	bubble_sort(a_list)
	print(a_list)
