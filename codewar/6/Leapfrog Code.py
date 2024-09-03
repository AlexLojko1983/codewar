# Implement a function `change_list(arr)` that takes a list as an argument and mutates its elements in such way:
# • If the element is an integer, square it
# • If the element is a string, append its reversed copy to its end like that "string" becomes "stringgnirts"
# • If the element is a bool, simply reverse it. True becomes False and False becomes True
# • Reverse the list
def change_list(arr):
    if type(arr) is int: return arr**2
    if type(arr) is bool: return not arr
    if type(arr) is str: return arr + ''.join(arr[::-1])
    if type(arr) is list: return arr.reverse()


print(change_list([5,10,11]))
