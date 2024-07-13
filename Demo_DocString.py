""" Moduel demo code for Documenation in python."""

def mutiply(firstarg,secondarg):
    """
    Get two interger and Peform Multiplication
    :param firstarg:  This is frist Argument.
    :param Secondarg: This is second Arugment.
    :return: return the Muliplication result.
    """
    return int(firstarg*secondarg)

print("*"*80)
print(mutiply.__doc__)
print("*"*80)

print()
print()

help(mutiply)


print()
print(mutiply(6,7))