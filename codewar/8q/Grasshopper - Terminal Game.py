# In this first kata in the series, you need to define a Hero prototype to be used in a terminal game.
# The hero should have the following attributes:
# attribute	value
# name	    user argument or 'Hero'
# position	'00'
# health	    100
# damage	    5
# experience	0
class Hero(object):
    def __init__(self, name=None, attribute=None):
        self._name = name
        self.attribute = attribute
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0

    @property
    def name(self) -> str:
        if self._name:
            return self._name
        else:
            return self.__class__.__name__

    @name.setter
    def name(self, value):
        self._name = value

    def print_name(self):
        if self.name:
            print(self.name)
        else:
            print(self.__class__.__name__)

a=Hero()
Hero.print_name(a)
a.name = 'Kat'
Hero.print_name(a)
print(a.name)