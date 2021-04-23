#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys


# i: if 0, then start
def watch(i, count_all):
    if i == 0:
        watch.start = time.time()
        return 0, 0, 0
    start = watch.start
    elapsed = time.time() - start
    whole = elapsed * (count_all / i)
    remain = whole - elapsed
    return elapsed, remain, whole


def to_str(t):
    t = int(t)
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    if h > 0:
        return "{}h{}m".format(h, m)
    if m > 0:
        return"{}m{}s".format(m, s)
    return "{}s".format(s)


def watch_as_str(i, count_all):
    elapsed, remain, whole = watch(i, count_all)
    return to_str(elapsed), to_str(remain), to_str(whole)


def progress(i, n):
    if i == 0:
        watch_as_str(0, n)
        return
    if i % 25 == 0:
        print(i, n, file=sys.stderr)  # debug
    if i % 1000 == 0:
        elapsed, remain, whole = watch_as_str(i, n)
        print("elapsed, remain, whole", elapsed, remain, whole, file=sys.stderr)  # debug


if __name__ == '__main__':
    import argparse
    # import pysnooper # @pysnooper.snoop()
    from pprint import pprint as pp
    from pprint import pformat as pf
    for i in range(5):
        a, b, c = watch_as_str(i, 5)
        print("a, b, c", a, b, c)  # debug
        time.sleep(1)
    count_all = 5000
    for i in range(count_all):
        progress(i, count_all)

    # parser = argparse.ArgumentParser()
    # args = parser.parse_args()
