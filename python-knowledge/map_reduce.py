from functools import reduce

my_list = [1,2,3,4,5]

# ----------------------------------------

def map_func(p_x):
    return p_x * p_x

map_result = list(map(map_func, my_list)) # must apply "data type" after map

print(map_result)

# -----------------------------------------

def reduce_func(p_x,p_y):
    return p_x+p_y

reduce_result = reduce(reduce_func, my_list) # going to be one value

print(reduce_result)


