# you can run this inside another program if you want just to get the values themselves and not print them

import shutil
data, f_data = shutil.disk_usage("C:\\"), []
for dat in data:
    f_data.append(f"{(round(dat / 1_000_000)) / 1_000} GB")
# you can import this file to just get the data in either form you want

# if this file is being run itself, then do all this printing and stuff
if __name__ == '__main__':
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
