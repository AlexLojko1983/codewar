'''
Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the
needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
See more examples in "Sample Tests:"
'''

def dir_reduc(arr):
    n = 1
    while n == 1 and len(arr) > 1:
        n = 0
        for i, j in enumerate(arr):
            if (j == 'NORTH' and arr[i + 1] == 'SOUTH'
                    or j == 'SOUTH' and arr[i + 1] == 'NORTH'
                    or j == 'WEST' and arr[i + 1] == 'EAST'
                    or j == 'EAST' and arr[i + 1] == 'WEST'):
                arr.remove(arr[i + 1])
                arr.remove(arr[i])
                n = 1
                break
    return arr


print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
