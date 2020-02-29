import _lib

def main():
	array = _lib.create_random_array()
	_lib.print_array(array)

	print()
	print(f'Max: {max(array)}')
	print(f'Min: {min(array)}')

main()