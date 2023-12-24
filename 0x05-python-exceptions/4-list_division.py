#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
	result_list = []

	for i in range(list_length):
		result = 0

		try:
			element_1 = my_list_1[i] if i < len(my_list_1) else 0
			element_2 = my_list_2[i] if i < len(my_list_2) else 0

			result = element_1 / element_2

			if result != result:
				raise ValueError

		except ZeroDivisionError:
			print("Division by 0")
		except (TypeError, ValueError):
			print("Wrong type")
			result = 0
		except IndexError:
			print("Out of range")

		finally:
			result_list.append(result)

	return result_list
