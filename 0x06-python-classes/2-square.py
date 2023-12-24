#!/usr/bin/python3

class Square:
	def __init__(self, size=0):
		if not isinstance(size, int):
			raise TypeError("size must be an integer")

		elif size < 0:
			raise ValueError("size must be grater than 0")
		else:
			self.__size = size