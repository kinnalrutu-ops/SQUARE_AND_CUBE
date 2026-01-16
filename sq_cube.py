def square_cube(n):
    arr=[]
    square = n * n
    cube = n * n * n
    arr.append(square)
    arr.append(cube)
    return square, cube

if __name__ == "__main__":
    s, c = square_cube(10)
    print("Square:", s)
    print("Cube:", c)
