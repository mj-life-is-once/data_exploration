import functools


def pydataLogger(func):
    """_summary_
            Decorator to catch exceptions
    Args:
            func (_type_): _description_
    """

    @functools.wraps(func)
    def exceptionHandler(*args, **kwargs):
        return_val = None
        try:
            return_val = func(*args, **kwargs)
        except ValueError as e:
            print(f"[{exceptionHandler.__name__}]Skipping invalid row: {e}")
        except Exception as e:
            print(f"[{exceptionHandler.__name__}]{e}")
        return return_val

    return exceptionHandler
