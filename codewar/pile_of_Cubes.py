"""Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of
�3n3 , the cube above will have volume of(�−1)3(n−1)3
  and so on until the top which will have a volume of1313.
You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?
The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as
�3+(�−1)3+(�−2)3+...+13=�n3 +(n−1)3 +(n−2)3 +...+13=m if such a n exists or -1 if there is no such n.

"""
m = int(input('Input m: '))

def find_nb(m):
    summ = 0
    for n in range(1, pow(m, 3), 1):
        if m == summ:
            return n-1
        elif m < summ:
            return -1
        elif m > summ:
            summ += pow(n, 3)


print(find_nb(m))