
class Time:
    """ Represents  the time of day.
     attributes : hour , minute ,  second
    """


def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def time_to_int (time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time (seconds):
    time=Time()
    minutes,time.second=divmod(seconds,60)
    time.hour,time.minute=divmod(minutes,60)
    return time

def increment(time,seconds):
    """Adds seconds to a Time object."""
    return int_to_time((time_to_int(time)+seconds))

def add_time(t1,t2):
    assert valid_time(t1) and valid_time(t2)
    seconds=time_to_int(t1)+time_to_int(t2)
    return int_to_time(seconds)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True
