def square_cube(n):
    square = n * n
    cube = n * n * n
    return square, cube

if __name__ == "__main__":
    s, c = square_cube(10)
    print("Square:", s)
    print("Cube:", c)
