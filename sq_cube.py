def square_cube(n):
    arr1=[]
    arr2=[]
    square = n * n
    cube = n * n * n
    arr1.append(square)
    arr2.append(cube)
    return square, cube

if __name__ == "__main__":
    s, c = square_cube(10)
    print(arr1)
    print(arr2)
    print("Square:", s)
    print("Cube:", c)
