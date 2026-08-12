def args_func(*args):
    print(args)
    print(type(args)) # should be tuple

def kwargs_func(**kwargs):
    print(kwargs)
    print(type(kwargs)) # should be dict

args_func(10,20,30)
kwargs_func(name='Matthew',status='single',age=22)

