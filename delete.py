
variable = {
    "value 1" : "value 0",
    "value 2" : "Value 1",
    "value 3" : "value 2"
}

print("{value 1},{value 2}".format(**variable),end='\n',sep='\n')

walrus := 

"""values_view = variable.values()

value_iterator = iter(values_view)

first_value = next(value_iterator)

second_value = next(value_iterator)

print(first_value)

print(second_value)

# next(iter(variable))
"""

#print(variable)

