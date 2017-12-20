# Copyright 2017 Sihan Wang shwang95@bu.edu

def max_uint_of_byte(byte):
	bit = byte * 8
	count = 2 ** bit
	return count - 1

def min_int_of_byte(byte):
	bit = byte * 8 - 1
	count = 2 ** bit
	return -count

def max_int_of_byte(byte):
	bit = byte * 8 - 1
	count = 2 ** bit
	return count - 1

Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for byte in range(1, 9):
	print(Table.format(byte, max_uint_of_byte(byte), min_int_of_byte(byte), max_int_of_byte(byte)))
