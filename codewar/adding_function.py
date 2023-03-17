""" We want to create a function that will add numbers together when called in succession.
add(1)(2)(3) # 6
"""
class add(int):

    def __call__(self, m):
        return add(self + m)




print(add(1)(2)(3))
