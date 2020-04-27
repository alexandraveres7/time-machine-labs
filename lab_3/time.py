import time
import functools


def timeit(fn):

    @functools.wraps(fn)
    def wrapee(*args, **kwargs):
        before = time.time()
        result = fn(*args, **kwargs)
        after = time.time()
        print(after - before)
        return result
    return wrapee


@timeit
def long_calculate():
    time.sleep(2)
    print('done')


long_calculate()
