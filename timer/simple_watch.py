import time


def simple_watch(i):
    if i == 0:
        simple_watch.start = time.time()
        return 0
    start = simple_watch.start
    elapsed = time.time() - start
    return elapsed


def to_str(t):
    t = int(t)
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    if h > 0:
        return "{}h{}m".format(h, m)
    if m > 0:
        return"{}m{}s".format(m, s)
    return "{}s".format(s)


def watch_as_str(i):
    elapsed = simple_watch(i)
    return to_str(elapsed)
