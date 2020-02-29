import _lib

def main():
    height = 5

    for triangle_index in range(0, height):
        triangle_height = 2 + triangle_index
        triangle_offset = height - triangle_index - 1

        triangle = _lib.build_triangle(triangle_height, triangle_offset)

        print(triangle.rstrip())

main()