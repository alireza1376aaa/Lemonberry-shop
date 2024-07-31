import re


def remove_spaces(string):
    pattern = r"[\s@&%^#]"
    return re.sub(pattern, "", string)
