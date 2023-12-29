#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    total = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            total += 1
        except IndexError:
            break
    print()
    return(total)
=======
	count = 0
	for i in range(x):
	    try:
		print("{}".format(my_list[i]), end="")
		count += 1
		print()
	except IndexError:
	    break
	print()
	return count
>>>>>>> 0a8a2d22f34647236cf61d216845fca6b9822178
