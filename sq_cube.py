def square_cube():
    i=1
    while i<=10:
        square=i*i
        cube=i*i*i
        i=i+1
    return square,cube

if "__name__" == "__main__":
    print("square and cube are:",square_cube(10))
