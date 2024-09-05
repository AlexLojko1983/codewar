# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples


def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) < 2:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], (len(names)-2))