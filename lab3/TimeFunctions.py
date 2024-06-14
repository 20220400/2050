import time

def time_function(func, args, n_trials = 10):
    """Return the min args fron  a trial of"""
    time_list = []
    for start in range(n_trials):
        start = time.time()
        func(args)
        end = time.time()
    execution = end - start
    time_list.append(execution)
    return min(time_list)

    
def time_function_flexible(f, args, n_trials = 10):
    """Unpacks the tumple for args and returns the min"""
    time_list = []
    min_time = float('inf')
    for start in range(n_trials):
        start = time.time()
        f(*args)
        end = time.time()
    execution = end - start
    min_time = min(min_time, execution)
    return min_time

if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    L3 = [i for i in range(10**5)]
    t3 = time_function_flexible(test_func, L1)

    L4 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t4 = time_function_flexible(test_func, L2)

    

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))

    print("t(L3) = {:.3g} ms".format(t3*1000))
    print("t(L4) = {:.3g} ms".format(t4*1000))