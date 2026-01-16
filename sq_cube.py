def square_cube():
    arr1 = []   
    arr2 = []   

    for i in range(1, 11):
        square = i * i
        cube = i * i * i

        arr1.append(square)
        arr2.append(cube)

    return arr1, arr2


if __name__ == "__main__":
    square, cube = square_cube()

    print("Squares from 1 to 10:", square)
    print("Cubes from 1 to 10:", cube)
