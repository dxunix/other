import time


def timing(func):
    """
    timing a function
    """
    def wrap(*args):
        """
        wrapper the time around the actual function
        """
        start = time.time()
        ret = func(*args)
        end = time.time()
        print('@timin: g[{:s}] took [{:.3f}] ms'.format(
            func.__name__,
            (end - start)*1000.0))
        return ret
    return wrap
