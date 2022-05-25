import timeit

def timer_func(func):
    def function_timer():
        start_time = timeit.default_timer()
        result = func()
        runtime = timeit.default_timer() - start_time
        print(result)
        return runtime
    return function_timer

def timer_func_with_result(func):
    def function_timer():
        start_time = timeit.default_timer()
        result = func()
        runtime = timeit.default_timer() - start_time
        return (runtime, result)
    return function_timer