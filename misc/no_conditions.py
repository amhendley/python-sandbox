
time_string = '0:1:34.123'
sep_count = time_string.count(':')
has_milliseconds = (time_string.count('.') > 0)

if sep_count == 1:
    if has_milliseconds:
        time_format = '%M:%S.%f'
    else:
        time_format = '%M:%S'
elif sep_count == 2:
    if has_milliseconds:
        time_format = '%H:%M:%S.%f'
    else:
        time_format = '%H:%M:%S'

print(f'First format found:  {time_format}')

# TO THIS >>>

time_formats = {1: {True: '%M:%S.%f', False: '%M:%S'},
                2: {True: '%H:%M:%S.%f', False: '%H:%M:%S'}}

sep_count = time_string.count(':')
has_milliseconds = (time_string.count('.') > 0)
time_format = time_formats[sep_count][has_milliseconds]

print(f'Second format found: {time_format}')
