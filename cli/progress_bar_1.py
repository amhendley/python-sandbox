import sys
import time
import random


def progress_bar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_length = int(round(bar_length * count_value / float(total)))
    percentage = round(100.0 * count_value/float(total), 1)
    bar = '=' * filled_up_length + '-' * (bar_length - filled_up_length)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percentage, '%', suffix))
    sys.stdout.flush()


for i in range(11):
    time.sleep(random.random())
    progress_bar(i, 10, 'Running')
