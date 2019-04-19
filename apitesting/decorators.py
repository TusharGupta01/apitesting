from functools import wraps
import time
import apitesting.logger as logger

logger = logger.get_logger(__name__)


def timeit(fn):
    '''
    Function decorator to measure execution time
    @example
    from apitesting.decorators import timeit
    @timeit
    def foo(sec):
        time.sleep(sec)
        print('foo')
    foo(1)
    # => foo
    # => Timed: foo 1000.9971ms
    '''
    @wraps(fn)
    def time_fn(*args, **kwargs):
        start = time.time()
        output = fn(*args, **kwargs)
        end = time.time()
        logger.debug3(f'Timed: {fn.__name__} {round((end - start) * 1000, 4)}ms')
        return output
    return time_fn