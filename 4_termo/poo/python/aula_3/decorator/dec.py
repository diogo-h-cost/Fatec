def decorator(f):
    def new_fuction():
        print("Extra")
        f()
    return new_fuction

@decorator # decorator_function_name p/ criar um decorador
def initial_function():
    print("Initial")

initial_function()