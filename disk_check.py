# you must import this file into another python program and call this files 'check' function to use it
import shutil


def check(drive_letter_name_string, *print_bool):
    # deal with type error
    if type(drive_letter_name_string) != str:
        raise TypeError(
            f"Parameter 'drive_letter_name_str' can not be {type(drive_letter_name_string)}, must be a string"
        )
    dlns = drive_letter_name_string.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # deal with errrors
    if dlns not in alphabet:
        raise ValueError("Parameter 'drive_letter_name_str' invalid, must be a letter")
    if len(dlns) != 1:
        raise ValueError("Parameter 'drive_letter_name_str' invalid, must be a single letter")
    drive_not_exist = False
    try:
        data = shutil.disk_usage(f"{dlns}:\\")
    except FileNotFoundError:
        drive_not_exist = True
    if drive_not_exist:
        raise FileNotFoundError(f"Drive '{drive_letter_name_string}' does not exist")
    f_data = []
    for dat in data:
        f_data.append(f"{(round(dat / 1_000_000)) / 1_000} GB")
    if print_bool:
        longest_data_len = 0
        for dat in f_data:
            longest_data_len = len(dat) if len(dat) > longest_data_len else longest_data_len
        f_strs, strs = [], [
            f"| Total Capacity: {f_data[0]} ",
            f"|     Used Space: {f_data[1]} ",
            f"|     Free Space: {f_data[2]} "
        ]
        longest_str_len = 0
        for s in strs:
            f_str = s + (' ' * (longest_data_len + 19 - len(s))) + '|'
            f_strs.append(f_str)
            f_str_len = len(f_str)
            longest_str_len = f_str_len if f_str_len > longest_str_len else longest_str_len
        spacer = '-' * longest_str_len
        title = "Disk usage stats"
        title_buffer_to_left = ' ' * round((longest_str_len - len(title)) / 2)
        print('\n' + title_buffer_to_left + title)
        print(spacer)
        for s in f_strs:
            print(s)
        print(spacer)
        ex = 'Press enter to exit...'
        ex_b = ' ' * round((longest_str_len - len(ex)) / 2)
        input(f"\n{ex_b}{ex}")
        quit()