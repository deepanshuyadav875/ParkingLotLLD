def get_level_name(level_no):
    """
    return `level_name` as Level (A1-Z1) for `level_no` 1-26, Level (A2-Z2) for `level_no` 27-52 and so on.
    assumes `level_no` starts for 1
    """
    d = level_no % 26
    chr_no = 64+26 if d == 0 else 64+d

    suffix = level_no//26
    suffix = suffix if d == 0 else suffix +1
    return f'Level {chr(chr_no)}{str(suffix)}'


def print_error(error_msg:str):
    """
    print error message in RED font-color
    """
    print(f"\033[91m Error:{error_msg}\033[00m")
