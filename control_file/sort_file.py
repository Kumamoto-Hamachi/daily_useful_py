import re


def convert_num_str_to_int(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [convert_num_str_to_int(c) for c in re.split(r'(\d+)', text)]


"""
img_names = sorted(img_names, key=natural_keys)
"""
