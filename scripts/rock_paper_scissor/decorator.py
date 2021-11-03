from datetime import datetime

"""
This is a decorator for displaying the Elapsed time in the game
"""
def log_time(func):
    def wrapped_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration // 3600
        minutes = duration // 60
        seconds = duration % 60
        print(f"Elapsed Time is : {hours}:{minutes}:{seconds}")
        return result

    return wrapped_function
